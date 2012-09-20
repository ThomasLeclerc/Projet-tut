"""
Le curseur utilisé pour naviguer entre chaque option
du menu. Sa position sera analysée afin de déterminer
l'option à sélectionner
"""
class curseur:
    positionCurseur = 0
    pasCurseur = 0
   

    def __init__(self, pos, pas):
        self.positionCurseur = pos
        self.pasCurseur = pas

    def setPosition(self, pos):
        self.positionCurseur = pos
    
    def setPas(self, pas):
        self.pasCurseur = pas
    
    def getPosition(self):
        return self.positionCurseur;
    
    def estPositionne(self, position):
        if self.getPosition() == position:
            return True
        else: return False