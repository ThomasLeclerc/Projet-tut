import pygame
from math import sin


class obstacle:
    posX = 0
    posY = 0
    
    def __init__(self,y,image):
        self.posX = 700
        self.posY = y
        self.setImg(image);

    def getPos(self):
        return (self.posX,self.posY)
    
    def setImg(self, image):
        self.img = pygame.image.load(file)
        self.ennemyRect = self.img.get_rect()


    def bouge(self,):
        self.posx-=8