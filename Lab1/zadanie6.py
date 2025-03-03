#Lab1/Zadanie 6
import socket
import sys
#NIC NIE DZIALA!!!!!
HOST = sys.argv[1]
PORT = sys.argv[1]
with socket.socket(socket.AF_INET) as s:
    s.connect((HOST, PORT))
    print("Connected")

