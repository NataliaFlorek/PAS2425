import socket
import threading

def client_thread(connection, address):
    print(f"Połączono z {address}")
    try:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            print(f"Otrzymano od klienta: {data.decode()}")
            connection.sendall(data)
    except Exception as e:
        print(f"Błąd podczas komunikacji: {e}")
    finally:
        connection.close()
        print(f"Zamknięto połączenie z {address}")

def server():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Serwer nasłuchuje na {host}:{port}")

    try:
        while True:
            connection, address = server_socket.accept()
            client_handler = threading.Thread(target=client_thread, args=(connection, address))
            client_handler.start()
    except KeyboardInterrupt:
        print("Serwer zatrzymany.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    server()
