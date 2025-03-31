#Lab3/ Zadanie 13

import socket


def parse_udp_datagram(hex_data):
    data_bytes = bytes.fromhex(hex_data)
    src_port = int.from_bytes(data_bytes[:2], byteorder='big')
    dst_port = int.from_bytes(data_bytes[2:4], byteorder='big')

    total_length = int.from_bytes(data_bytes[4:6], byteorder='big')

    data_length = total_length - 8

    data = data_bytes[8:8 + data_length].decode('utf-8', errors='ignore')

    return src_port, dst_port, data_length, data


def send_to_server(message):
    server_address = ('127.0.0.1', 2910)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.sendto(message.encode(), server_address)
        response, _ = sock.recvfrom(1024)
        return response.decode()


if __name__ == "__main__":
    hex_datagram = "ed740b550024effd70726f6772616d6d696e6720696e20707974686f6e2069732066756e"
    src_port, dst_port, data_length, data = parse_udp_datagram(hex_datagram)

    result_message = f"zad14odp;src;{src_port};dst;{dst_port};data;{data}"
    print("Wiadomość do wysłania:", result_message)

    response = send_to_server(result_message)
    print("Odpowiedź serwera:", response)