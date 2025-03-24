#Lab 4/ Zadanie 1
import socket
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5555

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Serwer nasłuchuje na {HOST}:{PORT}...")

    conn, addr = server_socket.accept()
    with conn:
        print(f"Połączono z {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            print(f"Otrzymano: {data.decode()} | Wysyłam: {current_time}")
            conn.sendall(current_time.encode())