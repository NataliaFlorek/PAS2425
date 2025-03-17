#Lab 2/ Zadanie 10

import socket


def udp_client():
    server_address = ('127.0.0.1', 2907)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        hostname = socket.gethostname()  
        print(f"Wysyłanie nazwy hosta: {hostname}")
        client_socket.sendto(hostname.encode(), server_address)
        data, _ = client_socket.recvfrom(1024)
        ip_address = data.decode()
        print(f"Otrzymany adres IP: {ip_address}")

    except Exception as e:
        print(f"Błąd: {e}")
    finally:
        client_socket.close()


if __name__ == "__main__":
    udp_client()