# Example client

import socket

HOST = '0.0.0.0'
PORT = 8020

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))

data = s.recv(1024)

while True:
    data_send = input()

    if data_send == 'exit':
        s.close()
    else:
        s.send(data_send.encode())

    # data = s.recv(1024).decode()

