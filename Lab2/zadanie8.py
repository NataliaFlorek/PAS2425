#Lab2/ Zadanie 7

import socket
import sys

def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

def get_service_name(port):
    try:
        service_name = socket.getservbyport(port)
        return service_name
    except OSError:
        return None

host = sys.argv[1]


try:
    if not host.replace('.', '').isdigit():
        host = socket.gethostbyname(host)
except socket.gaierror:
    print("Error: Unable to resolve host")
    sys.exit(1)

for port in range(1, 65536):
    if check_port(host, port):
        service = get_service_name(port)
        print(f"Port {port} is open ({service})")
