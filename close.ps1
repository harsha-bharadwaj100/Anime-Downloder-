Get-CimInstance Win32_Process -Filter "CommandLine LIKE '%chrome.exe%--headless%'" | %{Stop-Process $_.ProcessId}