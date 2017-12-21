#!/usr/bin/python
import RPi.GPIO as GPIO

class MotorDriver:
    freq = 50
    duty = 0.8

    def __init__(self):
        channels = [2,3]
        GPIO.setup(channels,GPIO.OUT)

    def __setting(self):
        GPIO.output(self.channels,GPIO.LOW)
        sleep(0.0001)
        
    def goFoward(self, duty):
        self.__setting()
        pwm = GPIO.PWM(2,self.freq)
        pwm.start(self.duty)

    def goBackward(self,duty):
        self.__setting()
        pwm = GPIO.PWM(3,self.freq)
        pwm.start(self.duty)

    def turbo(self):
        self.__setting()
        pwm = GPIO.PWM(2,self.freq)
        pwm.start(1.0)
        sleep(1)
        pwm.stop()

    def breaking(self):
        self.__setting()
        GPIO.output(channels,GPIO.HIGH)

    def stop(self):
        GPIO.output(channels,PGIO.LOW)

    def clean(self):
        GPIO.cleanup(channels)
