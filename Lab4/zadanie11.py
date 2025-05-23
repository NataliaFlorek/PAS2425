#!/usr/bin/env python

import socket, sys
from time import gmtime, strftime

def check_msgA_syntax(txt):
    s = len(txt.split(";"))
    if s != 9:
        return "BAD_SYNTAX"
    else:
        tmp = txt.split(";")
        if tmp[0] == "zad15odpA" and tmp[1] == "ver" and tmp[3] == "srcip" and tmp[5] == "dstip" and tmp[7] == "type":
            try:
                ver = int(tmp[2])
                srcip = tmp[4]
                dstip = tmp[6]
                type = int(tmp[8])
                if ver == 4 and type == 6 and srcip == "212.182.24.27" and dstip == "192.168.0.2":
                    return "TAK"
                else:
                    return "NIE"
            except ValueError:
                return "NIE"
        else:
            return "BAD_SYNTAX"

def check_msgB_syntax(txt):
    s = len(txt.split(";"))
    if s != 7:
        return "BAD_SYNTAX"
    else:
        tmp = txt.split(";")
        if tmp[0] == "zad15odpB" and tmp[1] == "srcport" and tmp[3] == "dstport" and tmp[5] == "data":
            try:
                srcport = int(tmp[2])
                dstport = int(tmp[4])
                data = tmp[6]
                if srcport == 2900 and dstport == 47526 and data == "network programming is fun":
                    return "TAK"
                else:
                    return "NIE"
            except ValueError:
                return "NIE"
        else:
            return "BAD_SYNTAX"

HOST = '127.0.0.1'
PORT = 2911

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    sock.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print("[%s] UDP ECHO Server is waiting for incoming connections ..." % strftime("%Y-%m-%d %H:%M:%S", gmtime()))

try:
    while True:
        data, address = sock.recvfrom(1024)
        data = data.decode()
        print('[%s] Received %s bytes from client %s. Data: %s' % (
            strftime("%Y-%m-%d %H:%M:%S", gmtime()), len(data), address, data))

        if data:
            tmp = data.split(";")
            print("DATA: %s" % data)

            if tmp[0] == "zad15odpA":
                answer = check_msgA_syntax(data)
                sent = sock.sendto(answer.encode(), address)
                print('[%s] Sent %s bytes back to client %s.' % (
                    strftime("%Y-%m-%d %H:%M:%S", gmtime()), sent, address))

            elif tmp[0] == "zad15odpB":
                answer = check_msgB_syntax(data)
                sent = sock.sendto(answer.encode(), address)
                print('[%s] Sent %s bytes back to client %s.' % (
                    strftime("%Y-%m-%d %H:%M:%S", gmtime()), sent, address))

            else:
                sent = sock.sendto("BAD_SYNTAX".encode(), address)
                print('[%s] Sent %s bytes back to client %s.' % (
                    strftime("%Y-%m-%d %H:%M:%S", gmtime()), sent, address))

finally:
    sock.close()
