import csv 
record = []
line = int(0)
col = int(0)
with open("./IT244_U5_Data.txt") as csvFile:
	csvParsed = csv.reader(csvFile, delimiter=',')
	for row in csvParsed:
		record.append([])
		for el in row:
			col += 1
			record[line].append(el)
		col = 0
		line += 1

record.append(["5","Brady","Bobby","4222 Clinton Way","Los Angeles","CA"])
for entry in range(len(record)):
	for el in range(len(record[entry])+1):
		if el == len(record[entry]):  record[entry].append("$500")

record.insert(0, ["Customer ID", "Last Name", "First Name", "Address", "City", "State", "Promo Credit"])

with open('IT244_U5_PromoCredit.csv', 'w+', newline ='')  as csvFile:
	csvOutput = csv.writer(csvFile, delimiter=',')
	for row in range(len(record)):
		csvOutput.writerow(record[row])

print("There were", len(record)-1, "records written to the promo credits csv file.")