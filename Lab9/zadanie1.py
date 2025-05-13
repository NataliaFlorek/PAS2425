import socket


def save_html(content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Strona zapisana jako {filename}")


def get_html_from_httpbin():
    host = 'httpbin.org'
    port = 80
    path = '/html'

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))


    request = f"GET {path} HTTP/1.1\r\n"
    request += f"Host: {host}\r\n"
    request += "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A\r\n"
    request += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
    request += "Accept-Language: en-us\r\n"
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

    response_str = response.decode('utf-8', errors='ignore')

    headers, body = response_str.split('\r\n\r\n', 1)

    save_html(body, 'strona.html')


if __name__ == "__main__":
    get_html_from_httpbin()