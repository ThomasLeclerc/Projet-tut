import pygame
import sys



class Menu:
    
    def __init__(self,filename):
        self.boutons = []
        self.setBgImage(filename)
        self.idSelectedButton=0

    def setBgImage(self, filename):
        self.image=pygame.image.load(filename)

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
                            sys.exit()
                    self.boutons[self.idSelectedButton].setSelected(True)
            self.blits(screen)
            pygame.display.update()
