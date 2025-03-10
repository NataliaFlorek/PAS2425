#Lab2/Zadanie 3
import socket

def tcp_client(host='127.0.0.1', port=2900):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            s.connect((host, port))
            print(f"Połączono z serwerem {host}:{port}. Wpisz 'exit' aby zakończyć.")

            while True:
                message = input("Wpisz wiadomość: ")
                if message.lower() == 'exit':
                    print("Zamykanie klienta...")
                    break

                s.sendall(message.encode('utf-8'))
                response = s.recv(1024).decode('utf-8')
                print(f"Odpowiedź z serwera: {response}")

    except socket.timeout:
        print('Błąd: Przekroczono limit czasu na połączenie')
    except ConnectionRefusedError:
        print('Błąd: Serwer odrzucił połączenie')
    except Exception as e:
        print(f'Błąd: {e}')

if __name__ == "__main__":
    tcp_client()
