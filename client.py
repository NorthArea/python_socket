import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))
client.sendall(b'Hello world!')
data = client.recv(1024)
client.close()
print('Received: ', repr(data))
