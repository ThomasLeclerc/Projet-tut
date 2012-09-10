import pygame
import sys
from math import *


class obstacle:
    posX = 0
    posY = 0
    coef = 0
    angleRotation = 160 #true si on monte et false si on descend
    versLeHaut = True
    img = pygame.image.load("./ship1.png")
    img = pygame.transform.rotate(img,angleRotation)
    obrect = img.get_rect()
    def __init__(self,x,y):
        self.posX = x
        self.posY = y
    def estTouche(self,x,y):
        if x > self.posX and x < self.posX+self.obrect.right and y > self.posY and y < self.posY+self.obrect.bottom:
            return True 
        else:
            return False
    
    def move(self, previousObstacle):
        (poPosX,_) = previousObstacle.getPos()
        if self.posX-poPosX >= 50:
            self.posX -= 3    
            self.coef += 0.12
            self.posY += (sin(self.coef)*17)
            
            
            self.img = pygame.image.load("./ship1.png")
            if self.angleRotation == 20:
                self.versLeHaut = False
                self.angleRotation +=5
                self.img = pygame.transform.rotate(self.img,self.angleRotation)                               
            elif self.angleRotation == 160:
                self.versLeHaut = True
                self.angleRotation -= 5
                self.img = pygame.transform.rotate(self.img,self.angleRotation)
            else:
                if self.versLeHaut == True:
                    self.angleRotation -= 5
                    self.img = pygame.transform.rotate(self.img,self.angleRotation)
                else :
                    self.angleRotation += 5
                    self.img = pygame.transform.rotate(self.img,self.angleRotation)  
                          
                
            

        
    def moveFirst(self):    
        self.coef += 0.12
        self.posX -= 3
        self.posY += (sin(self.coef)*17)
        self.img = pygame.image.load("./ship1.png")
        if self.angleRotation == 20:
            self.versLeHaut = False
            self.angleRotation +=5
            self.img = pygame.transform.rotate(self.img,self.angleRotation)                               
        elif self.angleRotation == 160:
            self.versLeHaut = True
            self.angleRotation -= 5
            self.img = pygame.transform.rotate(self.img,self.angleRotation)
        else:
           if self.versLeHaut == True:
                self.angleRotation -= 5
                self.img = pygame.transform.rotate(self.img,self.angleRotation)
           else :
               self.angleRotation += 5
               self.img = pygame.transform.rotate(self.img,self.angleRotation)  
        
        
    
    def getPos(self):
        return (self.posX,self.posY)



