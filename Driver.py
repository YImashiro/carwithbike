import pygame
from Parts import *
import RPi.GPIO as GPIO
import sys


pygame.init()
GPIO.setmode(GPIO.BCM)
motordriver = MotorDriver.MotorDriver(2,3)
servoMotor = ServoMotor.ServoMotor(4)
light = Light.Light(17,22,27)    
lw,rw,hl = 0,0,0 #flag

try:
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == 'K_ESCAPE':
                    light.clean()
                    servomotor.clean()
                    motordriver.clean()
                    
                if event.key == 'K_f':
                    if lw == 0:
                        light.leftWinkerOn()
                    else:
                        light.leftWinkerOff()
                        lw = 1-lw
                    
                elif event.key == 'K_j':
                    if rw == 0:
                        light.rightWinkerOn()
                    else:
                        light.rightWinkerOff()
                        rw = 1-rw
                    
                elif event.key == 'K_h':
                    if hl == 0:
                        light.headLampOn()
                    else:
                        light.headLampOff()
                        hl = 1-hl
                    
        '''    if event.key == K_UP:
                motordriver.stop()
                motordriver.goForward(50)
            elif event.key == K_DOWN:
                motordriver.stop()
                motordriver.goBackward(30)
            elif event.key == K_RIGHT:
                servomotor.servoControl(servomotor.right)
            elif event.key == K_LEFT:
                servomotor.servoControl(servomotor.left)'''
        

        pressed = pygame.key.get_pressed()
        if 'K_UP' and 'K_DOWN' in pressed:
            moverdriver.breaking()
        elif 'K_UP' in pressed:
            motordriver.goForward(50)
        elif 'K_DOWN' in pressed:
            motordriver.goBackward(30)
        if 'K_LEFT' and 'K_RIGHT' in pressed:
            servomotor.servoReset()
        elif 'K_LEFT' in pressed:
            servomotor.servocontrol(servomotor.left)
        elif 'K_RIGHT' in pressed:
            servomotor.servocontrol(servomotor.right)
            
            
        '''if event.type == KEYUP:
            if event.key == K_UP or K_DOWN:
                motordriver.stop()
            elif event.key == K_RIGHT or K_LEFT:
                servomotor.'''

except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit(0)
