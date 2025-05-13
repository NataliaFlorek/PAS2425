import socket
import threading
import datetime


def log_event(event):
    with open("server_log.txt", "a") as log_file:
        log_file.write(f"{event}\n")


def client_thread(connection, address):
    log_event(f"{datetime.datetime.now()} - Połączono z {address[0]}:{address[1]}")

    try:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            log_event(
                f"{datetime.datetime.now()} - Otrzymano dane od klienta {address[0]}:{address[1]}: {data.decode()}")
            connection.sendall(data)
    except Exception as e:
        log_event(f"{datetime.datetime.now()} - Błąd podczas komunikacji z {address[0]}:{address[1]}: {e}")
    finally:
        connection.close()
        log_event(f"{datetime.datetime.now()} - Zamknięto połączenie z {address[0]}:{address[1]}")


def server():
    host = '127.0.0.1'
    port = 54321
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Serwer nasłuchuje na {host}:{port}")

    log_event(f"{datetime.datetime.now()} - Serwer uruchomiony na {host}:{port}")

    try:
        while True:
            connection, address = server_socket.accept()
            client_handler = threading.Thread(target=client_thread, args=(connection, address))
            client_handler.start()
    except KeyboardInterrupt:
        print("Serwer zatrzymany.")
    finally:
        log_event(f"{datetime.datetime.now()} - Serwer zatrzymany.")
        server_socket.close()


if __name__ == "__main__":
    server()
