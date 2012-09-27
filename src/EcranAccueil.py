#import Menu
import pygame
import sys
import time

class EcranAccueil:    
    
    ##### PARAMETRES DE LA FENETRE #####
    size = width, height = 1024,780 
    screen = pygame.display.set_mode(size)
    
    ##### IMAGES DU MENU ET LEUR POSITIONS #####
    img0 = pygame.image.load("images/play_static.png")
    img1 = pygame.image.load("images/play_focus1.png")
    img2 = pygame.image.load("images/play_focus2.png")
    img3 = pygame.image.load("images/play_focus3.png")
    
    posX = width/2 - 160
    posY1 = 100
    posY2 = 250
    posY3 = 400
    
    ##### IMAGES DU STORE #####
    bgShop = pygame.image.load("images/background.jpg")
    
    ##### IMAGES DE L'ECRAN QUITTER ET LEUR POISITIONS #####
    imgQuitTxt  = pygame.image.load("images/lQuit.png")
    imgYes      = pygame.image.load("images/btnYes.png")
    imgNo       = pygame.image.load("images/btnNo.png")
    imgYes1     = pygame.image.load("images/btnYes_focus.png")
    imgNo1      = pygame.image.load("images/btnNo_focus.png")
    
    posY  = 150 
    posX1 = 250
    posX2 = 400
    
    posCurseur = posY1
    pas = 150
    
    
    screen.blit(img0, (posX,posY1))            
    screen.blit(img0, (posX,posY2))
    screen.blit(img0, (posX,posY3))
    
    switch = 0
    
    """ 
    ECRAN COURANT :
    0 = Menu principal
    1 = Play
    2 = Shop
    """
    ecranCourant = 0
    
    
    ##### ACCES A LA VARIBLE DE POSITION DU CURSEUR #####
    def getPositionCurseur():
        return posCurseur
    
    def setPositionCurseur(pos):
        posCurseur = pos
    
    while 1:
        
        
        ''' VITESSE D'AFFICHAGE '''
        clock = pygame.time.Clock()
        FRAMES_PER_SECOND = 50
        deltat = clock.tick(FRAMES_PER_SECOND)
    
        ''' COMMANDES CLAVIER '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            ##### APPUI SUR TOUCHE #####
            elif event.type == pygame.KEYDOWN:
                # HAUT
                if event.key == pygame.K_UP:
                    
                    if posCurseur > posY1:
                        posCurseur = posCurseur - pas
                    
                # BAS
                if event.key == pygame.K_DOWN:
     
                    if posCurseur < posY3:
                        posCurseur = posCurseur + pas;
                
                # GAUCHE
                if event.key == pygame.K_LEFT:
                    
                    if ecranCourant == 3:
                        if posCurseur < posX1:
                            posCurseur = posCurseur + pas;
                # DROITE
                if event.key == pygame.K_RIGHT:
                    
                    if ecranCourant == 3:
                        if posCurseur < posX2:
                            posCurseur = posCurseur + pas;
                        
                # ENTREE
                elif event.key == pygame.K_RETURN:
                    
                    if posCurseur == posY1:
                        ecranCourant = 1
                        
                    elif posCurseur == posY2:
                        ecranCourant = 2
                     
                    elif posCurseur == posY3:
                        ecranCourant = 3
                    
                    print(ecranCourant)
                    
                # ECHAP
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()
            """
            ##### TOUCHE RELACHEE #####
            elif event.type == pygame.KEYUP:
                # HAUT
                if event.key == pygame.K_UP:
                    print()
                # ESPACE
                elif event.key == pygame.K_SPACE:
                    print()
            """     
        
        
        ##### IMAGES REDESSINEES #####
        
        if ecranCourant == 0 or ecranCourant == 1:    
            
            screen.blit(img0, (posX,posY1))            
            screen.blit(img0, (posX,posY2))
            screen.blit(img0, (posX,posY3))
        
            """
            Pour gerer le temps de rafraichissement d'une image
            sans avoir a modifier le parametre FPS, j'ai choisi
            la methode time.sleep(float seconds) du module time
            """
            if switch == 0:
                screen.blit(img1, (posX,posCurseur))
                time.sleep(0.05)
                switch = 1
            elif switch == 1:
                screen.blit(img2, (posX,posCurseur))
                time.sleep(0.05)
                switch = 2
            elif switch == 2:
                screen.blit(img3, (posX,posCurseur))
                time.sleep(0.05)
                switch = 0    
            
        elif ecranCourant == 2:
            screen.blit(bgShop, (0,0))
        
        elif ecranCourant == 3:
            
            setPositionCurseur(posX1)
            
            screen.blit(bgShop, (0,0))
            screen.blit(imgQuitTxt, (width/2-200,posY))
            screen.blit(imgNo, (posX1,posY1))
            screen.blit(imgYes,(posX2,posY1))
            
            screen.blit(imgNo1, (posX1,getPositionCurseur()))
            screen.blit(imgYes1, (posX2,getPositionCurseur()))
            
        pygame.display.flip()
    
