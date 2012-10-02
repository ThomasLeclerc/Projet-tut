import pickle

class player:
    def __init__(self):
        self.record = 0
        #ameliorations possedees
        self.propulseurHorizontal = False
        self.aerofrein = False
        self.basicGunEvolution1 = False
        self.basicGunEvolution2 = False
        self.advancedGun = False
        self.advancedGunEvolution1 = False
        self.advancedGunEvolution2 = False
        #parametres generaux du jeu
        self.sound = True
        self.mucis = True
        self.name = "Player"
    
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
        
        
    