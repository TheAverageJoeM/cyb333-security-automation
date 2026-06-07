# Import the socket module (lower level network communication)
import socket

# Server information
server_ip = "127.0.0.1"
server_port = 5000

# Create the server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Attach the server to the IP address and port
    server.bind((server_ip, server_port))

    # Start listening for connections
    server.listen(1)

    print("Server is listening on port 5000...")

    # Wait for a client to connect
    connection, address = server.accept()

    print("Client connected:", address)

    # Keep receiving messages until the connection closes
    while True:

        # Receive data from the client
        message = connection.recv(1024).decode()

        # If nothing is received, the client disconnected
        if message == "":
            print("Client disconnected.")
            break

        print("Client says:", message)

        # Close the connection if the user types quit
        if message.lower() == "quit":
            connection.send("Goodbye!".encode())
            print("Closing connection.")
            break

        # Send a response back to the client
        reply = "Message received: " + message
        connection.send(reply.encode())

# Handle errors
except Exception as error:
    print("An error happened:", error)

# Close connections when finished
connection.close()
server.close()
