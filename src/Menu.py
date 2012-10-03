import pygame
import sys
import Bouton


class Menu:
    
    ''' Constructeur de Menu
        prend le nom du fichier image en parametre
    '''
    def __init__(self,filename, player=None):
        self.boutons = []
        self.setBgImage(filename)
        self.idSelectedButton=0
        self.player = player

    def setBgImage(self, filename):
        self.image=pygame.image.load(filename)
        pygame.transform.scale(pygame.image.load(filename), (1024, 768))

    ''' parcours la liste de bouton du menu
        et retourne le bouton selectionne '''
    def selectedButton(self):
        for bouton in self.boutons:
            if bouton.isSelected():
                return bouton
            
    def blits(self, screen):
        screen.blit(self.image,(0,0))
        for bouton in self.boutons:
            if bouton.isSelected:
                screen.blit(bouton.image,bouton.rect)
        pygame.display.update()
    
    def addButton(self,bouton):
        self.boutons.append(bouton)

    def whenEscape(self):
        sys.exit()
    ''' affiche le menu '''
    def afficher(self):
        ##### PARAMETRES DE LA FENETRE #####
        size = 1024,768
        screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        while 1:
            ''' COMMANDES CLAVIER '''
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                ##### APPUI SUR TOUCHE #####
                elif event.type == pygame.KEYDOWN:
                    # HAUT
                    if event.key == pygame.K_UP:
                        if self.idSelectedButton == 0:
                            self.boutons[self.idSelectedButton].setSelected(False)
                            self.idSelectedButton = len(self.boutons)-1
                        else:
                            self.boutons[self.idSelectedButton].setSelected(False)
                            self.idSelectedButton -= 1
                    # BAS
                    elif event.key == pygame.K_DOWN:
                        if self.idSelectedButton == len(self.boutons)-1:
                            self.boutons[self.idSelectedButton].setSelected(False)
                            self.idSelectedButton = 0
                        else:
                            self.boutons[self.idSelectedButton].setSelected(False)
                            self.idSelectedButton += 1
                    # ENTRER
                    elif event.key == pygame.K_RETURN:
                        self.boutons[self.idSelectedButton].action()
                    elif event.key == pygame.K_ESCAPE:
                            self.whenEscape()
                    self.boutons[self.idSelectedButton].setSelected(True)
            self.blits(screen)
            pygame.display.update()
            
class menuOption(Menu):
    def __init__(self, filename, player):
        Menu.__init__(self, filename)
        self.player = player
    def blits(self, screen):
        screen.blit(self.image,(0,0))
        if self.boutons[0].isSelected:
            if self.player.sound:
                screen.blit(self.boutons[0].image, self.boutons[0].rect)
            else:
                screen.blit(self.boutons[0].imageNon, (self.boutons[0].rect.left+100,self.boutons[0].rect.top))
        elif self.boutons[1].isSelected:
            if self.player.music:
                screen.blit(self.boutons[1].image, self.boutons[1].rect)
            else:
                screen.blit(self.boutons[1].imageNon, (self.boutons[1].rect.left+100,self.boutons[1].rect.top))  
        elif self.boutons[2].isSelected:
            screen.blit(self.boutons[2].image, self.boutons[2].rect)
        elif self.boutons[3].isSelected:
            screen.blit(self.boutons[3].image, self.boutons[3].rect)       
        pygame.display.update()
        
    def whenEscape(self):
        ecranAccueil = Menu("images/menu/menu.jpg")
        ecranAccueil.addButton(Bouton.BoutonStartGame("images/menu/menu_principal/titles/play.png",0, 270, True))
        ecranAccueil.addButton(Bouton.BoutonOption("images/menu/menu_principal/titles/option.png",0, 340, self.player))
        ecranAccueil.addButton(Bouton.BoutonCredits("images/menu/menu_principal/titles/credits.png",0, 415))
        ecranAccueil.addButton(Bouton.BoutonQuit("images/menu/menu_principal/titles/quit.png",0, 485))
        ecranAccueil.afficher()
