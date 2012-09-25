import pygame

class shot:  
    def getPos(self):
        return (self.posX,self.posY)
    
    def getDimensions(self):
        return (self.img.get_width(), self.img.get_height())
    
    def setImg(self, image):
        self.img = pygame.image.load(image)
        self.ennemyRect = self.img.get_rect()
#fin classe shot
    
class shotShip(shot):
    def __init__(self):
        self.posX = 0
        self.posY = 0
        self.setImg("images/vaisseaux/orange_ship/orange_ship_bullet.png")
        
    def bouge(self, width, missiles):
        self.posX+=25
        if self.posX>width:
            missiles.remove(self)
            
    def setPos(self,x,y):
        self.posX=x+70
        self.posY=y+40
        
class shotShooterEnnemy (shot):
    def __init__(self, x, y):
        self.posX = x
        self.posY = y
        self.setImg("images/vaisseaux/enemies/enemy1/enemy1_bullet.png") 
    def move(self, missilesShooter):
        self.posX-=10
        if self.posX<-20:
            missilesShooter.remove(self)
            
            
            
            