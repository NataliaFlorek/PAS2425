# Lab1/ Zadanie 3
import ipaddress

def validate_ip(ip_adress):
    try:
        ip = ipaddress.ip_address(ip_adress)
        print("Adres jest ok")
    except ValueError:
        print("Adres nie jest ok")


print("Podaj adres IP: ")
ip_adress = input()

validate_ip(ip_adress)
