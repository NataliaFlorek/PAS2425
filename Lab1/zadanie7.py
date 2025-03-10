#Lab1/Zadanie 7
import socket
import sys

def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

host = sys.argv[1]

if not host.replace('.', '').isdigit():
    host = socket.gethostbyname(host)


for port in range(1, 65536):
    if check_port(host, port):
        print(f"Port {port} is open")
