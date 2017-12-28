import socket
import recog
import threading
import time

angle = 0

def calculateAngle():
    global angle
    while True:
        recog.capturevideo()
        angle = "{:<3d}".format(recog.coordtoangle(recog.left_coord[0],recog.center_coord[0],recog.right_coord[0],recog.grav[0]))
        time.sleep(1)
        print(angle)

        
recog.setting()
th1 = threading.Thread(target=calculateAngle,daemon=True)
th1.start()

ADDRESS = ''
PORT = 57214
with socket.socket() as socket:
    socket.bind((ADDRESS,PORT))
    socket.listen(1)
    conn, address = socket.accept()
    with conn:
        print("Connected to {} ".format(address))
        while True:
            try:
                conn.sendall(angle.encode())
            except:
                print("error")
                break
        print("end")
