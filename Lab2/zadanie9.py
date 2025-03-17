#Lab2/ Zadanie 9
import socket


def udp_client():
    server_address = ('127.0.0.1', 2906)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        ip_address = socket.gethostbyname(socket.gethostname())
        sock.sendto(ip_address.encode(), server_address)
        data, _ = sock.recvfrom(1024)
        print(f"Hostname: {data.decode()}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        sock.close()


if __name__ == "__main__":
    udp_client()