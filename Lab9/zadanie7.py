import socket
import os
from datetime import datetime

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8080
SERVER_ROOT = os.path.dirname(os.path.abspath(__file__))


MIME_TYPES = {
    'html': 'text/html',
    'htm': 'text/html',
    'txt': 'text/plain',
    'css': 'text/css',
    'js': 'application/javascript',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'gif': 'image/gif',
    'ico': 'image/x-icon'
}

# Domyślne strony
DEFAULT_PAGE = 'index.html'
ERROR_404_PAGE = '404.html'


def get_mime_type(file_path):
    ext = file_path.split('.')[-1].lower()
    return MIME_TYPES.get(ext, 'application/octet-stream')


def handle_request(client_connection):
    request = client_connection.recv(1024).decode()
    if not request:
        return

    lines = request.split('\r\n')
    request_line = lines[0]
    method, path, _ = request_line.split()

    if '..' in path or path.startswith('/'):
        path = path.lstrip('/')
        path = os.path.normpath(path)
        if path.startswith('..'):
            path = ''

    if path == '' or path == '/':
        file_path = os.path.join(SERVER_ROOT, DEFAULT_PAGE)
    else:
        file_path = os.path.join(SERVER_ROOT, path)

    if os.path.isfile(file_path):
        with open(file_path, 'rb') as file:
            content = file.read()
        response_code = '200 OK'
        mime_type = get_mime_type(file_path)
    else:
        error_page_path = os.path.join(SERVER_ROOT, ERROR_404_PAGE)
        if os.path.isfile(error_page_path):
            with open(error_page_path, 'rb') as file:
                content = file.read()
            mime_type = get_mime_type(error_page_path)
        else:
            content = b'<html><body><h1>404 Not Found</h1></body></html>'
            mime_type = 'text/html'
        response_code = '404 Not Found'

    response_headers = [
        f'HTTP/1.1 {response_code}',
        f'Content-Type: {mime_type}',
        f'Content-Length: {len(content)}',
        'Connection: close',
        f'Date: {datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")}',
        'Server: SimplePythonHTTP/1.0',
        '',
    ]
    response = '\r\n'.join(response_headers).encode() + content

    client_connection.sendall(response)
    client_connection.close()


def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(1)
    print(f'Serwer HTTP działa pod adresem http://{SERVER_HOST}:{SERVER_PORT}')

    try:
        while True:
            client_connection, client_address = server_socket.accept()
            print(f'Połączenie od {client_address}')
            handle_request(client_connection)
    except KeyboardInterrupt:
        print('\nZamykanie serwera...')
    finally:
        server_socket.close()


if __name__ == '__main__':
    if not os.path.isfile(os.path.join(SERVER_ROOT, DEFAULT_PAGE)):
        with open(os.path.join(SERVER_ROOT, DEFAULT_PAGE), 'w') as f:
            f.write('<html><head><title>Strona główna</title></head><body><h1>Witaj na serwerze!</h1></body></html>')

    if not os.path.isfile(os.path.join(SERVER_ROOT, ERROR_404_PAGE)):
        with open(os.path.join(SERVER_ROOT, ERROR_404_PAGE), 'w') as f:
            f.write(
                '<html><head><title>404 Not Found</title></head><body><h1>404 - Strona nie znaleziona</h1></body></html>')

    run_server()