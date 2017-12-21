import RPi.GPIO as GPIO

class Light:
    freq = 1
    duty = 0.5
    def __init__(self):
        self.channels = [17,22,27]
        GPIO.setup(self.channels,GPIO.OUT)
        pwm_left = GPIO.PWM(17,self.freq)
        pwm_right = GPIO.PWM(27,self.freq)

    def __setup(self):
        GPIO.setup(self.channels,GPIO.OUT)
        pwm_left = GPIO.pwm(17,freq)
        pwm_right = GPIO.pwm(27,freq)
        
    def headLampOn(self):
        GPIO.output(22,GPIO.HIGH)
    def headLampOff(self):
        GPIO.output(22,GPIO.LOW)
        
    def leftWinkerOn(self):
        self.pwm_left.start(self.duty)
    def leftWinkerOff(self):
        self.pwm_left.stop()

    def rightWinkerOn(self):
        self.pwm_right.start(self.duty)
    def rightWinkerOff(self):
        self.pwm_right.stop() 

    def clean(self):
        GPIO.cleanup(channels)
        
