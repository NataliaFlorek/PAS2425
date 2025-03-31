import socket


def udp_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"Serwer UDP nasłuchuje na porcie {port}...")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        print(f"Połączono z {client_address}")
        server_socket.sendto(data, client_address)  # echo


if __name__ == "__main__":
    udp_server('127.0.0.1', 12346)
