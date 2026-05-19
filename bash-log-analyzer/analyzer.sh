#!/bin/bash

# SSH Brute Force Log Analyzer
# This script parses the auth.log file to find and count failed SSH login attempts.

LOG_FILE="/var/log/auth.log"

echo "[*] Initializing SSH Log Analyzer..."
echo "[*] Searching for failed login attempts in $LOG_FILE"
echo "---------------------------------------------------"

# Extracting IP addresses from 'Failed' lines, sorting, and counting unique occurrences
cat "$LOG_FILE" | grep "Failed" | awk '{print $11}' | sort | uniq -c | sort -nr

echo "---------------------------------------------------"
echo "[*] Analysis complete."
