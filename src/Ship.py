import pygame

class ship:
    monte = False
    desc = False
    posX = 20
    posY = 0
    speed=0
    switch=0
    chaleurMax=200
    chaleur=0
    charge=0
    inCharge=False
    enVie = True
    
    def getPos(self):
        return (self.posX,self.posY)
    def setImg(self, image):
        self.img = pygame.image.load(image)
        self.shipRect = self.img.get_rect()

    #
    # deplace le vaisseau,   
    # prend en param les 2 fichiers reacteurs alumes, et la largeur
    # de la	fenetre
    #
    def bouge(self,file0,file1, height):
        accel=1.5
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
            if self.posY+2 <= height-(self.shipRect).bottom:
                self.posY+=self.speed
                self.speed+=accel
            else:
                self.speed = 0
                
        #blockage du vaisseau dans la fenetre
        if self.posY < 0:
            self.posY = 0
            self.speed = 0
        elif self.posY > height-(self.shipRect).bottom:
            self.posY = height-(self.shipRect).bottom
            self.speed = 0

        '''
        '    lance-missile refroidit
        '''
        if(self.chaleur>0):
            self.chaleur-=2
            
        '''
        '    charge des tirs
        '''
        if(self.inCharge):
            if self.charge+3<(self.chaleurMax-self.chaleur):
                self.charge+=3
        
    #fin fonction bouge()
    
    def estTouche(self,(x,y), (obsWidth, obsHeight)):
        if ((self.posX+self.img.get_width() > x and self.posX+self.img.get_width() < x+obsWidth and self.posY > y and self.posY < y+obsHeight) or
        (self.posX+self.img.get_width() > x and self.posX+self.img.get_width() < x+obsWidth and self.posY+self.img.get_height() > y and self.posY+self.img.get_height() < y+obsHeight) or 
        (self.posX+self.img.get_width() > x and self.posX < x+obsWidth and self.posY+self.img.get_height() > y and self.posY+self.img.get_height() < y+obsHeight) or 
        (self.posX+self.img.get_width() > x and self.posX < x+obsWidth and self.posY > y and self.posY < y+obsHeight)):
            return True 
        else:
            return False
#fin classe ship

