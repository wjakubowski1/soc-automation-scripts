import socket
import sys
from datetime import datetime

# Check if an argument (target IP) was provided during execution
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Error! Usage: python3 port_scanner.py <Target_IP>")
    sys.exit()

# Display a nice banner with start information
print("-" * 50)
print("Scanning target: " + target)
print("Start time: " + str(datetime.now()))
print("-" * 50)

# List of common ports to scan (for quick execution)
# 21 (FTP), 22 (SSH), 80 (HTTP), 135 (RPC), 139 (NetBIOS), 443 (HTTPS), 445 (SMB), 3389 (RDP)
ports_to_scan = [21, 22, 80, 135, 139, 443, 445, 3389]

try:
    for port in ports_to_scan:
        # Create a socket using IPv4 (AF_INET) and TCP (SOCK_STREAM)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a 1-second timeout so the script doesn't hang on closed ports
        socket.setdefaulttimeout(1)
        
        # Attempt to connect. The connect_ex function returns '0' if successful.
        result = s.connect_ex((target, port))
        
        if result == 0:
            print(f"[*] Port {port} is OPEN")
            
        # Close the connection to clean up
        s.close()

# Error handling (e.g., when Ctrl+C is pressed)
except KeyboardInterrupt:
    print("\nProgram interrupted (Ctrl+C). Exiting.")
    sys.exit()
except socket.error:
    print("\nError: Could not connect to the server. Host may be down or IP is invalid.")
    sys.exit()

print("-" * 50)
print("Scanning completed!")
