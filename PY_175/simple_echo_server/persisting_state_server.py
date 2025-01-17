import socket
import random

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 3003))
server_socket.listen()

print("Server is running on localhost:3003")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    request_line = client_socket.recv(1024).decode()
    if not request_line or 'favicon.ico' in request_line:
        client_socket.close()
        continue

    path_and_params = request_line.splitlines()[0]
    http_method, path_and_params, _ = path_and_params.split(" ")
    if "?" in path_and_params:
        path, params = path_and_params.split("?")
    else:
        path = path_and_params
        params = "number=0"  #set a default parameter value to 0 so we can split it.

    params = params.split("&")
    params_dict = {}
    for param in params:
        key, value = param.split("=")
        params_dict[key] = value
    
    # the the value of the current key for number else 0
    number = int(params_dict.get('number', 0))

    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html\r\n"
        "\r\n"
        "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        "<html><head><title>Counter</title></head><body>"
        f"<h1>HTTP Request Information:</h1>"
        f"<p><strong>Request Line:</strong> {path_and_params}</p>"
        f"<p><strong>HTTP Method:</strong> {http_method}</p>"
        f"<p><strong>Path:</strong> {path}</p>"
        f"<p><strong>Parameters:</strong> {params_dict}</p>"
        "<h2>Counter:</h2>"
        f'<p style ="color: red;"> The current value of number is: {number} </p>'
        f"<a href='?number={number + 1}'>Add one</a>"
        "&nbsp;&nbsp;"
        f"<a href='?number={number - 1}'>Subtract one</a>"
        "</body></html>"
    )

    client_socket.sendall(response.encode())
    client_socket.close()