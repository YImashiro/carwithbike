#!/usr/bin/env python3
import RPi.GPIO as GPIO
import sys
import time
from bluepy.btle import DefaultDelegate
from bluepy.btle import Peripheral
from bluepy import btle
import threading
from Module import cscsensor
from Parts import MotorDriverwithCSC

def convertCSCtoDuty(csc):
    '''30km/h is 340w'''
    if csc < 0:
        csc =0
    elif csc > 30:
        csc = 30
        
    return csc*100/30.0

motor = MotorDriverwitCSC()
thread1 = threading.Thread(name="csc",target=cscsensor.init)
thread1.start()

while True:
    duty = convertCSCtoDuty(cscsensor.delegate.speed)
    cadence = cscsensor.delegate.cadence
    motor.gowithCSC(duty,cadence)
    time.sleep(1)
