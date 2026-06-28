#!/usr/bin/env python3
"""
22nd Survey Division — POC Tester
SSH to lab machines, run commands, capture real output for widgets.

Usage:
    python poc_tester.py --module 12 --machine 192.168.1.92 --commands "whoami,tasklist"
"""

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime

LAB_DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "lab_data")

# Machine configs
MACHINES = {
    "192.168.1.92": {
        "name": "LAPTOP-R32M8MLI",
        "user": "gwu07",
        "cpu": "Intel",
        "av": "Kaspersky ON, Defender OFF",
        "role": "Real-world target"
    },
    "192.168.1.42": {
        "name": "WUPC",
        "user": "swu",
        "cpu": "AMD Ryzen 7 3700X",
        "av": "No AV, Firewall OFF",
        "role": "Clean sandbox"
    },
    "192.168.1.145": {
        "name": "RADON",
        "user": "ghaleb jomma",
        "cpu": "Unknown",
        "av": "Unknown",
        "role": "Authorized target"
    }
}


def ssh_command(ip, user, command, timeout=30):
    """Run a command via SSH and return output."""
    ssh_cmd = [
        "ssh",
        "-o", "StrictHostKeyChecking=no",
        "-o", "ConnectTimeout=5",
        "-o", "BatchMode=yes",
        f"{user}@{ip}",
        command
    ]
    
    try:
        result = subprocess.run(
            ssh_cmd,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "exit_code": result.returncode,
            "success": result.returncode == 0
        }
    except subprocess.TimeoutExpired:
        return {
            "stdout": "",
            "stderr": "SSH timeout",
            "exit_code": -1,
            "success": False
        }
    except Exception as e:
        return {
            "stdout": "",
            "stderr": str(e),
            "exit_code": -1,
            "success": False
        }


def test_machine(ip, commands):
    """Test all commands on a machine and collect output."""
    machine = MACHINES.get(ip, {})
    user = machine.get("user", "gwu07")
    
    print(f"[*] Testing {machine.get('name', ip)} ({ip})...")
    
    results = {
        "machine": machine.get("name", ip),
        "ip": ip,
        "cpu": machine.get("cpu", "Unknown"),
        "av_status": machine.get("av", "Unknown"),
        "timestamp": datetime.now().isoformat(),
        "commands": []
    }
    
    for cmd in commands:
        print(f"  [>] {cmd}")
        output = ssh_command(ip, user, cmd)
        
        results["commands"].append({
            "command": cmd,
            "output": output["stdout"],
            "error": output["stderr"],
            "exit_code": output["exit_code"],
            "success": output["success"]
        })
        
        if output["success"]:
            print(f"  [+] Success ({len(output['stdout'])} chars)")
        else:
            print(f"  [-] Failed: {output['stderr'][:100]}")
    
    return results


def save_lab_data(module_id, data):
    """Save lab data to JSON file."""
    os.makedirs(LAB_DATA_DIR, exist_ok=True)
    filename = f"module_{module_id:02d}_data.json"
    filepath = os.path.join(LAB_DATA_DIR, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"[+] Lab data saved: {filepath}")
    return filepath


def main():
    parser = argparse.ArgumentParser(description="22nd Survey Division POC Tester")
    parser.add_argument("--module", type=int, required=True, help="Module ID")
    parser.add_argument("--machine", type=str, required=True, help="Target IP (192.168.1.92, .42, .145)")
    parser.add_argument("--commands", type=str, required=True, help="Comma-separated commands")
    parser.add_argument("--tab", type=str, default="demo", help="Which tab this data belongs to")
    
    args = parser.parse_args()
    
    commands = [c.strip() for c in args.commands.split(",")]
    
    # Test the machine
    results = test_machine(args.machine, commands)
    
    # Structure for widget generator
    lab_data = {
        args.tab: {
            "commands": [
                {
                    "command": cmd["command"],
                    "output": cmd["output"],
                    "note": f"Exit code: {cmd['exit_code']}" if not cmd["success"] else ""
                }
                for cmd in results["commands"]
            ]
        }
    }
    
    # Save
    filepath = save_lab_data(args.module, lab_data)
    
    print(f"[+] Module {args.module:02d} POC data collected")
    print(f"[+] Machine: {results['machine']} ({results['cpu']})")
    print(f"[+] AV: {results['av_status']}")
    print(f"[+] Commands: {len(results['commands'])}")
    print(f"[+] Output: {filepath}")


if __name__ == "__main__":
    main()
