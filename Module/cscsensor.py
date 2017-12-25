from bluepy.btle import DefaultDelegate
from bluepy.btle import Peripheral
from bluepy import btle
import struct
import sys

class DelegateForCSC(btle.DefaultDelegate):
    wheelrevlast, crankrevlast = 0, 0
    lwet,lcet = 0,0
    flag = 1
    
    def __init__(self):
        super().__init__()

    def __speed(self,data):
        wheelrevnow = struct.unpack("<L",data[1:5])[0]
        nwet = struct.unpack("<H",data[5:7])[0]
        if (nwet-self.lwet == 0):
            self.speed = 0
            return
        
        if (nwet-self.lwet < 0):
            self.lwet = nwet
            self.wheelrevlast = wheelrevnow
            return
        self.speed = (wheelrevnow-self.wheelrevlast)*2/((nwet-self.lwet)/1024.0) *3.6
        self.wheelrevlast = wheelrevnow
        self.lwet = nwet

    def __cadence(self,data):
        crankrevnow = struct.unpack("<H",data[7:9])[0]
        ncet = struct.unpack("<H",data[9:11])[0]
        if (ncet == self.lcet):
            self.cadence = 0
            return
        if (ncet-self.lcet < 0):
            self.lcet = ncet
            self.crankrevlast = crankrevnow
            return
        self.cadence = int((crankrevnow - self.crankrevlast)/((ncet-self.lcet)/1024.0) * 60) 
        self.lcet = ncet
        self.crankrevlast = crankrevnow

    def printSpeed(self,data):
        self.__speed(data)
        print("speed : {} kph".format(self.speed))
        
    def printCadence(self,data):
        self.__cadence(data)
        print("cadence: {} rpm ".format(self.cadence))

    
    def handleNotification(self,cHandle,data):
        if data[0] == 0:
            print("NO SENSOR AVAILABLE")
            self.flag = 0
        elif data[0] == 1:
            print("SPEED SENSOR AVAILABLE")
            self.printSpeed(data)
            
        elif data[1] == 2:
            print("CADENCE SENSOR AVAILABLE")
            self.printCadence(data)
            
        elif data[0] == 3:
            self.__speed(data)
            self.__cadence(data)

if __name__ == "__main__":       
    peripheral = Peripheral("d8:e3:66:b3:b9:95",btle.ADDR_TYPE_RANDOM)
    delegate = DelegateForCSC()
    peripheral.withDelegate(delegate)
    peripheral.writeCharacteristic(12,(1).to_bytes(2, byteorder='little'))

    try:
        while delegate.flag:
            if peripheral.waitForNotifications(10):
                delegate.speed
                continue
            break
    except:
        print("disconnected")
        
    finally:
        peripheral.disconnect()
        sys.exit(0)



    
