import requests
import sys

# VirusTotal API IoC Checker
# This script checks the reputation of a given IP address using the VirusTotal API.

# Insert your personal API key here
API_KEY = "YOUR_API_KEY_HERE"
URL = "https://www.virustotal.com/api/v3/ip_addresses/"

# Check if an IP address was provided as an argument
if len(sys.argv) != 2:
    print("Error! Usage: python3 vt_checker.py <IP_ADDRESS>")
    sys.exit()

target_ip = sys.argv[1]
headers = {
    "accept": "application/json",
    "x-apikey": API_KEY
}

print("-" * 50)
print(f"[*] Querying VirusTotal API for IP: {target_ip}")
print("-" * 50)

try:
    response = requests.get(URL + target_ip, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        stats = data['data']['attributes']['last_analysis_stats']
        
        print("[+] Scan Results:")
        print(f"    - Malicious:  {stats['malicious']}")
        print(f"    - Suspicious: {stats['suspicious']}")
        print(f"    - Undetected: {stats['undetected']}")
    else:
        print(f"[-] API Request Error. Status code: {response.status_code}")

except Exception as e:
    print(f"[-] An error occurred: {e}")

print("-" * 50)
