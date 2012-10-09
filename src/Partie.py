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
import Obstacle
import random
import Bonus
import Menu
import Bouton

''' CLASSE '''
class Partie:  
    
    pygame.init()  
    ''' FONCTION QUI INSTANCIE nombre DE SNAKE
    ''  le type de deplacement est tire aleatoirement
    ''  ainsi que les coefiscients pour un deplacement en droite '''
    def __init__(self, player):
        self.player = player
        self.music = pygame.mixer.Sound("sounds/music.wav")
        ##### GROUPES DE SPRITE #####
        self.missiles = pygame.sprite.Group()
        self.snakes = pygame.sprite.Group()
        self.shooters = pygame.sprite.Group()
        self.aleatoires = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.missilesShooter = pygame.sprite.Group()
        self.bonus = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.isRecordBattu = False

    def creerSnakes(self,width, height, nombre=0):
        positionChaine = random.randint(100,height-180)
        #on tire le type de deplacement au hasard
        typeDeplacement = random.randint(1,3)
        #type snake
        if typeDeplacement == 1:
            while(nombre!=0):
                self.snakes.add(Ennemi.Snake(width+(nombre*20), 0, 1, positionChaine))
                nombre -= 1 
        #type ligne
        elif typeDeplacement == 2:
            a = random.uniform(-0.8,0.8)
            if a < 0:
                b = random.uniform(height/2,height-10)
            else:
                b = random.uniform(10,height-height/2)
            while nombre!=0:
                self.snakes.add(Ennemi.Snake(width+(nombre*40), positionChaine, typeDeplacement, positionChaine, a, b))
                nombre -= 1
        #type escadron
        else:
            self.snakes.add(Ennemi.Snake(width+80, positionChaine-80, 3))
            self.snakes.add(Ennemi.Snake(width+50, positionChaine-40, 3))
            self.snakes.add(Ennemi.Snake(width+20, positionChaine, 3))
            self.snakes.add(Ennemi.Snake(width+50, positionChaine+40, 3))
            self.snakes.add(Ennemi.Snake(width+80, positionChaine+80, 3))   
        
    def creerShooters(self, width, height):
        self.shooters.add(Ennemi.Shooter(width, height/2-20))
            
    def creerAleatoires(self, width, height):
        self.aleatoires.add(Ennemi.Aleatoire(width, height/2))
        
    def creerBonus(self, ship, width, height):
        r = random.randint(1,3)
        if r == 1:
            self.bonus.add(Bonus.BonusAmmo(width,height,ship))
        elif r == 2:
            self.bonus.add(Bonus.BonusShield(width,height,ship))
        elif r == 3:
            self.bonus.add(Bonus.BonusGunV2(width,height,ship))
    '''Fonction qui gere l'apparition aleatoire de tous les ennemis'''
    def creerEnnemi(self, width, height, level, monVaisseau):
        if random.randint(0, level) > 2+level/4:
            self.creerSnakes(width, height, random.randint(6,10))
        if random.randint(0, level) > 4+level/4:
            self.creerShooters(width, height)
        if random.randint(0, level) > 2+level/4:
            self.creerAleatoires(width, height)
    '''Apparition aleatoire des asteroides'''
    def creerObstacle(self, width, height, level):
        if level==-1:
            self.obstacles.add(Obstacle.obstacleRecord(width, random.randint(10,height-200),"images/ingame/record/asteroid_crash_1.png"))
        else:
            y = random.randint(10, height)
            if random.randint(0, level) > int(level/4):
                typeObstacle = random.randint(1,5)
                self.obstacles.add(Obstacle.obstacle(width, y,"images/ingame/asteroids/asteroid"+str(typeObstacle)+".png"))

    def gameOver(self, (x, y), screen, distance, height, monVaisseau):
        monVaisseau.son.stop()
        imagesTemp = [(pygame.image.load("images/ingame/explosion/explosion"+str(compt)+".png"), 0.1) for compt in range(1,9)]
        explosion = pyganim.PygAnimation(imagesTemp, loop=False)
        explosion.play()
        self.music.stop()
        while(1):
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        ecranAccueil = Menu.Menu("images/menu/menu.jpg")
                        ecranAccueil.addButton(Bouton.BoutonStartGame("images/menu/menu_principal/titles/play.png",0, 270, self.player, True))
                        ecranAccueil.addButton(Bouton.BoutonOption("images/menu/menu_principal/titles/option.png",0, 340, self.player))
                        ecranAccueil.addButton(Bouton.BoutonCredits("images/menu/menu_principal/titles/credits.png",0, 415))
                        ecranAccueil.addButton(Bouton.BoutonQuit("images/menu/menu_principal/titles/quit.png",0, 485))
                        ecranAccueil.afficher()
                    elif event.key == pygame.K_RETURN:
                        p = Partie(self.player)
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
            #record
            if distance > self.player.record :
                self.player.record=distance 
            #argent total du joueur
            self.player.money += monVaisseau.money
            self.player.save()
            
            titreRec = policeDistance.render("record : "+str(self.player.record)+" m",1,(254,0,0))
            screen.blit(titreRec,(200,(height/2)+60))
            explosion.blit(screen, (x,y))
            pygame.display.update()
    '''Fonction qui gere les collisions'''
    def Collisions(self, monVaisseau, animObj, screen):
        #test des self.missiles contre snakes
        for monMissile in self.missiles:
            for snakeTemp in self.snakes:
                if snakeTemp.estTouche(monMissile):
                    monVaisseau.raiseScore(1)
                    (x,y) = snakeTemp.getPos()
                    snakeTemp.creerCoin(self.coins)
                    self.missiles.remove(monMissile)
                    snakeTemp.son.play()
                    self.snakes.remove(snakeTemp)
                    animObj.play()
                    animObj.blit(screen, (x,y))
                    break
            for shooterTemp in self.shooters:
                if shooterTemp.estTouche(monMissile):
                    self.missiles.remove(monMissile)
                    (x,y) = shooterTemp.getPos()
                    if shooterTemp.vie != 0:
                        shooterTemp.vie -= 1
                    elif shooterTemp.vie == 0:   
                        r = random.randint(0,100)
                        if 100-r < 40:
                            self.creerBonus(monVaisseau, x-10, y+20)
                        shooterTemp.creerCoin(self.coins)
                        shooterTemp.son.play()
                        self.shooters.remove(shooterTemp)
                        monVaisseau.raiseScore(2)
                    animObj.play()
                    animObj.blit(screen, (x,y))
                    break
            for aleaTemp in self.aleatoires:
                if aleaTemp.estTouche(monMissile):
                    (x,y) = aleaTemp.getPos()
                    aleaTemp.creerCoin(self.coins)
                    monVaisseau.raiseScore(1)
                    self.missiles.remove(monMissile)
                    aleaTemp.son.play()
                    self.aleatoires.remove(aleaTemp)
                    animObj.play()
                    animObj.blit(screen, (x,y))
                    break   
        for obsTemp in self.obstacles:
            for monMissile in self.missilesShooter:
                if obsTemp.estTouche(monMissile):
                    monMissile.setImg("images/ingame/impact.png")
                    screen.blit(monMissile.image, monMissile.rect)
                    self.missilesShooter.remove(monMissile)
            for monMissile in self.missiles:
                if obsTemp.estTouche(monMissile):
                    monMissile.setImg("images/ingame/impact.png")
                    screen.blit(monMissile.image, monMissile.rect)
                    self.missiles.remove(monMissile)
            #test des snakes contre obstacle
            for snakeTemp in self.snakes:
                if obsTemp.estTouche(snakeTemp):
                    (x,y) = snakeTemp.getPos()
                    snakeTemp.son.play()
                    self.snakes.remove(snakeTemp)
                    animObj.play()
                    animObj.blit(screen, (x,y)) 
            #test des self.shooters contre obstacle
            for shooterTemp in self.shooters:
                if obsTemp.estTouche(shooterTemp):
                    (x,y) = shooterTemp.getPos()
                    shooterTemp.son.play()
                    self.shooters.remove(shooterTemp)
                    animObj.play()
                    animObj.blit(screen, (x,y))  
            #test des self.shooters contre obstacle
            for aleaTemp in self.aleatoires:
                if obsTemp.estTouche(aleaTemp):
                    (x,y) = aleaTemp.getPos()
                    aleaTemp.son.play()
                    self.aleatoires.remove(aleaTemp)
                    animObj.play()
                    animObj.blit(screen, (x,y))             
            if monVaisseau.isBonusShield != True:                                 
            #test du ship contre les ennemis
                if monVaisseau.estTouche(obsTemp):
                    monVaisseau.enVie = False
        for snakeTemp in self.snakes:
            if monVaisseau.estTouche(snakeTemp):
                monVaisseau.raiseScore(1)
                (x,y) = snakeTemp.getPos()
                snakeTemp.creerCoin(self.coins)
                snakeTemp.son.play()
                self.snakes.remove(snakeTemp)
                animObj.play()
                animObj.blit(screen, (x,y))
                if not monVaisseau.isBonusShield:
                    monVaisseau.enVie = False
        for shooterTemp in self.shooters:
            if monVaisseau.estTouche(shooterTemp):
                (x,y) = shooterTemp.getPos()
                r = random.randint(0,100)
                if 100-r < 40:
                    self.creerBonus(monVaisseau, x, y)
                shooterTemp.creerCoin(self.coins)
                shooterTemp.son.play() 
                self.shooters.remove(shooterTemp)
                monVaisseau.raiseScore(2)
                animObj.play()
                animObj.blit(screen, (x,y))
                if not monVaisseau.isBonusShield:
                    monVaisseau.enVie = False
        for aleaTemp in self.aleatoires:
            if monVaisseau.estTouche(aleaTemp):
                (x,y) = aleaTemp.getPos()
                aleaTemp.creerCoin(self.coins)
                monVaisseau.raiseScore(1)
                aleaTemp.son.play()
                self.aleatoires.remove(aleaTemp)
                animObj.play()
                animObj.blit(screen, (x,y))
                if not monVaisseau.isBonusShield:
                    monVaisseau.enVie = False
        for self.missileshooterTemp in self.missilesShooter:
            if monVaisseau.estTouche(self.missileshooterTemp):
                if not monVaisseau.isBonusShield:
                    monVaisseau.enVie = False
                self.missilesShooter.remove(self.missileshooterTemp)
        #test vaisseau contre self.bonus
        for self.bonusTemp in self.bonus:
            if monVaisseau.estTouche(self.bonusTemp):
                self.bonusTemp.startTime=pygame.time.get_ticks()
                self.bonusTemp.stopTime=pygame.time.get_ticks()+10000               
                self.bonusTemp.isActive=True
                self.bonusTemp.isVisible=False
                self.bonusTemp.action(self.bonus,pygame.time.get_ticks())
            else:
                self.bonusTemp.action(self.bonus,pygame.time.get_ticks())
        #test vaisseau contre pieces de monnaie
        for coinTemp in self.coins:
            if monVaisseau.estTouche(coinTemp):
                monVaisseau.money += 1
                coinTemp.son.play()
                self.coins.remove(coinTemp)
    '''Fonction qui gere les mouvements de tous les objets'''
    def Mouvements(self, screen, width, height, monVaisseau):
        ##### MOUVEMENT JOUEUR #####
        monVaisseau.update(pygame.time.get_ticks(), height, screen)
        ##### MOUVEMENT DES SNAKE #####
        self.snakes.update(pygame.time.get_ticks(), self.snakes, width, height)
        ##### MOUVEMENT DES SHOOTERS #####
        self.shooters.update(pygame.time.get_ticks(), monVaisseau, self.shooters, self.missilesShooter, height)
        ##### MOUVEMENT DES ALEATOIRES #####
        self.aleatoires.update(pygame.time.get_ticks(), self.obstacles, height)
        ##### MOUVEMENT DES OBSTACLES #####
        self.obstacles.update(pygame.time.get_ticks())
        ##### MOUVEMENT DES BONUS #####
        self.bonus.update(pygame.time.get_ticks(),self.bonus)
        ##### MOUVEMENT self.missiles #####
        self.missiles.update(pygame.time.get_ticks(), width, self.missiles)
        ##### MOUVEMENT self.missiles ENNEMY #####        
        self.missilesShooter.update(pygame.time.get_ticks(), self.missilesShooter)
        ##### MOUVEMENT DES PIECES DE MONNAIE #####
        self.coins.update(pygame.time.get_ticks())
    '''Fonction qui gere les blits de tous les objets'''
    def Blits(self, width, height, screen, distance, monVaisseau):
        #jauge tir
        imgJauge = pygame.image.load("images/ingame/gauge.png")
        screen.blit(imgJauge, (1,10))
        if (monVaisseau.inCharge):
            pygame.draw.rect(screen, (255, 0, 0), (32, 38, monVaisseau.charge*139/monVaisseau.chaleurMax, 23))
        screen.blit(monVaisseau.image, monVaisseau.rect)
        #blits logo self.bonus
        if monVaisseau.isBonusAmmo:
            logoBonus =  pygame.transform.scale(pygame.image.load("images/bonus/ammo.png"),(25,25))
            screen.blit(logoBonus,(10,50))
        if monVaisseau.isBonusShield:
            logoBonus =  pygame.transform.scale(pygame.image.load("images/bonus/shield_icon.png"),(25,25))
            screen.blit(logoBonus,(40,50))
        #blits ennemies et self.missiles
        for o in self.obstacles.sprites(): screen.blit(o.image, o.rect)
        for c in self.coins.sprites(): screen.blit(c.image,c.rect)
        for s in self.snakes.sprites(): screen.blit(s.image, s.rect)
        for s in self.shooters.sprites(): screen.blit(s.image, s.rect)
        for a in self.aleatoires.sprites(): screen.blit(a.image, a.rect)
        for m in self.missiles.sprites(): screen.blit(m.image, m.rect)
        for m in self.missilesShooter.sprites(): screen.blit(m.image, m.rect)
        for b in self.bonus.sprites():
            if b.isVisible:
                screen.blit(b.image,b.rect)
        #blits record
        police = pygame.font.Font(None, 40)
        if not self.isRecordBattu:
            texte = police.render("record : "+str(self.player.record), 1, (254,50,100))
        else:
            texte = police.render("record : "+str(distance), 1, (100,255,100))
        screen.blit(texte, (width - 250, height - 150))       
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

    def supprimerObjets(self, width):
        for snakeTemp in self.snakes:
            (x, _) = snakeTemp.getPos()
            if x < -200:
                self.snakes.remove(snakeTemp)
        for shooterTemp in self.shooters:
            (x, _) = shooterTemp.getPos()
            if x < -200:
                self.shooters.remove(shooterTemp) 
        for aleaTemp in self.aleatoires :       
            (x, _) = aleaTemp.getPos()
            if x < -200:
                self.aleatoires.remove(aleaTemp)
        for obsTemp in self.obstacles :       
            (x, _) = obsTemp.getPos()
            if x < -200:
                self.obstacles.remove(obsTemp) 
        for self.missileshooterTemp in self.missilesShooter :       
            (x, _) = self.missileshooterTemp.getPos()
            if x < -200:
                self.missilesShooter.remove(self.missileshooterTemp)  
        for coinTemp in self.coins :       
            (x, _) = coinTemp.getPos()
            if x < -200:
                self.coins.remove(coinTemp) 
        for missileTemp in self.missiles :       
            (x, _) = missileTemp.getPos()
            if x > width+40:
                self.missiles.remove(missileTemp) 
                
    def jouer(self):     
        ##### PARAMETRES DE LA FENETRE #####
        size = width, height = 1024,768
        screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        ##### COMPTEURS #####
        distanceTemp = 0
        distance = 2
        distanceLevelTemp = 0
        level = 1
        ##### EXPLOSIONS #####
        imagesTemp = [(pygame.transform.scale(pygame.image.load("images/ingame/explosion/explosion"+str(compt)+".png"), (70, 70)), 0.6) for compt in range(2,6)]
        animObj = pyganim.PygAnimation(imagesTemp, loop=False)
        animObj.play()
        ##### IMAGES DU BACKGROUND #####
        background = pygame.image.load("images/background/background.jpg")
        i=0
        isRecordBattu=False
        ##### JOUEUR #####
        monVaisseau = Ship.ship([20, 0])
        monVaisseau.raiseChaleurMax(self.player.additionalMissiles)
        
        '''self.player.updateShopStateList(3,-1)'''

        if self.player.shopStateList[3]==1:
            monVaisseau.versionCanon=4
        elif self.player.shopStateList[2]==1:
            monVaisseau.versionCanon=3
        elif self.player.shopStateList[1]==1:
            monVaisseau.versionCanon=2
        else:
            monVaisseau.versionCanon=1
        
        ##### MUSIQUE #####
        if self.player.musicOn:
            self.music.play(-1)
        ##### MENU COMMENCER #####
        menuStartOn=True
        
        quitterVersMenuPrincipal = False
        '''################################################################## ''
        ''   BOUCLE DE JEU                                                    ''
        ''      (img par img)                                                 ''
        '' ##################################################################'''
        while 1:
            ''' VITESSE D'AFFICHAGE '''    
            clock = pygame.time.Clock()
            FRAMES_PER_SECOND = 30
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
                        if not monVaisseau.monte:
                            monVaisseau.monte=True
                            monVaisseau.son.play(-1)
                    # ESPACE
                    elif event.key == pygame.K_SPACE:
                        if not monVaisseau.inCharge:
                            monVaisseau.inCharge=True
                    # RIGHT
                    elif event.key == pygame.K_RIGHT:
                        if not monVaisseau.inBoost:
                            monVaisseau.inBoost=True
                    # LEFT
                    elif event.key == pygame.K_LEFT:
                        if not monVaisseau.inBreak:
                            monVaisseau.inBreak=True
                    # ECHAPE
                    elif event.key == pygame.K_ESCAPE:
                        menuPause = Menu.menuPause("images/menu/menu_pause/background_menu_pause.png", self.player)
                        menuPause.addButton(Bouton.BoutonReprendre("images/menu/menu_pause/reprendre.png", 133, 176, True))
                        menuPause.addButton(Bouton.BoutonMenuPrincipal("images/menu/menu_pause/menu_principal.png", 154, 292, self.player))
                        menuPause.afficher(screen, self)
                ##### RELACHE TOUCHE #####
                elif event.type == pygame.KEYUP:
                    # HAUT
                    if event.key == pygame.K_UP:
                        monVaisseau.monte=False
                        monVaisseau.son.stop()
                    # ESPACE
                    elif event.key == pygame.K_SPACE:
                        monVaisseau.tir(self.missiles);
                    # RIGHT
                    elif event.key == pygame.K_RIGHT:
                        monVaisseau.inBoost=False
                    # LEFT
                    elif event.key == pygame.K_LEFT:
                        monVaisseau.inBreak=False
            ##### BACKGROUND #####
            screen.blit(background, (-i,0)) 
            screen.blit(background, (3575-i,0))            
            i+=1
            if i > 3576:
                i=0
            ##### RECORD PRECEDENT #####
            if not isRecordBattu:
                if distance+35==self.player.record:
                    self.creerObstacle(width, height, -1)
                    isRecordBattu=True
            if not self.isRecordBattu:
                if distance>self.player.record:
                    self.isRecordBattu=True
            
            self.Mouvements(screen, width, height, monVaisseau)
            self.Collisions(monVaisseau, animObj, screen)
            self.Blits(width, height, screen, distance, monVaisseau)
            self.supprimerObjets(width)
            #incrementation du compteur generale de distance et creation d'ennemis et d'self.obstacles
            if distanceTemp != 4:
                distanceTemp += 1
            else:
                distanceTemp = 0
                distance += 1
              
             
            if distanceLevelTemp != 60:
                distanceLevelTemp += 1
                if distanceLevelTemp == 10:
                    self.creerEnnemi(width, height, level, monVaisseau)
                    self.creerObstacle(width, height, level) 
            else:
                distanceLevelTemp = 0
                level += 1
            
            if (monVaisseau.enVie == False):    
                self.gameOver(monVaisseau.getPos(), screen, distance, height, monVaisseau)
            pygame.display.update()
