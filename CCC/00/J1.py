from math import ceil

case = input().split()
startDay, numberOfDays = int(case[0]), int(case[1])

def genRow(row):
	res = ""
	for n in range(row[0], row[1] + 1):
		if n < 10:
			res += "  " + f"{n}"
		else:
			res += " " + f"{n}"
		
		if n != row[1]:
			res += " "

	return res
		
def nextRow(prevRow):
	res = [prevRow[1] + 1, prevRow[1] + 7]
	if res[1] > numberOfDays:
		res[1] = numberOfDays
	return res

# Set up the first row
row = [1, 8 - startDay]
printRow = ""
for _n in range(startDay - 1):
	printRow += "    "

# Print the rest of the rows
print("Sun Mon Tue Wed Thr Fri Sat")
numberOfRows = ceil((startDay - 1 + numberOfDays) / 7)

for n in range(numberOfRows):
	printRow += genRow(row)
	print(printRow)

	row = nextRow(row)
	printRow = ""