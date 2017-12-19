import pygame
import MotorDriver
import ServoMotor
import Light

pygame.init()
motordriver = MotorDriver()
servoMotor = ServoMotor()
light = Light()

lw,rw,hl = 0,0,0 #flag
while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == 'K_ESCAPE':
                light.clean()
                servomotor.clean()
                motordriver.clean()
            
            if event.key == 'K_f':
                if lw = 0:
                    light.leftWinkerOn()
                else:
                    light.leftWinkerOff()
                lw = 1-lw
                
            elif event.key == 'K_j':
                if rw = 0:
                    light.rightWinkerOn()
                else:
                    light.rightWinkerOff()
                rw = 1-rw
                
            elif event.key == 'K_h':
                if hl = 0:
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
        if pressed[K_UP] and pressed[K_DOWN]:
            moverdriver.breaking()
        elif pressed[K_UP]:
            motordriver.goForward(50)
        elif pressed[K_DOWN]:
            motordriver.goBackward(30)
        elif pressed[K_LEFT] and pressed[K_RIGHT]:
            servomotor.servoReset()
        elif pressed[K_LEFT]:
            servomotor.servocontrol(servomotor.left)
        elif pressed[K_RIGHT]:
            servomotor.servocontrol(servomotor.right)
            
            
        '''if event.type == KEYUP:
            if event.key == K_UP or K_DOWN:
                motordriver.stop()
            elif event.key == K_RIGHT or K_LEFT:
                servomotor.'''
            
                
            
                
                
    
