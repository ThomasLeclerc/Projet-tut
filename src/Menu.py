import pygame
import Curseur

"""
Un Menu est defini par :
- un identifiant determinant le type du menu
- un titre pour informer au joueur dans quel menu il se situe
- un curseur permettant de naviguer et d'interagir avec le menu
"""
class menu:
    idMenu = None
    titre = ''
    curseur = Curseur.curseur(0,0)
    
    ''' Instancie un nouveau menu dont le titre correspond au fichier image du meme nom '''
    def __init__(self, idMenu, titre, curseur):
        
        self.idMenu = idMenu
        self.titre  = titre
        self.curseur = curseur

    ''' Recupere le fichier image du titre du menu '''    
    def getTitre(self):
        return pygame.image.load("images/"+ self.titre +".png")
    
    
    ''' Retourne l'identifiant du menu '''
    ### Utile pour les structures conditionnelles/naviguer d'un menu a l'autre
    def getIdentifiant(self):
        return self.idMenu
    
    ''' Ajoute une nouvelle option dans le menu '''   
    def ajoutOption(self, img):
        return pygame.image.load("images/"+img)
        

class menuStartGame(menu):
    def __init__(self):
        self.idMenu=1
        self.titre='Start Menu'
        self.curseur=Curseur.curseur(0,0) 
        
    def entrerPourJouer(self):
        policeTitre = pygame.font.Font(None, 120)
        titre = policeTitre.render("APPUYER SUR ENTRER",1,(254,0,0))
        return titre
