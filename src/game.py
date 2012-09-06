import pygame
import sys
import Obstacle
import Shot
import Ship
import Player
pygame.init()



size = width, height = 640, 400
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FRAMES_PER_SECOND = 30
deltat = clock.tick(FRAMES_PER_SECOND)


background = pygame.image.load("night.jpg")
asteroid = pygame.image.load("asteroid.png")
stones = pygame.image.load("stones.png")
i=j=k=t=0


monPlayer = Player.player('Jean')
monVaisseau = Ship.ship()
#monVaisseau.setImg("ship.png")
#monVaisseau.setImg("chasseur.png")
monVaisseau.setImg("pinkship.png")

monJet = Ship.ship()
monJet.setImg("jetpack.png")

ob1 = Obstacle.obstacle(width,40)
ob2 = Obstacle.obstacle(width,40)
ob3 = Obstacle.obstacle(width,40)
ob4 = Obstacle.obstacle(width,40)

missiles = []
obstacles = []
obstacles.append(Obstacle.obstacle(width,40))
obstacles.append(Obstacle.obstacle(width,40))
obstacles.append(Obstacle.obstacle(width,40))
obstacles.append(Obstacle.obstacle(width,40))


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                monJet.monte=True
            elif event.key == pygame.K_UP:
                monVaisseau.monte=True
            elif event.key == pygame.K_SPACE:
                monMissile=Shot.shot()
                monMissile.setPos(monVaisseau.posX, monVaisseau.posY)
                missiles.append(monMissile)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_z:
                monJet.monte=False
                monJet.setImg("jetpack.png")
            elif event.key == pygame.K_UP:
                monVaisseau.monte=False
                #monVaisseau.setImg("ship.png")
                #monVaisseau.setImg("chasseur.png")
                monVaisseau.setImg("pinkship.png")

    # Background            
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
    #monVaisseau.bouge("ship0.png","ship1.png")
    #monVaisseau.bouge("chasseur0.png","chasseur1.png")
    monVaisseau.bouge("pinkship0.png","pinkship1.png", height)

    
    if len(obstacles)==1:
        obstacles[0].moveFirst()
    elif len(obstacles) > 1:
        obstacles[0].moveFirst()
        for m in [1,len(obstacles)-1]:
            obstacles[m].move(obstacles[m-1])
    else:
        obstacles.append(Obstacle.obstacle(width,40))
        obstacles.append(Obstacle.obstacle(width,40))
        obstacles.append(Obstacle.obstacle(width,40))
        obstacles.append(Obstacle.obstacle(width,40))
    
    monJet.bouge("jetpack0.png","jetpack1.png", height)
    for monMissile in missiles:
        monMissile.bouge(width, missiles)
            
    screen.blit(monVaisseau.img,monVaisseau.getPos())
    screen.blit(monJet.img,monJet.getPos())
	
    
    for monMissile in missiles:
        screen.blit(monMissile.img,monMissile.getPos())
        for testObstacle in obstacles:
            if testObstacle.estTouche(monMissile.posX,monMissile.posY):
                monPlayer.raiseScore(1)                
                missiles.remove(monMissile)
                obstacles.remove(testObstacle)
                #ob = Obstacle.obstacle(width+40,)
                #obstacles.append(ob)
                                     
        

    for monObstacle in obstacles:
        screen.blit(monObstacle.img,monObstacle.getPos())

	police = pygame.font.Font(None, 80)
	texte = police.render(str(monPlayer.getScore()),1,(254,0,0))
	screen.blit(texte,(550,300))


    pygame.display.flip()
