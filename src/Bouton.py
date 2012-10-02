import pygame
import Partie
import Menu
import sys


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
    
    def __init__(self, image, x, y, isSelected=False):
        Bouton.__init__(self, image, x, y, isSelected)
    
    def action(self):
        ecranOption = Menu.Menu("/images/menu/menu/bgMenu.jpg")
        #ecranOption.addButton()
        
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
