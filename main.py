from carpc import client
from carpc.Parts import ServoMotor
from carpc.Parts import MotorDriverwithCSC
from carpc import MotorwithCSC


servo = ServoMotor(4)
motor = MotorDriverwithCSC(19,26,13)

while True:
    try:
        servo.steeringContro(int(client.data))
        motor.gowithCSC(MotorwithCSC.duty,MotorwithCSC.cadence)

    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        break

print("exit")
