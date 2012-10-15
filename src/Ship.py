import pygame
import Shot

class ship(pygame.sprite.Sprite):
    monte = False
    desc = False
    speed=0
    switch=0
    animSwitch=2
    chaleurMissile=33
    chaleurMax=100
    chaleur=0
    charge=0
    inCharge=False
    inBoost=False
    inBreak=False
    enVie = True
    record = 0
    money = 0
    isBonusAmmo = False
    isBonusShield = False
    versionCanon = 1
    boosterOn = False
    spoilerOn = False
    score = 0
    
    def __init__(self, position_initiale, player):
        pygame.sprite.Sprite.__init__(self)
        self.next_update_time = 0 # update() hasn't been called yet.
        self.position = position_initiale
        self.setImg("images/vaisseaux/orange_ship/orange_ship_1.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position
        self.radius = self.image.get_height()/2 - 5
        self.son = pygame.mixer.Sound("sounds/shipAmbiance.wav")
        self.player = player

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
    
    def setImg(self, imageFile):
        self.image =  pygame.image.load(imageFile)
        
    '''prend le nbre de missiles A ajouter'''    
    def raiseChaleurMax(self, nbMissiles):
        self.chaleurMax+=(33*nbMissiles)
        
    def setVersionCanon(self,version):
        self.versionCanon = version
        
    def setBoosterOn(self,valeur):
        self.boosterOn = valeur
        
    def setSpoilerOn(self,valeur):
        self.spoilerOn = valeur
     
    def raiseScore(self, nombre):
        self.score += nombre 
        
    def reinitialiserScore(self):
        self.score=0

    def getScore(self):
        return self.score  
    # deplace le vaisseau,   
    # prend en param les 2 fichiers reacteurs alumes, et la largeur
    # de la	fenetre
    def update(self, current_time, height,screen):
        # Update every 10 milliseconds = 1/100th of a second.
        if self.next_update_time < current_time:
            file0 = "images/vaisseaux/orange_ship/orange_ship_1.png"
            file1 = "images/vaisseaux/orange_ship/orange_ship_2.png"
            file2 = "images/vaisseaux/orange_ship/orange_ship_3.png"
            file3 = "images/vaisseaux/orange_ship/orange_ship_4.png"
            file4 = "images/vaisseaux/orange_ship/orange_ship_5.png"
            accel=2.3
            #mouvement vertical
            if self.monte:
                if self.rect.top-2 >= 0:
                    self.rect.top+=self.speed
                    self.speed-=accel
                else:
                    self.speed = 0
                #animation    
                if self.animSwitch == 2:
                    self.setImg(file2)
                    self.animSwitch=3
                elif self.animSwitch == 3:
                    self.setImg(file3)
                    self.animSwitch=4
                elif self.animSwitch == 4:
                    self.setImg(file4)
                    self.animSwitch=2                                       
            else:
                if self.rect.top <= height-40:
                    self.rect.top+=self.speed
                    self.speed+=accel
                else:
                    self.speed = 0
                #animation    
                if self.switch == 0:
                    self.setImg(file0)
                    self.switch=1
                elif self.switch == 1:
                    self.setImg(file1)
                    self.switch=0 
            #mouvement horizontal (boost)
            if self.boosterOn:
                if self.inBoost:
                    if self.rect.left < 800:
                        self.rect.left += 10
                else:
                    if self.inBreak:
                        if self.spoilerOn:
                            if self.rect.left-10 > 0:
                                self.rect.left -= 15
                    else:
                        if self.rect.left-6 > 0:
                            self.rect.left -= 6
                
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
        

    def tir(self,missiles):
        self.inCharge=False
        #Basic Weapon Lvl 1
        if self.versionCanon==1:
            nbShoot = (self.charge/self.chaleurMissile)+1
            for m in range(nbShoot):
                if(self.chaleur+self.chaleurMissile<(self.chaleurMax)):
                    monMissile=Shot.shotShip(self.versionCanon,self.rect.left+40, self.rect.top-(nbShoot*30)+(60*m)+40, self.isBonusAmmo)
                    missiles.add(monMissile)
                    sound = pygame.mixer.Sound("sounds/rocket.wav")
                    if self.player.soundOn:
                        sound.play()                
                    if(self.chaleur+self.chaleurMissile<self.chaleurMax):
                        self.chaleur+=self.chaleurMissile
                    else:
                        self.chaleur=self.chaleurMax
                    if(self.isBonusAmmo):
                        self.chaleur-=self.chaleurMissile
        #Basic Weapon Lvl 2
        if self.versionCanon==2:
            nbShoot = 2#(self.charge/self.chaleurMissile)+2
            for m in range(nbShoot):
                if(self.chaleur+self.chaleurMissile/2<(self.chaleurMax)):
                    monMissile=Shot.shotShip(self.versionCanon,self.rect.left+40, self.rect.top-(nbShoot*15)+(30*m)+20, self.isBonusAmmo)
                    missiles.add(monMissile)
                    sound = pygame.mixer.Sound("sounds/rocket.wav")
                    sound.play()                
                    if(self.chaleur+self.chaleurMissile/2<self.chaleurMax):
                        self.chaleur+=self.chaleurMissile/2
                    else:
                        self.chaleur=self.chaleurMax
                    if(self.isBonusAmmo):
                        self.chaleur-=self.chaleurMissile/2
        #Extrem Weapon Lvl 1
        if self.versionCanon==3:
            nbShoot = (self.charge/self.chaleurMissile)+1
            for m in range(nbShoot):
                if(self.chaleur+self.chaleurMissile<(self.chaleurMax)):
                    monMissile=Shot.shotShip(self.versionCanon,self.rect.left+40, self.rect.top-(nbShoot*30)+(60*m)+40, self.isBonusAmmo)
                    missiles.add(monMissile)
                    sound = pygame.mixer.Sound("sounds/laser.wav")
                    sound.play()                
                    if(self.chaleur+self.chaleurMissile<self.chaleurMax):
                        self.chaleur+=self.chaleurMissile
                    else:
                        self.chaleur=self.chaleurMax
                    if(self.isBonusAmmo):
                        self.chaleur-=self.chaleurMissile
        #Extrem Weapon Lvl 2
        if self.versionCanon==4:
            nbShoot = (self.charge/self.chaleurMissile)+2
            for m in range(nbShoot):
                if(self.chaleur+self.chaleurMissile/2<(self.chaleurMax)):
                    monMissile=Shot.shotShip(self.versionCanon,self.rect.left+40, self.rect.top-(nbShoot*30)+(60*m)+40, self.isBonusAmmo)
                    missiles.add(monMissile)
                    sound = pygame.mixer.Sound("sounds/laser.wav")
                    sound.play()                
                    if(self.chaleur+self.chaleurMissile/2<self.chaleurMax):
                        self.chaleur+=self.chaleurMissile/2
                    else:
                        self.chaleur=self.chaleurMax
                    if(self.isBonusAmmo):
                        self.chaleur-=self.chaleurMissile/2

        self.charge=0


#fin classe ship

