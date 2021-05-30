from convertToMiles import kmToMiles
from convertToKilometers import milesToKm



class UserInterface:
	def __init__(self):
		self.running = False
		print('init')
		self.start()
	def start(self):
		self.running = True
		while self.running == True:
			self.mainQuestion()
	def mainQuestion(self):
		print("Convert a distance from Miles to KM or KM to Miles")
		inputDistance = str(input("Enter distance to convert (eg 2m or 2km) "))
		self.processAnswer(inputDistance)
	def processAnswer(self, ans):
		if len(ans) >= 2:
			ans = ans.strip().replace(' ', '')
			print(ans)
		else:
			print("input error")


program = UserInterface()