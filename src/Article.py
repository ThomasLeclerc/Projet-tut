import pygame

class Article(pygame.sprite.Sprite):
    def __init__(self,imageFileName, x, y, player, isSelected=False):
        pygame.sprite.Sprite.__init__(self)
        self.setImg(imageFileName, x, y)
        self.isSelected=isSelected
        self.isSold=False
        self.isAvailable=False
        self.player=player
    def setImg(self, imageFileName, x, y):
        self.image = pygame.image.load(imageFileName)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
    def setSelected(self,isSelected):
        self.isSelected=isSelected
