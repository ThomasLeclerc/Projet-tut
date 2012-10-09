import pygame
import random


class obstacle(pygame.sprite.Sprite):
    
    def __init__(self,x , y,image):
        pygame.sprite.Sprite.__init__(self)
        self.setImg(image)
        self.rect.left = x
        self.rect.top = y
        self.radius=self.image.get_width()/2 - 5
        self.next_update_time = 0 # update() hasn't been called yet.

    def getPos(self):
        return (self.rect.left,self.rect.top)
    
    def getDimensions(self):
        return (self.image.get_width(), self.image.get_height())
    
    def setImg(self, image):
        taille = [(81, 75), (162, 150), (162, 150), (232, 225)]
        self.image =  pygame.transform.scale(pygame.image.load(image), taille[random.randint(0,3)])
        self.rect = self.image.get_rect()


    def update(self, current_time):
        # Update every 10 milliseconds = 1/100th of a second.
        if self.next_update_time < current_time:
            self.rect.left-=6
        self.next_update_time = current_time + 10
        
    def estTouche(self, spr):
        return (pygame.sprite.collide_circle(self, spr))

class obstacleRecord(obstacle):
    def __init__(self,x , y,image):
        pygame.sprite.Sprite.__init__(self)
        self.setImg(image)
        self.rect.left = x
        self.rect.top = y
        self.radius=self.image.get_width()/2 - 5
        self.next_update_time = 0
    def setImg(self,image):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()