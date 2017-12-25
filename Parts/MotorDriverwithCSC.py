import MotorDriver

class MotorDriverwithCSC(MotorDriver):

    def __goForwardwithCSC(self,speed):
        self.speed = speed
        self.goForward(self,duty=speed)

    def __goBackwardwithCSC(self,speed):
        self.speed = speed
        self.goBackward(self,duty=speed)

    def gowithCSC(self,speed,cadence):
        if speed == 0:
            __goBackwardwithCSC(speed)
        else:
            __goForwardwithCSC(speed)
            
