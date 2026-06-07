# Import the socket module (lower level network communication)
import socket

# Server information
server_ip = "127.0.0.1"
server_port = 5000

# Create the client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    print("Connecting to server...")

    # Connect to the server
    client.connect((server_ip, server_port))

    print("Connected.")

    # Continue sending messages until quit is entered
    while True:

        # Ask the user for a message
        message = input("Type a message or type quit: ")

        # Send the message to the server
        client.send(message.encode())

        # Receive a response from the server
        reply = client.recv(1024).decode()

        print("Server says:", reply)

        # Exit if the user enters quit
        if message.lower() == "quit":
            print("Disconnecting.")
            break

# Error if the server is not running
except ConnectionRefusedError:
    print("Could not connect. Make sure the server is running.")

# Handle any other errors
except Exception as error:
    print("An error happened:", error)

# Close the client socket
client.close()