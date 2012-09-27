import pygame
import Partie


class Bouton(pygame.sprite.Sprite):
    
    def __init__(self,image, imageAlt, isSelected):
        pygame.sprite.Sprite.__init__(self)
        self.setImg(image,imageAlt)
        self.isSelected=isSelected
        
    def setImg(self, image, imageAlt):
        self.image = pygame.image.load(image)
        self.imageAlt = pygame.image.load(imageAlt)
        self.rect = self.image.get_rect()
        
    def setSelected(self,isSelected):
        self.isSelected=isSelected
    
class BoutonStartGame(Bouton):
    
    def __init__(self, image, imageAlt, isSelected=False):
        Bouton.__init__(self, image, imageAlt, isSelected)
    
    '''prend une instance de la classe Partie en param'''
    def action(self):
        p = Partie.Partie()
        p.jouer()

class BoutonRecord(Bouton):
    
    def __init__(self, image, imageAlt, isSelected=False):
        Bouton.__init__(self, image, imageAlt, isSelected)
    
    def action(self):
        #TODO
        print " "
