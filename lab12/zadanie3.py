import socket
import random
import threading


def handle_client(connection, address):
    print(f"[NOWE POŁĄCZENIE] Połączono z {address}")
    secret_number = random.randint(1, 100)
    print(f"[{address}] Wylosowana liczba to: {secret_number}")  # Do testów

    try:
        while True:
            data = connection.recv(1024)
            if not data:
                break

            message = data.decode().strip()

            try:
                guess = int(message)
            except ValueError:
                response = "Błąd: Wysłano coś, co nie jest liczbą!"
                connection.sendall(response.encode())
                continue

            if guess < secret_number:
                response = "Za mała liczba, spróbuj ponownie."
            elif guess > secret_number:
                response = "Za duża liczba, spróbuj ponownie."
            else:
                response = "Gratulacje! Odgadłeś liczbę!"
                connection.sendall(response.encode())
                break

            connection.sendall(response.encode())
    except Exception as e:
        print(f"[BŁĄD] {address}: {e}")
    finally:
        connection.close()
        print(f"[ROZŁĄCZONO] Połączenie z {address} zostało zakończone.")


def server():
    host = '127.0.0.1'
    port = 51423

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"[SERWER] Serwer nasłuchuje na {host}:{port}")

    try:
        while True:
            connection, address = server_socket.accept()
            thread = threading.Thread(target=handle_client, args=(connection, address))
            thread.start()
            print(f"[INFO] Liczba aktywnych wątków: {threading.active_count() - 1}")
    except KeyboardInterrupt:
        print("\n[ZAMYKANIE] Serwer wyłączany...")
    finally:
        server_socket.close()


if __name__ == "__main__":
    server()
