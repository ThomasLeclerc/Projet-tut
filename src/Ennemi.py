import pygame
import math
import Shot

class ennemy:
    posX = 0
    posY = 0
    
    def __init__(self,x,y,image):
        self.posX = x
        self.posY = y
        self.setImg(image);

    def getPos(self):
        return (self.posX,self.posY)
    
    def setImg(self, image):
        self.img = pygame.image.load(image)
        self.ennemyRect = self.img.get_rect()


class Snake(ennemy):
    versLeHaut = True
    def __init__(self,x,y, positionChaine):
        self.positionChaine=positionChaine
        ennemy.__init__(self,x,y, "images/chasseur1.png")
        self.img = pygame.transform.rotate(self.img,-75)
    def estTouche(self,x,y):
        if x > self.posX and x < self.posX+self.ennemyRect.right and y > self.posY and y < self.posY+self.ennemyRect.bottom:
            return True 
        else:
            return False
    
    def move(self,snakes):
        self.posX -= 1
        self.posY =  math.cos(self.posX*0.02)*120+self.positionChaine
        if self.posY > self.positionChaine+110:    
            self.img = pygame.image.load("images/chasseur1.png")
            self.img = pygame.transform.rotate(self.img,-75)
        elif self.posY < self.positionChaine-110:
            self.img = pygame.image.load("images/chasseur0.png")
            self.img = pygame.transform.rotate(self.img,75)
        
        if self.posX<0:
            snakes.remove(self)
        print self.posY


class Shooter(ennemy):
    vie = 2
    compteurTir = 0
    missilesShooter = []
    def __init__(self,x,y):
        ennemy.__init__(self,x,y, "images/ship1.png")  
        self.img = pygame.transform.rotate(self.img,90)
    
    def estTouche(self,x,y , ennemy, player):
        if x > self.posX and x < self.posX+self.ennemyRect.right and y > self.posY and y < self.posY+self.ennemyRect.bottom:
            self.vie -= 1
            if self.vie == 0:
                ennemy.remove(self)
                player.raiseScore(1)
            else:
                self.img = pygame.image.load("images/ship3.png") 
                self.img = pygame.transform.rotate(self.img,90)
            return True
        else:
            return False            
    
    def move(self, ship, ennemy):
           self.posX -= 2      
           (shipPosX, shipPosY) = ship.getPos()
           if self.posY < shipPosY and self.posY+3 < 600:
               self.posY += 4
           elif shipPosY < self.posY and self.posY-3 > 0:
               self.posY -= 4
           if self.posX<0:
               ennemy.remove(self)    
                
    def tir(self):
        self.compteurTir += 1
        if self.compteurTir%20 == 0:
            self.missilesShooter.append(Shot.shotShooterEnnemy(self.posX,self.posY+20))         
                          
                
            

        
   
     
    
        
        




