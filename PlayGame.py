<<<<<<< HEAD
import pygame
from pygame.locals import *
from pygame.transform import rotate,scale
from os.path import join
from random import randint as ri
import warnings
warnings.filterwarnings("ignore")
from time import sleep
#import cv2 #For waitkeys
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("--diff",help="Set Difficulty [Easy | Medium | Hard]",type=str)
args, leftovers = parser.parse_known_args()
if args.diff is None or args.diff=="Easy":
    TimeofGame=60
    GameSpeed=100
    SkyEntityVelocity=65 #Velocity of the entities floating in the sky
    RoadEntityVelocity=25
elif args.diff=="Medium":
    TimeofGame=180
    GameSpeed=80
    SkyEntityVelocity=65 #Velocity of the entities floating in the sky
    RoadEntityVelocity=25
    
else:
    TimeofGame=300
    GameSpeed=50
    SkyEntityVelocity=65 #Velocity of the entities floating in the sky
    RoadEntityVelocity=70
print(TimeofGame,GameSpeed,SkyEntityVelocity,RoadEntityVelocity) 
#Game variables
#Please note that except for these variables don't change any other variable as it may affect the logic of game

#Variables that are not recommended to change
ScreenSize=720 #Screen size in terms of X-Co ordinate
ScreenWidth=480 #Screen size in terms of Y-Co ordinate
CharacterSize=50 #Size of playing character
yInit=300  #initial Y-co ordinate of the player
xInit=50 #Initial X-co ordinate of the player

#Variables that can be changed
#TimeofGame=60 #Game Completion time in seconds
ExplosionSize=50 #Explosion on collision (Size of the surface [Explosion icon]
virussize=60 #Incoming Viruses Size
CloudLength=80 #Sky cloud Length
CloudWidth=30 #Sky Cloud width
BirdSquare=50 #1:1 Aspect ratio birds
BirdRectangleH=60 # Rectangular aspect ratio Bird Icons
BirdRectangleW=40 # Rectangular aspect ratio Bird Icons (If you change these make sure you change them in the same aspect ratio
SkyHeightY=100 #Location at which birds and clouds are flying
#GameSpeed=100 #Speed of occurences in the game
#SkyEntityVelocity=65 #Velocity of the entities floating in the sky
#RoadEntityVelocity=35 #Velocity of the entities moving on the road
jumpLim=jumpMag=7 #Jumping intensity of the Player
jumpGrowth=0.5 # Magnification factor of Height achieved per unit of jump
GameLives=3 #Total lives in Game
CarSpeed=40
CarHeightY=400
CarLength=150

#Game configurations
screen = pygame.display.set_mode([ScreenSize,ScreenWidth])
CharacterMove=[]
CharacterMove.append(scale(pygame.image.load("charfm1.png"),(CharacterSize,CharacterSize))) #Walke-01
CharacterMove.append(scale(pygame.image.load("charfm2.png"),(CharacterSize,CharacterSize))) #Walk-02
CharacterMove.append(scale(pygame.image.load("CharJump.png"),(CharacterSize,CharacterSize))) #Jump

CharacterMove.append(scale(pygame.image.load("Charduck.png"),(int((CharacterSize-20)/0.724),CharacterSize-20))) #Aspect Ratio Scaling Dodge


#Game Environment
Environment=[]
Environment.append(scale(pygame.image.load("cityBg.png"),(ScreenSize,ScreenWidth)))
Environment.append(scale(pygame.image.load("cityBg1.png"),(ScreenSize,ScreenWidth)))
Environment.append(scale(pygame.image.load("cityBg2.png"),(ScreenSize,ScreenWidth)))
Environment.append(scale(pygame.image.load("cityBg3.png"),(ScreenSize,ScreenWidth)))
#Environment.append(scale(pygame.image.load("cityBg02.png"),(ScreenSize,ScreenWidth)))
#Environment.append(scale(pygame.image.load("cityBg03.png"),(ScreenSize,ScreenWidth)))
#Sky Variables

Skies=[]
Skies.append(scale(pygame.image.load("cloud.png"),(CloudLength,CloudWidth)))
Skies.append(scale(pygame.image.load("cloud2.png"),(CloudLength,CloudWidth)))
Skies.append(scale(pygame.image.load("bird1.png"),(BirdRectangleH,BirdRectangleW)))
Skies.append(scale(pygame.image.load("bird2.png"),(BirdRectangleH,BirdRectangleW)))
Skies.append(scale(pygame.image.load("bird3.png"),(BirdSquare,BirdSquare)))

#Road Variables

Roads=[]
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
Roads.append([scale(pygame.image.load("cv12.png"),(virussize,virussize)),virussize,virussize,virusTYPE]) #upto index=11

#Cars
Cars=[]
Cars.append(scale(pygame.image.load("car1.png"),(CarLength,int(CarLength/3))))
Cars.append(scale(pygame.image.load("car2.png"),(CarLength,int(CarLength/3))))
Cars.append(scale(pygame.image.load("car3.png"),(CarLength,int(CarLength/3))))
Cars.append(scale(pygame.image.load("car4.png"),(CarLength,int(CarLength/3))))
Cars.append(scale(pygame.image.load("car5.png"),(CarLength,int(CarLength/3))))

#Protection Variables

SanetizerBottleSize=60
SanetizerProt=[scale(pygame.image.load("sanetizer.png"),(SanetizerBottleSize,int(5*SanetizerBottleSize/3))),int(5*SanetizerBottleSize/3)]
flyvirussize=80 #Aspect ratio is 2:1
virusTYPe=1
Roads.append([scale(pygame.image.load("fly1.png"),(flyvirussize,int(flyvirussize/2))),flyvirussize,int(flyvirussize/2),virusTYPe])
Roads.append([scale(pygame.image.load("fly2.png"),(flyvirussize,int(flyvirussize/2))),flyvirussize,int(flyvirussize/2),virusTYPe])

#Game Screens

ExitScreen=scale(pygame.image.load("FinalScreen.png"),(ScreenSize,ScreenWidth))
HomeSize=80
HomeSS=scale(pygame.image.load("home.png"),(HomeSize,HomeSize))
WinnerScreen=scale(pygame.image.load("WinnerScreen.png"),(ScreenSize,ScreenWidth))

#Explosions

Booom=[]
Booom.append(scale(pygame.image.load("explosion.png"),(ExplosionSize,ExplosionSize)))
Booom.append(scale(pygame.image.load("whiteSmoke.png"),(ExplosionSize,ExplosionSize)))
#Game Dynamics
#Static Functions
def reinitialize():
    return(ScreenSize)
#Dynamics Variables
IsSkyClear=True
IsRoadClear=True
IsCarClear=True
IsSanetizerOn=False
Crouch=False
Jump=False
SkyX=reinitialize()
FlyingVT=20
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
def CarMovement(xN,IsScreenClear):
    IsScreenClear=False
    if xN>=ScreenSize:
        IsScreenClear=True
        xN=0
    else:
        xN+=CarSpeed
    return(xN,IsScreenClear)
def getCarEntity():
    SkyIndex=ri(0,len(Cars)-1)
    EntitySky=Cars[SkyIndex]
    return(EntitySky,0,CarHeightY)
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
            #print("This comes true")
            tmp=y
            y=y+35
        return(EntitySky,reinitialize(),yInit+CharacterSize-y,tmp,1)
def jump(y,jumpLim,flag):
    if jumpLim==-jumpMag:
        jumpLim=jumpMag
        y=yInit
        flag=0
    else:
        y-=jumpLim*abs(jumpLim)*jumpGrowth
        jumpLim-=1
    #print(f"Jump values:{jumpLim}")
    return(y,jumpLim,flag)
def DrawFunction(screen,xC,yC,x1,y1,color=[255,0,0]): #This helped me a lot in debugging and building logic :-P
    pygame.draw.rect(screen, color, [xC, yC, x1, y1], 1)
def BoomEffect(screen,ind,Sanet,x,y):
    screen.blit(Environment[Sanet],(0,0))
    if ind:
        screen.blit(Booom[0],(x,y))
    else:
        #print("S Kills")
        #print(x,y)
        screen.blit(Booom[1],(x,y))
        screen.blit(CharacterMove[1],(xInit,yInit))
    pygame.display.update()
    pygame.time.delay(1000)

        
#Game-Play
alter=1
run=1
Danger=1
yTop=yInit
Sanet=0
roadRun=0
while run:
    print("T")
    if Sanet<0:
        Sanet=0
    screen.blit(Environment[Sanet],(0,0)) #Creating Environment
    if IsCarClear:
        EntityCar,CarX,CarY=getCarEntity()
        IsCarClear=False
    else:
        CarX,IsCarClear=CarMovement(CarX,IsCarClear)
        screen.blit(EntityCar,(CarX,CarY))
        print("Else happens")
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
        #DrawFunction(screen,RoadX,RoadY,HeightVirus,HeightVirus)
    keys = pygame.key.get_pressed()  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if keys[pygame.K_SPACE]:
        Jump=1
    elif keys[pygame.K_UP]:
        Jump=0
        jumpLim=jumpMag
        yInit=300
        Crouch=1
        #crouch()
    if RoadX>=xInit and RoadX<=xInit+CharacterSize:
        if (yTop<=RoadY+HeightVirus and yTop>=RoadY) or (yTop+CharacterSize<=RoadY+HeightVirus and yTop+CharacterSize>=RoadY):
            if Danger:
                if GameLives<=0:
                    print("Game Over!")
                    screen.blit(ExitScreen,(0,0))
                    pygame.display.update()
                    GameLives=3
                    sleep(4)
                else:
                    if Sanet>0:
                        print("Sanetization kills virus")
                        Sanet-=1
                        BoomEffect(screen,0,Sanet,RoadX,RoadY+20)
                        EntityRoad,RoadX,RoadY,HeightVirus,Danger=getRoadEntity()
                    else:
                        print("Collision")
                        BoomEffect(screen,1,Sanet,xInit+10,yTop-20)
                        EntityRoad,RoadX,RoadY,HeightVirus,Danger=getRoadEntity()
                        GameLives-=1
            else:
                print("Sanetization")
                Sanet=3
                DrawFunction(screen,xInit,yTop,CharacterSize,CharacterSize,[0,0,255])
    if alter==1 and not(Crouch) and not(Jump):            
        yTop=yInit
        screen.blit(CharacterMove[0],(xInit,yTop))
        if Sanet:
            DrawFunction(screen,xInit,yTop,CharacterSize,CharacterSize,[0,0,255])
    elif alter==-1 and not(Crouch) and not(Jump):
        yTop=yInit
        screen.blit(CharacterMove[1],(xInit,yTop))
        if Sanet:
            DrawFunction(screen,xInit,yTop,CharacterSize,CharacterSize,[0,0,255])
    elif Jump and not(Crouch):
        #print(f"{RoadY+HeightVirus}>={yTop} and {RoadY+HeightVirus}<={yTop+CharacterSize}")
        #DrawFunction(screen,xInit,yTop,CharacterSize,CharacterSize,[0,0,255])
        yTop,jumpLim,Jump=jump(yTop,jumpLim,Jump)
        screen.blit(CharacterMove[2],(xInit,yTop))
        if Sanet:
            DrawFunction(screen,xInit,yTop,CharacterSize,CharacterSize,[0,0,255])
    else:
        yTop=yInit+20
        screen.blit(CharacterMove[3],(xInit,yTop))
        if Sanet:
            DrawFunction(screen,xInit,yTop,CharacterSize,CharacterSize,[0,0,255])
        Crouch=0
    alter*=-1
    pygame.display.update()
    pygame.time.delay(GameSpeed)
    if pygame.time.get_ticks()>=TimeofGame*1000:
        xHome=ScreenSize
        alter=1
        while xHome>=xInit:
            xHome,_=Movement(xHome,False,0)
            sleep(0.1)
            screen.blit(Environment[0],(0,0))
            if alter==1:screen.blit(CharacterMove[0],(xInit,yInit))
            else:screen.blit(CharacterMove[1],(xInit,yInit))
            screen.blit(HomeSS,(xHome, yInit-20))
            pygame.display.update()
            alter*=-1
        screen.blit(Environment[0],(0,0))
        screen.blit(HomeSS,(xHome, yInit-20))
        pygame.display.update()
        sleep(2)
        screen.blit(WinnerScreen,(0,0))
        pygame.display.update()
        sleep(8)
        pygame.display.update()
        print("Game over")
        break
    
pygame.quit()


=======
import pygame
from pygame.locals import *
from pygame.transform import rotate,scale
from os.path import join
from random import randint as ri
import warnings
warnings.filterwarnings("ignore")
from time import sleep
#import cv2 #For waitkeys
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("--diff",help="Set Difficulty [Easy | Medium | Hard]",type=str)
args, leftovers = parser.parse_known_args()
if args.diff is None or args.diff=="Easy":
    TimeofGame=60
    GameSpeed=100
    SkyEntityVelocity=65 #Velocity of the entities floating in the sky
    RoadEntityVelocity=25
elif args.diff=="Medium":
    TimeofGame=180
    GameSpeed=80
    SkyEntityVelocity=65 #Velocity of the entities floating in the sky
    RoadEntityVelocity=25
    
else:
    TimeofGame=300
    GameSpeed=50
    SkyEntityVelocity=65 #Velocity of the entities floating in the sky
    RoadEntityVelocity=70
print(TimeofGame,GameSpeed,SkyEntityVelocity,RoadEntityVelocity) 
#Game variables
#Please note that except for these variables don't change any other variable as it may affect the logic of game

#Variables that are not recommended to change
ScreenSize=720 #Screen size in terms of X-Co ordinate
ScreenWidth=480 #Screen size in terms of Y-Co ordinate
CharacterSize=50 #Size of playing character
yInit=300  #initial Y-co ordinate of the player
xInit=50 #Initial X-co ordinate of the player

#Variables that can be changed
#TimeofGame=60 #Game Completion time in seconds
ExplosionSize=50 #Explosion on collision (Size of the surface [Explosion icon]
virussize=60 #Incoming Viruses Size
CloudLength=80 #Sky cloud Length
CloudWidth=30 #Sky Cloud width
BirdSquare=50 #1:1 Aspect ratio birds
BirdRectangleH=60 # Rectangular aspect ratio Bird Icons
BirdRectangleW=40 # Rectangular aspect ratio Bird Icons (If you change these make sure you change them in the same aspect ratio
SkyHeightY=100 #Location at which birds and clouds are flying
#GameSpeed=100 #Speed of occurences in the game
#SkyEntityVelocity=65 #Velocity of the entities floating in the sky
#RoadEntityVelocity=35 #Velocity of the entities moving on the road
jumpLim=jumpMag=7 #Jumping intensity of the Player
jumpGrowth=0.5 # Magnification factor of Height achieved per unit of jump
GameLives=3 #Total lives in Game
CarSpeed=40
CarHeightY=400
CarLength=150

#Game configurations
screen = pygame.display.set_mode([ScreenSize,ScreenWidth])
CharacterMove=[]
CharacterMove.append(scale(pygame.image.load("charfm1.png"),(CharacterSize,CharacterSize))) #Walke-01
CharacterMove.append(scale(pygame.image.load("charfm2.png"),(CharacterSize,CharacterSize))) #Walk-02
CharacterMove.append(scale(pygame.image.load("CharJump.png"),(CharacterSize,CharacterSize))) #Jump

CharacterMove.append(scale(pygame.image.load("Charduck.png"),(int((CharacterSize-20)/0.724),CharacterSize-20))) #Aspect Ratio Scaling Dodge


#Game Environment
Environment=[]
Environment.append(scale(pygame.image.load("cityBg.png"),(ScreenSize,ScreenWidth)))
Environment.append(scale(pygame.image.load("cityBg1.png"),(ScreenSize,ScreenWidth)))
Environment.append(scale(pygame.image.load("cityBg2.png"),(ScreenSize,ScreenWidth)))
Environment.append(scale(pygame.image.load("cityBg3.png"),(ScreenSize,ScreenWidth)))
#Environment.append(scale(pygame.image.load("cityBg02.png"),(ScreenSize,ScreenWidth)))
#Environment.append(scale(pygame.image.load("cityBg03.png"),(ScreenSize,ScreenWidth)))
#Sky Variables

Skies=[]
Skies.append(scale(pygame.image.load("cloud.png"),(CloudLength,CloudWidth)))
Skies.append(scale(pygame.image.load("cloud2.png"),(CloudLength,CloudWidth)))
Skies.append(scale(pygame.image.load("bird1.png"),(BirdRectangleH,BirdRectangleW)))
Skies.append(scale(pygame.image.load("bird2.png"),(BirdRectangleH,BirdRectangleW)))
Skies.append(scale(pygame.image.load("bird3.png"),(BirdSquare,BirdSquare)))

#Road Variables

Roads=[]
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
Roads.append([scale(pygame.image.load("cv12.png"),(virussize,virussize)),virussize,virussize,virusTYPE]) #upto index=11

#Cars
Cars=[]
Cars.append(scale(pygame.image.load("car1.png"),(CarLength,int(CarLength/3))))
Cars.append(scale(pygame.image.load("car2.png"),(CarLength,int(CarLength/3))))
Cars.append(scale(pygame.image.load("car3.png"),(CarLength,int(CarLength/3))))
Cars.append(scale(pygame.image.load("car4.png"),(CarLength,int(CarLength/3))))
Cars.append(scale(pygame.image.load("car5.png"),(CarLength,int(CarLength/3))))

#Protection Variables

SanetizerBottleSize=60
SanetizerProt=[scale(pygame.image.load("sanetizer.png"),(SanetizerBottleSize,int(5*SanetizerBottleSize/3))),int(5*SanetizerBottleSize/3)]
flyvirussize=80 #Aspect ratio is 2:1
virusTYPe=1
Roads.append([scale(pygame.image.load("fly1.png"),(flyvirussize,int(flyvirussize/2))),flyvirussize,int(flyvirussize/2),virusTYPe])
Roads.append([scale(pygame.image.load("fly2.png"),(flyvirussize,int(flyvirussize/2))),flyvirussize,int(flyvirussize/2),virusTYPe])

#Game Screens

ExitScreen=scale(pygame.image.load("FinalScreen.png"),(ScreenSize,ScreenWidth))
HomeSize=80
HomeSS=scale(pygame.image.load("home.png"),(HomeSize,HomeSize))
WinnerScreen=scale(pygame.image.load("WinnerScreen.png"),(ScreenSize,ScreenWidth))

#Explosions

Booom=[]
Booom.append(scale(pygame.image.load("explosion.png"),(ExplosionSize,ExplosionSize)))
Booom.append(scale(pygame.image.load("whiteSmoke.png"),(ExplosionSize,ExplosionSize)))
#Game Dynamics
#Static Functions
def reinitialize():
    return(ScreenSize)
#Dynamics Variables
IsSkyClear=True
IsRoadClear=True
IsCarClear=True
IsSanetizerOn=False
Crouch=False
Jump=False
SkyX=reinitialize()
FlyingVT=20
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
def CarMovement(xN,IsScreenClear):
    IsScreenClear=False
    if xN>=ScreenSize:
        IsScreenClear=True
        xN=0
    else:
        xN+=CarSpeed
    return(xN,IsScreenClear)
def getCarEntity():
    SkyIndex=ri(0,len(Cars)-1)
    EntitySky=Cars[SkyIndex]
    return(EntitySky,0,CarHeightY)
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
            #print("This comes true")
            tmp=y
            y=y+35
        return(EntitySky,reinitialize(),yInit+CharacterSize-y,tmp,1)
def jump(y,jumpLim,flag):
    if jumpLim==-jumpMag:
        jumpLim=jumpMag
        y=yInit
        flag=0
    else:
        y-=jumpLim*abs(jumpLim)*jumpGrowth
        jumpLim-=1
    #print(f"Jump values:{jumpLim}")
    return(y,jumpLim,flag)
def DrawFunction(screen,xC,yC,x1,y1,color=[255,0,0]): #This helped me a lot in debugging and building logic :-P
    pygame.draw.rect(screen, color, [xC, yC, x1, y1], 1)
def BoomEffect(screen,ind,Sanet,x,y):
    screen.blit(Environment[Sanet],(0,0))
    if ind:
        screen.blit(Booom[0],(x,y))
    else:
        #print("S Kills")
        #print(x,y)
        screen.blit(Booom[1],(x,y))
        screen.blit(CharacterMove[1],(xInit,yInit))
    pygame.display.update()
    pygame.time.delay(1000)

        
#Game-Play
alter=1
run=1
Danger=1
yTop=yInit
Sanet=0
roadRun=0
while run:
    print("T")
    if Sanet<0:
        Sanet=0
    screen.blit(Environment[Sanet],(0,0)) #Creating Environment
    if IsCarClear:
        EntityCar,CarX,CarY=getCarEntity()
        IsCarClear=False
    else:
        CarX,IsCarClear=CarMovement(CarX,IsCarClear)
        screen.blit(EntityCar,(CarX,CarY))
        print("Else happens")
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
        #DrawFunction(screen,RoadX,RoadY,HeightVirus,HeightVirus)
    keys = pygame.key.get_pressed()  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if keys[pygame.K_SPACE]:
        Jump=1
    elif keys[pygame.K_UP]:
        Jump=0
        jumpLim=jumpMag
        yInit=300
        Crouch=1
        #crouch()
    if RoadX>=xInit and RoadX<=xInit+CharacterSize:
        if (yTop<=RoadY+HeightVirus and yTop>=RoadY) or (yTop+CharacterSize<=RoadY+HeightVirus and yTop+CharacterSize>=RoadY):
            if Danger:
                if GameLives<=0:
                    print("Game Over!")
                    screen.blit(ExitScreen,(0,0))
                    pygame.display.update()
                    GameLives=3
                    sleep(4)
                else:
                    if Sanet>0:
                        print("Sanetization kills virus")
                        Sanet-=1
                        BoomEffect(screen,0,Sanet,RoadX,RoadY+20)
                        EntityRoad,RoadX,RoadY,HeightVirus,Danger=getRoadEntity()
                    else:
                        print("Collision")
                        BoomEffect(screen,1,Sanet,xInit+10,yTop-20)
                        EntityRoad,RoadX,RoadY,HeightVirus,Danger=getRoadEntity()
                        GameLives-=1
            else:
                print("Sanetization")
                Sanet=3
                DrawFunction(screen,xInit,yTop,CharacterSize,CharacterSize,[0,0,255])
    if alter==1 and not(Crouch) and not(Jump):            
        yTop=yInit
        screen.blit(CharacterMove[0],(xInit,yTop))
        if Sanet:
            DrawFunction(screen,xInit,yTop,CharacterSize,CharacterSize,[0,0,255])
    elif alter==-1 and not(Crouch) and not(Jump):
        yTop=yInit
        screen.blit(CharacterMove[1],(xInit,yTop))
        if Sanet:
            DrawFunction(screen,xInit,yTop,CharacterSize,CharacterSize,[0,0,255])
    elif Jump and not(Crouch):
        #print(f"{RoadY+HeightVirus}>={yTop} and {RoadY+HeightVirus}<={yTop+CharacterSize}")
        #DrawFunction(screen,xInit,yTop,CharacterSize,CharacterSize,[0,0,255])
        yTop,jumpLim,Jump=jump(yTop,jumpLim,Jump)
        screen.blit(CharacterMove[2],(xInit,yTop))
        if Sanet:
            DrawFunction(screen,xInit,yTop,CharacterSize,CharacterSize,[0,0,255])
    else:
        yTop=yInit+20
        screen.blit(CharacterMove[3],(xInit,yTop))
        if Sanet:
            DrawFunction(screen,xInit,yTop,CharacterSize,CharacterSize,[0,0,255])
        Crouch=0
    alter*=-1
    pygame.display.update()
    pygame.time.delay(GameSpeed)
    if pygame.time.get_ticks()>=TimeofGame*1000:
        xHome=ScreenSize
        alter=1
        while xHome>=xInit:
            xHome,_=Movement(xHome,False,0)
            sleep(0.1)
            screen.blit(Environment[0],(0,0))
            if alter==1:screen.blit(CharacterMove[0],(xInit,yInit))
            else:screen.blit(CharacterMove[1],(xInit,yInit))
            screen.blit(HomeSS,(xHome, yInit-20))
            pygame.display.update()
            alter*=-1
        screen.blit(Environment[0],(0,0))
        screen.blit(HomeSS,(xHome, yInit-20))
        pygame.display.update()
        sleep(2)
        screen.blit(WinnerScreen,(0,0))
        pygame.display.update()
        sleep(8)
        pygame.display.update()
        print("Game over")
        break
    
pygame.quit()


>>>>>>> 3ec7e2d9208b820b196d9baf6c174118de26571e
