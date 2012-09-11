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
    angleRotation = 160 #true si on monte et false si on descend
    versLeHaut = True
    ## setImg('src/images/ship1.png')      # fait par __init__
    ## self.ennemyRect = img.get_rect()    #
    def __init__(self,x,y):
        ennemy.__init__(self,x,y, "images/chasseur1.png")
        self.img = pygame.transform.rotate(self.img,-75)
    def estTouche(self,x,y):
        if x > self.posX and x < self.posX+self.ennemyRect.right and y > self.posY and y < self.posY+self.ennemyRect.bottom:
            return True 
        else:
            return False
    
    def move(self,):
        self.posX -= 3
        self.posY =  math.asin(math.sin(self.posX*0.03))*80+150
        if self.posY >= 270:    
            self.img = pygame.image.load("images/chasseur1.png")
            self.img = pygame.transform.rotate(self.img,-75)
        if self.posY <= 36:
            self.img = pygame.image.load("images/chasseur0.png")
            self.img = pygame.transform.rotate(self.img,75)
                    
            
                          
                
            

        
   
     
    
        
        




