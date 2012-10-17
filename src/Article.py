import pygame
import Menu

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
            self.isAvailable = True
        self.price = price
        self.setImg(imageFileName, x, y)
        self.isSelected=isSelected
        
        
    def setImg(self, imageFileName, x, y):
        self.image1 = pygame.image.load(imageFileName+"_selected.jpg")
        self.image2 = pygame.image.load(imageFileName+"_selected_unavailable.jpg")
        self.image3 = pygame.image.load(imageFileName+"_selected_sold.jpg")
        self.image4 = pygame.image.load(imageFileName+"_unselected.jpg")
        self.image5 = pygame.image.load(imageFileName+"_unselected_sold.jpg") 
        
        police = pygame.font.Font(None, 40)
        self.image1.blit(self.textOutline(police, str(self.price), (210, 210, 1), (38, 33, 4)), (400, 50)) 
           
        self.rect = self.image1.get_rect()
        self.rect.left = x
        self.rect.top = y
      
    #fonction pour faire une bordur autour du texte  
    def textHollow(self, font, message, fontcolor):
        notcolor = [c^0xFF for c in fontcolor]
        base = font.render(message, 0, fontcolor, notcolor)
        size = base.get_width() + 2, base.get_height() + 2
        img = pygame.Surface(size, 16)
        img.fill(notcolor)
        base.set_colorkey(0)
        img.blit(base, (0, 0))
        img.blit(base, (2, 0))
        img.blit(base, (0, 2))
        img.blit(base, (2, 2))
        base.set_colorkey(0)
        base.set_palette_at(1, notcolor)
        img.blit(base, (1, 1))
        img.set_colorkey(notcolor)
        return img
    
    def textOutline(self, font, message, fontcolor, outlinecolor):
        base = font.render(message, 0, fontcolor)
        outline = self.textHollow(font, message, outlinecolor)
        img = pygame.Surface(outline.get_size(), 16)
        img.blit(base, (1, 1))
        img.blit(outline, (0, 0))
        img.set_colorkey(0)
        return img

    def setSelected(self,isSelected):
        self.isSelected=isSelected
    
    def action(self):
        if self.player.shopStateList[self.positionShopStateList] == 0:
            if self.player.money - self.price >= 0:
                self.player.updateShopStateList(self.positionShopStateList, 1)
                self.player.money -= self.price
                if (self.positionShopStateList < 6) and (self.player.shopStateList[self.positionShopStateList + 1]==-1):
                    self.player.updateShopStateList(self.positionShopStateList+1 ,0)
        menuShop = Menu.menuShop("images/menu/menu_shop/background_menu_shop.jpg", self.player)
        menuShop.addButton(Article("images/menu/menu_shop/item1_gold_skin", 70, 160, self.player, 0, 10000, True))
        menuShop.addButton(Article("images/menu/menu_shop/item2_basic_weapon_lvl2", 70, 300, self.player, 1, 1000))
        menuShop.addButton(Article("images/menu/menu_shop/item3_xtreme_weapon_lvl1", 70, 440, self.player, 2, 2000))
        menuShop.addButton(Article("images/menu/menu_shop/item4_xtreme_weapon_lvl2", 70, 580, self.player, 3, 5000))
        menuShop.addButton(Article("images/menu/menu_shop/item5_booster", 70, 720, self.player, 4, 500))
        menuShop.addButton(Article("images/menu/menu_shop/item6_spoiler", 70, 860, self.player, 5, 750))
        menuShop.addButton(ArticleMissile("images/menu/menu_shop/item7_missile", 70, 1000, self.player, 6, self.player.prixMissile))
        menuShop.afficher()

class ArticleMissile(Article):
    def setImg(self, imageFileName, x, y):
        self.image1 = pygame.image.load(imageFileName+"_selected.jpg")
        self.image2 = pygame.image.load(imageFileName+"_unselected.jpg")
        
        police = pygame.font.Font(None, 40)
        self.image1.blit(self.textOutline(police, str(self.player.prixMissile), (210, 210, 1), (38, 33, 4)), (400, 50)) 
           
        self.rect = self.image1.get_rect()
        self.rect.left = x
        self.rect.top = y   
        
    def action(self):
        if self.player.money >= self.player.prixMissile:
            self.player.money -= self.player.prixMissile
            self.player.additionalMissiles += 1
            self.player.prixMissile = self.player.prixMissile*2
            self.player.save()
        menuShop = Menu.menuShop("images/menu/menu_shop/background_menu_shop.jpg", self.player)
        menuShop.addButton(Article("images/menu/menu_shop/item1_gold_skin", 70, 160, self.player, 0, 10000, True))
        menuShop.addButton(Article("images/menu/menu_shop/item2_basic_weapon_lvl2", 70, 300, self.player, 1, 1000))
        menuShop.addButton(Article("images/menu/menu_shop/item3_xtreme_weapon_lvl1", 70, 440, self.player, 2, 2000))
        menuShop.addButton(Article("images/menu/menu_shop/item4_xtreme_weapon_lvl2", 70, 580, self.player, 3, 5000))
        menuShop.addButton(Article("images/menu/menu_shop/item5_booster", 70, 720, self.player, 4, 500))
        menuShop.addButton(Article("images/menu/menu_shop/item6_spoiler", 70, 860, self.player, 5, 750))
        menuShop.addButton(ArticleMissile("images/menu/menu_shop/item7_missile", 70, 1000, self.player, 6, self.player.prixMissile))
        menuShop.afficher()
              
