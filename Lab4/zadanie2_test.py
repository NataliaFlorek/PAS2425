import socket

def test_echo_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(('127.0.0.1', 5555))
        message = input("Podaj wiadomość do wysłania: ").encode()
        client_socket.sendall(message)
        response = client_socket.recv(1024)
        print(f"Otrzymana odpowiedź: {response.decode()}")
        assert response == message, "Serwer nie odesłał poprawnej wiadomości"


if __name__ == '__main__':
    test_echo_server()