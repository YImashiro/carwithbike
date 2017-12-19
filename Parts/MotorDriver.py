#!/usr/bin/python
import RPi.GPIO as GPIO

class MotorDriver:
    freq = 50
    duty = 0.8

    def __init__(self):
        channels = [2,3]
        GPIO.setup(channels,GPIO.OUT)

    def goFoward(self, duty):
        pwm = GPIO.PWM(2,self.freq)
        pwm.start(duty)

    def goBackward(self,duty):
        pwm = GPIO.PWM(3,self.freq)
        pwm.start(duty)

    def breaking(self):
        GPIO.output(channels,GPIO.HIGH)

    def stop(self):
        GPIO.output(channels,PGIO.LOW)

    def clean(self):
        GPIO.cleanup(channels)
