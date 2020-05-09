import pygame
from pygame.locals import *
from pygame.transform import rotate,scale
from os.path import join
from random import randint as ri

#Game variables
ScreenSize=480
CharacterSize=50
TimeofGame=60
#Game configurations
screen = pygame.display.set_mode([ScreenSize,ScreenSize])
CharacterMove=[]

CharacterMove.append(scale(pygame.image.load("charfm1.png"),(CharacterSize,CharacterSize))) #Walke-01
CharacterMove.append(scale(pygame.image.load("charfm2.png"),(CharacterSize,CharacterSize))) #Walk-02
CharacterMove.append(scale(pygame.image.load("CharJump.png"),(CharacterSize,CharacterSize))) #Jump
CharacterMove.append(scale(pygame.image.load("charfm1.png"),(int(0.565*CharacterSize),CharacterSize))) #Aspect Ratio Scaling



#Game Dynamics
alter=1
run=1
while run:
    keys = pygame.key.get_pressed()  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if keys[pygame.K_SPACE]:
        flagJ=1
        jumpS=0
    elif keys[pygame.K_UP]:
        flagJ=0
        flagC=1
    screen.fill([255,0,0])
    #screen.blit(SkyScreen,(lengthCameraFrame,0,widthCameraFrame,int(widthCameraFrame/2)))
   # screen.blit(GroundScreen,(lengthCameraFrame,int(widthCameraFrame/2),widthCameraFrame,int(widthCameraFrame/2)))
    if alter==1:
        screen.blit(CharacterMove[0],(50,50))
    else:
        screen.blit(CharacterMove[1],(50,50))
    alter*=-1
    pygame.display.update()
    if pygame.time.get_ticks()>=TimeofGame*1000:
        print("Game over")
        break
    
pygame.quit()


