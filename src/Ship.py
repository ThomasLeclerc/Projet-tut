import pygame

class ship:
    monte = False
    desc = False
    posX = 20
    posY = 0
    speed=0
    switch=0
    chaleurMax=300
    chaleur=0
    charge=0
    inCharge=False
    
    def getPos(self):
        return (self.posX,self.posY)
    def setImg(self, image):
        self.img = pygame.image.load(image)
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

        '''
        '    lance-missile refroidit
        '''
        if(self.chaleur>0):
            self.chaleur-=1
            
        '''
        '    charge des tirs
        '''
        if(self.inCharge):
            if self.charge+3<(self.chaleurMax-self.chaleur):
                self.charge+=3
        
    #fin fonction bouge()
#fin classe ship

