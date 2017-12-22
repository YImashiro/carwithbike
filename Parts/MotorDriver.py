#!/usr/bin/python
import RPi.GPIO as GPIO
import sys

class MotorDriver:
    freq = 50
    duty = 0.8

    def __init__(self,pin1,pin2):
        channels = [pin1,pin2]
        GPIO.setup(channels,GPIO.OUT)
        
            
    def __setting(self):
        GPIO.output(self.channels,GPIO.LOW)
        sleep(0.0001)
        
    def goFoward(self, duty):
        self.__setting()
        pwm = GPIO.PWM(self.channels[0],self.freq)
        pwm.start(self.duty)

    def goBackward(self,duty):
        self.__setting()
        pwm = GPIO.PWM(self.channels[1],self.freq)
        pwm.start(self.duty)

    def turbo(self):
        self.__setting()
        pwm = GPIO.PWM(self.channels[0],self.freq)
        pwm.start(1.0)
        sleep(1)
        pwm.stop()

    def breaking(self):
        self.__setting()
        GPIO.output(self.channels,GPIO.HIGH)

    def stop(self):
        self.__setting()
        
    def clean(self):
        GPIO.cleanup(self.channels)

def test():
    try:
        import time
        GPIO.setmode(GPIO.BCM)
        motor = MotorDriver(2,3)
        print("goForward")
        motor.goForward()
        time.sleep(10)
        print("goBackward")
        motor.goBackward()
        time.sleep(10)
        print("breaking")
        motor.stop()
        time.sleep(5)
        print("stop")
        motor.breaking()
        time.sleep(5)
    except KeyboardInterrupt:
        pass
    finally:   
        motor.clean()
        print("end")

if __name__ == '__main__':
    test()
