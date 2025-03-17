#Lab2/ Zadanie 6
import socket

def udp_client(host='127.0.0.1', port=2902):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.settimeout(5)

            while True:
                num1 = input("Podaj pierwszą liczbę: ")
                operator = input("Podaj operator (+, -, *, /): ")
                num2 = input("Podaj drugą liczbę: ")


                s.sendto(num1.encode(), (host, port))
                s.sendto(operator.encode(), (host, port))
                s.sendto(num2.encode(), (host, port))

                try:
                    response, _ = s.recvfrom(1024)  #
                    print(f"Odpowiedź z serwera: {response.decode('utf-8')}")
                except socket.timeout:
                    print("Błąd: Serwer nie odpowiedział w czasie oczekiwania")


    except Exception as e:
        print(f'Błąd: {e}')


if __name__ == "__main__":
    udp_client()

