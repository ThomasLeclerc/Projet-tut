'''#####################
#''                   '#
#'  Classe Partie     '#
#'    Moteur de jeu   '#
#'                   ''#
#####################'''

''' IMPORTS '''
import pygame
import pyganim
import sys
import Ennemi
import Ship
import Player
import Obstacle
import random
import Bonus


''' CLASSE '''
class Partie:  

    ''' FONCTION QUI INSTANCIE nombre DE SNAKE
    ''  le type de deplacement est tire aleatoirement
    ''  ainsi que les coefiscients pour un deplacement en droite '''
    def creerSnakes(self,width, height, snakes, nombre=0):
        positionChaine = random.randint(100,height-180)
        #on tire le type de deplacement au hasard
        typeDeplacement = random.randint(1,3)
        #type snake
        if typeDeplacement == 1:
            while(nombre!=0):
                snakes.add(Ennemi.Snake(width+(nombre*30), 0, 1, positionChaine))
                nombre -= 1 
        #type ligne
        elif typeDeplacement == 2:
            a = random.uniform(-0.8,0.8)
            if a < 0:
                b = random.uniform(height/2,height-10)
            else:
                b = random.uniform(10,height-height/2)
            while nombre!=0:
                snakes.add(Ennemi.Snake(width+(nombre*40), positionChaine, typeDeplacement, positionChaine, a, b))
                nombre -= 1
        #type escadron
        else:
            snakes.add(Ennemi.Snake(width+80, positionChaine-80, 3))
            snakes.add(Ennemi.Snake(width+50, positionChaine-40, 3))
            snakes.add(Ennemi.Snake(width+20, positionChaine, 3))
            snakes.add(Ennemi.Snake(width+50, positionChaine+40, 3))
            snakes.add(Ennemi.Snake(width+80, positionChaine+80, 3))   
                            
    def creerShooters(self, width, height, shooters):
        shooters.add(Ennemi.Shooter(width, height/2-20))
            
    def creerAleatoires(self, width, height, aleatoires):
        aleatoires.add(Ennemi.Aleatoire(width, height/2))
        
    def creerBonus(self, bonus,ship, width, height):
        r = random.randint(1,3)
        if r == 1:
            bonus.add(Bonus.BonusAmmo(width,height,ship))
        elif r == 2:
            bonus.add(Bonus.BonusShield(width,height,ship))
        elif r == 3:
            bonus.add(Bonus.BonusGunV2(width,height,ship))
    
    '''Fonction qui gere l'apparition aleatoire de tous les ennemis'''
    def creerEnnemi(self, width, height, compApparitionSnake, compApparitionShooter, compApparitionAleatoire, distance, snakes, shooters, aleatoires, monVaisseau):
        if distance%compApparitionSnake == 0:
            compApparitionSnake -= 1
            self.creerSnakes(width, height, snakes, int(monVaisseau.chaleurMax/60))
        if distance%compApparitionShooter == 0:
            compApparitionShooter -= 1
            self.creerShooters(width, height, shooters)
        if distance%compApparitionAleatoire == 0:
            compApparitionAleatoire -= 1
            self.creerAleatoires(width, height, aleatoires)
    '''Apparition aleatoire des asteroides'''
    def creerObstacle(self, comptApparitionObstacle, width, height, distance, obstacles):
        y = random.randint(10, height)
        if distance%comptApparitionObstacle==0:
            comptApparitionObstacle -= 0
            typeObstacle = random.randint(1,5)
            obstacles.add(Obstacle.obstacle(width, y,"images/ingame/asteroids/asteroid"+str(typeObstacle)+".png"))

    def gameOver(self, (x, y), screen, distance, height, monVaisseau):
        
        imagesTemp = [(pygame.image.load("images/ingame/explosion/explosion"+str(compt)+".png"), 0.1) for compt in range(1,9)]
        explosion = pyganim.PygAnimation(imagesTemp, loop=False)
        explosion.play()
        
        
        while(1):
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    elif event.key == pygame.K_RETURN:
                        p = Partie()
                        p.jouer()
                        break
                        
            background = pygame.image.load("images/background.jpg")
            screen.blit(background, (0,0))
            #blit GAME OVER    
            policeTitre = pygame.font.Font(None, 120)
            titre = policeTitre.render("GAME OVER",1,(254,0,0))
            screen.blit(titre,(200,100)) 

            #blit Recommencer    
            policeTitre = pygame.font.Font(None, 20)
            titre = policeTitre.render("ENTRER POUR RECOMMENCER",1,(50,254,50))
            screen.blit(titre,(800,700)) 
                        
            #blit disctance parcourue
            policeDistance = pygame.font.Font(None, 80)
            titre = policeDistance.render("distance : "+str(distance)+" m",1,(254,0,0))
            screen.blit(titre,(200,height/2))
            monVaisseau.chargerRecord()
            if distance > monVaisseau.record :
                monVaisseau.record=distance
                monVaisseau.enregistrerRecord(monVaisseau.record)  
            titreRec = policeDistance.render("record : "+str(monVaisseau.record)+" m",1,(254,0,0))
            screen.blit(titreRec,(200,(height/2)+60))
            explosion.blit(screen, (x,y))
            pygame.display.update()

                        
    '''
    '    Fonction qui gere les collisions
    '''
    def Collisions(self, monPlayer, monVaisseau, missiles, snakes, shooters, aleatoires, obstacles, missilesShooter, animObj, screen, bonus, coins):

        #test des missiles contre snakes
        for monMissile in missiles:
            for snakeTemp in snakes:
                if snakeTemp.estTouche(monMissile):
                    monPlayer.raiseScore(1)
                    (x,y) = snakeTemp.getPos()
                    snakeTemp.creerCoin(coins)
                    missiles.remove(monMissile)
                    snakes.remove(snakeTemp)
                    animObj.play()
                    animObj.blit(screen, (x,y))
                    break
            for shooterTemp in shooters:
                if shooterTemp.estTouche(monMissile):
                    missiles.remove(monMissile)
                    (x,y) = shooterTemp.getPos()
                    r = random.randint(0,100)
                    if 100-r < 40:
                        self.creerBonus(bonus,monVaisseau, x, y)
                    shooterTemp.creerCoin(coins)
                    shooters.remove(shooterTemp)
                    monPlayer.raiseScore(2)
                    animObj.play()
                    animObj.blit(screen, (x,y))
                    break
            for aleaTemp in aleatoires:
                if aleaTemp.estTouche(monMissile):
                    (x,y) = aleaTemp.getPos()
                    aleaTemp.creerCoin(coins)
                    monPlayer.raiseScore(1)
                    missiles.remove(monMissile)
                    aleatoires.remove(aleaTemp)
                    animObj.play()
                    animObj.blit(screen, (x,y))
                    break

                    
        for obsTemp in obstacles:
            for monMissile in missiles:
                if obsTemp.estTouche(monMissile):
                    monMissile.setImg("images/ingame/impact.png")
                    screen.blit(monMissile.image, monMissile.rect)
                    missilesShooter.remove(monMissile)
                if obsTemp.estTouche(monMissile):
                    monMissile.setImg("images/ingame/impact.png")
                    screen.blit(monMissile.image, monMissile.rect)
                    missiles.remove(monMissile)
            #test des snakes contre obstacle
            for snakeTemp in snakes:
                if obsTemp.estTouche(snakeTemp):
                    (x,y) = snakeTemp.getPos()
                    snakes.remove(snakeTemp)
                    animObj.play()
                    animObj.blit(screen, (x,y)) 
            #test des shooters contre obstacle
            for shooterTemp in shooters:
                if obsTemp.estTouche(shooterTemp):
                    (x,y) = shooterTemp.getPos()
                    shooters.remove(shooterTemp)
                    animObj.play()
                    animObj.blit(screen, (x,y))  
            #test des shooters contre obstacle
            for aleaTemp in aleatoires:
                if obsTemp.estTouche(aleaTemp):
                    (x,y) = aleaTemp.getPos()
                    aleatoires.remove(aleaTemp)
                    animObj.play()
                    animObj.blit(screen, (x,y))             
                    
            if monVaisseau.isBonusShield != True:                                 
            #test du ship contre les ennemis
                if monVaisseau.estTouche(obsTemp):
                    monVaisseau.enVie = False
            
        for snakeTemp in snakes:
            if monVaisseau.estTouche(snakeTemp):
                monPlayer.raiseScore(1)
                (x,y) = snakeTemp.getPos()
                snakeTemp.creerCoin(coins)
                snakes.remove(snakeTemp)
                animObj.play()
                animObj.blit(screen, (x,y))
                if not monVaisseau.isBonusShield:
                    monVaisseau.enVie = False
        
        for shooterTemp in shooters:
            if monVaisseau.estTouche(shooterTemp):
                (x,y) = shooterTemp.getPos()
                r = random.randint(0,100)
                if 100-r < 40:
                    self.creerBonus(bonus,monVaisseau, x, y)
                shooterTemp.creerCoin(coins)
                shooters.remove(shooterTemp)
                monPlayer.raiseScore(2)
                animObj.play()
                animObj.blit(screen, (x,y))
                if not monVaisseau.isBonusShield:
                    monVaisseau.enVie = False
        
        for aleaTemp in aleatoires:
            if monVaisseau.estTouche(aleaTemp):
                (x,y) = aleaTemp.getPos()
                aleaTemp.creerCoin(coins)
                monPlayer.raiseScore(1)
                aleatoires.remove(aleaTemp)
                animObj.play()
                animObj.blit(screen, (x,y))
                if not monVaisseau.isBonusShield:
                    monVaisseau.enVie = False
        
        for missileShooterTemp in missilesShooter:
            if monVaisseau.estTouche(missileShooterTemp):
                monVaisseau.enVie = False

        #test vaisseau contre bonus
        for bonusTemp in bonus:
            if monVaisseau.estTouche(bonusTemp):
                bonusTemp.startTime=pygame.time.get_ticks()
                bonusTemp.stopTime=pygame.time.get_ticks()+10000               
                bonusTemp.isActive=True
                bonusTemp.isVisible=False
                bonusTemp.action(bonus,pygame.time.get_ticks())
            else:
                bonusTemp.action(bonus,pygame.time.get_ticks())
                    
                
           
        #test vaisseau contre pieces de monnaie
        for coinTemp in coins:
            if monVaisseau.estTouche(coinTemp):
                monVaisseau.money += 1
                coins.remove(coinTemp)
                

    '''
    '    Fonction qui gere les mouvements de tous les objets
    '''
    def Mouvements(self, screen, width, height, monVaisseau, missiles, snakes, shooters, aleatoires, obstacles, missilesShooter, bonus, coins):

        ##### MOUVEMENT JOUEUR #####
        monVaisseau.update(pygame.time.get_ticks(), height, screen)
        ##### MOUVEMENT DES SNAKE #####
        snakes.update(pygame.time.get_ticks(), snakes, width, height)
        ##### MOUVEMENT DES SHOOTERS #####
        shooters.update(pygame.time.get_ticks(), monVaisseau, shooters, missilesShooter, height)
        ##### MOUVEMENT DES ALEATOIRES #####
        aleatoires.update(pygame.time.get_ticks(), aleatoires, height)
        ##### MOUVEMENT DES OBSTACLES #####
        obstacles.update(pygame.time.get_ticks())
        ##### MOUVEMENT DES BONUS #####
        bonus.update(pygame.time.get_ticks(),bonus)
        ##### MOUVEMENT MISSILES #####
        missiles.update(pygame.time.get_ticks(), width, missiles)
        ##### MOUVEMENT MISSILES ENNEMY #####        
        missilesShooter.update(pygame.time.get_ticks(), missilesShooter)
        
        ##### MOUVEMENT DES PIECES DE MONNAIE #####
        coins.update(pygame.time.get_ticks())
        
    '''
    '    Fonction qui gere les blits de tous les objets
    '''
    def Blits(self, width, height, screen, distance, monVaisseau, missiles, snakes, shooters, aleatoires, obstacles, missilesShooter, bonus, coins):

        #jauge tir
        pygame.draw.rect(screen, (255, 0, 0), (1, 1, monVaisseau.chaleurMax + 3, 10), 1)
        if (monVaisseau.inCharge):
            pygame.draw.rect(screen, (255, 0, 0), (4, 4, monVaisseau.charge, 7))
        screen.blit(monVaisseau.image, monVaisseau.rect)
        #blits logo bonus
        if monVaisseau.isBonusAmmo:
            logoBonus =  pygame.transform.scale(pygame.image.load("images/bonus/ammo.png"),(25,25))
            screen.blit(logoBonus,(10,50))
        if monVaisseau.isBonusShield:
            logoBonus =  pygame.transform.scale(pygame.image.load("images/bonus/shield.png"),(25,25))
            screen.blit(logoBonus,(40,50))
        #blits ennemies et missiles
        for s in snakes.sprites(): screen.blit(s.image, s.rect)
        for s in shooters.sprites(): screen.blit(s.image, s.rect)
        for a in aleatoires.sprites(): screen.blit(a.image, a.rect)
        for o in obstacles.sprites(): screen.blit(o.image, o.rect)
        for m in missiles.sprites(): screen.blit(m.image, m.rect)
        for m in missilesShooter.sprites(): screen.blit(m.image, m.rect)
        for b in bonus.sprites():
            if b.isVisible:
                screen.blit(b.image,b.rect)

        for c in coins.sprites(): screen.blit(c.image,c.rect)

        #blits score
        screen.blit(pygame.image.load("images/ingame/Coin.png"), (width-200, height-100))
        police = pygame.font.Font(None, 60)
        texte = police.render(str(monVaisseau.money), 1, (210, 210, 1))
        screen.blit(texte, (width - 160, height - 110))
        #blits score
        police = pygame.font.Font(None, 60)
        texte = police.render(str(distance) + " m", 1, (254, 0, 0))
        screen.blit(texte, (width - 200, height - 70))
        #blits jauge chaleur
        image = pygame.image.load("images/rocket.png")
        for l in range(((monVaisseau.chaleurMax / monVaisseau.chaleurMissile) - 1) - ((monVaisseau.chaleur) / monVaisseau.chaleurMissile)):
            screen.blit(image, (10 * (l + 1), 10))
        if (monVaisseau.chaleur == 0):
            screen.blit(image, (10 * (l + 2), 10))
        if monVaisseau.isBonusShield:
            imgShield = pygame.image.load("images/bonus/Shield.png")
            (x,y) = monVaisseau.getPos()
            screen.blit(imgShield, (x,y-10))
    def jouer(self):
        pygame.init()       
        ##### PARAMETRES DE LA FENETRE #####
        size = width, height = 1024,768
        screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        
        ##### COMPTEURS #####
        comptApparitionSnake = 50
        comptApparitionShooter = 40
        comptApparitionAleatoire = 50
        comptApparitionObstacles = 40
        distanceTemp = 0
        distance = 2
        
        ##### EXPLOSIONS #####
        imagesTemp = [(pygame.transform.scale(pygame.image.load("images/ingame/explosion/explosion"+str(compt)+".png"), (70, 70)), 0.6) for compt in range(2,6)]
        animObj = pyganim.PygAnimation(imagesTemp, loop=False)
        animObj.play()
        
        
        ##### IMAGES DU BACKGROUND #####
        background = pygame.image.load("images/background/background.jpg")
        bgCouche1 = pygame.image.load("images/background_couche1.png")
        bgCouche2 = pygame.image.load("images/background_couche2.png")
        bgCouche3 = pygame.image.load("images/background_couche3.png")
        i=j=k=l=0
        
        ##### JOUEUR #####
        monPlayer = Player.player('Jean')
        monVaisseau = Ship.ship([20, 0])
        
        
        ##### GROUPES DE SPRITE #####
        missiles = pygame.sprite.Group()
        snakes = pygame.sprite.Group()
        shooters = pygame.sprite.Group()
        aleatoires = pygame.sprite.Group()
        obstacles = pygame.sprite.Group()
        missilesShooter = pygame.sprite.Group()
        bonus = pygame.sprite.Group()
        coins = pygame.sprite.Group()
        '''
        self.creerEnnemi(width, height, comptApparitionSnake, comptApparitionShooter, comptApparitionAleatoire, distance, snakes, shooters, aleatoires, monVaisseau)
        self.creerObstacle(comptApparitionObstacles, width, height, distance, obstacles)
        
        '''
        
        
        ##### MUSIQUE #####
        '''musique = pygame.mixer.Sound("sounds/BB078.WAV")
        play = 0'''
        
        
        ##### MENU COMMENCER #####
        menuStartOn=True
        
        
        '''################################################################## ''
        ''   BOUCLE DE JEU                                                    ''
        ''      (img par img)                                                 ''
        '' ##################################################################'''
        while 1:
            ''' VITESSE D'AFFICHAGE '''    
            clock = pygame.time.Clock()
            FRAMES_PER_SECOND = 20
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
                    # RIGHT
                    elif event.key == pygame.K_RIGHT:
                        monVaisseau.inBoost=True
                    # LEFT
                    elif event.key == pygame.K_LEFT:
                        monVaisseau.inBreak=True
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
                        monVaisseau.tir(missiles);
                    # RIGHT
                    elif event.key == pygame.K_RIGHT:
                        monVaisseau.inBoost=False
                    # LEFT
                    elif event.key == pygame.K_LEFT:
                        monVaisseau.inBreak=False
            ##### BACKGROUND #####
            screen.blit(background, (-i,0)) 
            screen.blit(background, (3576-i,0))            
            #screen.blit(bgCouche1, (width-j,j))
            #screen.blit(bgCouche2, (-k,0))
            #screen.blit(bgCouche2, (width-k,0))
            #screen.blit(bgCouche3, (-l,0))
            #screen.blit(bgCouche3, (width-l,0))
            i+=1
            #j+=2
            #k+=4
            #l+=6
            if i > 3576:
                i=0
            #if j > width:
            #    j=0
            #if k > width:
            #    k=0
            #if l > width:
            #    l=0
                
        
            
            self.Mouvements(screen, width, height, monVaisseau, missiles, snakes, shooters, aleatoires, obstacles, missilesShooter, bonus, coins)
        
            self.Collisions(monPlayer, monVaisseau, missiles, snakes, shooters, aleatoires, obstacles, missilesShooter, animObj, screen, bonus, coins)
               
            self.Blits(width, height, screen, distance, monVaisseau, missiles, snakes, shooters, aleatoires, obstacles, missilesShooter, bonus, coins)
            
            
            
            
            #incrementation du compteur generale de distance et creation d'ennemis et d'obstacles
            if distanceTemp != 10:
                distance += 1
            else:
                distanceTemp = 0
                distance += 1
            self.creerEnnemi(width, height, comptApparitionSnake, comptApparitionShooter, comptApparitionAleatoire, distance, snakes, shooters, aleatoires, monVaisseau)
            self.creerObstacle(comptApparitionObstacles, width, height, distance, obstacles)
                       
            if (monVaisseau.enVie == False):    
                self.gameOver(monVaisseau.getPos(), screen, distance, height, monVaisseau)
                            
            pygame.display.update()
    

