import socket


def save_image(data, filename):
    with open(filename, 'wb') as file:
        file.write(data)
    print(f"Obraz zapisany jako {filename}")


def get_png_from_httpbin():
    host = 'httpbin.org'
    port = 80
    path = '/image/png'

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    request = f"GET {path} HTTP/1.1\r\n"
    request += f"Host: {host}\r\n"
    request += "User-Agent: Python-HTTP-Client/1.0\r\n"
    request += "Accept: image/png, */*;q=0.8\r\n"
    request += "Connection: close\r\n"
    request += "\r\n"

    s.send(request.encode())

    response = b""
    while True:
        data = s.recv(4096)
        if not data:
            break
        response += data

    s.close()

    header_end = response.find(b'\r\n\r\n')
    if header_end == -1:
        print("Błąd: Nieprawidłowa odpowiedź serwera")
        return

    headers = response[:header_end].decode('utf-8')
    image_data = response[header_end + 4:]

    if "200 OK" not in headers.split('\r\n')[0]:
        print("Błąd: Serwer zwrócił nieprawidłową odpowiedź")
        print(headers)
        return

    save_image(image_data, 'obraz.png')


if __name__ == "__main__":
    get_png_from_httpbin()