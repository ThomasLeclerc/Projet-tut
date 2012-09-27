import pygame
import Partie
import sys


class Bouton(pygame.sprite.Sprite):
    
    def __init__(self,image, x, y, isSelected):
        pygame.sprite.Sprite.__init__(self)
        self.setImg(image, x, y)
        self.isSelected=isSelected
        
    def setImg(self, image, x, y):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        
    def setSelected(self,isSelected):
        self.isSelected=isSelected
    
class BoutonStartGame(Bouton):
    
    def __init__(self, image, x, y, isSelected=False):
        Bouton.__init__(self, image, x, y, isSelected)
    
    '''prend une instance de la classe Partie en param'''
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
        #TODO
        print " "
        
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
