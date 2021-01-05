import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
server.bind(('127.0.0.1', 8080))
server.listen(10)

while True:
    client_sock, client_address = server.accept()
    print('Connected by ', client_address)

    while True:
        data = client_sock.recv(1024)
        if not data:
            break
        client_sock.sendall(data)

    client_sock.close()
