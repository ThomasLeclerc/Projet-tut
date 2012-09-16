import pygame

#doit heriter de l'attribut screen
screen = None

class Menu:
    """Le menu permet de définir une ou plusieurs options
    que pourra choisir l'utilisateur"""
    
    name = ''
    bg_img = ''
    
    def __init__(self, name, bg_img):
        self.name = name
        self.bg_img = bg_img
        
    
    def setName(self, name):
        self.name = name

    def getName(self, name):
        return self.name    
    

    def setBackground(self, bg_img):
        self.bg_img = pygame.image.load(bg_img)
    
    def getBackground(self, bg_img):
        return self.bg_img    

        
    def setOptionImg(self, img):
        """Definit une image pour une option"""
        optionImg = pygame.image.load(img)
        return optionImg
       
    def getOptionImg(self, optionImg):
        """Permet la comparaison entre deux images"""
        return self.optionImg
        
class Shop(Menu):
    """Classe Shop héritée de menu, Shop est un menu permettant
    de changer l'apparence du vaiseau moyennant un certain 
    montant de credits"""
    
    def __init__(self):
        self.nom("Shop")
    
    def showSkin(self, image, pos_X, pos_Y):
        img = pygame.image.load(self.image, pos_X, pos_Y)
        return img
        
    def putSkin(self, selectedSkin):
        # Change l'image du vaisseau courant par l'image retournée par selectSkin
        
       














        