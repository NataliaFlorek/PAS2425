import socket
import time


def tcp_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    message = b'Hello, Server!'
    start_time = time.time()

    client_socket.sendall(message)
    data = client_socket.recv(1024)

    end_time = time.time()
    print(f"Otrzymano: {data.decode()}")
    print(f"Czas przesyłania TCP: {end_time - start_time:.6f} sekund")

    client_socket.close()


if __name__ == "__main__":
    tcp_client('127.0.0.1', 12345)
