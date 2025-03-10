#Lab2/ Zadanie 5

import socket

def udp_client(host='127.0.0.1', port=2901):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.settimeout(5)
            print(f"Połączono z serwerem {host}:{port}. Wpisz 'exit' aby zakończyć.")

            while True:
                message = input("Wpisz wiadomość: ")
                if message.lower() == 'exit':
                    print("Zamykanie klienta...")
                    break

                s.sendto(message.encode('utf-8'), (host, port))

                try:
                    response, _ = s.recvfrom(1024)
                    print(f"Odpowiedź z serwera: {response.decode('utf-8')}")
                except socket.timeout:
                    print("Błąd: Serwer nie odpowiedział w czasie oczekiwania")

    except Exception as e:
        print(f'Błąd: {e}')

if __name__ == "__main__":
    udp_client()
