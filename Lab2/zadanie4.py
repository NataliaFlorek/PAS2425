#Lab2/ Zadanie 4
import socket

def udp_client(host='127.0.0.1', port=2901, message='Hej :3'):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.settimeout(5)
            s.sendto(message.encode('utf-8'), (host, port))

            response, _ = s.recvfrom(1024) 
            return response.decode('utf-8')
    except socket.timeout:
        return 'Błąd: Przekroczono limit czasu na połączenie'
    except Exception as e:
        return f'Błąd: {e}'

if __name__ == "__main__":
    response = udp_client()
    print(f'Odpowiedź z serwera: {response}')
