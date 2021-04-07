from random import randrange

class IceCream:
	def __init__(self):
		self.sizes = {}
		self.flavors = ["Vanilla", "Chocolate", "Strawberry", "Pistachio", "Butter Pecan", "Cookie Dough", "Neapolitan"]
	def addSize(self,name,price,desc):
		newSize = ItemSize(name,price,desc)
		self.sizes.update({newSize.name: newSize})
	def changeFlavor(self, index, newName):
		if(0 < index < len(self.flavors)):
			self.flavors[index] = str(newName).title()
	def addFlavor(self, newName):
		self.flavors.append(str(newName).title())
	def sortFlavors(self):
		self.flavors.sort()

class ItemSize():
	def __init__(self, sizeName, sizePrice, sizeDescription):
		self.name = str(sizeName).title()
		self.price = int(sizePrice)
		self.desc = str(sizeDescription)

def iceCreamSelect(ic):
	global status
	userSize = str(input('Please enter the cone size of your choosing: S, M, or L: '))
	userFlavor = int(input('Please enter your flavor number: '))
	print("")
	sizeValid = ic.sizes.get(userSize.title(), False)
	if(sizeValid != False and 0 < userFlavor <= len(ic.flavors)):
		print("Your total is:  $" + str('%.2f' % (sizeValid.price/100) ))
		print("Your", sizeValid.desc, "sized cone of The Ice Shop's", ic.flavors[userFlavor-1], "will arrive shortly.")
		print("")
		print("Thank you for visiting the Ice Cream Shop")
		status = False
	else:
		print("An invalid ice cream selection was made.")
		print("")

def displayFlavors(flavors):
	print("The Ice Cream Shop has", len(flavors), "flavors for sale:")
	print("------------------------------------")
	print("")
	for i in range(0, len(flavors)):
		print("#" + str(i+1), flavors[i])
	print("")
	print("------------------------------------")
	print("")

ic = IceCream()
ic.addSize("S", 150, "Small")
ic.addSize("M", 250, "Medium")
ic.addSize("L", 350, "Large")
ic.changeFlavor(randrange(0,len(ic.flavors)), "Rocky Road")
ic.addFlavor("Mint Chocolate Chip")
ic.sortFlavors()
displayFlavors(ic.flavors)

status = True
while status == True:
	iceCreamSelect(ic)
