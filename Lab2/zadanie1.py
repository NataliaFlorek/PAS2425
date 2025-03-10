#Lab2/ Zadanie 2
import socket

def get_ntp_time(host='ntp.task.gda.pl', port=13):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            data = s.recv(1024).decode('utf-8').strip()
            return data
    except Exception as e:
        return f'Błąd: {e}'

if __name__ == "__main__":
    time_data = get_ntp_time()
    print(f'Aktualna data i czas z serwera: {time_data}')
