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




##### DEFINITION DES FCONTIONS #####

'''
'' FONCTION QUI INSTANCIE nombre DE SNAKE
'' le type de deplacement est tire aleatoirement
'' ainsi que les coefiscients pour un deplacement en droite
'''
def creerSnakes(nombre):
    positionChaine = random.randint(100,height-160)
    deplacement = random.randint(1,3)
    if deplacement == 2:
        a = random.uniform(-0.8,0.8)
        if a < 0:
            b = random.uniform(height/2,height-10)
        else:
            b = random.uniform(10,height-height/2)
        while nombre!=0:
            snakes.append(Ennemi.Snake(width+(nombre*40), 0, positionChaine, deplacement, a, b))
            nombre -= 1
    elif deplacement == 1:
        while(nombre!=0):
            snakes.append(Ennemi.Snake(width+(nombre*30), 0, positionChaine, 1))
            nombre -= 1 

def creerShooters():
    if len(ennemy) < 2:
        ennemy.append(Ennemi.Shooter(width, height/2-20))
        
def creerAleatoires():
    if len(aleatoires) < 4:
        aleatoires.append(Ennemi.Aleatoire(width, height/2))
        
'''
'' Fonction qui gere l'apparition aleatoire des ennemis
'' 
'''
def creerEnnemi(proba):
    r = random.randint(0,100)
    proba += 10
    if (r < proba):
        typeEnnemi = random.randint(1,3)
        if (typeEnnemi == 1):
            creerSnakes(int(monVaisseau.chaleurMax/33))
            proba -= 40 
        elif (typeEnnemi == 2):
            creerShooters()
            proba -= 40
        else:
            creerAleatoires()
            proba -= 30
        if proba == 100:
            proba = 0

'''
'' Apparition aleatoire des asteroides
'''
def creerObstacle(proba):
    r = random.randint(0,100)
    y = random.randint(10, height-54)
    proba += 10
    if (r < proba):
        typeObstacle = random.randint(1,5)
        obstacles.append(Obstacle.obstacle(y, "images/ingame/asteroids/asteroid"+str(typeObstacle)+".png"))
        proba = 0

pygame.init()


##### PARAMETRES DE LA FENETRE #####
size = width, height = 640, 480
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

##### COMPTEURS #####
probaEnnemis = 0
probaObstacles = 0
comptApparitionEnnemis = 0
comptApparitionObstacles = 0

##### IMAGES DU BACKGROUND #####
background = pygame.image.load("images/background.jpg")
bgCouche1 = pygame.image.load("images/background_couche1.png")
bgCouche2 = pygame.image.load("images/background_couche2.png")
bgCouche3 = pygame.image.load("images/background_couche3.png")
i=j=k=t=0

##### JOUEUR #####
monPlayer = Player.player('Jean')
monVaisseau = Ship.ship()
monVaisseau.setImg("images/orange_ship_small_1.png")


##### LISTES #####
missiles = []
snakes = []
ennemy = []
aleatoires = []
obstacles = []
missilesShooter = []
''''''
creerEnnemi(probaEnnemis)
creerObstacle(probaObstacles)
''''''

##### OBSTACLES #####
#obstacles.append(Obstacle(0,"images/meteorite.png"))

##### MUSIQUE #####
musique = pygame.mixer.Sound("sounds/BB078.WAV")
play = 0

'''
'' BOUCLE DE JEU
''    (img par img)
'''
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
                monVaisseau.setImg("images/orange_ship_small_1.png")
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
    monVaisseau.bouge("images/orange_ship_small_1.png","images/orange_ship_small_2.png", height)

    ##### MOUVEMENT DES SNAKE #####
    for snake in snakes:
        snake.move(snakes, width, height)
                  
    ##### MOUVEMENT DES SHOOTERS #####
    for shooter in ennemy:
        shooter.move(monVaisseau, ennemy)
        shooter.tir(missilesShooter)
                 
    ##### MOUVEMENT DES ALEATOIRES #####
    for aleatoire in aleatoires:
        aleatoire.move(aleatoires, height)  
        
    ##### MOUVEMENT DES OBSTACLES #####
    for obstacle in obstacles:
        obstacle.move()
        

    ##### MOUVEMENT MISSILES #####        
    for monMissile in missiles:
        monMissile.bouge(width, missiles)
    for missileShooterTemp in missilesShooter:
        missileShooterTemp.move(missilesShooter)

    '''
    ''    BLITS (deplacements)
    '''        
    #blit joueur    
    screen.blit(monVaisseau.img,monVaisseau.getPos())
    
    #tests de collisions des ennemis avec les missiles
    for monMissile in missiles:
        screen.blit(monMissile.img,monMissile.getPos())
        #test des snakes
        for snakeTemp in snakes:
            if snakeTemp.estTouche(monMissile.posX,monMissile.posY):
                monPlayer.raiseScore(1)                
                missiles.remove(monMissile)
                snakes.remove(snakeTemp)
    for monMissile in missiles:
        screen.blit(monMissile.img,monMissile.getPos())
        #test des shooters    
        for shooterTemp in ennemy:
            if shooterTemp.estTouche(monMissile.posX,monMissile.posY, ennemy): 
                missiles.remove(monMissile)
                ennemy.remove(shooterTemp)
                monPlayer.raiseScore(2)
                
    for monMissile in missiles:
        screen.blit(monMissile.img,monMissile.getPos())
        #test des aleatoires 
        for aleaTemp in aleatoires:
            if aleaTemp.estTouche(monMissile.posX,monMissile.posY, aleatoires):
                monPlayer.raiseScore(1)          
                missiles.remove(monMissile)
                aleatoires.remove(aleaTemp)
    
    #blits missiles
    for monMissile in missiles:
        screen.blit(monMissile.img,monMissile.getPos())           
                                     
    #blits snakes
    for snakeTemp in snakes:
        screen.blit(snakeTemp.img,snakeTemp.getPos())
        
    #blits shooters
    for shooterTemp in ennemy:
        screen.blit(shooterTemp.img,shooterTemp.getPos())
                
    #blits missiles shooter
    for missileShooterTemp in missilesShooter:
        screen.blit(missileShooterTemp.img,missileShooterTemp.getPos()) 
           
    #blits aleatoires
    for aleaTemp in aleatoires:
        screen.blit(aleaTemp.img,aleaTemp.getPos())
      
    #blits obstacles
    for obsTemp in obstacles:
        screen.blit(obsTemp.img,obsTemp.getPos())  
    #blits score
    police = pygame.font.Font(None, 80)
    texte = police.render(str(monPlayer.getScore()),1,(254,0,0))
    screen.blit(texte,(width-70,height-70))
    
    #blits jauge chaleur
    img = pygame.image.load("images/rocket.png")
    for l in range(((monVaisseau.chaleurMax/33)-1)-((monVaisseau.chaleur)/33)):
        screen.blit(img,(10*(l+1),10))
    if(monVaisseau.chaleur==0):
        screen.blit(img,(10*(l+2),10))
    
    #apparition aleatoire d'ennemis
    if (comptApparitionEnnemis%7 == 0):
        creerEnnemi(probaEnnemis)
        comptApparitionEnnemis = 0
    comptApparitionEnnemis += 1
    
    
    
    #apparition aleatoire d'obstacles
    if (comptApparitionObstacles%10 == 0):
        creerObstacle(probaObstacles)
        comptApparitionObstacles = 0
    comptApparitionObstacles += 1
    
    ''' PTITE ZIK '''
    if play == 0:
        musique.play()
        play = 1
    
    pygame.display.flip()
