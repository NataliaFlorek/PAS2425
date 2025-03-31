#Zadanie1/Lab5
import socket


def main():
    host = '127.0.01'
    port = 2912

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))

        user_input = input("Podaj liczbę do odgadnięcia: ")

        try:
            number = int(user_input)
        except ValueError:
            print("To nie jest poprawna liczba.")
            return

        client_socket.sendall(str(number).encode())

        response = client_socket.recv(1024).decode()

        print(f"Odpowiedź serwera: {response}")


if __name__ == '__main__':
    main()
