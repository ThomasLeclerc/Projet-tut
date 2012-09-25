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
from time import sleep




##### DEFINITION DES FCONTIONS #####

'''
'' FONCTION QUI INSTANCIE nombre DE SNAKE
'' le type de deplacement est tire aleatoirement
'' ainsi que les coefiscients pour un deplacement en droite
'''
def creerSnakes(nombre):
    positionChaine = random.randint(100,height-180)
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
    if len(shooters) < 2:
        shooters.append(Ennemi.Shooter(width, height/2-20))
        
def creerAleatoires():
    if len(aleatoires) < 4:
        aleatoires.append(Ennemi.Aleatoire(width, height/2))
        
'''
'' Fonction qui gere l'apparition aleatoire des ennemis
'' 
'''
def creerEnnemi(compApparitionSnake, compApparitionShooter, compApparitionAleatoire):
    if distance%compApparitionSnake == 0:
        compApparitionSnake -= 1
        creerSnakes(int(monVaisseau.chaleurMax/60))
    if distance%compApparitionShooter == 0:
        compApparitionShooter -= 1
        creerShooters()
    if distance%compApparitionAleatoire == 0:
        compApparitionAleatoire -= 1
        creerAleatoires()
'''
'' Apparition aleatoire des asteroides
'''
def creerObstacle(comptApparitionObstacle):
    r = random.randint(0,100)
    y = random.randint(10, height-54)
    if distance%comptApparitionObstacle==0:
        comptApparitionObstacle -= 0
        typeObstacle = random.randint(1,5)
        obstacles.append(Obstacle.obstacle(y, "images/ingame/asteroids/asteroid"+str(typeObstacle)+".png"))

def gameOver((x, y), screen):
    for g in range(1,9):
        screen.blit(background, (0,0))             
        screen.blit(pygame.image.load("images/ingame/explosion/explosion"+str(g)+".png"), (x,y))
        pygame.display.flip()
        sleep(0.1)
    
    #blit GAME OVER    
    policeTitre = pygame.font.Font(None, 120)
    titre = policeTitre.render("GAME OVER",1,(254,0,0))
    screen.blit(titre,(100,100)) 
    
    #blit disctance parcourue
    policeTitre = pygame.font.Font(None, 80)
    titre = policeTitre.render("distance : "+str(distance)+" m",1,(254,0,0))
    screen.blit(titre,(120,height/2))  
    
    pygame.display.flip()
    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

pygame.init()


        
##### PARAMETRES DE LA FENETRE #####
size = width, height = 640, 480
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

##### COMPTEURS #####
probaObstacles = 0
comptApparitionSnake = 90
comptApparitionShooter = 100
comptApparitionAleatoire = 70
comptApparitionObstacles = 80
distanceTemp = 0
distance = 2
perdu = False

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
shooters = []
aleatoires = []
obstacles = []
missilesShooter = []
''''''
creerEnnemi(comptApparitionSnake, comptApparitionShooter, comptApparitionAleatoire)
creerObstacle(comptApparitionObstacles)
''''''


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
    FRAMES_PER_SECOND = 40
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
                        monMissile=Shot.shotShip()
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
    for shooter in shooters:
        shooter.move(monVaisseau, shooters)
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



##### COLLISIONS ####
    #test des missiles contre snakes
    for monMissile in missiles:
        for snakeTemp in snakes:
            if snakeTemp.estTouche(monMissile.posX,monMissile.posY):
                monPlayer.raiseScore(1)                
                missiles.remove(monMissile)
                snakes.remove(snakeTemp)
                
    #test des missiles contre shooters 
    for monMissile in missiles:   
        for shooterTemp in shooters:
            if shooterTemp.estTouche(monMissile.posX,monMissile.posY, shooters): 
                missiles.remove(monMissile)
                shooters.remove(shooterTemp)
                monPlayer.raiseScore(2)
    
    #test des missiles contre aleatoires             
    for monMissile in missiles:
        for aleaTemp in aleatoires:
            if aleaTemp.estTouche(monMissile.posX,monMissile.posY, aleatoires):
                monPlayer.raiseScore(1)          
                missiles.remove(monMissile)
                aleatoires.remove(aleaTemp)

    #test des missiles contre obstacles                
    for monMissile in missiles:
        for obsTemp in obstacles:
            if obsTemp.estTouche(monMissile.posX,monMissile.posY):        
                missiles.remove(monMissile)
                
    #test du ship contre les ennemis
    for obsTemp in obstacles:
        if monVaisseau.estTouche(obsTemp.getPos(), obsTemp.getDimensions()):
            monVaisseau.enVie = False
            perdu = True
    for snakeTemp in snakes:
        if monVaisseau.estTouche(snakeTemp.getPos(), snakeTemp.getDimensions()):
            monVaisseau.enVie = False
            perdu = True
    for shooterTemp in shooters:
        if monVaisseau.estTouche(shooterTemp.getPos(), shooterTemp.getDimensions()):
            monVaisseau.enVie = False
            perdu = True
    for aleaTemp in aleatoires:
        if monVaisseau.estTouche(aleaTemp.getPos(), aleaTemp.getDimensions()):
            monVaisseau.enVie = False
            perdu = True
    for missileShooterTemp in missilesShooter:
        if monVaisseau.estTouche(missileShooterTemp.getPos(), missileShooterTemp.getDimensions()):
            monVaisseau.enVie = False
            perdu = True
    if perdu:
        break
    '''
    ''    BLITS (deplacements)
    '''        
    #blit joueur    
    screen.blit(monVaisseau.img,monVaisseau.getPos())
    
    #jauge tir
    pygame.draw.rect(screen,(255,0,0),(1,1,monVaisseau.chaleurMax+3,10),1)
    if (monVaisseau.inCharge):
        pygame.draw.rect(screen,(255,0,0),(4,4,monVaisseau.charge,7))
    
    
    #blits missiles
    for monMissile in missiles:
        screen.blit(monMissile.img ,monMissile.getPos())           
                                     
    #blits snakes
    for snakeTemp in snakes:
        screen.blit(snakeTemp.img,snakeTemp.getPos())
        
    #blits shooters
    for shooterTemp in shooters:
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
    police = pygame.font.Font(None, 60)
    texte = police.render(str(distance)+" m",1,(254,0,0))
    screen.blit(texte,(width-200,height-70))
    
    #blits jauge chaleur
    img = pygame.image.load("images/rocket.png")
    for l in range(((monVaisseau.chaleurMax/33)-1)-((monVaisseau.chaleur)/33)):
        screen.blit(img,(10*(l+1),10))
    if(monVaisseau.chaleur==0):
        screen.blit(img,(10*(l+2),10))
    
    
    
    
    #incrementation du compteur generale de distance et creation d'ennemis et d'obstacles
    if distanceTemp != 10:
        distance += 1
    else:
        distanceTemp = 0
        distance += 1
    creerEnnemi(comptApparitionSnake, comptApparitionShooter, comptApparitionAleatoire)
    creerObstacle(comptApparitionObstacles)
    
    ''' PTITE ZIK '''
    '''
    if play == 0:
        musique.play()
        play = 1'''
    
    pygame.display.flip()
    
if (monVaisseau.enVie == False):    
    gameOver(monVaisseau.getPos(), screen)