angle = 0

def init():
    import socket
    import time
    data = "data"
    ADDRESS = '192.168.100.104'
    PORT = 57214
    with socket.socket() as socket:
        socket.connect((ADDRESS,PORT))
        while True:
            angle = socket.recv(3)
            if not data:
                break
            time.sleep(1)
            
    print("end")
