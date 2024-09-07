import socket

# Server details
SERVER_HOST = "0.0.0.0"
SERVER_PORT = "8080"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # allows the socket to reuse an address without waiting for default timeout

server_socket.bind((SERVER_HOST, SERVER_PORT))
# 0.0.0.0 allows the server to be accessed by any device on the network,
# 8080 is the port, servers normally listen on port 80 for requests

server_socket.listen(5) # Max 5 connections can queue to connect
print("Listening on port {SERVER_PORT} ...") # Inital msg