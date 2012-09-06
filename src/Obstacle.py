import pygame
import sys


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
