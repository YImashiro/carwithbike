#!/usr/bin/env python3
import RPi.GPIO as GPIO
import sys
import time

class MotorDriver:
    freq = 100
    duty = 100

    def __init__(self,pin1,pin2,pin3):
        GPIO.setmode(GPIO.BCM)
        self.channels = [pin1,pin2,pin3]
        GPIO.setup(self.channels,GPIO.OUT)
        self.pwmf = GPIO.PWM(self.channels[0],self.freq) 
        self.pwmb = GPIO.PWM(self.channels[1],self.freq)
        self.pwml = GPIO.PWM(self.channels[2],self.freq)
        self.pwmf.start(0)
        self.pwmb.start(0)
        self.pwml.start(0)
        
    def __setting(self):
        self.pwmf.ChangeDutyCycle(0)
        self.pwmb.ChangeDutyCycle(0)
        self.pwml.ChangeDutyCycle(0)
        time.sleep(0.0001)
        
    def goForward(self,duty=60):
        self.__setting()
        self.pwmf.ChangeDutyCycle(duty)
        
    def goBackward(self,duty=60):
        self.__setting()
        self.pwmb.ChangeDutyCycle(duty)
               
    def turbo(self):
        self.__setting()
        self.pwmf.ChangeDutyCycle(100)
        time.sleep(1)
        self.goForward()

    def breaking(self):
        self.__setting()
        self.pwmf.ChangeDutyCycle(100)
        self.pwmb.ChangeDutyCycle(100)
        self.pwml.ChangeDutyCycle(100)

    def stop(self):
        self.__setting()
        
    def clean(self):
        GPIO.cleanup(self.channels)

class MotorDriverwithCSC(MotorDriver):
    def gowithCSC(self,duty,cadence):
        if duty == 0:
            if cadence > 100:
                cadence = 100
            self.goBackward(cadence)
        else:
            self.goForward(duty)
        
'''
def test():
    try:
        motor= MotorDriver(19,26,13)
        motor.goForward()
        time.sleep(10)
        print("goBackward")
        motor.goBackward()
        time.sleep(10)
        print("stop")
        motor.stop()
        time.sleep(3)
        print("breaking")
        motor.breaking()
        time.sleep(3)
    except KeyboardInterrupt:
        pass
    finally:   
        motor.clean()
        print("end")

if __name__ == '__main__':
    test()
'''
