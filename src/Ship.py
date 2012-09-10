import pygame
import sys

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
    # prend en param les 2 fichiers reacteurs alumes, et la largeur
    # de la	fenetre
    #
    def bouge(self,file0,file1, height):
        accel=0.8
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

