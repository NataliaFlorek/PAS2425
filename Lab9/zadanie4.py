import socket
import urllib.parse

def send_form_to_httpbin():
    print("Wprowadź dane formularza:")
    name = input("Imię: ")
    email = input("Email: ")
    message = input("Wiadomość: ")

    form_data = {
        'name': name,
        'email': email,
        'message': message
    }
    encoded_data = urllib.parse.urlencode(form_data).encode('utf-8')

    host = 'httpbin.org'
    port = 80
    path = '/post'

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    request = f"POST {path} HTTP/1.1\r\n"
    request += f"Host: {host}\r\n"
    request += "User-Agent: Python-HTTP-Client/1.0\r\n"
    request += "Content-Type: application/x-www-form-urlencoded\r\n"
    request += f"Content-Length: {len(encoded_data)}\r\n"
    request += "Connection: close\r\n"
    request += "\r\n"
    request += encoded_data.decode('utf-8')

    s.send(request.encode())

    response = b""
    while True:
        data = s.recv(4096)
        if not data:
            break
        response += data

    s.close()

    header_end = response.find(b'\r\n\r\n')
    headers = response[:header_end].decode('utf-8')
    body = response[header_end+4:].decode('utf-8')

    print("\nOdpowiedź serwera:")
    print(headers)
    print("\nCiało odpowiedzi:")
    print(body)

if __name__ == "__main__":
    send_form_to_httpbin()