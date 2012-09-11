'''
'  game.py
'    Moteur de jeu
'''

##### IMPORTS #####
import pygame
import sys
import Obstacle
import Shot
import Ship
import Player


pygame.init()


##### PARAMETRES DE LA FENETRE #####
size = width, height = 640, 400
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)



##### IMAGES DU BACKGROUND #####
background = pygame.image.load("images/night.jpg")
asteroid = pygame.image.load("images/asteroid.png")
stones = pygame.image.load("images/stones.png")
i=j=k=t=0

##### JOUEUR #####
monPlayer = Player.player('Jean')
monVaisseau = Ship.ship()
monVaisseau.setImg("images/pinkship.png")




##### LISTES #####
missiles = []
obstacles = []
ennemy = []



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
                if((monVaisseau.chaleur+33)<(monVaisseau.chaleurMax)):
                    monMissile=Shot.shot()
                    monMissile.setPos(monVaisseau.posX, monVaisseau.posY)
                    missiles.append(monMissile)
                    if(monVaisseau.chaleur+33<100):
                        monVaisseau.chaleur+=33
                    else:
                        monVaisseau.chaleur=100
            # ECHAPE
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
        ##### RELACHE TOUCHE #####
        elif event.type == pygame.KEYUP:
            # HAUT
            if event.key == pygame.K_UP:
                monVaisseau.monte=False
                monVaisseau.setImg("images/pinkship.png")

    ##### BACKGROUND #####            
    screen.blit(background, (-i,0))
    screen.blit(background, (width-i,0))
    screen.blit(asteroid, (-j,0))
    screen.blit(asteroid, (width-j,0))
    screen.blit(stones, (-k,0))
    screen.blit(stones, (width-k,0))
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
    monVaisseau.bouge("images/pinkship0.png","images/pinkship1.png", height)


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
        #test des obstacles
        for testObstacle in obstacles:
            if testObstacle.estTouche(monMissile.posX,monMissile.posY):
                monPlayer.raiseScore(1)                
                missiles.remove(monMissile)
                obstacles.remove(testObstacle)
                #ob = Obstacle.obstacle(width+40,)
                #obstacles.append(ob)
                                     
    #blits obstacles
    for monObstacle in obstacles:
        screen.blit(monObstacle.img,monObstacle.getPos())

    #blits score
    police = pygame.font.Font(None, 80)
    texte = police.render(str(monPlayer.getScore()),1,(254,0,0))
    screen.blit(texte,(550,300))
    
    #blits jauge chaleur
    img = pygame.image.load("images/rocket.png")
    for l in range(2-((monVaisseau.chaleur)/33)):
        screen.blit(img,(10*(l+1),10))
    if(monVaisseau.chaleur==0):
        screen.blit(img,(10*(l+2),10))


    pygame.display.flip()