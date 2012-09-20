#import Menu
import Curseur
import pygame
import sys

pygame.init()

##### PARAMETRES DE LA FENETRE #####
size = width, height = 1024,780 
screen = pygame.display.set_mode(size)

##### IMAGES #####
imgQuitTxt  = pygame.image.load("images/lQuit.png")
imgYes      = pygame.image.load("images/btnYes.png")
imgNo       = pygame.image.load("images/btnNo.png")
imgYes1     = pygame.image.load("images/btnYes_focus.png")
imgNo1      = pygame.image.load("images/btnNo_focus.png")

##### POSITIONS ######
posX = width/2 - 250
posY  = 100
posY1 = 300
posX1 = width/2 - 200
posX2 = width/2 + 100


##### CURSEUR #####
pas = posX2 - posX1
curseurStore = Curseur.curseur(posX1, pas)

##### SON #####
sonExplosion = pygame.mixer.Sound("sounds/cliclic.WAV")




screen.blit(imgQuitTxt, (posX,posY))            
screen.blit(imgNo, (posX1,posY1))
screen.blit(imgYes, (posX2,posY1))


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
            # GAUCHE
            if event.key == pygame.K_LEFT:
                
                    if curseurStore.getPosition() > posX1:
                        curseurStore.setPosition(curseurStore.getPosition() - pas)            
            # DROITE
            if event.key == pygame.K_RIGHT:
                   
                    if curseurStore.getPosition() < posX2:
                        curseurStore.setPosition(curseurStore.getPosition() + pas)
            # ENTREE
            elif event.key == pygame.K_RETURN:

                if curseurStore.estPositionne(posX1):
                    sonExplosion.play()
                        
                elif curseurStore.estPositionne(posX2):
                    sys.exit()     
            # ECHAP
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
                               
    screen.blit(imgQuitTxt, (posX,posY))            
    screen.blit(imgNo, (posX1,posY1))
    screen.blit(imgYes, (posX2,posY1))
    
    if curseurStore.estPositionne(posX1): 
        screen.blit(imgNo1, (posX1,posY1))
    if curseurStore.estPositionne(posX2):
        screen.blit(imgYes1, (posX2,posY1))
             
    pygame.display.flip()                
                
                
                