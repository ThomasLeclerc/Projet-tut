import pygame
import math
import Shot
import random

class ennemy:
    posX = 0
    posY = 0
    
    def __init__(self,x,y,image):
        self.posX = x
        self.posY = y
        self.setImg(image);

    def getPos(self):
        return (self.posX,self.posY)
    
    def setImg(self, image):
        self.img = pygame.image.load(image)
        self.ennemyRect = self.img.get_rect()


class Snake(ennemy):
    def __init__(self,x,y, positionChaine, typeDeplacement , a=0, b=0):
        self.positionChaine=positionChaine
        self.deplacement = typeDeplacement
        if typeDeplacement == 2:
            self.a = a
            self.b = b
        ennemy.__init__(self,x,y, "images/chasseur1.png")
        self.img = pygame.transform.rotate(self.img,-75)
    def estTouche(self,x,y):
        if x > self.posX and x < self.posX+self.ennemyRect.right and y > self.posY and y < self.posY+self.ennemyRect.bottom:
            return True 
        else:
            return False
    
    def move(self,snakes, width, height):
        self.posX -= 5
        
        # DEPLACEMENT EN COURBE SINUSALE
        if self.deplacement==1:
            self.posY =  math.cos(self.posX*0.02)*120+self.positionChaine
        
            # calcul de l'angle et rotation de l'image
            coefDir = -2.4*math.sin(0.02*self.posX)
            angle = math.degrees(math.atan(coefDir))  
            self.img = pygame.image.load("images/chasseur1.png")
            self.img = pygame.transform.rotate(self.img,-angle) 
        
            if self.posX<-200:
                snakes.remove(self)
        #DEPLACEMENT EN DROITE        
        elif self.deplacement==2:
            self.posY = self.a*self.posX + self.b
            angle = math.degrees(math.atan(self.a))
            self.img = pygame.image.load("images/chasseur1.png")
            self.img = pygame.transform.rotate(self.img,-angle)
            if self.posX<0:
                snakes.remove(self) 

class Shooter(ennemy):
    vie = 2
    compteurTir = 0
    switch = 0
    def __init__(self,x,y):
        ennemy.__init__(self,x,y, "images/vaisseaux/enemies/enemy1/enemy1_1.png")  
        self.img =  pygame.transform.scale(self.img, (80, 100))
    def estTouche(self,x,y , ennemy):
        if x > self.posX and x < self.posX+self.ennemyRect.right and y > self.posY and y < self.posY+self.ennemyRect.bottom:
            return True
        else:
            return False            
    
    def move(self, ship, ennemy):
        self.posX -= 2      
        (shipPosX, shipPosY) = ship.getPos()
        if self.posY < shipPosY-10 and self.posY+3 < 600:
            self.posY += 4
        elif shipPosY+10 < self.posY and self.posY-3 > 0:
            self.posY -= 4
        if self.posX<-100:
            ennemy.remove(self)  
               
        #animation    
        if self.switch == 0:
            self.img = self.img =  pygame.transform.scale(pygame.image.load("images/vaisseaux/enemies/enemy1/enemy1_2.png"), (80, 100))
            self.switch=1
        elif self.switch == 1:
            self.img = pygame.transform.scale(pygame.image.load("images/vaisseaux/enemies/enemy1/enemy1_1.png"), (80, 100))
            self.switch=0  
                
    def tir(self, missilesShooter):
        self.compteurTir += 1
        if self.compteurTir%30 == 0:
            missilesShooter.append(Shot.shotShooterEnnemy(self.posX,self.posY+20))         
                          
   
'''
'' Ennemi qui se deplace aleatoirement
'''             
class Aleatoire(ennemy):
    vie = 2
    sens = 1
    switch = 0
    def __init__(self,x,y):
        ennemy.__init__(self,x,y, "images/vaisseaux/enemies/enemy2/enemy2_1.png")   
        self.img =  pygame.transform.scale(self.img, (50, 50))
        
    def estTouche(self,x,y , ennemy):
        if x > self.posX and x < self.posX+self.ennemyRect.right and y > self.posY and y < self.posY+self.ennemyRect.bottom:
            self.vie -= 1
            if self.vie == 0:
                ennemy.remove(self)
            else:
                self.img = self.img =  pygame.transform.scale(pygame.image.load("images/ship3.png") , (50, 50))
                self.img = pygame.transform.rotate(self.img,90)
            return True
        else:
            return False            
    
    def move(self, ennemy, height):
        self.posX -= 8
        if (self.posX)%25 == 0:
           self.sens = random.randint(0,1)   
        
        if self.sens == 0:
            if self.posY > height-20:
                self.sens = 1
                self.posY -= 3
            else:
                self.posY += 3
            
        else:
            if self.posY < 20:
                self.sens = 0
                self.posY += 3
            else:
                self.posY -= 3
        
        if self.posY > height-20:
            self.sens = 1
          
        if self.posX<-50:
               ennemy.remove(self)  
               
        #animation    
        if self.switch == 0:
            self.img = pygame.transform.scale(pygame.image.load("images/vaisseaux/enemies/enemy2/enemy2_2.png") , (50, 50))
            self.switch=1
        elif self.switch == 1:
            self.img = pygame.transform.scale(pygame.image.load("images/vaisseaux/enemies/enemy2/enemy2_2.png") , (50, 50))
            self.switch=0  
        
                
            

        
   
     
    
        
        




