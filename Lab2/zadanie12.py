#Lab2/ Zadanie 12

import socket


def format_message(message, length=20):
    if len(message) < length:
        return message.ljust(length)
    return message[:length]


def send_all(sock, message):
    total_sent = 0
    while total_sent < len(message):
        sent = sock.send(message[total_sent:].encode('utf-8'))
        if sent == 0:
            raise RuntimeError("Błąd połączenia - wysyłanie zatrzymane.")
        total_sent += sent


def recv_all(sock, length):
    data = b''
    while len(data) < length:
        chunk = sock.recv(length - len(data))
        if chunk == b'':
            raise RuntimeError("Błąd połączenia - odbiór zatrzymany.")
        data += chunk
    return data.decode('utf-8')


def tcp_client(host='127.0.0.1', port=2908, message='Hej :3'):
    message = format_message(message)

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            s.connect((host, port))

            send_all(s, message)
            response = recv_all(s, 20)

            return response.strip()
    except Exception as e:
        return f'Błąd: {e}'


if __name__ == "__main__":
    user_message = input("Podaj wiadomość do wysłania: ")
    response = tcp_client(message=user_message)
    print(f'Odpowiedź z serwera: {response}')