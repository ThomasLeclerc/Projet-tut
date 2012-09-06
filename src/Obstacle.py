import pygame
import sys
from math import *


class obstacle:
    posX = 0
    posY = 0
    coef = 0
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
	
    def move(self, previousObstacle):
        (poPosX,_) = previousObstacle.getPos()
        if self.posX-poPosX >= 70:
            self.coef += 0.1
            self.posX -= 3	
            self.posY += (sin(self.coef)*12)
		
    def moveFirst(self):	
		self.coef += 0.1
		self.posX -= 3
		self.posY += (sin(self.coef)*12)
	
    def getPos(self):
        return (self.posX,self.posY)



