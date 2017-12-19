import RPi.GPIO

class ServoMotor:
    '''PWM period may be 50Hz(20ms) 
       Duty Cycle is 0.5~2.4ms ~0.5ms is -90deg /~2.4ms +90deg'''
    period = 1/freq

    #pulsetime
    highest = 2.4
    lowest = 0.5
    middle =  (highest+lowest)/2

    #duty ratio
    right = highest/ period
    left = 0
    straight = middle/period
    
    def __init__(self,pin):
        self.freq = 50
        self.duty = self.middle / (1/self.freq)
        self.pin = pin
        GPIO.setup(pin,GPIO.OUT)
        self.pwm = GPIO.pwm(self.pin,self.freq)
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
    
        
        

