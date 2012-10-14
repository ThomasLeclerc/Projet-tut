import pygame

class Bonus(pygame.sprite.Sprite):
    def __init__(self,x,y,filename,ship):
        pygame.sprite.Sprite.__init__(self)
        self.setImg(filename)
        self.rect.left = x
        self.rect.top = y
        self.radius=self.image.get_width()/2 - 5
        self.next_update_time = 0 # update() hasn't been called yet.
        self.ship = ship
        self.startTime = 0
        self.stopTime = 0
        self.isActive = False
        self.isVisible = True
        self.isTerminated = False
    def getPos(self):
        return (self.rect.left,self.rect.top)
    def getDimensions(self):
        return (self.image.get_width(), self.image.get_height())
    def setImg(self, filename):
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
    def estTouche(self,spr):
        return (pygame.sprite.collide_circle(self, spr))
    def update(self, current_time, bonus):
        # Update every 10 milliseconds = 1/100th of a second.
        if self.next_update_time < current_time:
            self.rect.left-=6
        self.next_update_time = current_time + 10

class BonusAmmo(Bonus):
    def __init__(self,x,y,ship):
        Bonus.__init__(self, x, y,"images/bonus/ammo.png",ship)
        self.son = pygame.mixer.Sound("sounds/cliclic.WAV")
    def estTouche(self,spr,current_time):
        return (pygame.sprite.collide_circle(self, spr))                
    def action(self,bonus,current_time):
        if self.isActive == True:
            if self.ship.isBonusAmmo==False:
                self.ship.isBonusAmmo=True
                self.son.play() 
            elif current_time > self.stopTime:
                self.isActive=False
                self.ship.isBonusAmmo=False

class BonusShield(Bonus):
    def __init__(self,x,y,ship):
        Bonus.__init__(self, x, y,"images/bonus/shield_icon.png",ship)
        self.son = pygame.mixer.Sound("sounds/shield.wav")
    def estTouche(self,spr,current_time):
        return (pygame.sprite.collide_circle(self, spr))                
    def action(self,bonus,current_time):
        if self.isActive == True:
            if self.ship.isBonusShield==False:
                self.ship.isBonusShield=True
                self.son.play()
            elif current_time > self.stopTime:
                self.isActive=False
                self.ship.isBonusShield=False
        

