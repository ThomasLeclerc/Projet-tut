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
    
    def getPos(self):
        return (self.rect.left,self.rect.top)
    
    def getDimensions(self):
        return (self.image.get_width(), self.image.get_height())

    def setImg(self, filename):
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()       

    def estTouche(self,spr):
        return (pygame.sprite.collide_circle(self, spr))
    
    def update(self, current_time):
        # Update every 10 milliseconds = 1/100th of a second.
        if self.next_update_time < current_time:
            self.rect.left-=6
        self.next_update_time = current_time + 10

class BonusAmmo(Bonus):

    def __init__(self,x,y,ship):
        Bonus.__init__(self, x, y,"images/bonus/ammo.png",ship)
    
    def estTouche(self,spr):
        if Bonus.estTouche(self, spr):
            self.action(spr)
    
    def action(self):
        self.ship.isBonusAmmo=True