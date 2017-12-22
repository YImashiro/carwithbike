#!/usr/bin/python
import RPi.GPIO as GPIO
import sys
import time

class MotorDriver:
    freq = 100
    duty = 100
    f,b = 0,0

    def __init__(self,pin1,pin2):
        GPIO.setmode(GPIO.BCM)
        self.channels = [pin1,pin2]
        GPIO.setup(self.channels,GPIO.OUT)
            
    def __setting(self):
        GPIO.output(self.channels,GPIO.LOW)
        time.sleep(0.0001)
        if(self.f):
            self.pwmf.stop()
            self.f = 0
        if(self.b):
            self.pwmb.stop()
            self.b = 0
        
    def goForward(self):
        self.__setting()
        self.pwmf = GPIO.PWM(self.channels[0],self.freq)
        self.pwmf.start(self.duty)
        self.f = 1
        
    def goBackward(self):
        self.__setting()
        self.pwmb = GPIO.PWM(self.channels[1],self.freq)
        self.pwmb.start(self.duty)
        self.b = 1
        
    def turbo(self):
        self.__setting()
        pwm = GPIO.PWM(self.channels[0],self.freq)
        pwm.start(100)
        sleep(1)
        pwm.stop()

    def breaking(self):
        self.__setting()
        GPIO.output(self.channels,GPIO.HIGH)
        time.sleep(3)

    def stop(self):
        self.__setting()
        
    def clean(self):
        GPIO.cleanup(self.channels)

def test():
    try:
        motor= MotorDriver(19,26)
        motor.goForward()
        time.sleep(10)
        print("goBackward")
        motor.goBackward()
        time.sleep(10)
        print("breaking")
        motor.stop()
        time.sleep(3)
        print("stop")
        motor.breaking()
        time.sleep(3)
    except KeyboardInterrupt:
        pass
    finally:   
        motor.clean()
        print("end")
if __name__ == '__main__':
    test()
