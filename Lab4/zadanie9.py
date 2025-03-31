#!/usr/bin/env python

import socket
import sys
from time import gmtime, strftime


def check_msg_syntax(txt):
    parts = txt.split(";")
    if len(parts) != 7:
        return "BAD_SYNTAX"

    try:
        if parts[0] == "zad13odp" and parts[1] == "src" and parts[3] == "dst" and parts[5] == "data":
            src_port = int(parts[2])
            dst_port = int(parts[4])
            data = parts[6]

            if src_port == 2900 and dst_port == 35211 and data == "hello :)":
                return "TAK"
            else:
                return "NIE"
        else:
            return "BAD_SYNTAX"
    except ValueError:
        return "BAD_SYNTAX"


HOST = "127.0.0.1"
PORT = 2909

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    sock.bind((HOST, PORT))
    print(f"[{strftime('%Y-%m-%d %H:%M:%S', gmtime())}] UDP Server is running on {HOST}:{PORT} ...")
except socket.error as msg:
    print(f"Bind failed. Error: {msg.strerror}")
    sys.exit()

try:
    while True:
        data, address = sock.recvfrom(1024)
        message = data.decode()

        print(f"[{strftime('%Y-%m-%d %H:%M:%S', gmtime())}] Received {len(data)} bytes from {address}. Data: {message}")

        response = check_msg_syntax(message)
        sent = sock.sendto(response.encode(), address)

        print(f"[{strftime('%Y-%m-%d %H:%M:%S', gmtime())}] Sent {sent} bytes back to {address}.")
finally:
    sock.close()
