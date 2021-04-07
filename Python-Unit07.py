from random import randrange

class GolfHole:
	def __init__(self, numArg, scoreArg, parArg):
		self.number = int(numArg)
		self.score = int(scoreArg)
		self.par = int(parArg)
	def setScore(self, score): 
		self.score = int(score)
		print(self.checkPar(), self.checkResult())
	def checkResult(self):return "on hole #" + str(self.number) + " with a par of " + str(self.par)
	def checkPar(self):
		if self.score > self.par:return "You scored Over Par"
		if self.score < self.par:return "You scored Under Par"
		if self.score == self.par: return "You are at Par"

def scoreUser():
	userHole = int(input("Enter the hole number: "))
	userScore = input("Enter you score: ")
	if userHole == 1: hole1.setScore(userScore)
	elif userHole == 2: hole2.setScore(userScore)
	elif userHole == 3: hole3.setScore(userScore)
	else: print("Hole not found. no score set.")
	print("")

hole1 = GolfHole(1, 0, randrange(2,5))
hole2 = GolfHole(2, 0, randrange(3,5))
hole3 = GolfHole(3, 0, randrange(3,5))
while True:scoreUser()