import pygame
import math
import Shot
import random

class ennemy(pygame.sprite.Sprite):
    
    def __init__(self,x,y,image):
        pygame.sprite.Sprite.__init__(self)
        self.setImg(image)
        self.rect.left = x
        self.rect.top = y
        self.next_update_time = 0 # update() hasn't been called yet.
        

    def getPos(self):
        return (self.rect.left,self.rect.top)
    
    def getDimensions(self):
        return (self.image.get_width(), self.image.get_height())
    
    def setImg(self, image):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()


class Snake(ennemy):
    def __init__(self,x,y, positionChaine, typeDeplacement , a=0, b=0):
        self.positionChaine=positionChaine
        self.deplacement = typeDeplacement
        if typeDeplacement == 2:
            self.a = a
            self.b = b
        ennemy.__init__(self,x,y, "images/chasseur1.png")
        self.image = pygame.transform.rotate(self.image,-75)
    def estTouche(self,x,y):
        if x > self.rect.left and x < self.rect.left+self.rect.right and y > self.rect.top and y < self.rect.top+self.rect.bottom:
            return True 
        else:
            return False
    
    def update(self, current_time, snakes, width, height):
        # Update every 10 milliseconds = 1/100th of a second.
        if self.next_update_time < current_time:
            self.rect.left -= 5
            
            # DEPLACEMENT EN COURBE SINUSALE
            if self.deplacement==1:
                self.rect.top =  math.cos(self.rect.left*0.02)*120+self.positionChaine
            
                # calcul de l'angle et rotation de l'image
                coefDir = -2.4*math.sin(0.02*self.rect.left)
                angle = math.degrees(math.atan(coefDir))  
                self.image = pygame.image.load("images/chasseur1.png")
                self.image = pygame.transform.rotate(self.image,-angle) 
            
                if self.rect.left<-200:
                    snakes.remove(self)
            #DEPLACEMENT EN DROITE        
            elif self.deplacement==2:
                self.rect.top = self.a*self.rect.left + self.b
                angle = math.degrees(math.atan(self.a))
                self.image = pygame.image.load("images/chasseur1.png")
                self.image = pygame.transform.rotate(self.image,-angle)
                if self.rect.left<0:
                    snakes.remove(self) 
        self.next_update_time = current_time + 10

class Shooter(ennemy):
    vie = 2
    compteurTir = 0
    switch = 0
    def __init__(self,x,y):
        ennemy.__init__(self,x,y, "images/vaisseaux/enemies/enemy1/enemy1_1.png")  
        self.image =  pygame.transform.scale(self.image, (80, 100))
    def estTouche(self,x,y , ennemy):
        if x > self.rect.left and x < self.rect.left+self.rect.right and y > self.rect.top and y < self.rect.top+self.rect.bottom:
            return True
        else:
            return False            
    
    def update(self, current_time, ship, ennemy):
        # Update every 10 milliseconds = 1/100th of a second.
        if self.next_update_time < current_time:
            self.rect.left -= 2      
            (_, shipPosY) = ship.getPos()
            if self.rect.top < shipPosY-10 and self.rect.top+3 < 600:
                self.rect.top += 4
            elif shipPosY+10 < self.rect.top and self.rect.top-3 > 0:
                self.rect.top -= 4
            if self.rect.left<-100:
                ennemy.remove(self)  
                   
            #animation    
            if self.switch == 0:
                self.image = self.image =  pygame.transform.scale(pygame.image.load("images/vaisseaux/enemies/enemy1/enemy1_2.png"), (80, 100))
                self.switch=1
            elif self.switch == 1:
                self.image = pygame.transform.scale(pygame.image.load("images/vaisseaux/enemies/enemy1/enemy1_1.png"), (80, 100))
                self.switch=0  
        self.next_update_time = current_time + 10
                    
    def tir(self, missilesShooter):
            self.compteurTir += 1
            if self.compteurTir%30 == 0:
                missilesShooter.append(Shot.shotShooterEnnemy(self.rect.left,self.rect.top+20))         
                          
   
'''
'' Ennemi qui se deplace aleatoirement
'''             
class Aleatoire(ennemy):
    vie = 2
    sens = 1
    switch = 0
    def __init__(self,x,y):
        ennemy.__init__(self,x,y, "images/vaisseaux/enemies/enemy2/enemy2_1.png")   
        self.image =  pygame.transform.scale(self.image, (50, 50))
        
    def estTouche(self,x,y , ennemy):
        if x > self.rect.left and x < self.rect.left+self.rect.right and y > self.rect.top and y < self.rect.top+self.rect.bottom:
            self.vie -= 1
            if self.vie == 0:
                ennemy.remove(self)
            else:
                self.image = self.image =  pygame.transform.scale(pygame.image.load("images/ship3.png") , (50, 50))
                self.image = pygame.transform.rotate(self.image,90)
            return True
        else:
            return False            
    
    def update(self, current_time, ennemy, height):
        # Update every 10 milliseconds = 1/100th of a second.
        if self.next_update_time < current_time:    
            self.rect.left -= 8
            if (self.rect.left)%25 == 0:
                self.sens = random.randint(0,1)   
            
            if self.sens == 0:
                if self.rect.top > height-20:
                    self.sens = 1
                    self.rect.top -= 3
                else:
                    self.rect.top += 3
                
            else:
                if self.rect.top < 20:
                    self.sens = 0
                    self.rect.top += 3
                else:
                    self.rect.top -= 3
            
            if self.rect.top > height-20:
                self.sens = 1
              
            if self.rect.left<-50:
                ennemy.remove(self)  
                   
            #animation    
            if self.switch == 0:
                self.image = pygame.transform.scale(pygame.image.load("images/vaisseaux/enemies/enemy2/enemy2_2.png") , (50, 50))
                self.switch=1
            elif self.switch == 1:
                self.image = pygame.transform.scale(pygame.image.load("images/vaisseaux/enemies/enemy2/enemy2_2.png") , (50, 50))
                self.switch=0  
        self.next_update_time = current_time + 10
                
            

        
   
     
    
        
        




