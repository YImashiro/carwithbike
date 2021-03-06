from carpc import client
from carpc.Parts import ServoMotor
from carpc.Parts import MotorDriver
from carpc import cscsensor
import multiprocessing
import threading
import time


def motor():
    print("a")
    th2 = threading.Thread(target=cscsensor.init)
    th2.start()
    motor = MotorDriver.MotorDriverwithCSC(19,26,13)
    while True:
        duty = cscsensor.delegate.speed
        cadence = cscsensor.delegate.cadence
        print("main {} {}".format(duty,cadence))
        time.sleep(1)
        motor.gowithCSC(duty,cadence)

def servo():
    th1 = threading.Thread(target=client.init)
    th1.start()
    servo = ServoMotor.ServoMotor(4)
    while th1.is_alive():
        time.sleep(1)
        print("main {}".format(client.angle))
        servo.steeringControl(client.angle)
           

p1 = multiprocessing.Process(target=motor)
p2 = multiprocessing.Process(target=servo)
p1.start()
p2.start()
time.sleep(1000)

