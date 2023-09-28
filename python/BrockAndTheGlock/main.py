import 
import math
import random
import time
from os import listdir
pygame.init()

# SETUP WINDOW
(width, height) = (500, 375)
win = pygame.display.set_mode((width, height), pygame.RESIZABLE)
worldSurface = pygame.Surface((width, height-25))
surfaceOffset = (0,0)

# TEXT
startTime = time.time()
gameFont = pyg freetype.Font("DTM-SANS.OTF", 25)

# hello
clock = pygame.time.Clock()
FRAMERATE = 60

# LOAD SPRITES
iDir = 'Sprites/'
# player
playerSpr = pygame.image.load(iDir + 'player.png')

playerRunSpr = [pygame.image.load(iDir + 'playerRun1.png'),pygame.image.load(iDir + 'playerRun2.png')]

gunSpr = pygame.image.load(iDir + 'gun.png')
gunSpr = pygame.transform.scale(gunSpr, (40, 40))

# world
stageSprs = []
targetSpr = pygame.image.load(iDir + 'target.png')
downSpikesSpr = pygame.image.load(iDir + 'downSpikes.png')
boxSpr = pygame.image.load(iDir + 'box.png')

stagePath = 'Sprites/Stage/'
spriteNames = listdir(stagePath)

i = 0
while i < len(spriteNames)-1:
    stageSprs.append(pygame.image.load(stagePath + spriteNames[i]))
    i += 1


# bullet
bulletSpr = pygame.image.load(iDir + 'bullet.png')
bulletSpr = pygame.transform.scale(bulletSpr, (20, 15))
# UI
bulletIcon = pygame.image.load(iDir + "bulletIcon.png")
bulletIcon = pygame.transform.scale(bulletIcon, (12, 17))
# particles
dustAnim = [pygame.image.load(iDir + 'dust0000.png'), pygame.image.load(iDir + 'dust0001.png'), pygame.image.load(iDir + 'dust0002.png')]
boxPartSpr = [pygame.image.load(iDir + 'boxPart1.png'), pygame.image.load(iDir + 'boxPart2.png'), pygame.image.load(iDir + 'boxPart3.png'), pygame.image.load(iDir + 'boxPart4.png')]

i = 0
for sprite in dustAnim:
    dustAnim[i] = pygame.transform.scale(sprite, (32,32))
    i += 1

# LOAD SOUNDS
sDir = 'Sounds/'
# sounds
targetSnd = pygame.mixer.Sound(sDir + "destroyTarget.wav")
landSnd = pygame.mixer.Sound(sDir + "landSound.wav")
shootSnd = pygame.mixer.Sound(sDir + "shootSound.wav")
winSnd = pygame.mixer.Sound(sDir + "winLevel.wav")
boxSnd = pygame.mixer.Sound(sDir + "destroyBox.wav")
dieSnd = pygame.mixer.Sound(sDir + "playerDie.wav")
# music
pygame.mixer.music.load(sDir + 'music.wav')
pygame.mixer.music.play(-1)

# INIT WORLD DATA
# grid is 20 wide, 14 high 
# 0=nothing, 1-17 and 21-22=block, 24=player, 19=door, 23=target, 18,25=spike, 26=box
level1 = ([
[4,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,5],
[8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,0,0,26,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,1,2,2,2,2,3,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,6,7,7,7,7,8,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,6,7,7,7,7,8,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,6,7,7,7,7,8,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,6,7,7,7,7,8,0,0,0,0,0,0,6],
[8,0,0,24,0,0,0,6,7,7,7,7,8,0,0,0,19,0,0,6],
[9,2,2,2,2,2,2,10,7,7,7,7,9,2,2,2,2,2,2,10],
], 3, False)

level2 = ([
[4,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,5],
[8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,0,0,26,19,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,1,2,2,2,2,3,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,11,12,12,12,12,13,0,0,0,0,0,0,6],
[8,0,0,23,0,0,0,0,0,0,0,0,0,0,0,0,0,23,0,6],
[8,0,0,0,0,0,26,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,1,3,0,0,0,0,0,0,1,3,0,0,0,0,6],
[8,0,0,0,0,6,8,0,0,0,0,0,0,6,8,0,0,0,0,6],
[8,0,0,0,0,6,8,0,0,0,0,0,0,6,8,0,0,0,0,6],
[8,0,0,0,0,6,8,0,0,0,0,0,0,6,8,0,0,0,0,6],
[8,18,18,18,18,6,8,0,0,24,0,0,0,6,8,18,18,18,18,6],
[9,2,2,2,2,10,9,2,2,2,2,2,2,10,9,2,2,2,2,10],
], 4, False)

level3 = ([
[4,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,5],
[8,0,0,0,0,0,0,0,0,0,0,0,6,8,0,0,0,0,0,6],
[8,0,0,0,0,0,0,0,0,0,0,0,6,8,0,0,0,0,0,6],
[8,0,0,0,0,0,0,0,0,0,0,0,6,8,0,0,0,0,0,6],
[8,0,0,0,0,0,18,18,18,0,0,0,6,8,0,0,0,26,19,6],
[8,0,0,0,0,0,1,2,3,0,0,0,6,8,0,0,0,1,2,10],
[8,0,0,0,0,0,6,7,8,0,0,0,6,8,0,0,0,6,7,7],
[8,0,0,0,0,0,6,7,8,0,0,0,11,13,0,0,0,6,7,7],
[8,0,0,0,0,0,6,7,8,0,0,0,0,0,0,0,0,6,7,7],
[8,0,0,0,0,0,6,7,8,0,0,0,0,0,0,0,0,6,7,7],
[8,0,0,0,0,0,6,7,8,0,0,0,0,0,0,0,0,6,7,7],
[8,0,0,0,0,0,6,7,8,0,0,0,0,0,0,0,0,6,7,7],
[8,0,0,24,0,26,6,7,8,18,18,18,18,18,18,18,18,6,7,7],
[9,2,2,2,2,2,10,7,9,2,2,2,2,2,2,2,2,10,7,7],
], 5, False)

level4 = ([
[4,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,5],
[8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,23,0,6],
[8,0,24,0,0,26,0,0,0,0,0,0,0,0,0,26,0,0,0,6],
[9,2,2,2,2,2,2,3,0,0,0,0,1,2,2,2,2,2,2,10],
[4,12,12,12,12,12,5,8,0,0,0,0,11,12,12,12,12,12,12,5],
[8,0,0,0,0,0,6,8,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,0,6,8,0,0,0,0,0,0,0,26,0,23,0,6],
[8,0,0,0,0,19,6,8,0,0,0,0,1,2,2,2,2,2,2,10],
[8,0,0,0,0,16,12,13,0,0,0,0,11,12,12,12,12,12,12,5],
[8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,26,26,0,26,0,0,0,0,26,0,23,0,6],
[9,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,10],
[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7],
], 4, False)

level5 = ([
[4,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,5],
[8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,19,0,0,0,26,26,26,0,0,26,0,0,0,0,0,0,0,6],
[8,2,2,2,2,2,2,2,2,2,2,2,2,3,0,0,0,0,0,6],
[8,12,12,12,12,12,12,12,12,12,12,12,12,13,0,0,0,0,0,6],
[8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,18,18,0,0,0,18,18,0,0,0,0,0,6],
[8,0,0,0,0,0,0,1,3,0,0,0,1,3,0,0,0,0,0,6],
[8,0,0,0,0,0,0,6,8,0,0,0,6,8,0,0,0,0,0,6],
[8,0,0,0,0,0,0,6,8,0,0,0,6,8,0,0,0,0,0,6],
[8,0,0,24,26,0,0,6,8,0,0,0,6,8,0,0,0,0,0,6],
[9,2,2,2,2,2,2,10,9,2,2,2,2,2,2,2,2,2,2,10],
], 5, False)

level6 = ([
[4,12,12,12,12,12,12,12,12,5,4,12,12,12,12,5,4,12,12,5],
[8,0,0,0,0,0,0,0,0,6,8,0,0,0,0,11,13,0,0,6],
[8,0,0,0,0,0,0,0,0,6,8,0,0,0,0,0,0,0,0,6],
[8,0,23,0,0,0,0,0,0,6,8,0,0,0,0,0,0,0,23,6],
[8,0,0,0,0,0,0,0,0,6,8,0,0,0,0,18,18,0,0,6],
[8,0,0,0,0,26,0,0,0,6,8,0,19,26,0,1,3,0,0,6],
[8,0,0,0,0,1,3,0,0,6,9,2,2,2,2,10,8,0,0,6],
[8,0,0,0,0,6,8,0,0,11,12,12,12,12,12,12,13,0,0,6],
[8,0,0,0,0,6,8,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,6,8,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,6,8,0,23,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,6,8,0,0,0,0,0,0,0,0,0,0,1,2,10],
[8,0,24,0,0,6,8,18,18,18,18,18,18,18,18,18,18,6,7,7],
[9,2,2,2,2,10,9,2,2,2,2,2,2,2,2,2,2,10,7,7],
], 6, False)

level7 = ([
[4,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,5],
[8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,0,26,24,19,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,16,14,2,2,14,17,0,0,0,0,0,0,6],
[8,0,0,23,0,0,0,0,0,6,8,0,0,0,0,0,23,0,0,6],
[8,0,0,0,0,0,0,0,0,6,8,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,0,0,6,8,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,0,0,11,13,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,0,0,23,26,0,0,0,0,0,0,0,0,6],
[8,18,18,18,18,18,18,18,18,1,3,18,18,18,18,18,18,18,18,6],
[9,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,10],
], 3, False)

level8 = ([
[4,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,5],
[8,0,0,0,0,15,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,15,0,0,23,0,0,23,0,0,0,0,0,0,0,6],
[8,24,0,0,0,15,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,17,0,0,0,15,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,22,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,0,0,0,0,0,0,0,18,18,18,0,0,6],
[8,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,0,0,6],
[8,0,0,0,0,0,0,0,0,0,0,0,0,0,6,12,13,0,0,6],
[8,0,0,0,0,0,0,0,0,0,0,0,0,0,15,0,0,0,0,6],
[8,0,0,0,0,0,0,0,0,0,0,0,0,0,15,0,0,0,0,6],
[8,18,18,18,18,18,18,18,18,18,18,18,18,18,15,0,19,26,0,6],
[9,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,10],
], 5, False)

winScreen = ([
[4,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,5],
[8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[8,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
[9,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,10],
], 3, True)

levelHolder = [level1, level2, level3, level4, level5, level6, level7, level8, winScreen]

# INIT GLOBALS 
tileSize = 25
thePlayer = None
targetCount = 0
levelNumb = 1


screenShake = False
screenShakeAmount = (0, 8)
screenShakeTime = 5
curScreenShakeTime = 0

curTime = 0

# CLASSES
class player(object):
    def __init__(self,x,y):
        # INIT VARIABLES
        # movement
        self.x = x
        self.y = y
        self.spd = 3
        # animation
        self.left = False
        self.walk = False
        self.frameNumber = 0
        self.animationSpd = 10
        self.walkCount = 0
        # gravity
        self.vel_y = 0
        self.gravityIncrement = 0.25
        self.maxFallVel = 10
        # collision
        scaleSprite = pygame.transform.scale(playerSpr, (20, 40))
        self.rect = scaleSprite.get_rect()
        self.width = scaleSprite.get_width()
        self.height = scaleSprite.get_height()
        self.rect.x = x
        self.rect.y = y
        # shooting
        self.bullets = []
        self.bulletSpd = 22
        self.pointAngle = 0
        # knockback
        self.xKnockback = 0
        self.yKnockback = 0
        self.xknockbackAmount = 25
        self.yknockbackAmount = 40
        self.knockbackDampen = 0.8
        #dust
        self.dustWait = 10
        self.dustCounter = 0
        self.dustPart = []
        self.dustOffset = 20
    
    def spawn(self,x,y):
        # SET POSITION
        self.rect.x = x
        self.rect.y = y
        self.x = self.rect.x
        self.y = self.rect.y

    def draw(self):

        mySprite = playerSpr
        if(self.walk):
            mySprite = playerRunSpr[self.frameNumber]
            self.walkCount += 1

            if(self.walkCount == self.animationSpd):
                self.walkCount = 0
                self.frameNumber += 1

                if(self.frameNumber > len(playerRunSpr)-1):
                    self.frameNumber = 0

        # draw player
        if(self.left == False):
            worldSurface.blit(pygame.transform.scale(mySprite, (20, 40)), (self.x, self.y, self.width, self.height))
        else:
            worldSurface.blit(pygame.transform.flip(pygame.transform.scale(mySprite, (20, 40)), True, False), (self.x, self.y, self.width, self.height))

        # draw rotated gun
        deg = math.degrees(-self.pointAngle)
        
        rotated_image = pygame.transform.rotate(gunSpr, deg)
        worldSurface.blit(rotated_image, (self.x, self.y))
        
        # debug draw colliders
        #pygame.draw.rect(win,(255,255,255),self.rect,2)
    
    def update(self):
        # INIT LOCALS
        (moveX, moveY) = (0,0)

        # point gun
        self.pointAtMouse()

        # PLAYER MOVEMENT
        (moveX, moveY) = self.doPlayerMovement(moveX, moveY)

        # KNOCKBACK
        (moveX, moveY) = self.applyKnockback(moveX, moveY)

        # GRAVITY
        if(moveY < -2):
            self.vel_y = 0
        self.vel_y += self.gravityIncrement

        # limit gravity
        if(self.vel_y > self.maxFallVel):
            self.vel_y = self.maxFallVel
        # apply gravity
        moveY += self.vel_y

        # COLLISIONS
        (moveX, moveY) = self.doCollision(moveX,moveY)
        self.destroyBoxes()
            
        # APPLY MOVEMENT
        self.rect.x += moveX
        self.rect.y += moveY
        self.x = self.rect.x
        self.y = self.rect.y
    
    def doPlayerMovement(self, moveX, moveY):
        # detect input
        keys = pygame.key.get_pressed()

        moveX = 0
        moveY = 0

        # do movement
        if(keys[pygame.K_a]):
            moveX = -self.spd
            self.left = True
        elif(keys[pygame.K_d]):
            moveX = self.spd
            self.left = False

        # animation
        self.walk = (abs(moveX) + abs(moveY) > 0)
        
        # return values
        return (moveX, moveY)

    def doDustAnimation(self):
        # spawn dust particles
        thePlayer.dustCounter += 1
        if(self.dustCounter == self.dustWait):
            self.dustCounter = 0

            # create dust and add it to the dust particle list
            theDust = dust(self.x,self.y+self.dustOffset)
            self.dustPart.append(theDust)

    def applyKnockback(self, moveX, moveY):
        # apply knockback and reduce it until it goes to zero
        if abs(self.xKnockback) > 0:
            moveX += self.xKnockback
            self.xKnockback *= self.knockbackDampen
            if(abs(self.xKnockback) < 0.1):
                self.xKnockback = 0

        if abs(self.yKnockback) > 0:
            moveY += self.yKnockback
            self.yKnockback *= self.knockbackDampen
            if(abs(self.yKnockback) < 0.1):
                self.yKnockback = 0
        # return values
        return (moveX, moveY)

    def doCollision(self, moveX, moveY):
        for tile in theLevel.tileList:
            # X DIRECTION

            # find which direction I'm moving in
            xIncrement = tileSize-1
            theDir = 1
            if(moveX < 0):
                theDir = -1

            # if moving really fast
            # right
            if(moveX > xIncrement and theDir == 1):
                moveAmount = xIncrement
                while(moveAmount < moveX):
                    if tile[1].colliderect(self.rect.x + moveAmount, self.rect.y, self.width, self.height):
                        moveX = 0
                        self.xKnockback = 0
                    moveAmount += xIncrement
            # left
            elif(moveX < -xIncrement and theDir == -1):
                moveAmount = -xIncrement
                while(moveAmount > moveX):
                    if tile[1].colliderect(self.rect.x + moveAmount, self.rect.y, self.width, self.height):
                        moveX = 0
                        self.xKnockback = 0
                    moveAmount += -xIncrement
            else:
            # normal collision detection
                if tile[1].colliderect(self.rect.x + moveX, self.rect.y, self.width, self.height):
                    moveX = 0
            
            # Y DIRECTION

            # find which direction I'm moving in
            yIncrement = tileSize-1
            theDir = 1
            if(moveY < 0):
                theDir = -1

            # if moving really fast
            # down
            if(moveY > yIncrement and theDir == 1):
                moveAmount = yIncrement
                while(moveAmount < moveY):
                    if tile[1].colliderect(self.rect.x, self.rect.y + moveAmount, self.width, self.height):
                        moveY = tile[1].top - self.rect.bottom
                        self.vel_y = 0

                        # dust particles
                        if(abs(moveX) > 0):
                            self.doDustAnimation()
                    moveAmount += yIncrement
            # up
            elif(moveY < -yIncrement and theDir == -1):
                moveAmount = -yIncrement
                while(moveAmount > moveY):
                    if tile[1].colliderect(self.rect.x, self.rect.y + moveAmount, self.width, self.height):
                        moveY = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    moveAmount += -yIncrement
            else:
                # normal collision detection
                if tile[1].colliderect(self.rect.x, self.rect.y + moveY, self.width, self.height):
                    # if block is above
                    if theDir < 0:
                        moveY = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                        self.yKnockback = 0
                    # if block is below
                    if theDir >= 0:
                        moveY = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.yKnockback = 0

                        # dust particles
                        if(abs(moveX) > 0):
                            self.doDustAnimation()
        # return values
        return (moveX, moveY)

    def pointAtMouse(self):
        # POINT TOWARDS MOUSE ----- CODE SOURCE: https://stackoverflow.com/questions/63495823/how-to-shoot-a-bullet-towards-mouse-cursor-in-pygame
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_x -= surfaceOffset[0]
        mouse_y -= surfaceOffset[1]

        distance_x = mouse_x - self.x
        distance_y = mouse_y - self.y

        self.pointAngle = math.atan2(distance_y, distance_x)

    def doShooting(self):
        global curScreenShakeTime, screenShakeTime, screenShake
        # play sound
        pygame.mixer.Sound.play(shootSnd)

        # do screenshake
        curScreenShakeTime = screenShakeTime
        screenShake = True
        
        # uses trig to point the bullet at the mouse
        xMove = math.cos(self.pointAngle)
        yMove = math.sin(self.pointAngle)
        
        theBullet = bullet(self.x, self.y, self.bulletSpd, xMove, yMove, self.pointAngle)
        self.bullets.append(theBullet)

        # do knockback in the opposite direction of the bullets
        self.xKnockback = -xMove * self.xknockbackAmount
        self.yKnockback = -yMove * self.yknockbackAmount

    def destroyBoxes(self):
        for box in theLevel.boxes:
            if box[1].colliderect(self.rect.x, self.rect.y, self.width, self.height):
                theLevel.destroyBox(box)

    def resetVelocity(self):
        self.vel_y = 0

        self.xKnockback = 0
        self.yKnockback = 0

        self.dustCounter = 0

        self.frameNumber = 0
        self.walkCount = 0
        self.pointAngle = 0

class world(object):
    def __init__(self, levelIndex):
        # INIT VARIABLES
        # globals
        global targetCount
        targetCount = 0
        # bullet count
        self.bulletCount = 0
        self.curbulletCount = 0

        # box particles
        self.boxPartAmount = 5
        self.boxParts = []

        self.isWinScreen = False

        # LOAD LEVEL 1
        self.loadLevel(levelIndex)
    
    def loadLevel(self, levelIndex):
        global targetCount, levelNumb

        # delete existing bullets / dust
        thePlayer.dustPart.clear()
        thePlayer.bullets.clear()
        self.boxParts.clear()
        # load data
        if levelIndex >= len(levelHolder):
            # do nothing (for now)
            pass
        else:
            (theMap, self.bulletCount, self.isWinScreen) = levelHolder[levelIndex]

            # bullet count
            self.curbulletCount = self.bulletCount
            # ui
            theUI.bulletCountUI(self.curbulletCount)
            # reset target count
            targetCount = 0
            
            # level
            self.allTiles = []
            self.tileList = []
            self.doorTile = None
            self.targets = []
            self.spikes = []
            self.boxes = []

            # LOAD LEVEL
            row_count = 0
            for row in theMap:
                col_count = 0
                for tile in row:
                    # block
                    # 0=nothing, 1-17 and 21-22=block, 24=player, 19=door, 23=target, 18=spike, 26=box
                    if (tile > 0 and tile < 18) or (tile > 20 and tile < 23):
                        img = pygame.transform.scale(stageSprs[tile], (tileSize, tileSize))
                        img_rect = img.get_rect()
                        img_rect.x = col_count*tileSize
                        img_rect.y = row_count*tileSize

                        tile = (img, img_rect)
                        self.tileList.append(tile)
                        self.allTiles.append(tile)
                    
                    # player
                    if tile == 24:
                        thePlayer.spawn(col_count*tileSize,row_count*tileSize)
                    
                    # door
                    if tile == 19:
                        img = pygame.transform.scale(stageSprs[tile], (tileSize, tileSize))
                        img_rect = img.get_rect()
                        img_rect.x = col_count*tileSize
                        img_rect.y = row_count*tileSize

                        door = (img, img_rect)
                        self.doorTile = door
                        self.allTiles.append(door)
                    
                    # target
                    if tile == 23:
                        img = pygame.transform.scale(targetSpr, (tileSize, tileSize))
                        img_rect = img.get_rect()
                        img_rect.x = col_count*tileSize
                        img_rect.y = row_count*tileSize

                        target = (img, img_rect)
                        self.targets.append(target)  
                        self.allTiles.append(target)

                        targetCount += 1
                    
                    # spikes
                    if tile == 18:
                        img = pygame.transform.scale(stageSprs[tile], (tileSize, tileSize))
                        img_rect = img.get_rect()
                        img_rect.x = col_count*tileSize
                        img_rect.y = row_count*tileSize

                        spike = (img, img_rect)
                        self.spikes.append(spike)  
                        self.allTiles.append(spike)

                    # down spikes
                    if tile == 25:
                        img = pygame.transform.scale(downSpikesSpr, (tileSize, tileSize))
                        img_rect = img.get_rect()
                        img_rect.x = col_count*tileSize
                        img_rect.y = row_count*tileSize

                        spike = (img, img_rect)
                        self.spikes.append(spike)  
                        self.allTiles.append(spike)

                    # destructable boxes
                    if tile == 26:
                        img = pygame.transform.scale(boxSpr, (tileSize, tileSize))
                        img_rect = img.get_rect()
                        img_rect.x = col_count*tileSize
                        img_rect.y = row_count*tileSize

                        box = (img, img_rect)
                        self.boxes.append(box)  
                        self.allTiles.append(box)

                    col_count += 1
                row_count += 1

    def draw(self):
        for tile in self.allTiles:
            worldSurface.blit(tile[0], tile[1])
        
        # box particles
        for part in self.boxParts:
            worldSurface.blit(part.sprite, part.rect)
        
        # win text
        if self.isWinScreen:
            # draw header
            color = (255,255,255)
            header, rect = gameFont.render("You Win!", color)
            worldSurface.blit(header, (200, 50))

            # draw instructions
            color = (255,255,255)
            header, rect = gameFont.render("Press [TAB] To Restart", color)
            worldSurface.blit(header, (125, 100))

    def destroyTarget(self, target):
        global targetCount
        self.targets.remove(target)
        self.allTiles.remove(target)
        targetCount -= 1

    def destroyBox(self, box):
        # play sound
        pygame.mixer.Sound.play(dieSnd)
        # destroy box
        self.boxes.remove(box)
        self.allTiles.remove(box)

        # create particles   
        i = 0
        while i < self.boxPartAmount:
            self.boxParts.append(boxPart(box[1].x,box[1].y))
            i += 1

class bullet(object):
    def __init__(self,x,y,spd,xMove,yMove,angle):
        # movement
        self.x = x
        self.y = y

        self.angle = angle
        self.spd = spd
        self.xMove = xMove
        self.yMove = yMove
        # collision
        self.width = bulletSpr.get_width()
        self.height = bulletSpr.get_height()
        self.rect = bulletSpr.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def draw(self):
        deg = math.degrees(-self.angle)
        
        rotated_image = pygame.transform.rotate(bulletSpr, deg)
        worldSurface.blit(rotated_image, (self.x, self.y, self.width, self.height))
        # debug draw colliders
        #pygame.draw.rect(win,(255,255,255),self.rect,2)
    
    def move(self):
        # DETECT COLLISION
        for target in theLevel.targets:
            if target[1].colliderect(self.rect.x, self.rect.y, self.width, self.height):
                thePlayer.bullets.remove(self)
                theLevel.destroyTarget(target)
                pygame.mixer.Sound.play(targetSnd)
                return
        
        for tile in theLevel.tileList:
            if tile[1].colliderect(self.rect.x, self.rect.y, self.width, self.height):
                thePlayer.bullets.remove(self)
                return
        
        self.destroyBoxes()

        # APPLY MOVEMENT
        (moveX, moveY) = (self.spd * math.cos(self.angle), self.spd * math.sin(self.angle))

        self.rect.x += moveX
        self.rect.y += moveY
        self.x = self.rect.x
        self.y = self.rect.y

    def destroyBoxes(self):
        for box in theLevel.boxes:
            if box[1].colliderect(self.rect.x, self.rect.y, self.width, self.height):
                theLevel.destroyBox(box)

class ui(object):
    def __init__(self):
        self.bulletLoc = (450, 10)
        self.bulletOffset = 25

        self.UIList = []
    
    def draw(self):
        for ui in self.UIList:
            win.blit(ui[0], (ui[1].x + surfaceOffset[0], ui[1].y))
    
    def bulletCountUI(self, bulletCount):
        theUI.UIList.clear()
        i = 0
        while(i < bulletCount):
            # make a bullet icon
            bul = bulletIcon
            bul_rect = bul.get_rect()
            bul_rect.x = self.bulletLoc[0] - (self.bulletOffset * i)
            bul_rect.y = self.bulletLoc[1]
            
            ui = (bul, bul_rect)
            self.UIList.append(ui)
            i += 1

class dust(object):
    def __init__(self,x,y):
        # location / size
        self.x = x
        self.y = y
        self.width = 3
        self.height = 3

        # animation
        self.animCount = 0
        self.animationSpeed = 5
        self.frameCount = 3
    
    def draw(self):
        if self.animCount +1 >= self.animationSpeed * self.frameCount:
            self.animCount = 0
        
        worldSurface.blit(dustAnim[self.animCount//self.animationSpeed], (self.x, self.y, self.width, self.height))
        self.animCount += 1

        # destroy after playing animation
        if(self.animCount+self.animationSpeed > 16):
            thePlayer.dustPart.remove(self)

class boxPart(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        # looks
        self.rotation = random.randint(0,180)
        self.sprite = pygame.transform.rotate(pygame.transform.scale(boxPartSpr[random.randint(0,len(boxPartSpr)-1)], (15, 8)), self.rotation)
        self.rect = self.sprite.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()

        # gravity
        self.vel_y = 0
        self.gravityIncrement = 0.25
        self.maxFallVel = 10

        # knockback
        self.xKnockback = 0
        self.yKnockback = 0
        self.xknockbackAmount = random.randint(5,13)
        self.yknockbackAmount = random.randint(10,18)
        self.knockbackDampen = 0.8
        self.doneMoving = False

        # do the knockback
        xMove = math.cos(self.rotation)
        yMove = math.sin(self.rotation)

        self.xKnockback = xMove * self.xknockbackAmount
        self.yKnockback = yMove * self.yknockbackAmount

        # do some screenshake
        global curScreenShakeTime, screenShake
        curScreenShakeTime = 2
        screenShake = True
    
    def draw(self):
        worldSurface.blit(self.sprite, (self.x, self.y, self.width, self.height))
    
    def update(self):
        # knockback
        (moveX, moveY) = self.applyKnockback()

        # gravity
        if(moveY < -2):
            self.vel_y = 0
        self.vel_y += self.gravityIncrement
        # apply gravity
        moveY += self.vel_y

        # do collisions
        (moveX, moveY) = self.doCollision(moveX, moveY)

        # apply movement
        self.rect.x += moveX
        self.rect.y += moveY
        self.x = self.rect.x
        self.y = self.rect.y

        # done moving
        if abs(moveX) + abs(moveY) == 0:
            self.doneMoving = True

    def applyKnockback(self):
        # apply knockback and reduce it until it goes to zero
        moveX = 0
        moveY = 0
        if abs(self.xKnockback) > 0:
            moveX = self.xKnockback
            self.xKnockback *= self.knockbackDampen
            if(abs(self.xKnockback) < 0.1):
                self.xKnockback = 0

        if abs(self.yKnockback) > 0:
            moveY = self.yKnockback
            self.yKnockback *= self.knockbackDampen
            if(abs(self.yKnockback) < 0.1):
                self.yKnockback = 0
        
        return(moveX,moveY)

    def doCollision(self, moveX, moveY):
        for tile in theLevel.tileList:
            # X DIRECTION
            # find which direction I'm moving in
            theDir = 1
            if(moveX < 0):
                theDir = -1

            # normal collision detection
            if tile[1].colliderect(self.rect.x + moveX, self.rect.y, self.width, self.height):
                moveX = 0
            
            # Y DIRECTION
            # find which direction I'm moving in
            theDir = 1
            if(moveY < 0):
                theDir = -1

            # normal collision detection
            if tile[1].colliderect(self.rect.x, self.rect.y + moveY, self.width, self.height):
                # if block is above
                if theDir < 0:
                    moveY = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                    self.yKnockback = 0
                # if block is below
                if theDir >= 0:
                    moveY = tile[1].top - self.rect.bottom
                    self.vel_y = 0
                    self.yKnockback = 0
        # return values
        return (moveX, moveY)

# DEFINE FUNCTIONS
# game related
def RedrawGameWindow():
    global curTime, surfaceOffset
    # fill the background with black
    win.fill((0,0,0))
    #fill the screen with dark purple
    worldSurface.fill((75,20,60))

    # draw the stage
    theLevel.draw()

    # draw the particles
    for i in thePlayer.dustPart:
        i.draw()
    
    # draw the player
    thePlayer.draw()

    # draw the bullets
    for i in thePlayer.bullets:
        i.draw()

    # screen shake
    shakeX = 0
    shakeY = 0
    if screenShake:
        shakeX += random.randint(screenShakeAmount[0],screenShakeAmount[1]) - screenShakeAmount[1]/2
        shakeY += random.randint(screenShakeAmount[0],screenShakeAmount[1]) - screenShakeAmount[1]/2

    # actually render it to the window
    centerScreen = (win.get_width()/2, win.get_height()/2)
    surfaceOffset =  (centerScreen[0] - worldSurface.get_width()/2, centerScreen[1] - worldSurface.get_height()/2)
    surfacePos = (surfaceOffset[0] + shakeX, surfaceOffset[1] + shakeY + 12)
    win.blit(worldSurface, surfacePos)

    # draw uia
    theUI.draw()

    # draw timer
    if theLevel.isWinScreen == False:
        curTime = str(round(time.time()-startTime, 2))
    text_surface, rect = gameFont.render(curTime, (255, 255, 255))
    win.blit(text_surface, (225 + surfaceOffset[0], 10))

    # update the window
    pygame.display.update()

def bulletMovement():
    global score
    for i in thePlayer.bullets:
        # movement
        i.x += i.xMove * i.spd
        i.y += i.yMove * i.spd   

def true_coords(obj, coords):
    objw = obj.get_width()
    objh = obj.get_height()

    true_coords = coords[0] - (objw / 2), coords[1] - (objh /2)
    return(true_coords)

def checkForWin():
    # if all targets broken
    if(targetCount == 0):
        # if touching door
        if(theLevel.doorTile != None and theLevel.doorTile[1].colliderect(thePlayer.rect.x, thePlayer.rect.y, thePlayer.width, thePlayer.height)):
            global levelNumb
            pygame.mixer.Sound.play(winSnd)
            
            # load next level
            levelNumb += 1
            theLevel.loadLevel(levelNumb-1)

def doGeneralEvents():
    global run        
    # other events
    for event in pygame.event.get(): 
        # end the game if x is pressed
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if(event.button == 1): #if left mouse button
                if(theLevel.curbulletCount > 0): # if enough bullets
                    theLevel.curbulletCount -= 1
                    # do shooting
                    thePlayer.doShooting()
                    # update ui
                    theUI.bulletCountUI(theLevel.curbulletCount)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                restartGame()
            elif event.key == pygame.K_r:
                restartLevel()
            elif event.key == pygame.K_ESCAPE:
                run = False
                pygame.QUIT

def checkForDeath():
    for i in theLevel.spikes:
        if(i[1].colliderect(thePlayer.rect.x, thePlayer.rect.y, thePlayer.width, thePlayer.height)):
            pygame.mixer.Sound.play(dieSnd)
            restartLevel()

def restartLevel():
    thePlayer.resetVelocity()
    theLevel.loadLevel(levelNumb-1)

def restartGame():
    global startTime, levelNumb, curTime, curScreenShakeTime, run
    thePlayer.resetVelocity()
    # INIT GLOBALS 
    levelNumb = 1
    startTime = time.time()
    curTime = 0

    theLevel.loadLevel(0)
    run = True

# MAIN LOOP
theUI = ui()
thePlayer = player(0,0)
theLevel = world(0)
run = True

while run:
    clock.tick(FRAMERATE)

    # BASIC EVENTS
    time.time()
    doGeneralEvents()

    # screen shake countdown
    if screenShake:
        curScreenShakeTime -= 1
        if curScreenShakeTime == 0:
            screenShake = False

    # move bullets
    for i in thePlayer.bullets:
        i.move()
    
    # move box particles
    for box in theLevel.boxParts:
        if(box.doneMoving == False):
            box.update()
    
    # move player and collide
    thePlayer.update()
    # check for win
    checkForWin()
    # check if touched spikes
    checkForDeath()
    # draw bullets, player and stage
    RedrawGameWindow()