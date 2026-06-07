# Import modules needed for scanning
import socket
import time
from datetime import datetime

# Approved hosts for the assignment
allowed_hosts = [
    "localhost",
    "127.0.0.1",
    "scanme.nmap.org"
]

print("Basic Python Port Scanner")
print("Scan started:", datetime.now())

# Ask the user which host to scan
target = input("Enter target host: ")

# Verify the host is allowed
if target not in allowed_hosts:
    print("Error: You are only allowed to scan localhost, 127.0.0.1, or scanme.nmap.org.")

else:
    try:
        # Ask for beginning and ending ports
        start_port = int(input("Enter starting port: "))
        end_port = int(input("Enter ending port: "))

        # Validate port numbers
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            print("Error: Invalid port range.")

        else:
            print("Scanning", target)

            # Check each port in the selected range
            for port in range(start_port, end_port + 1):

                # Create a socket for testing the port
                scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                # Prevent long wait times
                scanner.settimeout(1)

                # Try connecting to the port
                result = scanner.connect_ex((target, port))

                # A result of 0 means the port is open
                if result == 0:
                    print("Port", port, "is OPEN")
                else:
                    print("Port", port, "is CLOSED")

                # Close the scanner socket
                scanner.close()

                # Small delay between scans
                time.sleep(0.1)

            print("Scan finished.")

    # Error if a user enters letters instead of numbers
    except ValueError:
        print("Error: Ports must be numbers.")

    # Error if the host name cannot be found
    except socket.gaierror:
        print("Error: Host could not be found.")

    # Catch any other errors
    except Exception as error:
        print("An error happened:", error)