#Lab3/ Zadanie 15
import socket
import struct


def parse_ip_packet(packet_hex):
    packet_bytes = bytes.fromhex(packet_hex)

    version = (packet_bytes[0] >> 4) & 0xF

    src_ip = ".".join(map(str, packet_bytes[12:16]))
    dst_ip = ".".join(map(str, packet_bytes[16:20]))

    protocol_type = packet_bytes[9]

    if protocol_type == 6:
        src_port, dst_port = struct.unpack('!HH', packet_bytes[20:24])
        header_length = (packet_bytes[32] >> 4) * 4
        data_offset = 20 + header_length
        data = packet_bytes[data_offset:].decode('utf-8', errors='ignore').strip()
    else:
        src_port, dst_port, data = None, None, ""

    return version, src_ip, dst_ip, protocol_type, src_port, dst_port, data


def send_udp_message(server_ip, server_port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(5)
    try:
        sock.sendto(message.encode(), (server_ip, server_port))
        response, _ = sock.recvfrom(1024)
        return response.decode().strip()
    except socket.timeout:
        print("Błąd: Brak odpowiedzi od serwera!")
        return None
    finally:
        sock.close()


def main():
    packet_hex = (
        "4500004ef7fa400038069d33d4b6181bc0a800020b54b9a6"
        "fbf93c57c10a06c1801800e3ce9c00000101080a03a6eb01"
        "000bf8e56e6574776f726b2070726f6772616d6d696e6720"
        "69732066756e"
    )

    version, src_ip, dst_ip, protocol, src_port, dst_port, data = parse_ip_packet(packet_hex)

    print(f"Version: {version}, Src IP: {src_ip}, Dst IP: {dst_ip}, Protocol: {protocol}")
    print(f"Src Port: {src_port}, Dst Port: {dst_port}, Data: '{data}'")

    server_ip = "127.0.0.1"
    server_port = 2911
    msg_a = f"zad15odpA;ver;{version};srcip;{src_ip};dstip;{dst_ip};type;{protocol}"
    print(f"Sending: {msg_a}")

    response_a = send_udp_message(server_ip, server_port, msg_a)
    if response_a:
        print(f"Server Response: {response_a}")

    if response_a == "TAK" and src_port and dst_port:
        msg_b = f"zad15odpB;srcport;{src_port};dstport;{dst_port};data;{data}"
        print(f"Sending: {msg_b}")
        response_b = send_udp_message(server_ip, server_port, msg_b)
        if response_b:
            print(f"Server Response: {response_b}")


if __name__ == "__main__":
    main()
