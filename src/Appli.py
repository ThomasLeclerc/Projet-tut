import Menu
import Player2
import Bouton

##### LISTES DE BOUTONS #####


player = Player2.player.loadDatas()
'''Affichage du menu d'accueil'''
ecranAccueil = Menu.Menu("images/menu/menu.jpg")
ecranAccueil.addButton(Bouton.BoutonStartGame("images/menu/menu/titles/play.png",0, 270, True))
ecranAccueil.addButton(Bouton.BoutonOption("images/menu/menu/titles/option.png",0, 340))
ecranAccueil.addButton(Bouton.BoutonCredits("images/menu/menu/titles/credits.png",0, 415))
ecranAccueil.addButton(Bouton.BoutonQuit("images/menu/menu/titles/quit.png",0, 485))
ecranAccueil.afficher()