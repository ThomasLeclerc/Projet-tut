import Bouton
import Menu

''' classe EcranAccueil
    herite de la classe Menu
'''
class EcranAccueil(Menu.Menu):    
    
    def __init__(self,filename):
        Menu.Menu.__init__(self, filename)
        self.addButton(Bouton.BoutonStartGame("images/menu/menu/titles/play.png",0, 270, True))
        self.addButton(Bouton.BoutonOption("images/menu/menu/titles/option.png",0, 340))
        #self.addButton(Bouton.BoutonRecord("images/menu/menu/titles/ranking.png",0, 410))
        self.addButton(Bouton.BoutonCredits("images/menu/menu/titles/credits.png",0, 415))
        self.addButton(Bouton.BoutonQuit("images/menu/menu/titles/quit.png",0, 485))