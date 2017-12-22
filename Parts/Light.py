import RPi.GPIO as GPIO

class Light:
    freq = 1
    duty = 50
    def __init__(self,pin1,pin2,pin3):
        self.channels = [pin1,pin2,pin3]
        GPIO.setup(self.channels,GPIO.OUT)
        GPIO.output(self.channels,GPIO.LOW)
        self.pwm_left = GPIO.PWM(self.channels[0],self.freq)
        self.pwm_right = GPIO.PWM(self.channels[2],self.freq)        


    def headLampOn(self):
        GPIO.output(self.channels[1],GPIO.HIGH)
    def headLampOff(self):
        GPIO.output(self.channels[1],GPIO.LOW)
        
    def leftWinkerOn(self):
        self.pwm_left.start(self.duty)
    def leftWinkerOff(self):
        self.pwm_left.stop()

    def rightWinkerOn(self):
        self.pwm_right.start(self.duty)
    def rightWinkerOff(self):
        self.pwm_right.stop() 

    def clean(self):
        GPIO.cleanup(self.channels)

def test():
    GPIO.setmode(GPIO.BCM)
    import time
    try:
        light = Light(17,22,27)
        '''print("headlamp on")
        light.headLampOn()
        time.sleep(5)
        print("headlamp off")
        light.headLampOff()
        '''
        print("right on, left Off")
        light.rightWinkerOn()
        time.sleep(5)
        light.rightWinkerOff()
        print("leftWinker On")
        light.leftWinkerOn()
        time.sleep(5)
        light.leftWinkerOff()
    
    except:
        pass
    finally:
        light.clean()
    
if __name__ == "__main__":
    test()
