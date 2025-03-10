#Lab1/Zadanie 6
import socket
import sys

HOST = sys.argv[1]
PORT = int(sys.argv[2])
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("Connected")
except Exception as e:
    print("Not connected")

