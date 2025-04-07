#Lab5/zadanie3
import socket
import time

HOST = '127.0.0.1'
UDP_BASE_PORT = 666
TCP_PORT = 2913
TIMEOUT = 0.5
PING_MESSAGE = b"PING"
PONG_MESSAGE = b"PONG"

def find_valid_udp_ports():
    valid_ports = []

    def try_port(port):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.settimeout(TIMEOUT)
            try:
                s.sendto(PING_MESSAGE, (HOST, port))
                data, _ = s.recvfrom(1024)
                if data.strip() == PONG_MESSAGE:
                    valid_ports.append(port)
                    print(f"Znaleziono port: {port}")
            except (socket.timeout, ConnectionResetError):
                pass
            except Exception as e:
                print(f"Błąd przy porcie {port}: {str(e)}")

    for port in range(UDP_BASE_PORT, 65536, 1000):
        try_port(port)

    return valid_ports


def perform_port_knocking(ports):
    knocks = []

    def knock_port(port):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            try:
                s.sendto(PING_MESSAGE, (HOST, port))
                print(f"Wysłano PING na port {port}")
            except Exception as e:
                print(f"Błąd przy port knocking {port}: {str(e)}")

    for port in ports:
        knocks.append(knock_port(port))
        time.sleep(0.1)

    for knock in knocks:
        knock


def get_tcp_message():
    retries = 3
    attempt = 0
    while attempt < retries:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, TCP_PORT))
                response = s.recv(1024).decode()
                return response
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {str(e)}")
            attempt += 1
            time.sleep(1)
    return f"Failed to establish TCP connection after {retries} attempts."


def main():
    print("Rozpoczynanie skanowania portów UDP...")
    valid_ports = find_valid_udp_ports()

    if not valid_ports:
        print("Nie znaleziono żadnych portów w sekwencji")
        return

    print(f"\nZnalezione porty: {valid_ports}")
    print("\nRozpoczynanie port knocking...")
    perform_port_knocking(valid_ports)

    print("\nPróba połączenia TCP...")
    print(get_tcp_message())


if __name__ == "__main__":
    main()
