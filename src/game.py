'''
'  game.py
'    Moteur de jeu
'''

##### IMPORTS #####
import pygame
import sys
import Ennemi
import Shot
import Ship
import Player
import Obstacle
import random

def creerSnakes(nombre):
    r = random.randint(100,height-160)
    print r
    while(nombre!=0):
        snakes.append(Ennemi.Snake(width+(nombre*20),0,r))
        nombre -= 1

pygame.init()


##### PARAMETRES DE LA FENETRE #####
size = width, height = 640, 480
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)



##### IMAGES DU BACKGROUND #####
background = pygame.image.load("images/background.jpg")
bgCouche1 = pygame.image.load("images/background_couche1.png")
bgCouche2 = pygame.image.load("images/background_couche2.png")
bgCouche3 = pygame.image.load("images/background_couche3.png")
i=j=k=t=0

##### JOUEUR #####
monPlayer = Player.player('Jean')
monVaisseau = Ship.ship()
monVaisseau.setImg("images/orange_ship_1.png")


##### LISTES #####
missiles = []
snakes = []
ennemy = []
obstacles = []
''''''
#creerSnakes(int(monVaisseau.chaleurMax/33))
creerSnakes(1)
ennemy.append(Ennemi.Shooter(width, height/2-20))
''''''

##### OBSTACLES #####
#obstacles.append(Obstacle(0,"images/meteorite.png"))




'''
'' BOUCLE DE JEU
''    (img par img)
'''
while 1:
    
    ''' VITESSE D'AFFICHAGE '''    
    clock = pygame.time.Clock()
    FRAMES_PER_SECOND = 30
    deltat = clock.tick(FRAMES_PER_SECOND)
    
    ''' COMMANDES CLAVIER '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        ##### APPUI SUR TOUCHE #####
        elif event.type == pygame.KEYDOWN:
            # HAUT
            if event.key == pygame.K_UP:
                monVaisseau.monte=True
            # ESPACE
            elif event.key == pygame.K_SPACE:
                monVaisseau.inCharge=True
            # ECHAPE
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
        ##### RELACHE TOUCHE #####
        elif event.type == pygame.KEYUP:
            # HAUT
            if event.key == pygame.K_UP:
                monVaisseau.monte=False
                monVaisseau.setImg("images/orange_ship_1.png")
            # ESPACE
            elif event.key == pygame.K_SPACE:
                monVaisseau.inCharge=False
                nbShoot = (monVaisseau.charge/33)+1
                for m in range(nbShoot):
                    if(monVaisseau.chaleur+33<(monVaisseau.chaleurMax)):
                        monMissile=Shot.shot()
                        monMissile.setPos(monVaisseau.posX, monVaisseau.posY-(nbShoot*10)+(20*m))
                        missiles.append(monMissile)
                        if(monVaisseau.chaleur+33<monVaisseau.chaleurMax):
                            monVaisseau.chaleur+=33
                        else:
                            monVaisseau.chaleur=monVaisseau.chaleurMax
                monVaisseau.charge=0
    ##### BACKGROUND #####
    screen.blit(background, (0,0))            
    screen.blit(bgCouche1, (-i,0))
    screen.blit(bgCouche1, (width-i,0))
    screen.blit(bgCouche2, (-j,0))
    screen.blit(bgCouche2, (width-j,0))
    screen.blit(bgCouche3, (-k,0))
    screen.blit(bgCouche3, (width-k,0))
    i+=2
    j+=4
    k+=8
    if i > width:
        i=0
    if j > width:
        j=0
    if k > width:
        k=0
        


    ##### MOUVEMENT JOUEUR #####
    monVaisseau.bouge("images/orange_ship_2.png","images/orange_ship_2.png", height)


    ##### MOUVEMENT DES SNAKE #####
    if (len(snakes)!=0):
        for snake in snakes:
            snake.move(snakes)
            
            
    ##### MOUVEMENT DES SHOOTERS #####
    if (len(ennemy)!=0):
        for shooter in ennemy:
            shooter.move(monVaisseau, ennemy)
            shooter.tir()
            if len(shooter.missilesShooter)!=0:
                for missileShooterTemp in shooter.missilesShooter:
                    missileShooterTemp.move(shooter.missilesShooter)
      
            

    ##### MOUVEMENT MISSILES #####        
    for monMissile in missiles:
        monMissile.bouge(width, missiles)

    '''
    ''    BLITS (deplacements)
    '''        
    #blit joueur    
    screen.blit(monVaisseau.img,monVaisseau.getPos())
    
    #blits missiles
    for monMissile in missiles:
        screen.blit(monMissile.img,monMissile.getPos())
        #test des ennemis
        for snakeTemp in snakes:
            if snakeTemp.estTouche(monMissile.posX,monMissile.posY):
                monPlayer.raiseScore(1)                
                missiles.remove(monMissile)
                snakes.remove(snakeTemp)
        for shooterTemp in ennemy:
            if shooterTemp.estTouche(monMissile.posX,monMissile.posY, ennemy, monPlayer):         
                missiles.remove(monMissile)
                ennemy.remove(shooterTemp)
                
                                     
    #blits snakes
    for snakeTemp in snakes:
        screen.blit(snakeTemp.img,snakeTemp.getPos())
        
    #blits shooters
    for shooterTemp in ennemy:
        screen.blit(shooterTemp.img,shooterTemp.getPos())
        if len(shooter.missilesShooter)!=0:
                for missileShooterTemp in shooter.missilesShooter:
                    screen.blit(missileShooterTemp.img,missileShooterTemp.getPos())
        

    #blits score
    police = pygame.font.Font(None, 80)
    texte = police.render(str(monPlayer.getScore()),1,(254,0,0))
    screen.blit(texte,(550,300))
    
    #blits jauge chaleur
    img = pygame.image.load("images/rocket.png")
    for l in range(((monVaisseau.chaleurMax/33)-1)-((monVaisseau.chaleur)/33)):
        screen.blit(img,(10*(l+1),10))
    if(monVaisseau.chaleur==0):
        screen.blit(img,(10*(l+2),10))
    
    if len(snakes)==0:
        creerSnakes(int(monVaisseau.chaleurMax/33))

    pygame.display.flip()
