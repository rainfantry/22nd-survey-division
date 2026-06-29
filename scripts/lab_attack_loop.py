#!/usr/bin/env python3
"""
22ND SURVEY DIVISION — Attack/Detect/Teach Loop Controller
Operator: SERVITOR
Purpose: Run benign attacks on lab machines and capture defensive recon output
"""

import subprocess
import json
import datetime
import sys
import os

LABS = {
    "wupc": {"ip": "192.168.1.42", "user": "SWu"},
    "host": {"ip": "192.168.1.92", "user": "gwu07"},
}

LOG_FILE = "C:\\Users\\gwu07\\Desktop\\repos\\22nd-survey-division\\scripts\\lab_attack_loop.log"

def log(msg):
    ts = datetime.datetime.utcnow().isoformat()
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")

def ssh_run(host, user, cmd):
    full_cmd = [
        "ssh",
        "-o", "StrictHostKeyChecking=no",
        "-o", "ConnectTimeout=10",
        f"{user}@{host}",
        cmd
    ]
    try:
        result = subprocess.run(full_cmd, capture_output=True, text=True, timeout=30)
        return {
            "cmd": " ".join(full_cmd),
            "stdout": result.stdout,
            "stderr": result.stderr,
            "rc": result.returncode
        }
    except Exception as e:
        return {"cmd": " ".join(full_cmd), "error": str(e), "rc": -1}

def main():
    log("=== ATTACK/DETECT/TEACH LOOP STARTED ===")
    
    # Attack 1: Start a benign Python listener on WUPC .42
    log("[ATTACK 1] Starting benign Python reverse listener on WUPC .42 port 9999")
    attack_cmd = """
$listener = [System.Net.Sockets.TcpListener]::new([System.Net.IPAddress]::Any, 9999);
$listener.Start();
Write-Host "Listener started on port 9999";
$client = $listener.AcceptTcpClient();
$stream = $client.GetStream();
$writer = [System.IO.StreamWriter]::new($stream);
$writer.WriteLine((whoami));
$writer.Flush();
$client.Close();
$listener.Stop();
"""
    # Fire-and-forget listener in background
    listener_result = ssh_run(LABS["wupc"]["ip"], LABS["wupc"]["user"], f'powershell -Command "{attack_cmd}"')
    log(f"Listener start result: rc={listener_result.get('rc')} stdout={listener_result.get('stdout','')[:200]}")
    
    # Detection 1: netstat shows new listener
    log("[DETECT 1] Running netstat on WUPC .42")
    netstat_result = ssh_run(LABS["wupc"]["ip"], LABS["wupc"]["user"], "netstat -ano | findstr 9999")
    log(f"netstat result: {netstat_result.get('stdout','')[:500]}")
    
    # Detection 2: process identification
    log("[DETECT 2] Identifying process owning port 9999")
    proc_result = ssh_run(LABS["wupc"]["ip"], LABS["wupc"]["user"], "powershell -Command \"Get-NetTCPConnection -LocalPort 9999 | Select-Object LocalAddress, LocalPort, OwningProcess, State | Format-Table -AutoSize\"")
    log(f"process result: {proc_result.get('stdout','')[:500]}")
    
    # Detection 3: command line of suspicious process
    log("[DETECT 3] Getting command line of suspicious process")
    cmdline_result = ssh_run(LABS["wupc"]["ip"], LABS["wupc"]["user"], "powershell -Command \"$p=(Get-NetTCPConnection -LocalPort 9999).OwningProcess; Get-CimInstance Win32_Process -Filter \\\"ProcessId=$p\\\" | Select-Object Name, ProcessId, CommandLine | Format-Table -AutoSize\"")
    log(f"cmdline result: {cmdline_result.get('stdout','')[:500]}")
    
    # Cleanup
    log("[CLEANUP] Stopping listener on WUPC .42")
    cleanup_result = ssh_run(LABS["wupc"]["ip"], LABS["wupc"]["user"], "powershell -Command \"Get-NetTCPConnection -LocalPort 9999 -ErrorAction SilentlyContinue | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue }\"")
    log(f"cleanup result: rc={cleanup_result.get('rc')}")
    
    log("=== LOOP COMPLETE ===")

if __name__ == "__main__":
    main()
