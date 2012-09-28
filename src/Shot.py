import pygame

class shot(pygame.sprite.Sprite):  
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.setImg(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = [x+20,y+20]
        self.next_update_time = 0 # update() hasn't been called yet.
    
    def getPos(self):
        return [self.rect.left,self.rect.top]
    
    def getDimensions(self):
        return (self.image.get_width(), self.image.get_height())
    
    def setImg(self, image):
        self.image = pygame.image.load(image)
        
#fin classe shot
    
class shotShip(shot):
    def __init__(self, x, y):
        shot.__init__(self,x, y, "images/vaisseaux/orange_ship/orange_ship_bullet.png")
        
        
    def update(self, current_time, width, missiles):
        # Update every 10 milliseconds = 1/100th of a second.
        if self.next_update_time < current_time:
            self.rect.left+=20
            if self.rect.left>width:
                missiles.remove(self)
        self.next_update_time = current_time + 10
            

        
class shotShooterEnnemy (shot):
    def __init__(self, x, y):
        shot.__init__(self,x, y, "images/vaisseaux/enemies/enemy1/enemy1_bullet.png")
        
    def update(self, current_time, missilesShooter):
        # Update every 10 milliseconds = 1/100th of a second.
        if self.next_update_time < current_time:
            self.rect.left-=20
            if self.rect.left<-20:
                missilesShooter.remove(self)
        self.next_update_time = current_time + 10
            
            
            
            