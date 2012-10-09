import pygame

class Article(pygame.sprite.Sprite):
    price = 0
    def __init__(self,imageFileName, x, y, player, positionShopStateList, price, isSelected=False):
        pygame.sprite.Sprite.__init__(self)
        self.player=player
        self.positionShopStateList = positionShopStateList
        self.isSold=False
        self.isAvailable=False
        if self.player.shopStateList[self.positionShopStateList] == 0:
            self.isAvailable = True
        elif self.player.shopStateList[self.positionShopStateList] == 1:
            self.isSold = True
        self.setImg(imageFileName, x, y)
        self.isSelected=isSelected
        self.price = price
        
        
    def setImg(self, imageFileName, x, y):
        self.image1 = pygame.image.load(imageFileName+"_selected.jpg")
        self.image2 = pygame.image.load(imageFileName+"_selected_unavailable.jpg")
        self.image3 = pygame.image.load(imageFileName+"_selected_sold.jpg")
        self.image4 = pygame.image.load(imageFileName+"_unselected.jpg")
        self.image5 = pygame.image.load(imageFileName+"_unselected_sold.jpg") 
        
        police = pygame.font.Font(None, 40)
        texte = police.render(str(self.price), 1, (83,89,7))
        self.image1.blit(texte, (420, 50)) 
           
        self.rect = self.image1.get_rect()
        self.rect.left = x
        self.rect.top = y
    def setSelected(self,isSelected):
        self.isSelected=isSelected
    
    def action(self):
        if self.player.shopStateList[self.positionShopStateList] == 0:
            self.player.shopStateList[self.positionShopStateList] = 1
              
