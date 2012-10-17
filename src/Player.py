import pickle

class Player:
    additionalMissiles=0
    '''contenu de la liste shopStateList:
    0:goldskin
    1:basicWeapLvl2
    2:ExtremWeapLvl1
    3:ExtremWeapLvl2
    4:Booster
    5:Spoiler
    6:AdditionalMissile
       etat de larticle :
    -1 non dispo ; 0 dispo ; 1 achete'''
    def __init__(self):
        self.record = 0
        self.money = 0
        #parametres generaux du jeu
        self.soundOn = True
        self.musicOn = True
        self.shopStateList=[0,0,-1,-1,0,-1,0]
        self.prixMissile = 300
       
    def updateShopStateList(self,indice,newState):
        if indice in range(7):
            if newState in range(-1,2):
                self.shopStateList[indice]=newState
                self.save()
            else:
                print "usage : updateShopStateList(indice,nouvelEtat)"
        

    
    def save(self):
        f = open("saves/player_data.txt", 'wb')
        pickle.dump(self, f)
        f.close()

    # methode static (signalee par le @staticmethod)
    @staticmethod  
    def loadDatas():
        f = open("saves/player_data.txt", 'rb')
        return pickle.load(f)
        
        
    