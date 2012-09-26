import pygame

class shot(pygame.sprite.Sprite):  
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.next_update_time = 0 # update() hasn't been called yet.
    
    def getPos(self):
        return (self.rect.left,self.rect.top)
    
    def getDimensions(self):
        return (self.image.get_width(), self.image.get_height())
    
    def setImg(self, image):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
#fin classe shot
    
class shotShip(shot):
    def __init__(self):
        shot.__init__(self)
        self.setImg("images/vaisseaux/orange_ship/orange_ship_bullet.png")
        self.rect.left = 0
        self.rect.top = 0
        
        
    def update(self, current_time, width, missiles):
        # Update every 10 milliseconds = 1/100th of a second.
        if self.next_update_time < current_time:
            self.rect.left+=15
            if self.rect.left>width:
                missiles.remove(self)
        self.next_update_time = current_time + 10
            
    def setPos(self,x,y):
        self.rect.left=x+20
        self.rect.top=y+20

        
class shotShooterEnnemy (shot):
    def __init__(self, x, y):
        shot.__init__(self)
        self.setImg("images/vaisseaux/enemies/enemy1/enemy1_bullet.png") 
        self.rect.left = x
        self.rect.top = y
        
    def update(self, current_time, missilesShooter):
        # Update every 10 milliseconds = 1/100th of a second.
        if self.next_update_time < current_time:
            self.rect.left-=10
            if self.rect.left<-20:
                missilesShooter.remove(self)
        self.next_update_time = current_time + 10
            
            
            
            