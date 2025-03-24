#Lab 4/Zadanie 5
import socket


def get_hostname(ip_address):
    try:
        return socket.gethostbyaddr(ip_address)[0]
    except socket.herror:
        return "Hostname not found"


def udp_server(host='127.0.0.1', port=5555):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((host, port))
        print(f"Serwer nasłuchuje na {host}:{port}")

        while True:
            data, client_address = server_socket.recvfrom(1024)
            ip_address = data.decode('utf-8')
            print(f"Otrzymano IP: {ip_address} od {client_address}")

            hostname = get_hostname(ip_address)
            server_socket.sendto(hostname.encode('utf-8'), client_address)
            print(f"Wysłano hostname: {hostname} do {client_address}")


if __name__ == "__main__":
    udp_server()
