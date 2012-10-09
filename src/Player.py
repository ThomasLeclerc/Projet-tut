import pickle

class Player:
    additionalMissiles=0
    def __init__(self):
        self.record = 0
        self.money = 0
        #ameliorations possedees
        #self.goldShipOn = False
        #self.propulseurHorizontalOn = False
        #self.aerofreinOn = False
        #self.basicGunEvolution1On = False
        #self.basicGunEvolution2On = False
        #self.advancedGunOn = False
        #self.advancedGunEvolution1On = False
        #self.advancedGunEvolution2On = False
        #parametres generaux du jeu
        self.sound = True
        self.musicOn = True
        self.name = "Player"
        '''contenu de la liste shopStateList:
        goldskin,basicWeapLvl2,ExtremWeapLvl1,ExtremWeapLvl2,Booster,Spoiler,AdditionalMissile
           etat de larticle :
        -1 non dispo ; 0 dispo ; 1 achete'''
        self.shopStateList = [0,0,-1,-1,0,-1,-1]
        
    def updateShopStateList(self,indice,newState):
        if indice in range(7):
            if newState in range(-1,2):
                self.shopStateList[indice]=newState
            else:
                print "usage : updateShopStateList(indice,nouvelEtat)"
        print "usage : updateShopStateList(indice,nouvelEtat)"
        
    def setName(self, name):
        self.name = name
    
    def save(self):
        f = open("saves/player_data.txt", 'wb')
        pickle.dump(self, f)
        f.close()

    # methode static (signalee par le @staticmethod)
    @staticmethod  
    def loadDatas():
        f = open("saves/player_data.txt", 'rb')
        return pickle.load(f)
        
        
    