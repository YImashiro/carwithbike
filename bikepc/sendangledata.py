import recog
import threading
import socket

recog.setting()
th1 = threading.Thread(target=recog.capturevideo)
th1.start()


while True:
    angle = recog.coordtoangle(recog.left_coord[0],recog.center_coord[0],recog.right_coord[0],recog.grav[0])
    print(angle)

        
