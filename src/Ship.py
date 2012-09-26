import pygame



class ship(pygame.sprite.Sprite):
    monte = False
    desc = False
    speed=0
    switch=0
    chaleurMax=200
    chaleur=0
    charge=0
    inCharge=False
    enVie = True
    record = 0
    
    def __init__(self, position_initiale):
        pygame.sprite.Sprite.__init__(self)
        self.next_update_time = 0 # update() hasn't been called yet.
        self.position = position_initiale
        self.setImg("images/vaisseaux/orange_ship/orange_ship_0.png", self.position)
        self.rect.topleft = self.position
        
    def enregistrerRecord(self,record):
        file1 = open('saves/sav.txt','w')
        file1.write(str(self.record))
        file1.close()
        
    def chargerRecord(self):
        file1 = open('saves/sav.txt','r')
        strRec = file1.read()
        self.record = int(strRec)
    
    def getPos(self):
        return [self.rect.left,self.rect.top]
    
    def setImg(self, image, position):
        self.image =  pygame.image.load(image)
        self.rect = self.image.get_rect()
        
        

    #
    # deplace le vaisseau,   
    # prend en param les 2 fichiers reacteurs alumes, et la largeur
    # de la	fenetre
    #
    def update(self, current_time, height):
        # Update every 10 milliseconds = 1/100th of a second.
        if self.next_update_time < current_time:
            file0 = "images/vaisseaux/orange_ship/orange_ship_1.png"
            file1 = "images/vaisseaux/orange_ship/orange_ship_2.png"
            accel=1.5
            if self.monte == True:
                if self.rect.top-2 >= 0:
                    self.rect.top+=self.speed
                    self.speed-=accel
                    self.position = self.getPos()
                else:
                    self.speed = 0
                #animation    
                if self.switch == 0:
                    self.setImg(file0, self.position)
                    self.switch=1
                elif self.switch == 1:
                    self.setImg(file1, self.position)
                    self.switch=0
            else:
                self.setImg("images/vaisseaux/orange_ship/orange_ship_0.png", self.position)
                if self.rect.top <= height-40:
                    self.rect.top+=self.speed
                    self.speed+=8*accel
                    self.position = self.getPos()
                else:
                    self.speed = 0
                
            #blockage du vaisseau dans la fenetre
            if self.rect.top < 0:
                self.speed = 0
            elif self.rect.top > height-40:
                self.speed = 0
    
            
            #lance-missile refroidit
            if(self.chaleur>0):
                self.chaleur-=3
                
            #charge des tirs
            if(self.inCharge):
                if self.charge+3<(self.chaleurMax-self.chaleur):
                        self.charge+=3
                        
            self.next_update_time = current_time + 10
            self.position = self.getPos()
    #fin fonction bouge()
    
    def estTouche(self, obs):
        return (pygame.sprite.collide_rect(self, obs))
 

    def estTouche2(self,(x,y), (obsWidth, obsHeight)):
        if ((self.posX+self.img.get_width()-9 > x and self.posX+self.img.get_width()-9 < x+obsWidth and self.posY+14 > y and self.posY+14 < y+obsHeight) or
        (self.posX+self.img.get_width()-9 > x and self.posX+self.img.get_width()-9 < x+obsWidth and self.posY+self.img.get_height() > y and self.posY+self.img.get_height() < y+obsHeight) or 
        (self.posX+self.img.get_width()-9 > x and self.posX+35 < x+obsWidth and self.posY+self.img.get_height()-11 > y and self.posY+self.img.get_height()-11 < y+obsHeight) or 
        (self.posX+self.img.get_width()-9 > x and self.posX+35 < x+obsWidth and self.posY+14 > y and self.posY+14 < y+obsHeight)):
            return True 
        else:
            return False  

#fin classe ship

