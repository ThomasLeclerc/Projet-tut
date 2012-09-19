import pygame

class shot:
    posX = 0
    posY = 0
    img = pygame.image.load("images/vaisseaux/orange_ship/orange_ship_bullet.png")
    def setPos(self,x,y):
        self.posX=x+20
        self.posY=y+20
    def bouge(self, width, missiles):
        self.posX+=15
        if self.posX>width:
            missiles.remove(self)
    def getPos(self):
        return (self.posX,self.posY)
#fin classe shot
    
class shotShooterEnnemy (shot):
    img = pygame.image.load("images/vaisseaux/enemies/enemy1/enemy1_bullet.png") 
    def __init__(self, x, y):
        self.posX = x
        self.posY = y
    def move(self, missilesShooter):
        self.posX-=10
        if self.posX<-20:
            missilesShooter.remove(self)
            
            
            
            