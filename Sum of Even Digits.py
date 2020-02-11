#inputs file by line
def fileCheck():
	start = input("Press any key to begin!")

	try:
		numHashFile = open("dataFile.txt","r")
		numbersByLine = numHashFile.readlines()
		textFile.close()

		for i in range(len(numbersByLine)):
			numbersByLine[i] = int(numbersByLine[i])

		return numbersByLine
		print(numbersByLine)
		menu()

	except:
		print("The file required to run this program is missing: (dataFile.txt), please grab it from Blenkhornes D2L shell!")
		return ""

#finds greatest number in file
def greatestNumFunc(numInput):
	remaingNum = numInput#starting num
	testedNum = []#numbers that have been tested
	winingNum = []#Largers numbers in the round
	while not(len(remaingNum) == 1):#does rounds until only one num in remaing num
		for i in range(len(remaingNum)):#for loops starts round
			if not(i == len(remaingNum)-1):#checks if number is last. If it is then does not check it as it will already be checked
				if remaingNum[i] >  remaingNum[i+1]:#if num a > b
					if not(remaingNum[i] in testedNum):#checks if the winner has been tested
						winingNum.append(remaingNum[i])#if not puts winner in the winners lists
				else:
					if not(remaingNum[i+1] in testedNum):
						winingNum.append(remaingNum[i+1])
				testedNum.append(remaingNum[i])#puts the two numbers/combatants in the tests lists
				testedNum.append(remaingNum[i+1])
		remaingNum = winingNum#all lossing numbers get elimanated and makes wining numbers in remaing num for next round
		testedNum = []#emptes tested nums and winning nums for next round
		winingNum = []
	return remaingNum[0]

def leastNumFunc(numInput):#works exactly the same as greatest nums except conddiont ">" is replaced with "<"
	remaingNum = numInput
	testedNum = []
	winingNum = []
	while not(len(remaingNum) == 1):
		for i in range(len(remaingNum)):
			if not(i == len(remaingNum)-1):
				if remaingNum[i] <  remaingNum[i+1]:#change happened here
					if not(remaingNum[i] in testedNum):
						winingNum.append(remaingNum[i])
				else:
					if not(remaingNum[i+1] in testedNum):
						winingNum.append(remaingNum[i+1])
				testedNum.append(remaingNum[i])
				testedNum.append(remaingNum[i+1])
		remaingNum = winingNum
		testedNum = []
		winingNum = []
	return remaingNum[0]

#sumOfAllNum
def sOEDFunc(numInput):
	evenNum = []#list for all even numbers
	sOED = 0#final number
	for i in range(len(numInput)):#loop that checks if numbers are even
		if numInput[i] %2 == 0:
			evenNum.append(numInput[i])
	for i1 in range(len(evenNum)):#loop that gets each even number
		number = str(evenNum[i1])#makes number equal to the the current even number as a string
		for i2 in range(len(number)):#loop to add each digit
			sOED = sOED + int(number[i2])#turns each digit to int and then adds to final number
	return sOED#returns final number

def menu():
	print("1 = greatest Number")#gives choices for user
	print("2 = smallest Number")
	print("3 = sum of all even Numumber digits")
	userChoice =  input("input all choices you want.Ex.123,231,21	-	")
	for i in range(len(userChoice)):#loop that gets everything the user wants
		if userChoice[i] == "1":
			print("The greatest number from the file is " + str(greatestNum(file)))
			print("")
		elif userChoice[i] == "2":
			print("The smallest number from the file is " + str(leastNum(file)))
			print("")
		else:
			print("The sum of all the digits of every even numbers is " + str(sOEDFunc(file)))
			print("")
	print("")#resarts function
	print("")
	menu()

fileCheck()