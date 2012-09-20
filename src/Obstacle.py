import pygame


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
        self.img =  pygame.transform.scale(pygame.image.load(image), (81, 75))
        self.ennemyRect = self.img.get_rect()


    def move(self):
        self.posX-=8