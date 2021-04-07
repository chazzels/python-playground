def askDegree():return int(input("Enter a temperature value: "))
def askUnit():return str(input("Enter a single letter to indicate the temperature scale (C or F): ")).lower()
def c2f(cDeg):return (cDeg * 9/5) + 32 
def f2c(fDeg):return (fDeg - 32) * (5/9)
def finalOutput(cDeg, fDeg):
	global userDegreeVal
	print("You entered", userDegreeVal, "degrees", userUnitVal.title(), ">>>")
	print("The temperature in Celsius is", round(cDeg, 2))
	print("The temperature in Fahrenheit is", round(fDeg, 2))
#main
userDegreeVal = askDegree()
status = True
while status: 
	userUnitVal = askUnit()
	if userUnitVal == "c" or userUnitVal == "f":
		status = False
		if userUnitVal == "c":finalOutput(userDegreeVal, c2f(userDegreeVal))
		if userUnitVal == "f":finalOutput(f2c(userDegreeVal), userDegreeVal)
	else:print("You have made an incorrect selection. Try again.")