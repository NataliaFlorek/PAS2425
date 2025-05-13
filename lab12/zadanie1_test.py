import socket

host = '127.0.0.1'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

client_socket.sendall(b'Hello, Server!')

response = client_socket.recv(1024)
print(f"Otrzymana odpowiedź: {response.decode()}")

client_socket.close()
