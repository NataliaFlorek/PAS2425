#!/usr/bin/env python

import socket, select
from time import gmtime, strftime

HOST = '127.0.0.1'
PORT = 2900
BUFFER_SIZE = 20 

connected_clients_sockets = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(10)

connected_clients_sockets.append(server_socket)

print ("[%s] TCP ECHO Server is waiting for incoming connections on port %s ... " % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), PORT))

def recv_full(sock, length):
    data = b''
    while len(data) < length:
        packet = sock.recv(length - len(data))
        if not packet:
            return None
        data += packet
    return data

def send_full(sock, data):
    total_sent = 0
    while total_sent < len(data):
        sent = sock.send(data[total_sent:])
        if sent == 0:
            return False
        total_sent += sent
    return True

while True:
    read_sockets, _, _ = select.select(connected_clients_sockets, [], [])

    for sock in read_sockets:
        if sock == server_socket:
            sockfd, client_address = server_socket.accept()
            connected_clients_sockets.append(sockfd)
            print ("[%s] Client %s connected ... " % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), client_address))
        else:
            try:
                data = recv_full(sock, BUFFER_SIZE)
                if data:
                    if not send_full(sock, data):
                        print ("[%s] Error sending data to client %s" % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), sock.getpeername()))
                        sock.close()
                        connected_clients_sockets.remove(sock)
                    else:
                        print ("[%s] Sent to client %s: ['%s']" % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), sock.getpeername(), data))
                else:
                    print ("[%s] Client (%s) disconnected" % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), sock.getpeername()))
                    sock.close()
                    connected_clients_sockets.remove(sock)
            except:
                print ("[%s] Client (%s) is offline" % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), sock.getpeername()))
                sock.close()
                connected_clients_sockets.remove(sock)
                continue

server_socket.close()