import socket
import os


def save_image(data, filename):
    with open(filename, 'wb') as file:
        file.write(data)
    print(f"Obraz zapisany jako {filename} (rozmiar: {len(data)} bajtów)")


def load_last_modified():
    if os.path.exists("last_modified.txt"):
        with open("last_modified.txt", "r") as f:
            return f.read().strip()
    return None


def save_last_modified(date_str):
    with open("last_modified.txt", "w") as f:
        f.write(date_str)


def download_image_in_parts():
    host = '212.182.24.27'
    port = 8080
    path = '/image.jpg'

    part_sizes = [1024, 2048, 0]
    all_parts = bytearray()

    last_modified = load_last_modified()

    for i, size in enumerate(part_sizes, 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))

        request = f"GET {path} HTTP/1.1\r\n"
        request += f"Host: {host}:{port}\r\n"
        request += "User-Agent: Python-Conditional-Download/1.0\r\n"
        request += "Accept: image/jpeg, */*;q=0.8\r\n"

        if last_modified:
            request += f"If-Modified-Since: {last_modified}\r\n"

        if size > 0:
            start = len(all_parts)
            end = start + size - 1
            request += f"Range: bytes={start}-{end}\r\n"

        request += "Connection: close\r\n"
        request += "\r\n"

        s.send(request.encode())

        response = b""
        while True:
            data = s.recv(4096)
            if not data:
                break
            response += data

        s.close()

        header_end = response.find(b'\r\n\r\n')
        if header_end == -1:
            print(f"Błąd: Nieprawidłowa odpowiedź serwera (część {i})")
            return

        headers = response[:header_end].decode('utf-8')
        part_data = response[header_end + 4:]

        status_line = headers.split('\r\n')[0]
        if "304 Not Modified" in status_line:
            print("Obraz nie został zmieniony – pomijam pobieranie.")
            return

        if "206 Partial Content" not in status_line and i > 1:
            print(f"Błąd: Serwer nie obsługuje pobierania częściowego (część {i})")
            print(headers)
            return

        # Zapisz nową datę Last-Modified z odpowiedzi
        for line in headers.split('\r\n'):
            if line.lower().startswith("last-modified:"):
                new_last_modified = line.split(":", 1)[1].strip()
                save_last_modified(new_last_modified)

        all_parts.extend(part_data)
        print(f"Pobrano część {i} (rozmiar: {len(part_data)} bajtów)")

    save_image(all_parts, 'pobrany_obraz.jpg')


if __name__ == "__main__":
    download_image_in_parts()
