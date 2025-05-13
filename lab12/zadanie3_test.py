import socket

HOST = '127.0.0.1'
PORT = 51423


def main():
    print("Połączono z serwerem gry w zgadywanie liczby.")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        while True:
            guess = input("Podaj liczbę (lub wpisz 'exit' aby zakończyć): ")
            if guess.lower() == 'exit':
                print("Zamykam połączenie.")
                break

            s.sendall(guess.encode())
            response = s.recv(1024).decode()
            print("Serwer:", response)

            if "Gratulacje" in response:
                print("Zgadłeś poprawną liczbę! Kończę grę.")
                break


if __name__ == "__main__":
    main()
