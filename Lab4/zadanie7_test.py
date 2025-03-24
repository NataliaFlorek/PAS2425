import socket

def tcp_client(host='127.0.0.1', port=2900, message='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            s.connect((host, port))

            s.sendall(message.encode('utf-8'))

            response = s.recv(1024).decode('utf-8')

            return response
    except Exception as e:
        return f'Błąd: {e}'


if __name__ == "__main__":
    response = tcp_client()
    print(f'Odpowiedź z serwera: {response}')