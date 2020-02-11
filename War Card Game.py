
initialDeck=[]	
finalDeck = []
finalDeck2 = []
pot=[]
#creates list variables

fd =''
fd2=''
fd3=''
fd4=''
#creates string variables

import random
#imports random module

condition = 0
condition2 = 0
#creates two number variables

def deckCreator1():#function that creates the deck
	global initialDeck #states global variable
	
	suits = ["Clubs","Diamonds", "Spades", "Hearts"]
	numbers = ["Two of","Three of","Four of","Five of","Six of","Seven of","Eight of","Nine of","Ten of","Jack of","Queen of","King of","Ace of"]
	#creates card portions

	for i in range(13):
		initialDeck.append("%s %s" %(numbers[i],suits[0]))
		initialDeck.append("%s %s" %(numbers[i],suits[1]))	
		initialDeck.append("%s %s" %(numbers[i],suits[2]))
		initialDeck.append("%s %s" %(numbers[i],suits[3]))
	#for loop puts the deck together	

def shuffleDeck(deck):#function that shuffles the deck
	for i in range(len(deck)):
		t = deck[i]
		s = random.randrange(len(deck))
		deck[i] = deck[s]
		deck[s] = t
	return deck
	#moves the deck around by swapping indicies of an already randomized list

def selectFirstWord(string):
	return string.partition(' '[0])[0]
	#function that grabs the first word in a string 

def threeCondFunc():#function that determines who wins when both cards are equal to each other
	global pot
	global finalDeck2
	global finalDeck
	#states global variables

	fd3 = pot[4]
	fd4 = pot[9]
	#string variables equal list indicies

	print("---------------")
	print("(You  ||  CPU)")
	print("("+fd3+"||"+fd4+")")
	#interface
		   
	valueDict2 = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}
	#dictionary that assigns numerical values to words

	uVal2 = valueDict2[selectFirstWord(fd3)]
	cpuVal2 = valueDict2[selectFirstWord(fd4)]
	#gets the user and cpu values of their cards by getting th first word of their card names and using the dictionary

	if uVal2 > cpuVal2:
		condition2 = 1
	elif uVal2 < cpuVal2:
		condition2 = 2
	elif uVal2 == cpuVal2:
		condition2 = 3
	#compares the values and gives a variable a numerical value in relation to the outcome

	if condition2 == 1:#if the users card value is higher than the cpu's

		finalDeck.extend(pot)#user wins back his/her cards and the cpu's cards
		pot =[]#the seperate pot that was containing their cards is now empty
								
		print("Your card value was greater than the computers, you take all ten cards and add them to your deck.")
		print("( Your amount of cards:  %s ||  computers amount of cards: %s )" %((str(len(finalDeck))),(str(len(finalDeck2)))))
		print("__________________________________________________________________________________________")
		print("__________________________________________________________________________________________")
		#interface

		continu = input("Press enter to continue")
		while len(continu) > 0:
			continu = input("Just Press enter to give your top card and the cpu will give its own.")
		#requests user input for next action	

	elif condition2 == 2:#if the users card value is less than the cpu's
								
		finalDeck2.extend(pot)#user wins back his/her cards and the cpu's cards
		pot =[]#the seperate pot that was containing their cards is now empty
						
		print("Your card value was less than the computers, the computer takes all ten cards and adds them to its deck.")
		print("( Your amount of cards:  %s ||  computers amount of cards: %s )" %((str(len(finalDeck))),(str(len(finalDeck2)))))
		print("__________________________________________________________________________________________")
		print("__________________________________________________________________________________________")
		#interface

		continu = input("Press enter to continue")
		while len(continu) > 0:
			continu = input("Just Press enter to give your top card and the cpu will give its own.")
		#requests user input for next action

	elif condition2 == 3:#if the users card value is equal to the cpu's
		potFunction()#runs pot function

def potFunction():#Function that creates a seperate list containing some of the cards
	global pot
	global finalDeck2
	global finalDeck
	#states global variables

	print("__________________________________________________________________________________________")
	bonus = input("You Both have the same card value! Press enter to give three more cards and flip over the fourth one.")
	print("__________________________________________________________________________________________")
	while len(bonus) > 0:
		bonus = input("Just Press enter to give your fourth card and the cpu will give its own.")
	#requests user input for next action	

	pot.extend(finalDeck[:5])
	pot.extend(finalDeck2[:5])
	#adds the top five cards from both decks into a new list

	del finalDeck[:5] 
	del finalDeck2[:5]
	#takes the cards out of the two decks

	if len(pot) !=0:
		threeCondFunc()
		#runs the next comparison function once the pot is populated

def cardComparator():#first function that compares the cards

	num = 0 #numerical value representing the number of times "live" has looped

	layerInput = input("Welcome to War! Press enter to give your top card and the cpu will give its own. if you or the computer has less than 5 cards and both of your flipped cards are the same then the person with more cards wins by default")
	while len(layerInput) > 0:
		layerInput = input("Just Press enter to give your top card and the cpu will give its own.")
	#gives intro message and asks for user input
		
	else:
		live = True

		while live:

			num +=1	#everytime "live" runs the value of num increases by 1

			if num == 10:
				random.shuffle(finalDeck)
				random.shuffle(finalDeck2)
				num = 0

			try:#while the program can still grab the first indicie of a players deck

				fd = str(finalDeck[0])
				fd2 = str(finalDeck2[0])

				print("---------------")
				print("(You  ||  CPU)")
				print("("+fd+"||"+fd2+")")
			   	#interface

				valueDict = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}
				#dictionary that assigns numerical values to words

				uVal = valueDict[selectFirstWord(fd)]
				cpuVal = valueDict[selectFirstWord(fd2)]
				#gets the user and cpu values of their cards by getting th first word of their card names and using the dictionary

				if uVal > cpuVal:
					condition = 1
				elif uVal < cpuVal:
					condition = 2
				elif uVal == cpuVal:
					condition = 3
				#compares the values and gives a variable a numerical value in relation to the outcome


				if condition == 1:#if the users card value is higher than the cpu's
				
					finalDeck.append(finalDeck.pop(0))#keeps the top card and puts it at the bottom
					finalDeck.append(finalDeck2.pop(0))#takes the other card and 

					print(".")			
					print("Your card value was greater than the computer, you take both cards and add them to your deck.")
					print("( Your amount of cards:  %s ||  computers amount of cards: %s )" %((str(len(finalDeck))),(str(len(finalDeck2)))))
					print("__________________________________________________________________________________________")
					print("__________________________________________________________________________________________")
					#interface

					continu = input("Press enter to continue")
					while len(continu) > 0:
						continu = input("Just Press enter to give your top card and the cpu will give its own.")
					#requests user input for next action	

				elif condition == 2:#if the users card value is less than the cpu's
			
					finalDeck2.append(finalDeck.pop(0))
					finalDeck2.append(finalDeck2.pop(0))

					print(".")
					print("Your card value was less than the computer, the computer takes both cards and adds them to its deck.")
					print("( Your amount of cards:  %s ||  computers amount of cards: %s )" %((str(len(finalDeck))),(str(len(finalDeck2)))))
					print("___________________________________________________________________________________________")
					print("___________________________________________________________________________________________")
					#interface


					continu = input("Press enter to continue")
					while len(continu) > 0:
						continu = input("Just Press enter to give your top card and the cpu will give its own.")
					#requests user input for next action	


				elif condition == 3:#if the users card value is equal to the cpu's
					potFunction()#runs pot function


			except:
					if len(finalDeck) > len(finalDeck2):
						print("The game is over you won!")
						live = False
						return ""
					else:
						print("The game is over the computer won!")
						live = False
						return ""
						

deckCreator1()
newDeck = shuffleDeck(initialDeck)
finalDeck.extend(newDeck[:26])
finalDeck2.extend(newDeck[26:])
cardComparator()

''' DEV NOTES:
 - If the game runs and there is a war within a war it loops. Just restart the program, this error shouldn't occur too often.
   Given the way I programmed it, theoretically should allow for a war within a war but I couldn't seem to find what was preventing
   it from functioning.
'''