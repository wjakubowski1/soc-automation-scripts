# SOC Automation & Security Scripts

Welcome to my repository! This is a collection of scripts and tools I create and maintain while learning the fundamentals of task automation for SOC (Security Operations Center) and Blue Team operations.

## Project Structure:

* `/bash-log-analyzer` - A Linux (Bash) script that automatically parses system logs (`auth.log`) and extracts the IP addresses of attackers using Brute Force methods over the SSH protocol.
* `/python-vt-checker` - A Python script integrating with the VirusTotal API. It checks selected IP addresses for their reputation and flags potential threats.
* `/ActiveDirectory-Auto-Defender` - A custom SOAR PowerShell script that monitors Windows Server Event Logs for failed logons (Event ID `4625`) and dynamically deploys Windows Firewall rules to block malicious IPs.

## Technologies & Tools:

* Bash (grep, awk, sort, uniq)
* Python 3 (requests, venv, API handling)
* PowerShell (Get-WinEvent, NetFirewallRule)
* Git / GitHub
* Linux Ubuntu & Windows Server 2025
