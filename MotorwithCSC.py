#!/usr/bin/env python3
#import RPi.GPIO as GPIO
import sys
import time
from bluepy.btle import DefaultDelegate
from bluepy.btle import Peripheral
from bluepy import btle
import threading
from Module import cscsensor
#from Parts import MotorDriver

def convertCSCtoDuty(csc):
    '''30km/h is 340w'''
    if csc < 0:
        csc =0
    elif csc > 30:
        csc = 30
        
    return csc*100/30.0

    
peripheral = Peripheral("d8:e3:66:b3:b9:95",btle.ADDR_TYPE_RANDOM)
delegate = cscsensor.DelegateForCSC()
peripheral.withDelegate(delegate)
peripheral.writeCharacteristic(12,(1).to_bytes(2, byteorder='little'))
#motor = MotorDriverwithCSC(pin1,pin2)


try:
    while delegate.flag:
        if peripheral.waitForNotifications(10):
            duty = convertCSCtoDuty(delegate.speed)
            cadence = delegate.cadence
            print(duty,cadence)
            #motor.gowithCSC(duty,cadence)
            continue
        break
except:
    print("disconnected")
finally:
    peripheral.disconnect()
    sys.exit()
    

