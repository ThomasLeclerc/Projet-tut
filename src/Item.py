import Player

class item:
    bought = False
    player = Player.player()
    
    
    def __init__(self, bought, player):
        self.player = player
        self.bought = bought
        
    ''' Retourne vrai si l'item courant a été acheté '''     
    def isAchete(self):
        if self.bought:
            return True
        else: return False
    
    ''' Definit le deroulement de l'achat d'un item '''
    def purchase(self, cost, skin):
        
        score = self.player.getScore()
        if self.isAchete() == True:
            print("Vous avez déjà acheté cet objet !")
        elif score >= self.cost:
            #player.setScore(score - self.cost)
            #vaisseau.setSkin(self.skin)
    
        
        
    