import Menu
import Player2
import Bouton

##### LISTES DE BOUTONS #####


player = Player2.Player.loadDatas()
'''Affichage du menu d'accueil'''
ecranAccueil = Menu.Menu("images/menu/menu.jpg")
ecranAccueil.addButton(Bouton.BoutonStartGame("images/menu/menu_principal/titles/play.png",0, 270, True))
ecranAccueil.addButton(Bouton.BoutonOption("images/menu/menu_principal/titles/option.png",0, 340, player))
ecranAccueil.addButton(Bouton.BoutonCredits("images/menu/menu_principal/titles/credits.png",0, 415))
ecranAccueil.addButton(Bouton.BoutonQuit("images/menu/menu_principal/titles/quit.png",0, 485))
ecranAccueil.afficher()