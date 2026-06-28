#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scan_range.py — 22DIV IP Range Automation
george wu // rainfantry

Usage:
    python scan_range.py 192.168.1.0/24
    python scan_range.py 192.168.1.1-192.168.1.50
    python scan_range.py 192.168.1.92              # single host
    python scan_range.py 192.168.1.0/24 --ssh-user gwu07 --winrecon
    python scan_range.py 192.168.1.0/24 --ports 22,80,443,1337,4443,8080 --threads 50

Options:
    --ports       Comma-separated port list (default: common attack-surface ports)
    --threads     Concurrent threads (default: 64)
    --timeout     Socket timeout in seconds (default: 0.8)
    --ssh-user    Username for SSH winrecon deployment
    --ssh-key     Path to SSH private key
    --winrecon    Auto-run winrecon.ps1 on discovered Windows hosts via SSH
    --json        Output JSON to scan_<timestamp>.json
    --quiet       Only print findings, no banner
"""

import argparse
import ipaddress
import json
import os
import socket
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

# ── Terminal colors ───────────────────────────────────────────────────────────
R  = '\033[91m'   # red
Y  = '\033[93m'   # yellow
G  = '\033[92m'   # green
C  = '\033[96m'   # cyan
M  = '\033[95m'   # magenta
W  = '\033[97m'   # white
DIM= '\033[2m'
RST= '\033[0m'
BLD= '\033[1m'

# ── Port intelligence ─────────────────────────────────────────────────────────
# Default scan set: common attack surface + known C2/suspicious ports
DEFAULT_PORTS = [
    21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 465, 587,
    993, 995, 1080, 1337, 1433, 1521, 3306, 3389, 4443, 4444, 4445,
    5432, 5900, 6379, 7001, 7547, 8080, 8443, 8888, 9090, 9200,
    11434, 27017, 27036, 49152
]

# Port labels — anything not here gets "unknown"
PORT_LABELS = {
    21:    ('FTP',         'dim'),
    22:    ('SSH',         'ok'),
    23:    ('Telnet',      'warn'),
    25:    ('SMTP',        'dim'),
    53:    ('DNS',         'ok'),
    80:    ('HTTP',        'ok'),
    110:   ('POP3',        'dim'),
    135:   ('RPC',         'warn'),
    139:   ('NetBIOS',     'warn'),
    143:   ('IMAP',        'dim'),
    443:   ('HTTPS',       'ok'),
    445:   ('SMB',         'warn'),
    1080:  ('SOCKS',       'warn'),
    1337:  ('CUSTOM/C2',   'crit'),
    1433:  ('MSSQL',       'warn'),
    1521:  ('Oracle',      'warn'),
    3306:  ('MySQL',       'warn'),
    3389:  ('RDP',         'warn'),
    4443:  ('C2/HTTPS-alt','crit'),
    4444:  ('Meterpreter', 'crit'),
    4445:  ('C2',          'crit'),
    5432:  ('PostgreSQL',  'ok'),
    5900:  ('VNC',         'warn'),
    6379:  ('Redis',       'warn'),
    7001:  ('WebLogic',    'warn'),
    8080:  ('HTTP-alt',    'ok'),
    8443:  ('HTTPS-alt',   'ok'),
    8888:  ('Jupyter/alt', 'warn'),
    9090:  ('Custom',      'dim'),
    9200:  ('Elasticsearch','warn'),
    11434: ('Ollama/LLM',  'warn'),
    27017: ('MongoDB',     'warn'),
    27036: ('Steam',       'dim'),
}

SUSPICIOUS_PORTS = {1337, 4443, 4444, 4445}


def banner():
    sys.stdout.buffer.write((
        f"\n{C}+------------------------------------------------------+\n"
        f"|  SCAN_RANGE -- 22ND SURVEY DIVISION                 |\n"
        f"|  IP Range Automation // george wu // rainfantry     |\n"
        f"+------------------------------------------------------+{RST}\n\n"
    ).encode('utf-8'))
    sys.stdout.buffer.flush()


def parse_range(target):
    """Returns a list of IPv4Address objects from CIDR, range, or single IP."""
    hosts = []
    if '/' in target:
        net = ipaddress.IPv4Network(target, strict=False)
        hosts = list(net.hosts())
    elif '-' in target:
        parts = target.split('-')
        start = ipaddress.IPv4Address(parts[0].strip())
        # Support both "192.168.1.1-192.168.1.50" and "192.168.1.1-50"
        end_str = parts[1].strip()
        if '.' in end_str:
            end = ipaddress.IPv4Address(end_str)
        else:
            base = '.'.join(str(start).split('.')[:3])
            end = ipaddress.IPv4Address(f"{base}.{end_str}")
        current = int(start)
        while current <= int(end):
            hosts.append(ipaddress.IPv4Address(current))
            current += 1
    else:
        hosts = [ipaddress.IPv4Address(target)]
    return hosts


def probe_port(ip, port, timeout):
    """Returns True if port is open."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            return s.connect_ex((str(ip), port)) == 0
    except Exception:
        return False


def grab_banner(ip, port, timeout=2.0):
    """Try to grab a service banner."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((str(ip), port))
            if port in (80, 8080, 8443):
                s.sendall(b"HEAD / HTTP/1.0\r\nHost: target\r\n\r\n")
            data = s.recv(256)
            return data.decode(errors='replace').strip().split('\n')[0][:80]
    except Exception:
        return ''


def scan_host(ip, ports, timeout):
    """Scan a single host — returns dict with open ports or None if down."""
    # Host discovery: try top 4 ports first for speed
    discovery_ports = [22, 80, 445, 135]
    alive = any(probe_port(ip, p, timeout) for p in discovery_ports)
    if not alive:
        # Try all ports before declaring dead
        alive = any(probe_port(ip, p, timeout) for p in ports if p not in discovery_ports)
    if not alive:
        return None

    # Full port scan on confirmed-live host
    open_ports = {}
    for port in ports:
        if probe_port(ip, port, timeout):
            label, severity = PORT_LABELS.get(port, ('unknown', 'dim'))
            banner = ''
            if port in (22, 80, 8080, 21, 25):
                banner = grab_banner(ip, port)
            open_ports[port] = {
                'label': label,
                'severity': severity,
                'banner': banner
            }
    return open_ports if open_ports else {}


def run_winrecon_ssh(ip, ssh_user, ssh_key=None, winrecon_path=None):
    """SSH to host and run winrecon.ps1, return output."""
    winrecon = winrecon_path or r'C:\Users\gwu07\vader-workspace\winrecon-lab\winrecon.ps1'
    cmd = ['ssh', '-o', 'BatchMode=yes', '-o', 'StrictHostKeyChecking=no',
           '-o', 'ConnectTimeout=10']
    if ssh_key:
        cmd += ['-i', ssh_key]
    cmd += [f'{ssh_user}@{ip}',
            f'powershell -NonInteractive -ExecutionPolicy Bypass -File "{winrecon}"']
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        return result.stdout
    except subprocess.TimeoutExpired:
        return '[TIMEOUT] winrecon took >120s'
    except Exception as e:
        return f'[ERROR] {e}'


def color_port(port, info):
    sev = info['severity']
    label = info['label']
    banner = f"  {DIM}{info['banner']}{RST}" if info['banner'] else ''
    if sev == 'crit':
        return f"  {R}{BLD}{port:>5}/tcp  {label:<18}{RST}{banner}"
    elif sev == 'warn':
        return f"  {Y}{port:>5}/tcp  {label:<18}{RST}{banner}"
    elif sev == 'ok':
        return f"  {G}{port:>5}/tcp  {label:<18}{RST}{banner}"
    else:
        return f"  {DIM}{port:>5}/tcp  {label:<18}{RST}{banner}"


def assess_host(open_ports):
    """Return risk label and key findings."""
    findings = []
    risk = 'LOW'

    suspicious = [p for p in open_ports if p in SUSPICIOUS_PORTS]
    if suspicious:
        risk = 'CRITICAL'
        findings.append(f"C2/suspicious ports open: {suspicious}")

    if 3389 in open_ports:
        risk = max(risk, 'HIGH') if risk != 'CRITICAL' else 'CRITICAL'
        findings.append("RDP exposed")

    if 445 in open_ports or 139 in open_ports:
        if risk not in ('CRITICAL', 'HIGH'):
            risk = 'HIGH'
        findings.append("SMB exposed - check for EternalBlue / relay")

    if 6379 in open_ports:
        findings.append("Redis exposed - likely no auth")

    if 9200 in open_ports:
        findings.append("Elasticsearch exposed - likely no auth")

    if 11434 in open_ports:
        findings.append("Ollama LLM API exposed - unauthenticated inference")

    if 23 in open_ports:
        findings.append("Telnet - cleartext auth")

    return risk, findings


def print_host_result(ip, open_ports, elapsed):
    risk, findings = assess_host(open_ports)

    risk_color = {'CRITICAL': R, 'HIGH': Y, 'MEDIUM': C, 'LOW': G}.get(risk, W)
    print(f"\n{BLD}{W}+- {ip}{RST}  {risk_color}[{risk}]{RST}  {DIM}{elapsed:.1f}s{RST}")

    if not open_ports:
        print(f"  {DIM}(alive - no open ports in scan set){RST}")
    else:
        for port in sorted(open_ports.keys()):
            print(color_port(port, open_ports[port]))

    for f in findings:
        print(f"  {R}[!] {f}{RST}")


def main():
    ap = argparse.ArgumentParser(description='22DIV IP Range Scanner')
    ap.add_argument('target', help='CIDR, range (x.x.x.x-y), or single IP')
    ap.add_argument('--ports', help='Comma-separated ports', default=None)
    ap.add_argument('--threads', type=int, default=64)
    ap.add_argument('--timeout', type=float, default=0.8)
    ap.add_argument('--ssh-user', help='SSH username for winrecon')
    ap.add_argument('--ssh-key', help='SSH key path')
    ap.add_argument('--winrecon', action='store_true', help='Run winrecon on SSH-accessible Windows hosts')
    ap.add_argument('--json', action='store_true', help='Save JSON report')
    ap.add_argument('--quiet', action='store_true')
    args = ap.parse_args()

    ports = [int(p) for p in args.ports.split(',')] if args.ports else DEFAULT_PORTS

    if not args.quiet:
        banner()

    try:
        hosts = parse_range(args.target)
    except Exception as e:
        print(f"{R}[ERROR] Invalid target: {e}{RST}")
        sys.exit(1)

    print(f"{C}[*]{RST} Target:  {W}{args.target}{RST}  ({len(hosts)} hosts)")
    print(f"{C}[*]{RST} Ports:   {len(ports)} ports  ({min(ports)}-{max(ports)})")
    print(f"{C}[*]{RST} Threads: {args.threads}  Timeout: {args.timeout}s")
    print(f"{C}[*]{RST} Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    results = {}
    live_count = 0
    start_time = time.time()

    def scan_one(ip):
        t0 = time.time()
        open_ports = scan_host(ip, ports, args.timeout)
        elapsed = time.time() - t0
        return str(ip), open_ports, elapsed

    print(f"{DIM}Scanning...{RST}")
    with ThreadPoolExecutor(max_workers=args.threads) as ex:
        futures = {ex.submit(scan_one, ip): ip for ip in hosts}
        for future in as_completed(futures):
            ip_str, open_ports, elapsed = future.result()
            if open_ports is None:
                continue  # host down
            live_count += 1
            results[ip_str] = {'ports': open_ports, 'elapsed': elapsed}
            print_host_result(ip_str, open_ports, elapsed)

    total_time = time.time() - start_time
    print(f"\n{C}------------------------------------------------------{RST}")
    print(f"{G}[+]{RST} Scan complete: {W}{live_count}/{len(hosts)}{RST} hosts up  |  {total_time:.1f}s total")

    # Summary of critical findings
    crits = [(ip, d) for ip, d in results.items()
             if any(p in SUSPICIOUS_PORTS for p in d['ports'])]
    if crits:
        print(f"\n{R}{BLD}[!] CRITICAL FINDINGS:{RST}")
        for ip, d in crits:
            bad = [p for p in d['ports'] if p in SUSPICIOUS_PORTS]
            labels = [PORT_LABELS.get(p, ('?',''))[0] for p in bad]
            print(f"  {R}{ip}{RST}  ->  ports {bad} ({labels})")

    # Optional winrecon over SSH
    if args.winrecon and args.ssh_user:
        ssh_candidates = [ip for ip, d in results.items()
                          if 22 in d['ports'] and 445 in d['ports']]
        if ssh_candidates:
            print(f"\n{C}[*]{RST} Running winrecon on {len(ssh_candidates)} Windows hosts via SSH...")
            for ip in ssh_candidates:
                print(f"\n{C}[WINRECON] {ip}{RST}")
                output = run_winrecon_ssh(ip, args.ssh_user, args.ssh_key)
                print(output[:3000])  # cap output
                results[ip]['winrecon'] = output

    # JSON output
    if args.json:
        ts = datetime.now().strftime('%Y%m%d_%H%M%S')
        fname = f"scan_{ts}.json"
        with open(fname, 'w') as f:
            json.dump({
                'target': args.target,
                'timestamp': ts,
                'hosts_scanned': len(hosts),
                'hosts_live': live_count,
                'results': {
                    ip: {
                        'ports': {str(p): v for p, v in d['ports'].items()},
                        'winrecon': d.get('winrecon', '')
                    }
                    for ip, d in results.items()
                }
            }, f, indent=2)
        print(f"\n{G}[+]{RST} JSON report saved: {W}{fname}{RST}")

    return results


if __name__ == '__main__':
    main()
