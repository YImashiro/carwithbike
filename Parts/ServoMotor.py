import RPi.GPIO as GPIO

class ServoMotor:
    '''PWM period may be 50Hz(20ms) 
       Duty Cycle is 0.5~2.4ms ~0.5ms is -90deg /~2.4ms +90deg'''
    #pulsetime
    highest, lowest = 2.4, 0.5
    middle =  (highest+lowest)/2
    
    def __init__(self,pin):
        self.freq = 50.0
        self.duty = self.middle / (1/self.freq)
        self.pin = pin
        self.period = 1.0/self.freq
        GPIO.setup(pin,GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin,self.freq)
        #duty ratio
        self.right = self.highest/ self.period
        self.left = 0
        self.straight = self.middle/ self.period
        self.pwm.start(self.straight)
    

    def servoControl(self,dir):
        if dir == "left":
            pwm.start(left)
        elif dir == "right":
            pwm.start(right)
        else:
            pwm.start(middle)

    def servoReset(self):
        pwm.start(middle)

    def clean(self):
        GPIO.cleanup(self.pin)
    
        
def test():
    import time
    GPIO.setmode(GPIO.BCM)
    servo = ServoMotor(4)
    servoControl("left")
    time.sleep(5)
    servo.servoControl("right")
    time.sleep(5)
    servo.reset()

if __name__ == "__main__":
    test()
