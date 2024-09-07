# imports
import socket

# Server details
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # allows the socket to reuse an address without waiting for default timeout

server_socket.bind((SERVER_HOST, SERVER_PORT))
# 0.0.0.0 allows the server to be accessed by any device on the network,
# 8080 is the port, servers normally listen on port 80 for requests

server_socket.listen(5) # Max 5 connections can queue to connect
print(f"Listening on port {SERVER_PORT} ...") # Initial msg

while True: # With setblock being false, server will crash if no connections are queued
    # Accept client connections
    client_socket, client_address = server_socket.accept()
    request = client_socket.recv(1500).decode() # Accept http request and store as string
    print(request)
    headers = request.split('\n') # store http request as a string and split
    first_header_components = headers[0].split() # sotre first line of the request as string and split 
    http_request_method = first_header_components[0] # determine request type (POST, GET, DELETE ETC)
    path = first_header_components[1] # where are they coming to on the server
    
    if http_request_method == 'GET':
        if path == '/': # serve local content to the client
            fin = open('index.html')
            content = fin.read()
            fin.close()
            response = 'HTTP/1.1 200 OK \n\n' + content
            
        elif path == '/portfolio': # redirect client to portfolio site on Github Pages
            response = 'HTTP/1.1 302 Found\nLocation: https://kiancurranmahon.github.io/\n\n'
        else:
            pass # handle edge case
    else:
        response = 'HTTP/1.1 405 Method Not Allowed \n\n Allow: GET' # request rejected

    client_socket.sendall(response.encode()) # sends data to client
    client_socket.close() # close client connection

# Close server socket
server_socket.close()