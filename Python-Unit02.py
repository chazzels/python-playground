def questionAsk():
	global status
	textOuput("Your color choices are red, blue, green, white or yellow.")
	userVal = str(input("Enter a color from the list above: ")).lower()
	print("")
	if userVal == "exit": status = False
	return userVal

def checkQuestion(userVal):
	result = colorDict.get(userVal, False)
	if result != False and len(str(result)) > 0: result = True
	return result

def printResult(validColor, userVal):
	if validColor: return "The color " + userVal + " in Spanish is " + colorDict.get(userVal)
	else: return "That is not a valid color for this program. Ese no es un color válido."

def textOuput(msg):
	print(str(msg))
	print("")

colorDict = {'red':"rojo", 'blue':"azul", 'green':"verde", 'white':"blanco", 'yellow':"amarillo"}
status = True
while status == True:
	userColor = questionAsk()
	validColor = True
	validColor = checkQuestion(userColor)
	textOuput(printResult(validColor, userColor))