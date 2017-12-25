import MotorDriver

class MotorDriverwithCSC(MotorDriver):

    def __goForwardwithCSC(self,duty):
        self.goForward(self,duty)

    def __goBackwardwithCSC(self,cadence):
        self.goBackward(self,cadence)

    def gowithCSC(self,duty,cadence):
        if duty == 0:
            if cadence > 100:
                cadence = 100
            __goBackwardwithCSC(cadence)
        else:
            __goForwardwithCSC(duty)
            
