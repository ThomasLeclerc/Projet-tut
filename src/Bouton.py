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
        ecranOption = Menu.menuOption("images/menu/menu.jpg", self.player)
        ecranOption.addButton(BoutonSound("images/menu/menu/titles/sound.png", 0, 270, self.player, True))
        ecranOption.addButton(BoutonMusic("images/menu/menu/titles/music.png", 0, 340, self.player))
        #ecranOption.addButton(BoutonChangeName("images/menu/menu/titles/modifierNom.png"), 200, 400)
        ecranOption.addButton(BoutonReinitialiser("images/menu/menu/titles/reinitialiser.png",0 , 485, self.player))
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
        self.player = player      
    def action(self):
        if self.player.sound: self.player.sound = False
        else: self.player.sound = True
        
class BoutonMusic(Bouton): 
    def __init__(self, image, x, y, player, isSelected=False):
        Bouton.__init__(self, image, x, y, isSelected)
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
