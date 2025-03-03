# Lab1/ Zadanie 5
import socket

import sys

host_name= sys.argv[1]

try:
    ip = socket.gethostbyname(host_name)
    print(ip)
except socket.herror:
    print("Nie znaleziono adresu IP")