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
from pygame.locals import *



##### DEFINITION DES FONCTIONS #####

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
            snakes.add(Ennemi.Snake(width+(nombre*40), 0, positionChaine, deplacement, a, b))
            nombre -= 1
    elif deplacement == 1:
        while(nombre!=0):
            snakes.add(Ennemi.Snake(width+(nombre*30), 0, positionChaine, 1))
            nombre -= 1 

def creerShooters():
    if len(shooters) < 2:
        shooters.add(Ennemi.Shooter(width, height/2-20))
        
def creerAleatoires():
    if len(aleatoires) < 4:
        aleatoires.add(Ennemi.Aleatoire(width, height/2))
        
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
def creerObstacle(comptApparitionObstacle, width):
    r = random.randint(0,100)
    y = random.randint(10, height-54)
    if distance%comptApparitionObstacle==0:
        comptApparitionObstacle -= 0
        typeObstacle = random.randint(1,5)
        obstacles.add(Obstacle.obstacle(width, y,"images/ingame/asteroids/asteroid"+str(typeObstacle)+".png"))

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
    monVaisseau.chargerRecord()
    if distance > monVaisseau.record :
        monVaisseau.record=distance
        monVaisseau.enregistrerRecord(monVaisseau.record)  
    titreRec = policeTitre.render("record : "+str(monVaisseau.record)+" m",1,(254,0,0))
    screen.blit(titreRec,(120,(height/2)+60))

    
    pygame.display.flip()
    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                    
'''
'    Fonction qui gere les collisions
'''
def Collisions(monPlayer, monVaisseau, missiles, snakes, shooters, aleatoires, obstacles):
    perdu = False
#test des missiles contre snakes
    for monMissile in missiles:
        for snakeTemp in snakes:
            if snakeTemp.estTouche(monMissile):
                monPlayer.raiseScore(1)
                missiles.remove(monMissile)
                snakes.remove(snakeTemp)
    
#test des missiles contre shooters
    for monMissile in missiles:
        for shooterTemp in shooters:
            if shooterTemp.estTouche(monMissile):
                missiles.remove(monMissile)
                shooters.remove(shooterTemp)
                monPlayer.raiseScore(2)
    
#test des missiles contre aleatoires
    for monMissile in missiles:
        for aleaTemp in aleatoires:
            if aleaTemp.estTouche(monMissile):
                monPlayer.raiseScore(1)
                missiles.remove(monMissile)
                aleatoires.remove(aleaTemp)
    
#test des missiles contre obstacles
    for monMissile in missiles:
        for obsTemp in obstacles:
            if obsTemp.estTouche(monMissile):
                missiles.remove(monMissile)
    
#test du ship contre les ennemis
    for obsTemp in obstacles:
        if monVaisseau.estTouche(obsTemp):
            monVaisseau.enVie = False
            perdu = True
    
    for snakeTemp in snakes:
        if monVaisseau.estTouche(snakeTemp):
            monVaisseau.enVie = False
            perdu = True
    
    for shooterTemp in shooters:
        if monVaisseau.estTouche(shooterTemp):

            monVaisseau.enVie = False
            perdu = True
    
    for aleaTemp in aleatoires:
        if monVaisseau.estTouche(aleaTemp):
            monVaisseau.enVie = False
            perdu = True
    
    for missileShooterTemp in missilesShooter:
        if monVaisseau.estTouche(missileShooterTemp):
            monVaisseau.enVie = False
            perdu = True
    
    return perdu

'''
'    Fonction qui gere les mouvements
'''
def Mouvements(width, height, monVaisseau, missiles, snakes, shooters, aleatoires, obstacles):
    ##### MOUVEMENT JOUEUR #####
    monVaisseau.update(pygame.time.get_ticks(), height)
    ##### MOUVEMENT DES SNAKE #####
    snakes.update(pygame.time.get_ticks(), snakes, width, height)
    
    ##### MOUVEMENT DES SHOOTERS #####
    shooters.update(pygame.time.get_ticks(), monVaisseau, shooters, missilesShooter)
    
    ##### MOUVEMENT DES ALEATOIRES #####
    aleatoires.update(pygame.time.get_ticks(), aleatoires, height)
    
    ##### MOUVEMENT DES OBSTACLES #####
    obstacles.update(pygame.time.get_ticks())
    
    ##### MOUVEMENT MISSILES #####
    missiles.update(pygame.time.get_ticks(), width, missiles)
    
    missilesShooter.update(pygame.time.get_ticks(), missilesShooter)
    
'''
'    Fonction qui gere les blits
'''
def Blits(width, height, screen, distance, monVaisseau, missiles, snakes, shooters, aleatoires, obstacles):

    screen.blit(monVaisseau.image, monVaisseau.rect)
    for s in snakes.sprites(): screen.blit(s.image, s.rect)
    for s in shooters.sprites(): screen.blit(s.image, s.rect)
    for a in aleatoires.sprites(): screen.blit(a.image, a.rect)
    for o in obstacles.sprites(): screen.blit(o.image, o.rect)
    for m in missiles.sprites(): screen.blit(m.image, m.rect)
    for m in missilesShooter.sprites(): screen.blit(m.image, m.rect)
    
#blits score
    police = pygame.font.Font(None, 60)
    texte = police.render(str(distance) + " m", 1, (254, 0, 0))
    screen.blit(texte, (width - 200, height - 70))
#blits jauge chaleur
    image = pygame.image.load("images/rocket.png")
    for l in range(((monVaisseau.chaleurMax / 33) - 1) - ((monVaisseau.chaleur) / 33)):
        screen.blit(image, (10 * (l + 1), 10))
    
    if (monVaisseau.chaleur == 0):
        screen.blit(image, (10 * (l + 2), 10))

pygame.init()


        
##### PARAMETRES DE LA FENETRE #####
size = width, height = 1024,768
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

##### COMPTEURS #####
probaObstacles = 0
comptApparitionSnake = 90
comptApparitionShooter = 100
comptApparitionAleatoire = 70
comptApparitionObstacles = 60
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
monVaisseau = Ship.ship([20, 0])


##### LISTES #####
missiles = pygame.sprite.Group()
snakes = pygame.sprite.Group()
shooters = pygame.sprite.Group()
aleatoires = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
missilesShooter = pygame.sprite.Group()
''''''
creerEnnemi(comptApparitionSnake, comptApparitionShooter, comptApparitionAleatoire)
creerObstacle(comptApparitionObstacles, width)
''''''


##### MUSIQUE #####
musique = pygame.mixer.Sound("sounds/BB078.WAV")
play = 0


##### MENU COMMENCER #####
menuStartOn=True


'''################################################################## ''
''   BOUCLE DE JEU                                                    ''
''      (img par img)                                                 ''
'' ##################################################################'''
while 1:
    
    ''' VITESSE D'AFFICHAGE '''    
    clock = pygame.time.Clock()
    FRAMES_PER_SECOND = 60
    deltat = clock.tick(FRAMES_PER_SECOND)
    
    '''APPUYER SUR ENTRER POUR COMMENCER'''
    while menuStartOn:
        purisa = pygame.font.match_font('Purisa')
        policeTitre = pygame.font.Font(purisa, 40)
        titre = policeTitre.render("APPUYER SUR ENTRER",1,(50,0,200))
        screen.blit(titre,(100,100))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menuStartOn=False
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()
                
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
            # ESPACE
            elif event.key == pygame.K_SPACE:
                monVaisseau.inCharge=False
                nbShoot = (monVaisseau.charge/33)+1
                for m in range(nbShoot):
                    if(monVaisseau.chaleur+33<(monVaisseau.chaleurMax)):
                        monMissile=Shot.shotShip(monVaisseau.rect.left+40, monVaisseau.rect.top-(nbShoot*30)+(60*m)+40)
                        missiles.add(monMissile)
                        if(monVaisseau.chaleur+33<monVaisseau.chaleurMax):
                            monVaisseau.chaleur+=33
                        else:
                            monVaisseau.chaleur=monVaisseau.chaleurMax
                monVaisseau.charge=0
    ##### BACKGROUND #####
    screen.blit(background, (0,0))            
    screen.blit(bgCouche1, (width-i,i))
    screen.blit(bgCouche2, (-j,0))
    screen.blit(bgCouche2, (width-j,0))
    screen.blit(bgCouche3, (-k,0))
    screen.blit(bgCouche3, (width-k,0))
    i+=4
    j+=4
    k+=8
    if i > width:
        i=0
    if j > width:
        j=0
    if k > width:
        k=0
        

    
    Mouvements(width, height, monVaisseau, missiles, snakes, shooters, aleatoires, obstacles)

    perdu = Collisions(monPlayer, monVaisseau, missiles, snakes, shooters, aleatoires, obstacles)
       
    Blits(width, height, screen, distance, monVaisseau, missiles, snakes, shooters, aleatoires, obstacles)
    
    
    
    
    #incrementation du compteur generale de distance et creation d'ennemis et d'obstacles
    if distanceTemp != 10:
        distance += 1
    else:
        distanceTemp = 0
        distance += 1
    creerEnnemi(comptApparitionSnake, comptApparitionShooter, comptApparitionAleatoire)
    creerObstacle(comptApparitionObstacles, width)
    

    play = 1
    
    if (monVaisseau.enVie == False):    
        gameOver(monVaisseau.getPos(), screen)
                    
    pygame.display.flip()
    

