#Lab 4/ Zadanie 6
import socket


def start_server(host='127.0.0.1', port=5555):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print(f"Serwer UDP nasłuchuje na {host}:{port}")

    while True:
        try:
            data, client_address = server_socket.recvfrom(1024)
            hostname = data.decode().strip()
            print(f"Otrzymano zapytanie o hostname: {hostname} od {client_address}")

            try:
                ip_address = socket.gethostbyname(hostname)
            except socket.gaierror:
                ip_address = "Nie znaleziono IP"

            server_socket.sendto(ip_address.encode(), client_address)
            print(f"Odesłano IP: {ip_address} do {client_address}")

        except KeyboardInterrupt:
            print("Serwer UDP zatrzymany.")
            break

    server_socket.close()


if __name__ == "__main__":
    start_server()