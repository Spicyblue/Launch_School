'''
Creating a simple server
'''
import socket

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

    path_and_params = request_line.splitlines()[0]
    response = ("HTTP/1.1 200 OK\r\n"
            "Content-Type: text/plain\r\n"
            "\r\n"
            f"{path_and_params}\n")
    
    #send response to client and close connection
    client_socket.sendall(response.encode())
    client_socket.close()