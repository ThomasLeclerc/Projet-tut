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
        self.setImg("images/vaisseaux/orange_ship/orange_ship_0.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position
        self.radius = self.image.get_height()/2 - 5
        
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
    
    def setImg(self, image):
        self.image =  pygame.image.load(image)
        
        
        

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
            accel=3
            if self.monte == True:
                if self.rect.top-2 >= 0:
                    self.rect.top+=self.speed
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
                self.setImg("images/vaisseaux/orange_ship/orange_ship_0.png")
                if self.rect.top <= height-40:
                    self.rect.top+=self.speed
                    self.speed+=accel
                else:
                    self.speed = 0
                
            #blockage du vaisseau dans la fenetre
            if self.rect.top < 0:
                self.rect.top = 0
                self.speed = 0
            elif self.rect.top > height-100:
                self.rect.top = height-100
                self.speed = 0
    
            
            #lance-missile refroidit
            if(self.chaleur>0):
                self.chaleur-=3
                
            #charge des tirs
            if(self.inCharge):
                if self.charge+7<(self.chaleurMax-self.chaleur):
                        self.charge+=7
                        
            self.next_update_time = current_time + 10
            self.position = self.getPos()
    #fin fonction bouge()
    
    def estTouche(self, obs):
        return (pygame.sprite.collide_circle(self, obs))
 


#fin classe ship

