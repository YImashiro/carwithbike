import pygame
from pygame.locals import *
#from Parts import *
#import RPi.GPIO as GPIO
import sys

def makeScreen():
    SCREEN_SIZE = (100,100)
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    screen.fill((0,0,0))
    
'''GPIO.setmode(GPIO.BCM)
motordriver = MotorDriver.MotorDriver(2,3)
servoMotor = ServoMotor.ServoMotor(4)
light = Light.Light(17,22,27)    
'''
lw,rw,hl = 0,0,0 #flag


makeScreen()
try:
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    print("K_ESCAPE")
                    '''light.clean()
                    servomotor.clean()
                    motordriver.clean()
                    '''
                elif event.key == K_f:
                    if lw == 0:
                        #light.leftWinkerOn()
                        print("K_f,{}".format(lw))
                    else:
                        #light.leftWinkerOff()
                        print("K_f,{}".format(lw))
                    lw = 1-lw
                    
                elif event.key == K_j:
                    if rw == 0:
                        print("K_j,{}".format(rw))
                        #light.rightWinkerOn()
                    else:
                        print("K_j,{}".format(rw))
                        #light.rightWinkerOff()
                    rw = 1-rw
                    
                elif event.key == K_h:
                    if hl == 0:
                        #light.headLampOn()
                        print("K_h,{}".format(hl))
                    else:
                        #light.headLampOff()
                        print("K_h,{}".format(hl))
                    hl = 1-hl

        pressed = pygame.key.get_pressed()
        if pressed[K_UP] and pressed[K_DOWN]:
            print("K_UP and K_DOWN")
             #moverdriver.breaking()
        elif pressed[K_UP]:
            print("K_UP")
            #motordriver.goForward(50)
        elif pressed[K_DOWN]:
            print("K_DOWN")
            #motordriver.goBackward(30)

            
        if pressed[K_LEFT] and pressed[K_RIGHT]:
            print("K_LEFT, K_RIGHT")
            #servomotor.servoReset()
        elif pressed[K_LEFT]:
            print("K_LEFT")
            #servomotor.servocontrol(servomotor.left)
        elif pressed[K_RIGHT]:
            print("K_RIGHT")
            #servomotor.servocontrol(servomotor.right)
        else:
            #servomotor.servoReset()
            
        '''if event.type == KEYUP:
            if event.key == K_UP or K_DOWN:
                motordriver.stop()
            elif event.key == K_RIGHT or K_LEFT:
                servomotor.'''

except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit(0)
