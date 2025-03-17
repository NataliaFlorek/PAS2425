#Lab2/ Zadanie 11

import socket


def format_message(message, length=20):
    if len(message) < length:
        return message.ljust(length)
    return message[:length]


def tcp_client(host='127.0.0.1', port=2908, message='Hej :3'):
    message = format_message(message)

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            s.connect((host, port))

            s.sendall(message.encode('utf-8'))

            response = s.recv(20).decode('utf-8')
            return response.strip()
    except Exception as e:
        return f'Błąd: {e}'


if __name__ == "__main__":
    user_message = input("Podaj wiadomość do wysłania: ")
    response = tcp_client(message=user_message)
    print(f'Odpowiedź z serwera: {response}')