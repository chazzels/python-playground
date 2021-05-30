import convertToMiles
import convertToKilometers

class Convert:
	def __init__(self):
		print('init')
	def convertMiles(self, distance):
		convertToMiles.kmToMiles(distance)
	def convertKilometers(self, distance):
		convertToKilometers.milesToKm(distance)
	def detectUnits(self, units):
		units = str(units).lowercase()
		if units == convertToKilometers.kilometerUnit:
			print('km unit')
		elif units == convertToMiles.milesUnit:
			print('miles unit')
		


class UserInterface:
	def __init__(self):
		self.running = False
		self.convert = Convert()
		print('init')
		self.start()
	def start(self):
		self.running = True
		while self.running == True:
			self.mainQuestion()
	def exit(self):
		self.running = False
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