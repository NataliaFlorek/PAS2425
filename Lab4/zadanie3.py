#Lab 4/ Zadanie 8
import socket


def start_udp_echo_server(host='127.0.0.1', port=5555):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((host, port))
        print(f"Serwer UDP echo działa na {host}:{port}")

        while True:
            data, addr = server_socket.recvfrom(1024)
            print(f"Odebrano od {addr}: {data.decode()}")
            server_socket.sendto(data, addr)
            print(f"Odesłano do {addr}: {data.decode()}")


if __name__ == "__main__":
    start_udp_echo_server()
