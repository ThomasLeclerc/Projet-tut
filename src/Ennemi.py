import pygame
import sys

class ennemy:
    posX = 0
    posY = 0
    
    def __init__(self,x,y):
        self.posX = x
        self.posY = y

    def getPos(self):
        return (self.posX,self.posY)
    
    def setImg(self, file):
        self.img = pygame.image.load(file)
        self.shiprect = self.img.get_rect()
