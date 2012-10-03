import pygame
import Partie
import Menu
import sys
import Player2


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
    
class BoutonStartGame(Bouton): 
    def __init__(self, image, x, y, isSelected=False):
        Bouton.__init__(self, image, x, y, isSelected)
    def action(self):
        p = Partie.Partie()
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
        ecranOption.addButton(BoutonSound("images/menu/menu_option/on.png", 500, 250, self.player, True))
        ecranOption.addButton(BoutonMusic("images/menu/menu_option/on.png", 500, 290, self.player))
        ecranOption.addButton(BoutonShop("images/menu/menu_option/shop.png",400 , 380, self.player))
        ecranOption.addButton(BoutonBack("images/menu/menu_option/back.png",450 , 460, self.player, self.player))
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
        
class BoutonSound(Bouton): 
    def __init__(self, image, x, y, player, isSelected=False):
        Bouton.__init__(self, image, x, y, isSelected)
        self.imageNon = pygame.image.load("images/menu/menu_option/off.png")
        self.player = player      
    def action(self):
        if self.player.sound: self.player.sound = False
        else: self.player.sound = True
        
class BoutonMusic(Bouton): 
    def __init__(self, image, x, y, player, isSelected=False):
        Bouton.__init__(self, image, x, y, isSelected)
        self.imageNon = pygame.image.load("images/menu/menu_option/off.png")
        self.player = player    
    def action(self):
        if self.player.music: self.player.music = False
        else: self.player.music = True

class BoutonReinitialiser(Bouton): 
    def __init__(self, image, x, y, player, isSelected=False):
        Bouton.__init__(self, image, x, y, isSelected)
        self.player = player    
    def action(self):
        self.player = Player2.Player()
        self.player.save()
        ecranOption = Menu.menuOption("images/menu/menu.jpg", self.player)
        ecranOption.addButton(BoutonSound("images/menu/menu/titles/sound.png", 0, 270, self.player, True))
        ecranOption.addButton(BoutonMusic("images/menu/menu/titles/music.png", 0, 340, self.player))
        #ecranOption.addButton(BoutonChangeName("images/menu/menu/titles/modifierNom.png"), 200, 400)
        ecranOption.addButton(BoutonReinitialiser("images/menu/menu/titles/reinitialiser.png",0 , 485, self.player))
        ecranOption.afficher()

class BoutonShop(Bouton): 
    def __init__(self, image, x, y, isSelected=False):
        Bouton.__init__(self, image, x, y, isSelected)
    def action(self):
        menuShop = Menu.Menu("images/menu/menu_shop/exemple_shop.jpg")
        menuShop.afficher()
        
class BoutonBack(Bouton): 
    def __init__(self, image, x, y, player, isSelected=False):
        Bouton.__init__(self, image, x, y, isSelected)
        self.player = player
    def action(self):
        ecranAccueil = Menu.Menu("images/menu/menu.jpg")
        ecranAccueil.addButton(BoutonStartGame("images/menu/menu_principal/titles/play.png",0, 270, True))
        ecranAccueil.addButton(BoutonOption("images/menu/menu_principal/titles/option.png",0, 340, self.player))
        ecranAccueil.addButton(BoutonCredits("images/menu/menu_principal/titles/credits.png",0, 415))
        ecranAccueil.addButton(BoutonQuit("images/menu/menu_principal/titles/quit.png",0, 485))
        ecranAccueil.afficher()