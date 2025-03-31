import socket

def main():
    host = '127.0.0.1'
    port = 2912

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print("Połączono z serwerem.")

        while True:
            user_input = input("Podaj liczbę do odgadnięcia (lub 'exit' aby zakończyć): ")

            if user_input.lower() == 'exit':
                print("Zakończenie gry.")
                break

            try:
                number = int(user_input)
            except ValueError:
                print("Proszę podać poprawną liczbę.")
                continue

            client_socket.sendall(str(number).encode())

            response = client_socket.recv(1024).decode()

            print(f"Odpowiedź serwera: {response}")

            if response == "Brawo, odgadłeś liczbę!":
                break

if __name__ == '__main__':
    main()
