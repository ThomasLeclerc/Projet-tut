import pygame

class Coin(pygame.sprite.Sprite):  
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.setImg("images/ingame/Coin.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
        self.next_update_time = 0 # update() hasn't been called yet.
        self.son = pygame.mixer.Sound("sounds/coin.wav")
    
    def setImg(self, image):
        self.image = pygame.image.load(image)
    
    def getPos(self):
        return (self.rect.left,self.rect.top) 
    
    def update(self, current_time):
        if self.next_update_time < current_time:
            self.rect.left -= 6
        

        
#fin classe shot