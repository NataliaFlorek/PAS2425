#Lab 4/Zadanie 2

import socket


def start_echo_server(host='127.0.0.1', port=5555):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Serwer echo działa na {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Połączono z {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(f"Odebrano: {data.decode()}")
                    conn.sendall(data)  
                    print(f"Odesłano: {data.decode()}")


if __name__ == "__main__":
    start_echo_server()
