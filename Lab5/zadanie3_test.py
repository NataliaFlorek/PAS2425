import socket
import threading
from time import time, sleep

UDP_SEQUENCE = [8666, 9666, 10666]
TCP_PORT = 2913
ALLOWED_TIMEOUT = 10
PING_MESSAGE = b"PING"
PONG_MESSAGE = b"PONG"

client_progress = {}
allowed_ips = {}
lock = threading.Lock()


def handle_knock(port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('0.0.0.0', port))
        print(f"[UDP] Nasłuchiwanie na porcie {port}")

        while True:
            try:
                data, addr = sock.recvfrom(1024)
                ip = addr[0]

                if data.strip() == PING_MESSAGE:
                    with lock:
                        step = client_progress.get(ip, 0)

                        if port == UDP_SEQUENCE[step]:
                            step += 1
                            sock.sendto(PONG_MESSAGE, addr)
                            print(f"[UDP] {ip}: poprawny krok {step}/{len(UDP_SEQUENCE)}")

                            if step == len(UDP_SEQUENCE):
                                allowed_ips[ip] = time() + ALLOWED_TIMEOUT
                                print(f"[✓] {ip} odblokował dostęp TCP!")
                                client_progress[ip] = 0
                            else:
                                client_progress[ip] = step
                        else:
                            client_progress[ip] = 0
                            sock.sendto(PONG_MESSAGE, addr)
                            print(f"[UDP] {ip}: zła sekwencja — reset")

            except Exception as e:
                print(f"[Błąd] {e}")


def cleanup_ips():
    while True:
        sleep(1)
        now = time()
        with lock:
            expired = [ip for ip, expiry in allowed_ips.items() if expiry < now]
            for ip in expired:
                del allowed_ips[ip]


def tcp_gate():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(('0.0.0.0', TCP_PORT))
        server.listen()
        print(f"[TCP] Oczekiwanie na porcie {TCP_PORT}")

        while True:
            conn, addr = server.accept()
            ip = addr[0]

            with lock:
                if ip in allowed_ips:
                    conn.sendall(b"Congratulations! You found the hidden.\n")
                    del allowed_ips[ip]
                    print(f"[TCP] {ip} otrzymał nagrodę")
                else:
                    conn.sendall(b"Access denied. Complete port knocking first.\n")
            conn.close()


if __name__ == '__main__':
    for p in UDP_SEQUENCE:
        threading.Thread(target=handle_knock, args=(p,), daemon=True).start()

    threading.Thread(target=cleanup_ips, daemon=True).start()
    tcp_gate()
