#Lab2/ Zadanie 7
import socket
import sys


def get_service_name(port):
    try:
        service_name = socket.getservbyport(port)
        return service_name
    except OSError:
        return None


HOST = sys.argv[1]
PORT = int(sys.argv[2])

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(5)
        s.connect((HOST, PORT))
        print(f"Connected to {HOST} on port {PORT}")

        service = get_service_name(PORT)
        if service:
            print(f"Service running on port {PORT}: {service}")
        else:
            print(f"No service name found for port {PORT}")
except Exception as e:
    print(f"Not connected to {HOST} on port {PORT}. Error: {e}")

