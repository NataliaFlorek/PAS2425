#Lab 4/ Zadanie 4

import socket


def calculate(expression: str):
    try:
        num1, operator, num2 = expression.split()
        num1, num2 = float(num1), float(num2)
        if operator == '+':
            return str(num1 + num2)
        elif operator == '-':
            return str(num1 - num2)
        elif operator == '*':
            return str(num1 * num2)
        elif operator == '/':
            return str(num1 / num2) if num2 != 0 else "Błąd: Dzielenie przez zero"
        else:
            return "Błąd: Nieznany operator"
    except Exception:
        return "Błąd: Niepoprawne dane"


def start_udp_math_server(host='127.0.0.1', port=5555):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((host, port))
        print(f"Serwer UDP kalkulator działa na {host}:{port}")

        while True:
            data, addr = server_socket.recvfrom(1024)
            expression = data.decode()
            print(f"Odebrano od {addr}: {expression}")
            result = calculate(expression)
            server_socket.sendto(result.encode(), addr)
            print(f"Odesłano do {addr}: {result}")


if __name__ == "__main__":
    start_udp_math_server()
