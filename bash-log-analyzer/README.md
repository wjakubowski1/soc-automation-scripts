# SSH Log Analyzer

A simple script written in Bash, created as part of learning task automation in a SOC environment (Blue Team).

## What does this script do?

The script searches Linux system logs (`/var/log/auth.log` or test files) for failed SSH login attempts. It uses pipes and system tools such as `grep`, `awk`, `sort`, and `uniq` to extract and count the IP addresses of potential attackers (Brute Force).

## How to run it?

1. Grant execution permissions: `chmod +x analizator.sh`
2. Run the script: `./analizator.sh`
