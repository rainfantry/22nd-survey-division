#!/usr/bin/env python3
"""
22nd Survey Division — Git Push & Verify
Automated deploy with URL verification.

Usage:
    python git_push.py --files widgets/module_12_widget.html --verify
"""

import argparse
import os
import subprocess
import sys
import time
from urllib.request import urlopen
from urllib.error import HTTPError

REPO_DIR = os.path.join(os.path.dirname(__file__), "..")
RAW_URL = "https://raw.githubusercontent.com/rainfantry/22nd-survey-division/main"
PAGES_URL = "https://rainfantry.github.io/22nd-survey-division"


def run_git_command(args, cwd=None):
    """Run a git command and return result."""
    cmd = ["git"] + args
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=cwd or REPO_DIR
        )
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "exit_code": result.returncode,
            "success": result.returncode == 0
        }
    except Exception as e:
        return {
            "stdout": "",
            "stderr": str(e),
            "exit_code": -1,
            "success": False
        }


def check_url(url, timeout=10):
    """Check if a URL returns 200."""
    try:
        response = urlopen(url, timeout=timeout)
        return response.status == 200
    except HTTPError as e:
        return e.code == 200
    except Exception:
        return False


def push_files(files, message):
    """Add, commit, and push files."""
    print(f"[*] Adding files...")
    for f in files:
        result = run_git_command(["add", f])
        if not result["success"]:
            print(f"[-] Failed to add {f}: {result['stderr']}")
            return False
        print(f"  [+] Added {f}")
    
    print(f"[*] Committing...")
    result = run_git_command(["commit", "-m", message])
    if not result["success"]:
        print(f"[-] Commit failed: {result['stderr']}")
        return False
    print(f"  [+] Committed: {message}")
    
    print(f"[*] Pushing to origin/main...")
    result = run_git_command(["push", "origin", "main"])
    if not result["success"]:
        print(f"[-] Push failed: {result['stderr']}")
        return False
    print(f"  [+] Pushed successfully")
    
    return True


def verify_live(files, max_retries=5, delay=10):
    """Verify files are live on GitHub Pages."""
    print(f"[*] Verifying live URLs...")
    
    for f in files:
        # Check raw URL first (faster)
        raw_file_url = f"{RAW_URL}/{f}"
        print(f"  [>] Checking raw: {raw_file_url}")
        
        for attempt in range(max_retries):
            if check_url(raw_file_url):
                print(f"  [+] Raw URL OK (attempt {attempt + 1})")
                break
            else:
                print(f"  [-] Raw URL not ready (attempt {attempt + 1}/{max_retries})")
                if attempt < max_retries - 1:
                    time.sleep(delay)
        else:
            print(f"  [-] Raw URL failed after {max_retries} attempts")
            return False
        
        # Check Pages URL
        pages_url = f"{PAGES_URL}/{f}"
        print(f"  [>] Checking Pages: {pages_url}")
        
        for attempt in range(max_retries):
            if check_url(pages_url):
                print(f"  [+] Pages URL OK (attempt {attempt + 1})")
                break
            else:
                print(f"  [-] Pages URL not ready (attempt {attempt + 1}/{max_retries})")
                if attempt < max_retries - 1:
                    time.sleep(delay)
        else:
            print(f"  [-] Pages URL failed after {max_retries} attempts")
            return False
    
    return True


def main():
    parser = argparse.ArgumentParser(description="22nd Survey Division Git Push & Verify")
    parser.add_argument("--files", type=str, required=True, help="Comma-separated file paths")
    parser.add_argument("--message", type=str, default="Update course widgets", help="Commit message")
    parser.add_argument("--verify", action="store_true", help="Verify live URLs after push")
    
    args = parser.parse_args()
    
    files = [f.strip() for f in args.files.split(",")]
    
    # Push
    if not push_files(files, args.message):
        print("[-] Push failed. Aborting.")
        sys.exit(1)
    
    # Verify
    if args.verify:
        if verify_live(files):
            print("[+] All files verified live!")
        else:
            print("[-] Verification failed. Check URLs manually.")
            sys.exit(1)
    
    print("[+] Deploy complete.")


if __name__ == "__main__":
    main()
