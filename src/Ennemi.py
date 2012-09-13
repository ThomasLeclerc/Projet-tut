import pygame
import math


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
        self.posX -= 3
        self.posY =  math.asin(math.sin(self.posX*0.03))*80+self.positionChaine
        if self.posY >= self.positionChaine+120:    
            self.img = pygame.image.load("images/chasseur1.png")
            self.img = pygame.transform.rotate(self.img,-75)
        if self.posY <= self.positionChaine-120:
            self.img = pygame.image.load("images/chasseur0.png")
            self.img = pygame.transform.rotate(self.img,75)

        if self.posX<0:
            snakes.remove(self)


class Shooter(ennemy):
    vie = 2
    def __init__(self,x,y):
        ennemy.__init__(self,x,y, "images/ship1.png")  
        self.img = pygame.transform.rotate(self.img,90)
    
    def estTouche(self,x,y):
        if x > self.posX and x < self.posX+self.ennemyRect.right and y > self.posY and y < self.posY+self.ennemyRect.bottom:
            self.vie -= 1
            if self.vie == 0:
                return True
            else:
                self.img = pygame.image.load("images/ship3.png") 
                self.img = pygame.transform.rotate(self.img,90)
                return False
        else:
            return False            
    
    def move(self, ship):
           self.posX -= 2      
           (shipPosX, shipPosY) = ship.getPos()
           if self.posY < shipPosY and self.posY+3 < 600:
               self.posY += 4
           elif shipPosY < self.posY and self.posY-3 > 0:
               self.posY -= 4
               
                
                
                          
                
            

        
   
     
    
        
        




