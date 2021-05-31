import re
import convertToMiles
import convertToKilometers

class Convert:
	def __init__(self):()
	def convert(self, distance, unit):
		if unit == convertToKilometers.kilometerUnit:
			return self.convertMiles(distance)
		elif unit == convertToMiles.milesUnit:
			return self.convertKilometers(distance)
		else:
			return None
	def convertMiles(self, distance):return str(round(convertToMiles.kmToMiles(distance),2))+' miles'
	def convertKilometers(self, distance):return str(round(convertToKilometers.milesToKm(distance),2))+' kilometers'

class UserInterface:
	def __init__(self):
		self.running = False
		self.convert = Convert()
		self.response = ''
		self.start()
	def start(self):
		self.running = True
		while self.running == True:
			status = self.mainQuestion()
			if status != None and status != 'exit':
				print()
				print(self.response, ' = ', status)
				print()
			elif status == 'exit':
				return
			else:
				print()
				print("there was an issue with the input. please try again")
				print()
	def exit(self):
		self.running = False
	def mainQuestion(self):
		print("Convert a distance from Miles to KM or KM to Miles")
		print('[type exit to stop processing] (units auto-detected)')
		inputDistance = str(input("Enter distance to convert: "))
		self.response = inputDistance
		if inputDistance.lower() == 'exit':
			self.exit()
			return 'exit'
		else:
			result = self.processAnswer(inputDistance)
			if result == None:
				print()
				print('there was an issue with the input. please try again.')
				print()
				return None
			else:
				return self.convert.convert(result.get('distance'), result.get('unit'))
	def processAnswer(self, ans):
		if len(ans) >= 2:
			ans = ans.strip().replace(' ', '').lower()
			intNum = re.search(r'[0-9]+', ans)
			floatNum = re.search(r'[0-9]+\.[0-9]+', ans)
			if intNum == None and floatNum == None:
				print('input error')
				return None
			elif floatNum == None and intNum != None:
				distance = int(ans[intNum.start(0):intNum.end(0)])
				unit = ans[intNum.end(0):len(ans)]
			elif floatNum != None and intNum != None:
				distance = float(ans[floatNum.start(0):floatNum.end(0)])
				unit = ans[floatNum.end(0):len(ans)]
			return {'distance': distance, 'unit': unit}
		else:
			print()
			print("input error")
			print()
			return None


program = UserInterface()