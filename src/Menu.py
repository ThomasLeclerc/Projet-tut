import pygame
import sys
import Bouton
import Article

class Menu:
    
    ''' Constructeur de Menu
        prend le nom du fichier image en parametre
    '''
    def __init__(self,filename, player):
        self.boutons = []
        self.player = player
        self.setBgImage(filename)
        self.idSelectedButton=0
        

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
        Menu.__init__(self, filename, player)
    def blits(self, screen):
        screen.blit(self.image,(0,0))
        if self.boutons[0].isSelected:
            if self.player.sound:
                screen.blit(self.boutons[0].image, self.boutons[0].rect)
            else:
                screen.blit(self.boutons[0].imageNon, (self.boutons[0].rect.left+93,self.boutons[0].rect.top))
        elif self.boutons[1].isSelected:
            if self.player.musicOn:
                screen.blit(self.boutons[1].image, self.boutons[1].rect)
            else:
                screen.blit(self.boutons[1].imageNon, (self.boutons[1].rect.left+93,self.boutons[1].rect.top))  
        elif self.boutons[2].isSelected:
            screen.blit(self.boutons[2].image, self.boutons[2].rect)
        elif self.boutons[3].isSelected:
            screen.blit(self.boutons[3].image, self.boutons[3].rect)
        elif self.boutons[4].isSelected:
            screen.blit(self.boutons[4].image, self.boutons[4].rect)         
        pygame.display.update()
        
    def whenEscape(self):
        ecranAccueil = Menu("images/menu/menu.jpg", self.player)
        ecranAccueil.addButton(Bouton.BoutonStartGame("images/menu/menu_principal/titles/play.png",0, 270, self.player, True))
        ecranAccueil.addButton(Bouton.BoutonOption("images/menu/menu_principal/titles/option.png",0, 340, self.player))
        ecranAccueil.addButton(Bouton.BoutonCredits("images/menu/menu_principal/titles/credits.png",0, 415))
        ecranAccueil.addButton(Bouton.BoutonQuit("images/menu/menu_principal/titles/quit.png",0, 485))
        ecranAccueil.afficher()
        
class menuPause(Menu):
    def __init__(self, filename, player):
        Menu.__init__(self, filename, player)
    def afficher(self, screen, partie):
        ##### PARAMETRES DE LA FENETRE #####
        repriseOn = False
        while repriseOn == False:
            ''' COMMANDES CLAVIER '''
            for event in pygame.event.get():
                ##### APPUI SUR TOUCHE #####
                if event.type == pygame.KEYDOWN:
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
                        if self.idSelectedButton == 0:
                            repriseOn = self.boutons[self.idSelectedButton].action()
                        elif self.idSelectedButton == 1:
                            partie.music.stop() 
                            self.boutons[self.idSelectedButton].action()
                    elif event.key == pygame.K_ESCAPE:
                            repriseOn = True
                    self.boutons[self.idSelectedButton].setSelected(True)
            self.blits(screen)
            pygame.display.update()
    
class menuShop(Menu):
    def __init__(self, filename, player):
        Menu.__init__(self, filename, player)
     
    def setBgImage(self, filename):
        self.image=pygame.image.load(filename)
        police = pygame.font.Font(None, 43)
        texte = police.render("Your money : "+str(self.player.money), 1, (210, 210, 1))
        self.image.blit(texte, (370, 100))
        
    def blits(self, screen):
        screen.blit(self.image,(0,0))
        for bouton in self.boutons:
            if (bouton.rect.top+140 > 160)and(bouton.rect.top < 710):
                if bouton.isSelected:
                    if bouton.isAvailable == False:
                        screen.blit(bouton.image2, bouton.rect)
                    else:
                        if bouton.isSold:
                            screen.blit(bouton.image3,bouton.rect)
                        else:
                            screen.blit(bouton.image1,bouton.rect)
                else:
                    if bouton.isSold:
                        screen.blit(bouton.image5,bouton.rect)
                    else:
                        screen.blit(bouton.image4,bouton.rect)
        pygame.display.update()
           
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
                        if self.idSelectedButton != 0:
                            self.boutons[self.idSelectedButton].setSelected(False)
                            self.idSelectedButton -= 1
                            if self.idSelectedButton < 2:
                                if self.boutons[0].rect.top+140 < 170:
                                    for bouton in self.boutons:
                                        bouton.rect.top += 140
                    # BAS
                    elif event.key == pygame.K_DOWN:
                        if self.idSelectedButton != len(self.boutons)-1:
                            self.boutons[self.idSelectedButton].setSelected(False)
                            self.idSelectedButton += 1
                            if self.idSelectedButton > 3:
                                if self.boutons[len(self.boutons)-1].rect.top > 710:
                                    for bouton in self.boutons:
                                        bouton.rect.top -= 140
                    # ENTRER
                    elif event.key == pygame.K_RETURN:
                        self.boutons[self.idSelectedButton].action()
                    elif event.key == pygame.K_ESCAPE:
                            self.whenEscape()
                    self.boutons[self.idSelectedButton].setSelected(True)
            self.blits(screen)
            pygame.display.update()
        
    def whenEscape(self):
        ecranOption = menuOption("images/menu/menu_option/background_menu_option.jpg", self.player)
        ecranOption.addButton(Bouton.BoutonSound("images/menu/menu_option/on.png", 530, 255, self.player, True))
        ecranOption.addButton(Bouton.BoutonMusic("images/menu/menu_option/on.png", 530, 325, self.player))
        ecranOption.addButton(Bouton.BoutonReinitialiser("images/menu/menu_option/reset_profile.png",344 , 388, self.player))
        ecranOption.addButton(Bouton.BoutonShop("images/menu/menu_option/shop.png",414 , 455, self.player))
        ecranOption.addButton(Bouton.BoutonMenuPrincipal("images/menu/menu_option/back.png",460 , 543, self.player))
        ecranOption.afficher()
    
