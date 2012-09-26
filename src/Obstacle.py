import pygame


class obstacle(pygame.sprite.Sprite):
    
    def __init__(self,x , y,image):
        pygame.sprite.Sprite.__init__(self)
        self.setImg(image)
        self.rect.left = x
        self.rect.top = y
        self.next_update_time = 0 # update() hasn't been called yet.

    def getPos(self):
        return (self.rect.left,self.rect.top)
    
    def getDimensions(self):
        return (self.image.get_width(), self.image.get_height())
    
    def setImg(self, image):
        self.image =  pygame.transform.scale(pygame.image.load(image), (81, 75))
        self.rect = self.image.get_rect()


    def update(self, current_time):
        # Update every 10 milliseconds = 1/100th of a second.
        if self.next_update_time < current_time:
            self.rect.left-=8
        self.next_update_time = current_time + 10
        
    def estTouche(self,x,y):
        if x > self.rect.left and x < self.rect.left+self.rect.right and y > self.rect.top and y < self.rect.top+self.rect.bottom:
            return True 
        else:
            return False