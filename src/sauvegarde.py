import os
import pickle

CHEMIN = "C:/Users/Eollys/Documents/workspace/ProjetTut/jeu/saves"
os.chdir(CHEMIN)

score = {
         "money": 1,
         "score": 2,
         "selected_ship": 3,
         }

with open('donnees.txt', 'wb') as fichier:
    save_picker = pickle.Pickler(fichier)
    save_picker.dump(score)
    print("partie sauvegardee")