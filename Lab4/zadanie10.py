#!/usr/bin/env python

import socket
import sys
from time import gmtime, strftime


def check_msg_syntax(txt):
    parts = txt.split(";")
    if len(parts) != 7:
        return "BAD SYNTAX"

    if parts[0] == "zad14odp" and parts[1] == "src" and parts[3] == "dst" and parts[5] == "data":
        try:
            src_port = int(parts[2])
            dst_port = int(parts[4])
            data = parts[6]
        except ValueError:
            return "BAD SYNTAX"

        if src_port == 60788 and dst_port == 2901 and data == "programming in python is fun":
            return "TAK"
        else:
            return "NIE"
    else:
        return "BAD SYNTAX"


HOST = '127.0.0.1'
PORT = 2910

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    sock.bind((HOST, PORT))
except socket.error as msg:
    print(f'Bind failed. Error Code: {msg[0]} Message: {msg[1]}')
    sys.exit()

print(f"[{strftime('%Y-%m-%d %H:%M:%S', gmtime())}] UDP Server is waiting for incoming messages...")

try:
    while True:
        data, address = sock.recvfrom(1024)
        print(
            f"[{strftime('%Y-%m-%d %H:%M:%S', gmtime())}] Received {len(data)} bytes from {address}. Data: {data.decode()}")

        if data:
            response = check_msg_syntax(data.decode())
            sock.sendto(response.encode(), address)
            print(f"[{strftime('%Y-%m-%d %H:%M:%S', gmtime())}] Sent response '{response}' to {address}.")
finally:
    sock.close()
