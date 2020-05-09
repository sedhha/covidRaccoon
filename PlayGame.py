import pygame
from pygame.locals import *
from pygame.transform import rotate,scale
from os.path import join
from random import randint as ri

#Game variables
ScreenSize=720
ScreenWidth=480
CharacterSize=50
TimeofGame=60
yInit=300
CloudLength=80
CloudWidth=30
BirdSquare=50
BirdRectangleH=60
BirdRectangleW=40


#Game configurations
screen = pygame.display.set_mode([ScreenSize,ScreenWidth])
CharacterMove=[]
CharacterMove.append(scale(pygame.image.load("charfm1.png"),(CharacterSize,CharacterSize))) #Walke-01
CharacterMove.append(scale(pygame.image.load("charfm2.png"),(CharacterSize,CharacterSize))) #Walk-02
CharacterMove.append(scale(pygame.image.load("CharJump.png"),(CharacterSize,CharacterSize))) #Jump
CharacterMove.append(scale(pygame.image.load("charfm1.png"),(int(0.565*CharacterSize),CharacterSize))) #Aspect Ratio Scaling


#Game Environment
Environment=scale(pygame.image.load("cityBg.png"),(ScreenSize,ScreenWidth))
#Sky Variables

Skies=[]
Skies.append(scale(pygame.image.load("cloud.png"),(CloudLength,CloudWidth)))
Skies.append(scale(pygame.image.load("cloud2.png"),(CloudLength,CloudWidth)))
Skies.append(scale(pygame.image.load("bird1.png"),(BirdRectangleH,BirdRectangleW)))
Skies.append(scale(pygame.image.load("bird2.png"),(BirdRectangleH,BirdRectangleW)))
Skies.append(scale(pygame.image.load("bird3.png"),(BirdSquare,BirdSquare)))

#Road Variables

Roads=[]
virussize=60
virusTYPE=0
Roads.append([scale(pygame.image.load("cv1.png"),(virussize,virussize)),virussize,virussize,virusTYPE])
Roads.append([scale(pygame.image.load("cv2.png"),(virussize,virussize)),virussize,virussize,virusTYPE])
Roads.append([scale(pygame.image.load("cv3.png"),(89,59)),89,59,virusTYPE]) #Long Sized Virus
Roads.append([scale(pygame.image.load("cv4.png"),(virussize,virussize)),virussize,virussize,virusTYPE])
Roads.append([scale(pygame.image.load("cv5.png"),(virussize,virussize)),virussize,virussize,virusTYPE])
Roads.append([scale(pygame.image.load("cv6.png"),(virussize,virussize)),virussize,virussize,virusTYPE])
Roads.append([scale(pygame.image.load("cv7.png"),(virussize,virussize)),virussize,virussize,virusTYPE])
Roads.append([scale(pygame.image.load("cv8.png"),(virussize,virussize)),virussize,virussize,virusTYPE])
Roads.append([scale(pygame.image.load("cv9.png"),(virussize,virussize)),virussize,virussize,virusTYPE])
Roads.append([scale(pygame.image.load("cv10.png"),(virussize,virussize)),virussize,virussize,virusTYPE])
Roads.append([scale(pygame.image.load("cv11.png"),(virussize,virussize)),virussize,virussize,virusTYPE])
Roads.append([scale(pygame.image.load("cv12.png"),(virussize,virussize)),virussize,virussize,virusTYPE])

SanetizerBottleSize=60
SanetizerProt=[scale(pygame.image.load("sanetizer.png"),(SanetizerBottleSize,int(5*SanetizerBottleSize/3))),int(5*SanetizerBottleSize/3)]
flyvirussize=80 #Aspect ratio is 2:1
virusTYPe=1
Roads.append([scale(pygame.image.load("fly1.png"),(flyvirussize,int(flyvirussize/2))),flyvirussize,int(flyvirussize/2),virusTYPe])
Roads.append([scale(pygame.image.load("fly2.png"),(flyvirussize,int(flyvirussize/2))),flyvirussize,int(flyvirussize/2),virusTYPe])

#Game Dynamics
#Static Functions
def reinitialize():
    return(ScreenSize)
#Dynamics Variables
IsSkyClear=True
IsRoadClear=True
IsSanetizerOn=False
SkyEntityVelocity=45
RoadEntityVelocity=30
SkyX=reinitialize()
SkyHeightY=100
GameSpeed=100
FlyingVT=20
xInit=50 #Character X position
#Dynamics Functions
def Movement(xn,IsScreenClear,Type):
    IsScreenClear=False
    if Type:
        xn-=SkyEntityVelocity
    else:
        xn-=RoadEntityVelocity
    if xn<=0:
        xn=reinitialize()
        IsScreenClear=True
    return(xn,IsScreenClear)
def getSkyEntity():
    SkyIndex=ri(0,len(Skies)-1)
    EntitySky=Skies[SkyIndex]
    return(EntitySky,reinitialize(),SkyHeightY)
def getRoadEntity():
    Type=0
    if ri(0,15)==0: #Making this event less likely
        EntitySky,y=SanetizerProt
        return(EntitySky,reinitialize(),yInit+CharacterSize-y,y,0)
    else:
        RoadIndex=ri(0,len(Roads)-1)
        EntitySky,_,y,Type=Roads[RoadIndex]
        tmp=y
        if Type:
            print("This comes true")
            tmp=y
            y=y+30
        return(EntitySky,reinitialize(),yInit+CharacterSize-y,tmp,1)
    
#Game-Play
alter=1
run=1
Danger=1
while run:
    screen.blit(Environment,(0,0)) #Creating Environment
    if IsSkyClear:
        #Get the Sky Entity EntitySky,SkyX,SkyY=getSkyEntity()
        EntitySky,SkyX,SkyY=getSkyEntity()
        IsSkyClear=False
    else:
        SkyX,IsSkyClear=Movement(SkyX,IsSkyClear,1)
        screen.blit(EntitySky,(SkyX,SkyY))
    if IsRoadClear:
        #Get the Road Entity EntityRoad,RoadY,RoadY=getSkyEntity()
        EntityRoad,RoadX,RoadY,HeightVirus,Danger=getRoadEntity()
        IsRoadClear=False
    else:
        RoadX,IsRoadClear=Movement(RoadX,IsRoadClear,0)
        screen.blit(EntityRoad,(RoadX,RoadY))
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
    if RoadX>=xInit and RoadX<=xInit+CharacterSize:
        if RoadY+HeightVirus>=yInit and RoadY+HeightVirus<=yInit+CharacterSize:
            if Danger:print("Collision")
            else:print("Sanetization")
    if alter==1:
        screen.blit(CharacterMove[0],(xInit,yInit))
    else:
        screen.blit(CharacterMove[1],(xInit,yInit))
    alter*=-1
    pygame.display.update()
    pygame.time.delay(GameSpeed)
    if pygame.time.get_ticks()>=TimeofGame*1000:
        print("Game over")
        break
    
pygame.quit()


