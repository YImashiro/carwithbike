from carpc import client
from carpc.Parts import ServoMotor
from carpc.Parts import MotorDriverwithCSC
from carpc import MotorwithCSC
import multiprocessing


def motor():
    motor = MotorDriverwithCSC(19,26,13)
    while True:
        motor.gowithCSC(MotorwithCSC.duty,MotorwithCSC.cadence)

def servo():
    servo = ServoMotor(4)
    while True:
        servo.steeringContro(int(client.data))
           

p1 = multiprocessing.Process(target=motor)
p2 = multiprocessing.Process(target=servo)
p1.start()
p2.start()


