# Lab1/ Zadanie 4
import socket
import ipaddress
import sys
def validate_ip(ip_adress):
    try:
        ip = ipaddress.ip_address(ip_adress)
        return True
    except ValueError:
        return False

ip= sys.argv[1]
if not validate_ip(ip):
    print("Niepoprawny adres IP")
    sys.exit(1)
try:
    host_name = socket.gethostbyaddr(ip)
    print(host_name)
except socket.herror:
    print("Nie znaleziono hostname")