import Bouton
import Menu


class EcranAccueil(Menu.Menu):    
    
    def __init__(self,filename):
        Menu.Menu.__init__(self, filename)
        self.addButton(Bouton.BoutonStartGame("images/menu/menu/titles/play.png","images/menu/menu/titles/playAlt.png",True))
