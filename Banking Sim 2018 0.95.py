from datetime import datetime
now = datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
#imports datetime library and grabs details in seperate variables

user =""
iniMoney = 0

def login(year,month,day,hour,minute,iniMoney,user):

	print("-----------------------------------------------------------------------------------------------")
	print("_________________________________!Welcome to Thirsk Banking!___________________________________")
	print("-----------------------------------------------------------------------------------------------")
	print(".")
	print(".")
	user = input("Enter a user name to get started: ")
	#prints UI plus asks for input

	while len(user) == 0:#if nothing is typed	
		print(".")
		print(".")
		user = input("Enter a user name to get started:")

	try: #trys running all of its code without error
		userFile = open(""+user+"s Bank Note.txt", "r")
		alllines = userFile.readlines()
		userFile.close()
		#checks to see if bank account exists

		for line in alllines[:1]:
			line = str(line)
		#grabs password from text file

		print(".")
		print("Account has been found!")
		print(".")
		passW = input("Give your password: ")
		#asks for password

		while passW != line[:-1]:# compares input with password grabbed from text file, while it doesnt match
			print(".")
			passW = input("That is not the right password of this account, passowrd: ")

		#if the password is correct VVV
		print(".")
		print("Welcome back!")
		command(year,month,day,hour,minute,user)# goes to command function

	except:# if the bank account doesnt exist and an error is made
		print("-")
		print("-")
		print("We have detected that this account does not exist!")
		print(".")
		cmd = input("Enter |S| to search for another account or |N| to make a new one with the user you typed: ")
		#asks if user wants to search again or make that username a new account

		while cmd.lower() != "s" and cmd.lower() != "n":
			print(".")
			cmd = input("Search or new s/n: ")
		#verifies that appropriate input was made

		if cmd.lower() == "s":
			login(year,month,day,hour,minute,iniMoney,user)# runs login function again

		elif cmd.lower() == "n":
			print(".")
			passW = input("Give us a passowrd (5 characters long) : ")
			#asks user to make password 5 characters long

			while len(passW) < 5 or len(passW) > 5:
				print(".")
				passW = input("Your password must be no more and no less than 5 characters long! password: ")
			#verifies appropiate input was made

			with open(""+user+"s Bank Note.txt",'w') as userFile:
				userFile.write(passW+"\n")
				userFile.write("-----------------------------------------------------------------------------------------------\n")
				iniMoney +=100
				userFile.write("TOTAL CURRENT MONEY:\n")
				userFile.write(str(iniMoney)+"\n")
				userFile.write("\n")
				userFile.write("BANK HISTORY:\n")
				userFile.write("\n")
				print(".")
				print("Wellcome "+user+"! We are starting you off with $100!")
				userFile.write(user+" Has deposited $100 @ "+str(year)+";"+str(month)+";"+str(day)+";"+str(hour)+";"+str(minute)+"\n ")
				userFile.write("\n")
			# creates bank history text file for user and starts them off with $100

	command(year,month,day,hour,minute,user)# goes to command function

def command(year,month,day,hour,minute,user):

	print(".")
	action = input("You can VIEW,DEPOSIT,TRANSFER and WITHDRAW! Press V to view, D to deposit, T to transfer and W to withdraw: ")
	#asks for input
	while action.lower() != "d" and action.lower() != "v" and action.lower() != "w" and action.lower() != "t":
			print(".")
			action = input("View Deposit Transfer or Withdraw? v/d/t/w : ")
	#verifies input 

	if action.lower() == "d":
		deposit(user,year,month,day,hour,minute)
	elif action.lower() == "w":
		withdraw(user,year,month,day,hour,minute)
	elif action.lower() == "v":
		view(year,month,day,hour,minute,user)
	elif action.lower() == "t":
		transfer(year,month,day,hour,minute,user)
	#each command goes to its appropriate function	
		
def view(year,month,day,hour,minute,user):

	with open(user+"s Bank Note.txt",'r') as userFile:
		alllines = userFile.readlines()
		for line in alllines[1:]:#every line except the first
			print(line, end="")

	print("-----------------------------------------------------------------------------------------------")
	#opens the text file associated with the account, gets its contents and prints everything as
	#a string in the console with the exception of the password which is on the first line

	cOrLO(year,month,day,hour,minute,user)#goes to continue or log out function		
	
def withdraw(user,year,month,day,hour,minute):
	print(".")
	witt = input("How much would you like to withdraw? ")
	#asks for input

	while witt.isnumeric() == False:
		print(".")
		witt = input("You must give a numerical value (ex: type 10 for ten dollars)! ")
	#verifies input is a number 
	witt = int(witt)
	#makes input an integer
	while witt <1: 
		print(".")
		print("You cannot withdraw nothing!")
		withdraw(user,year,month,day,hour,minute)
	#verifies the input again

	with open(user+"s Bank Note.txt",'r+') as userFile:
		line = userFile.readlines()
		i = int(line[3][:-1])
		#opens bank history text file, grabs the current money on line 4 and converts it into an integer var
		while witt >= i:
			print(".")
			print("Total Money Available: "+str(i))
			print("You cannot withdraw more than you have, or all of your money at once.")
			withdraw(user,year,month,day,hour,minute)
		#goes through final input verification process and if it fails the function restarts 

		totalMon = i - witt 
		totalMon = str(totalMon)
		#creates total money var and makes it equal to the total current money subtracted by the input var
		#it then becomes a string
		print(".")
		print("Money Left: "+totalMon)
		#tells user their new balance
		content = line[2:]
		# saves all the lines of the text file starting with line 4 into a var
		content[1] = totalMon
		#gets the line with current money and replaces it with the new total
		content[1] = (content[1]+"\n")
		#adds newline tag to the new total
		line[2:] = content
		# makes everything after line 3 in the text file equal the updated var 

	with open(user+"s Bank Note.txt", 'w') as userFile:
		userFile.write("".join(line))
		userFile.write(user+" Has withdrawn $"+str(witt)+" @ "+str(year)+";"+str(month)+";"+str(day)+";"+str(hour)+";"+str(minute)+"\n ")
		userFile.write("\n")
		#rewrites to the file with the new balance, existing history, and new actions made
	print(".")
	print("Transaction complete!")
	#tells user that the transaction worked
	cOrLO(year,month,day,hour,minute,user)#goes to continue or log out function	

def deposit(user,year,month,day,hour,minute):
	print(".")
	dep = input("How much would you like to deposit? (ex: type 10 for ten dollars) ")
	#asks for input 

	while dep.isnumeric() == False:
		print(".")
		dep = input("You must give a numerical value (ex: type 10 for ten dollars)! ")
	#verifies input is a number

	dep = int(dep)
	#makes input an integer

	with open(user+"s Bank Note.txt",'r+') as userFile:
		line = userFile.readlines()
		i = int(line[3][:-1])
		#opens bank history text file, grabs the current money on line 4 and converts it into an integer var
		totalMon = dep + i
		totalMon = str(totalMon)
		#creates total money var and makes it equal to the total current money added to the input var
		#it then becomes a string
		print(".")
		print("Total Money Available: "+totalMon)
		#tells user their new balance
		content = line[2:]
		# saves all the lines of the text file starting with line 4 into a var
		content[1] = totalMon
		#gets the line with current money and replaces it with the new total
		content[1] = (content[1]+"\n")
		#adds newline tag to the new total
		line[2:] = content
		# makes everything after line 3 in the text file equal the updated var 

	with open(user+"s Bank Note.txt", 'w') as userFile:
		userFile.write("".join(line))
		userFile.write(user+" Has deposited $"+str(dep)+" @ "+str(year)+";"+str(month)+";"+str(day)+";"+str(hour)+";"+str(minute)+"\n ")
		userFile.write("\n")
		#rewrites to the file with the new balance, existing history, and new actions made
	print(".")
	print("Transaction complete!")#tells user that the transaction worked
	cOrLO(year,month,day,hour,minute,user)#goes to continue or log out function	    

def transfer(year,month,day,hour,minute,user):

	user2 = input("Type the username that you wish to transfer money to: ")
	#asks for the username the user wants to transfer money to
	while len(user2) == 0:	
		print(".")
		print(".")
		user2 = input("Type the username that you wish to transfer money to: ")
	#verifies input

	try:# trys to grab the username and transfer money to the other user
		userFile2 = open(""+user2+"s Bank Note.txt", "r")
		alllines2 = userFile2.readlines()
		userFile2.close()
		#tries opening and closing the file

		print(".")
		print("Account has been found!")
		print(".")
		tr = input("How much would you like to transfer? (ex: type 10 for ten dollars) ")
		#asks for input
		while tr.isnumeric() == False:
			print(".")
			tr = input("You must give a numerical value (ex: type 10 for ten dollars)! ")
		#verifies input is a number 
		tr = int(tr)
		#makes input an integer
		while tr <1: 
			print(".")
			print("You cannot transfer nothing!")
			transfer(user,year,month,day,hour,minute)
		#verifies the input again
		with open(user+"s Bank Note.txt",'r+') as userFile:
			line = userFile.readlines()
			i = int(line[3][:-1])
		#opens bank history text file for first user, grabs the current money on line 4 and converts it into an integer var
			while tr >= i:
				print(".")
				print("Total Money Available: "+str(i))
				print("You cannot withdraw more than you have, or all of your money at once.")
				transfer(user,year,month,day,hour,minute)
			#goes through final input verification process and if it fails the function restarts 

			totalMon = i - tr
			totalMon = str(totalMon)
			#creates total money var and makes it equal to the total current money subtracted by the input var
			#it then becomes a string
			print(".")
			print("Total Money Available: "+totalMon)
			#tells user their new balance
			content = line[2:]
			# saves all the lines of the text file starting with line 4 into a var
			content[1] = totalMon
			#gets the line with current money and replaces it with the new total
			content[1] = (content[1]+"\n")
			#adds newline tag to the new total
			line[2:] = content
			# makes everything after line 3 in the text file equal the updated var 
			
			with open(user+"s Bank Note.txt",'w') as userFile:
				userFile.write("".join(line))
				userFile.write(user+" Has transfered $"+str(tr)+" @ "+str(year)+";"+str(month)+";"+str(day)+";"+str(hour)+";"+str(minute)+" to "+user2+"s account!\n ")
				userFile.write("\n")
				#rewrites to the first users file with the new balance, existing history, and new actions made

		with open(user2+"s Bank Note.txt",'r+') as userFile2:
			line2 = userFile2.readlines()
			i2 = int(line2[3][:-1])
			#opens bank history text file for first user, grabs the current money on line 4 and converts it into an integer var
			totalMon2 = i2 + tr
			totalMon2 = str(totalMon2)
			#creates total money var 2 for second account and makes it equal to the total current money of that user + the input var
			#it then becomes a string
			content2 = line2[2:]
			# saves all the lines of the text file starting with line 4 into a var
			content2[1] = totalMon2
			#gets the line with current money and replaces it with the new total
			content2[1] = (content2[1]+"\n")
			#adds newline tag to the new total
			line2[2:] = content2
			# makes everything after line 3 in the text file equal the updated var 

			with open(user2+"s Bank Note.txt",'w') as userFile2:
				userFile2.write("".join(line2))
				userFile2.write(user2+" Has been transfered $"+str(tr)+" @ "+str(year)+";"+str(month)+";"+str(day)+";"+str(hour)+";"+str(minute)+" from "+user+"s account!\n ")
				userFile2.write("\n")
				#rewrites to the 2nd users file with the new balance, existing history, and new actions made
		print(".")
		print("Transaction complete!")    
		cOrLO(year,month,day,hour,minute,user)#goes to continue or log out function	

	except:# if the user doesn't exist and error is found
		print("-")
		print("-")
		print("We have detected that this account does not exist!")
		cmd = input("Press |S| to search for another account or |C| to pick a different command: ")
		# asks if user wants to search again or go to a different command
		while cmd.lower() != "c" and cmd.lower() != "s":
			print(".")
			cmd = input("Press |S| to search for another account or |C| to pick a different command: ")
		#verifies input
		if cmd.lower() == "c":
			command(year,month,day,hour,minute,user)
		elif cmd.lower() == "s":
			transfer(user,year,month,day,hour,minute)	
		#each input leads to appropriate function

def cOrLO(year,month,day,hour,minute,user):
	print(".")
	cmd = input("Would you like to continue? (c) or would you like to logoff (l)? ")
	# asks if user wants make a different command or log out
	while cmd.lower() != "c" and cmd.lower() != "l":
		print(".")
		cmd = input("Continue (c) or logoff (l)? ")
	#verifies input
	if cmd.lower() == "c":
		command(year,month,day,hour,minute,user)
	elif cmd.lower() == "l":
		print("You have logged off!")
		login(year,month,day,hour,minute,iniMoney,user)
	#each input leads to appropriate function 
	#if the user logs off the program restarts so another user can log in
		
login(year,month,day,hour,minute,iniMoney,user)#starts the program 

