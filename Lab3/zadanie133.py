#Lab3/Zadanie 14
import socket


def parse_tcp_segment(hex_data):
    bytes_data = bytes.fromhex(hex_data)
    src_port = int.from_bytes(bytes_data[0:2])
    dst_port = int.from_bytes(bytes_data[2:4])
    data_offset = (bytes_data[12] >> 4) * 4
    data = bytes_data[data_offset:].decode('utf-8', errors='ignore')

    return src_port, dst_port, data


def send_to_server(src_port, dst_port, data):
    message = f"zad13odp;src;{src_port};dst;{dst_port};data;{data}"
    server_address = ('127.0.0.1', 2909)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.sendto(message.encode(), server_address)
        response, _ = sock.recvfrom(1024)

    return response.decode()


tcp_segment_hex = "0b54898b1f9a18ecbbb164f2801800e3677100000101080a02c1a4ee001a4cee68656c6c6f203a29"

src_port, dst_port, data = parse_tcp_segment(tcp_segment_hex)

response = send_to_server(src_port, dst_port, data)
print(response)
