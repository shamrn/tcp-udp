import socket
import threading
from art_net import send_dmx

HOST = '0.0.0.0'
PORT = 8000


def start_server():
    """Start server tcp"""

    socket_ = socket.socket()
    socket_.bind((HOST, PORT))
    socket_.listen(10)

    while True:
        sock, _ = socket_.accept()
        t = threading.Thread(target=handler, args=(sock,))
        t.start()


def handler(sock):
    """Handler request"""

    sock.send('success'.encode())

    while True:
        data = sock.recv(1024).decode()
        if not data: break  # NOQA
        send_dmx(data)

    sock.close()


start_server()
