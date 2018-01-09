angle = 0

def init():
    global angle
    import socket
    import time
    data = "data"
    ADDRESS = '192.168.100.102'
    PORT = 57214
    with socket.socket() as socket:
        socket.connect((ADDRESS,PORT))
        while True:
            angle = int(socket.recv(3).decode())
            if not data:
                break
    print("end")
