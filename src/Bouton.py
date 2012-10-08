import pygame
import Partie
import Menu
import sys
import Player


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
        if self.player.sound: self.player.sound = False
        else: 
            self.player.sound = True
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
        ecranAccueil = Menu.Menu("images/menu/menu.jpg")
        ecranAccueil.addButton(BoutonStartGame("images/menu/menu_principal/titles/play.png",0, 270, self.player, True))
        ecranAccueil.addButton(BoutonOption("images/menu/menu_principal/titles/option.png",0, 340, self.player))
        ecranAccueil.addButton(BoutonCredits("images/menu/menu_principal/titles/credits.png",0, 415))
        ecranAccueil.addButton(BoutonQuit("images/menu/menu_principal/titles/quit.png",0, 485))
        ecranAccueil.afficher()
        
class BoutonShop(Bouton): 
    def __init__(self, image, x, y, isSelected=False):
        Bouton.__init__(self, image, x, y, isSelected)
    def action(self):
        menuShop = Menu.Menu("images/menu/menu_shop/background_menu_shop.jpg")
        menuShop.addButton(BoutonGoldShip("images/menu/menu_shop/item1_gold_skin_selected.jpg", "images/menu/menu_shop/item1_gold_skin_unselected.jpg", 20, 150, True))
        menuShop.afficher()
  
  
##### BOUTONS SHOP #####    
class BoutonGoldShip(Bouton): 
    def __init__(self, image, imageAlt, x, y, isSelected=False):
        Bouton.__init__(self, image, x, y, isSelected)
        self.imageAlt = pygame.image.load(imageAlt)
    def action(self):
        print " "

##### BOUTONS MENU PAUSE #####
class BoutonReprendre(Bouton): 
    def __init__(self, image, x, y,  isSelected=False):
        Bouton.__init__(self, image, x, y, isSelected)
    def action(self):
        return True
