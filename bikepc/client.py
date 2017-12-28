import socket
import time

ADDRESS = '192.168.100.104'
PORT = 8000
with socket.socket() as socket:
    socket.connect((ADDRESS,PORT))
    while True:
        data = socket.recv(8)
        if not data:
            break
        print(data.decode())
        time.sleep(1)

print("end")