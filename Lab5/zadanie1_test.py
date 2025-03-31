import socket
import random

def start_server():
    host = '127.0.0.1'
    port = 2912

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Serwer nasłuchuje na porcie {port}...")

        client_socket, client_address = server_socket.accept()
        with client_socket:
            print(f"Połączono z {client_address}")

            secret_number = random.randint(1, 100)
            print(f"Wylosowana liczba to {secret_number} (serwer nie wyświetla tej liczby)")

            while True:
                client_number = client_socket.recv(1024).decode()

                if not client_number:
                    break

                try:
                    client_number = int(client_number)
                except ValueError:
                    client_socket.sendall("Podana wartość nie jest liczbą.".encode())
                    continue


                if client_number < secret_number:
                    client_socket.sendall("Za mało!".encode())
                elif client_number > secret_number:
                    client_socket.sendall("Za dużo!".encode())
                else:
                    client_socket.sendall("Brawo, odgadłeś liczbę!".encode())
                    break

if __name__ == '__main__':
    start_server()
