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
    
    def getDimensions(self):
        return (self.img.get_width(), self.img.get_height())
    
    def setImg(self, image):
        self.img =  pygame.transform.scale(pygame.image.load(image), (81, 75))
        self.obstacleRect = self.img.get_rect()


    def move(self):
        self.posX-=8
        
    def estTouche(self,x,y):
        if x > self.posX and x < self.posX+self.obstacleRect.right and y > self.posY and y < self.posY+self.obstacleRect.bottom:
            return True 
        else:
            return False