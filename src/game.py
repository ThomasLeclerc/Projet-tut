import pygame, sys
pygame.init()

class obstacle:
    posX = 0
    posY = 0
    s = False
    img = pygame.image.load("cible.png")
    obrect = img.get_rect()
    def __init__(self,x,y):
        self.posX = x
        self.posY = y
    def estTouche(self,x,y):
        if x > self.posX and x < self.posX+self.obrect.right and y > self.posY and y < self.posY+self.obrect.bottom:
            return True 
        else:
            return False
    def getPos(self):
        return (self.posX,self.posY)

class shot:
    posX = 0
    posY = 0
    img = pygame.image.load("rocket.png")
    def setPos(self,x,y):
        self.posX=x+20
        self.posY=y+20
    def bouge(self):
        self.posX+=15
        if self.posX>width:
            missiles.remove(self)
    def getPos(self):
        return (self.posX,self.posY)
#fin classe shot

class ship:
    monte = False
    desc = False
    posX = 20
    posY = 0
    speed=0
    switch=0
    def getPos(self):
        return (self.posX,self.posY)
    def setImg(self, file):
        self.img = pygame.image.load(file)
        self.shiprect = self.img.get_rect()

    #
    # deplace le vaisseau,   
    # prend en param les 2 fichiers reacteurs alumes
    #
    def bouge(self,file0,file1):
        accel=1.5
        if self.monte == True:
            if self.posY-2 >= 0:
                self.posY+=self.speed
                self.speed-=accel
            else:
                self.speed = 0
            #animation    
            if self.switch == 0:
                self.setImg(file0)
                self.switch=1
            elif self.switch == 1:
                self.setImg(file1)
                self.switch=0
        else:
            if self.posY+2 <= height-(self.shiprect).bottom:
                self.posY+=self.speed
                self.speed+=accel
            else:
                self.speed = 0
                
        #blockage du vaisseau dans la fenetre
        if self.posY < 0:
            self.posY = 0
            self.speed = 0
        elif self.posY > height-(self.shiprect).bottom:
            self.posY = height-(self.shiprect).bottom
            self.speed = 0
    #fin fonction bouge()
#fin classe ship

size = width, height = 640, 400
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FRAMES_PER_SECOND = 30
deltat = clock.tick(FRAMES_PER_SECOND)


background = pygame.image.load("night.jpg")
asteroid = pygame.image.load("asteroid.png")
stones = pygame.image.load("stones.png")
i=j=k=t=0


monVaisseau = ship()
#monVaisseau.setImg("ship.png")
#monVaisseau.setImg("chasseur.png")
monVaisseau.setImg("pinkship.png")

monJet = ship()
monJet.setImg("jetpack.png")

cible = obstacle(400,200)

missiles = []
obstacles = []
obstacles.append(cible)
s=1
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                monJet.monte=True
            elif event.key == pygame.K_UP:
                monVaisseau.monte=True
            elif event.key == pygame.K_SPACE:
                monMissile=shot()
                monMissile.setPos(monVaisseau.posX, monVaisseau.posY)
                missiles.append(monMissile)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_z:
                monJet.monte=False
                monJet.setImg("jetpack.png")
            elif event.key == pygame.K_UP:
                monVaisseau.monte=False
                #monVaisseau.setImg("ship.png")
                #monVaisseau.setImg("chasseur.png")
                monVaisseau.setImg("pinkship.png")

    # Background            
    screen.blit(background, (-i,0))
    screen.blit(background, (width-i,0))
    screen.blit(asteroid, (-j,0))
    screen.blit(asteroid, (width-j,0))
    screen.blit(stones, (-k,0))
    screen.blit(stones, (width-k,0))
    i+=2
    j+=4
    k+=8
    if i > width:
        i=0
    if j > width:
        j=0
    if k > width:
        k=0

    #monVaisseau.bouge("ship0.png","ship1.png")
    #monVaisseau.bouge("chasseur0.png","chasseur1.png")
    monVaisseau.bouge("pinkship0.png","pinkship1.png")

    monJet.bouge("jetpack0.png","jetpack1.png")
    for monMissile in missiles:
        monMissile.bouge()
            
    screen.blit(monVaisseau.img,monVaisseau.getPos())
    screen.blit(monJet.img,monJet.getPos())

    ob1 = obstacle(400,200)
    ob2 = obstacle(400,300)

    for monMissile in missiles:
        screen.blit(monMissile.img,monMissile.getPos())
        for testObstacle in obstacles:
            if testObstacle.estTouche(monMissile.posX,monMissile.posY):
                missiles.remove(monMissile)
                obstacles.remove(testObstacle)
                if s==1:
                    obstacles.append(ob1)
                    s=0
                else:
                    obstacles.append(ob2)
                    s=1                  
        

    for monObstacle in obstacles:
        screen.blit(monObstacle.img,monObstacle.getPos())

    pygame.display.flip()
