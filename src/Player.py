import pygame, sys

class player:
    #best_score = getBestScore()
	score = 0
	def __init__(self,name):
		self.name = name
    
	def raiseScore(self, nombre):
		self.score += nombre

	#def beatBestScore():
	#	if score > best_score:
			# afficher

	def reinitialiserScore(self):
		self.score=0

	def getScore(self):
		return self.score
	#def getBestScore():
		#TODO
		