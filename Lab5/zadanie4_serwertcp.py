import socket


def tcp_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Serwer TCP nasłuchuje na porcie {port}...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Połączono z {client_address}")
        data = client_socket.recv(1024)
        if data:
            client_socket.sendall(data)  # echo
        client_socket.close()


if __name__ == "__main__":
    tcp_server('127.0.0.1', 12345)
