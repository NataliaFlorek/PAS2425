import socket


def udp_client(server_ip='127.0.0.1', server_port=5555):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        ip_address = input("Podaj adres IP: ")
        client_socket.sendto(ip_address.encode('utf-8'), (server_ip, server_port))

        hostname, _ = client_socket.recvfrom(1024)
        print(f"Odpowiedź serwera: {hostname.decode('utf-8')}")


if __name__ == "__main__":
    udp_client()