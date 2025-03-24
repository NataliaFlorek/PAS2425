import socket


def query_server(server_host='127.0.0.1', server_port=5555):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        hostname = input("Podaj nazwę hosta: ").strip()

        client_socket.sendto(hostname.encode(), (server_host, server_port))

        data, _ = client_socket.recvfrom(1024)
        ip_address = data.decode()

        print(f"Adres IP dla {hostname}: {ip_address}")

    except Exception as e:
        print(f"Błąd: {e}")

    finally:
        client_socket.close()


if __name__ == "__main__":
    query_server()
