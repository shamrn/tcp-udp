# Example client

import socket

HOST = '0.0.0.0'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))

data = s.recv(1024)


data_send = 'data for dmx controller'

s.send(data_send.encode())
data = s.recv(1024).decode()

s.close()
