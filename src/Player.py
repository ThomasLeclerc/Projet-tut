import pickle

class Player:
    def __init__(self):
        self.record = 0
        self.money = 0
        #ameliorations possedees
        self.goldShipOn = False
        self.propulseurHorizontalOn = False
        self.aerofreinOn = False
        self.basicGunEvolution1On = False
        self.basicGunEvolution2On = False
        self.advancedGunOn = False
        self.advancedGunEvolution1On = False
        self.advancedGunEvolution2On = False
        #parametres generaux du jeu
        self.sound = True
        self.musicOn = True
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
        
        
    