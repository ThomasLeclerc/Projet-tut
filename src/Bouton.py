import pygame
import Partie
import Menu
import sys
import Player
import Article


class Bouton(pygame.sprite.Sprite):
    ''' constructeur de la classe Bouton
        prend en parametre le nom du fichier image,
        les coordonees x et y, et un booleen isSelected
    '''
    def __init__(self,imageFileName, x, y, isSelected):
        pygame.sprite.Sprite.__init__(self)
        self.setImg(imageFileName, x, y)
        self.isSelected=isSelected  
    def setImg(self, imageFileName, x, y):
        self.image = pygame.image.load(imageFileName)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y    
    def setSelected(self,isSelected):
        self.isSelected=isSelected

##### BOUTONS MENU PRINCIPAL #####    
class BoutonStartGame(Bouton): 
    def __init__(self, image, x, y, player, isSelected=False):
        Bouton.__init__(self, image, x, y, isSelected)
        self.player = player
    def action(self):
        p = Partie.Partie(self.player)
        p.jouer()

class BoutonRecord(Bouton):
    def __init__(self, image, x, y, isSelected=False):
        Bouton.__init__(self, image, x, y, isSelected)
    def action(self):
        #TODO
        print " "

class BoutonOption(Bouton):  
    def __init__(self, image, x, y, player, isSelected=False):
        Bouton.__init__(self, image, x, y, isSelected)
        self.player = player
    def action(self):
        ecranOption = Menu.menuOption("images/menu/menu_option/background_menu_option.jpg", self.player)
        ecranOption.addButton(BoutonSound("images/menu/menu_option/on.png", 530, 255, self.player, True))
        ecranOption.addButton(BoutonMusic("images/menu/menu_option/on.png", 530, 325, self.player))
        ecranOption.addButton(BoutonReinitialiser("images/menu/menu_option/reset_profile.png",344 , 388, self.player))
        ecranOption.addButton(BoutonShop("images/menu/menu_option/shop.png",414 , 455, self.player))
        ecranOption.addButton(BoutonMenuPrincipal("images/menu/menu_option/back.png",460 , 543, self.player))
        ecranOption.afficher()
        
class BoutonCredits(Bouton):   
    def __init__(self, image, x, y, isSelected=False):
        Bouton.__init__(self, image, x, y, isSelected) 
    def action(self):
        #TODO
        print " "
        
class BoutonQuit(Bouton):  
    def __init__(self, image, x, y, isSelected=False):
        Bouton.__init__(self, image, x, y, isSelected) 
    def action(self):
        sys.exit()
 
 
##### BOUTONS MENU OPTION #####       
class BoutonSound(Bouton): 
    def __init__(self, image, x, y, player, isSelected=False):
        Bouton.__init__(self, image, x, y, isSelected)
        self.imageNon = pygame.image.load("images/menu/menu_option/off.png")
        self.player = player      
    def action(self):
        if self.player.soundOn: 
            self.player.soundOn = False
        else: 
            self.player.soundOn = True
        self.player.save()
        
class BoutonMusic(Bouton): 
    def __init__(self, image, x, y, player, isSelected=False):
        Bouton.__init__(self, image, x, y, isSelected)
        self.imageNon = pygame.image.load("images/menu/menu_option/off.png")
        self.player = player    
    def action(self):
        if self.player.musicOn: self.player.musicOn = False
        else: 
            self.player.musicOn = True
        self.player.save()

class BoutonReinitialiser(Bouton): 
    def __init__(self, image, x, y, player, isSelected=False):
        Bouton.__init__(self, image, x, y, isSelected)
        self.player = player    
    def action(self):
        self.player = Player.Player()
        self.player.save()
        ecranOption = Menu.menuOption("images/menu/menu_option/background_menu_option.jpg", self.player)
        ecranOption.addButton(BoutonSound("images/menu/menu_option/on.png", 530, 255, self.player, True))
        ecranOption.addButton(BoutonMusic("images/menu/menu_option/on.png", 530, 325, self.player))
        ecranOption.addButton(BoutonReinitialiser("images/menu/menu_option/reset_profile.png",344 , 388, self.player))
        ecranOption.addButton(BoutonShop("images/menu/menu_option/shop.png",414 , 455, self.player))
        ecranOption.addButton(BoutonMenuPrincipal("images/menu/menu_option/back.png",460 , 543, self.player))
        ecranOption.afficher()
        
#sert a revenir au menu principal. est utilise autre part que dans le menu option      
class BoutonMenuPrincipal(Bouton): 
    def __init__(self, image, x, y, player, isSelected=False):
        Bouton.__init__(self, image, x, y, isSelected)
        self.player = player
    def action(self):
        ecranAccueil = Menu.Menu("images/menu/menu.jpg", self.player)
        ecranAccueil.addButton(BoutonStartGame("images/menu/menu_principal/titles/play.png",0, 270, self.player, True))
        ecranAccueil.addButton(BoutonOption("images/menu/menu_principal/titles/option.png",0, 340, self.player))
        ecranAccueil.addButton(BoutonCredits("images/menu/menu_principal/titles/credits.png",0, 415))
        ecranAccueil.addButton(BoutonQuit("images/menu/menu_principal/titles/quit.png",0, 485))
        ecranAccueil.afficher()
        
class BoutonShop(Bouton): 
    def __init__(self, image, x, y, player, isSelected=False):
        Bouton.__init__(self, image, x, y, isSelected)
        self.player = player
    def action(self):
        menuShop = Menu.menuShop("images/menu/menu_shop/background_menu_shop.jpg", self.player)
        menuShop.addButton(Article.Article("images/menu/menu_shop/item1_gold_skin", 70, 160, self.player, 0, 10000, True))
        menuShop.addButton(Article.Article("images/menu/menu_shop/item2_basic_weapon_lvl2", 70, 300, self.player, 1, 1000))
        menuShop.addButton(Article.Article("images/menu/menu_shop/item3_xtreme_weapon_lvl1", 70, 440, self.player, 2, 2000))
        menuShop.addButton(Article.Article("images/menu/menu_shop/item4_xtreme_weapon_lvl2", 70, 580, self.player, 3, 5000))
        menuShop.addButton(Article.Article("images/menu/menu_shop/item5_booster", 70, 720, self.player, 4, 500))
        menuShop.addButton(Article.Article("images/menu/menu_shop/item6_spoiler", 70, 860, self.player, 5, 750))
        menuShop.addButton(Article.ArticleMissile("images/menu/menu_shop/item7_missile", 70, 1000, self.player, 6, self.player.prixMissile))
        menuShop.afficher()
  
  


##### BOUTONS MENU PAUSE #####
class BoutonReprendre(Bouton): 
    def __init__(self, image, x, y,  isSelected=False):
        Bouton.__init__(self, image, x, y, isSelected)
    def action(self):
        return True
