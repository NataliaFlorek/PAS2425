import socket
import time


def udp_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message = b'Hello, Server!'
    start_time = time.time()

    client_socket.sendto(message, (host, port))
    data, server_address = client_socket.recvfrom(1024)

    end_time = time.time()
    print(f"Otrzymano: {data.decode()}")
    print(f"Czas przesyłania UDP: {end_time - start_time:.6f} sekund")

    client_socket.close()


if __name__ == "__main__":
    udp_client('127.0.0.1', 12346)
