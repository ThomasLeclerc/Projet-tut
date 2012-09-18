#import Menu
import pygame
import sys
import time



##### PARAMETRES DE LA FENETRE #####
size = width, height = 1024,780 
screen = pygame.display.set_mode(size)

##### IMAGES DU MENU #####
img0 = pygame.image.load("images/play_static.png")
img1 = pygame.image.load("images/play_focus1.png")
img2 = pygame.image.load("images/play_focus2.png")
img3 = pygame.image.load("images/play_focus3.png")

posX = width/2 - 160
posY1 = 100
posY2 = 250
posY3 = 400
pas = 150

posCurseur = posY1

screen.blit(img0, (posX,posY1))            
screen.blit(img0, (posX,posY2))
screen.blit(img0, (posX,posY3))

switch = 0

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
                    posCurseur = posCurseur - pas;
                    
            # BAS
            if event.key == pygame.K_DOWN:
                if posCurseur < posY3:
                    posCurseur = posCurseur + pas;
                    
            # ENTREE
            elif event.key == pygame.K_RETURN:
                print(posCurseur);
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
    
    
    pygame.display.flip()
    
