import socket


def test_udp_echo_server():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        server_address = ('127.0.0.1', 5555)
        message = input("Podaj wiadomość do wysłania: ").encode()
        client_socket.sendto(message, server_address)
        response, _ = client_socket.recvfrom(1024)
        print(f"Otrzymana odpowiedź: {response.decode()}")
        assert response == message, "Serwer nie odesłał poprawnej wiadomości"


if __name__ == "__main__":
    test_udp_echo_server()

