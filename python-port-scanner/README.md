# Custom Python Port Scanner

A lightweight, custom-built TCP port scanner developed in Python. Created as part of understanding Red Team reconnaissance techniques and network socket programming.

## What does this script do?

This script utilizes the Python `socket` library to perform a rapid TCP connect scan against a target IP address. It is configured to check the most common ports associated with network vulnerabilities and active services (e.g., FTP, SSH, HTTP, SMB, RDP). The script includes built-in timeout handling to bypass firewalled or unresponsive ports efficiently.

## Technologies Used
* **Language:** Python 3
* **Libraries:** `socket`, `sys`, `datetime`
* **Target Environment:** Tested against a Windows Server 2025 Domain Controller in a local homelab.

## How to run it?

1. Ensure you have Python 3 installed.
2. Run the script via terminal, providing the target IP address as an argument:
   ```bash
   python3 port_scanner.py <Target_IP>
