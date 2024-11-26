'''
Creating a simple server with some added functionality
'''
import socket
import random

#used IPV4 for continious streams of data
server_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 3003))
server_socket.listen()
print('Server is running on locahost:3003')

# listen for new incomming connnections
while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection received from {addr}")
    
    #read incoming data with buffer max size of 1024 bytes
    request_line = client_socket.recv(1024).decode()
    
    
    #ignore favicons and empty requests
    if (not request_line) or ('favicon.ico' in request_line):
        client_socket.close()
        continue

    roll = random.randint(1, 6)

    path_and_params = request_line.splitlines()[0]
    http_method, path_and_params, _ = path_and_params.split(" ")
    print(f'http_method = {http_method}, path_and_params = {path_and_params}, others = {_}')
    path, params = path_and_params.split("?")

    params = params.split("&")
    params_dict = {}
    for param in params:
        key, value = param.split("=")
        params_dict[key] = value
    
    rolls = int(params_dict.get('rolls', '1'))
    sides = int(params_dict.get('sides', '6'))

    response = ("HTTP/1.1 200 OK\r\n"
            "Content-Type: text/plain\r\n"
            "\r\n"
            f"Request Line: {path_and_params}\n"
            f"HTTP Method: {http_method}\n"
            f"Path: {path}\n"
            f"Parameters {params_dict}\n")
    
    for _ in range(rolls):
        roll = random.randint(1, sides)
        response += f'Roll: {roll}\n'
    
    #send response to client and close connection
    client_socket.sendall(response.encode())
    client_socket.close()