initialDeck=[]	
dealer =[]
player =[]
player2 =[]

#lists


dealerVal=0
dealerValTwo=0
playerValOne=0
playerValTwo=0
playerValThree=0
player2ValOne=0
player2ValTwo=0
fullPVal=0
fullPVal2=0
fullDVal=0
hD=0
use=0
use2=0
bet=0
money = 100

#numerical values


sH1 = False
sH2 = False
tH1 = False
tH2 = False

bust = False
bust2 = False

#booleans

 
action =''
d=''
d2=''
p1=''
p2=''
p3=''
p1Two=''
p2Two=''

#strings


import random
# gets random library

print("")
print("-----------------------------------------------------------------------------------------------")
print("____________________________________!Welcome to Blackjack!_____________________________________")
print("-----------------------------------------------------------------------------------------------")
print("RULES RULES RULES RULES RULES RULES RULES RULES RULES RULES RULES RULES RULES RULES RULES RULES")
print("")
print("A round starts off when the dealer deals himself a card and you two cards. You then have the op")
print("-tion to HIT or STAND. If your two cards share the same value you SPLIT.")
print("")
print("HITTING: Both of your cards make a total value, thats your hand! When you HIT, you add another ")
print("card to your total value, increasing your hand value! The goal is to get that value to 21 or as")
print("close to 21 as possible without going over. If you go over 21 you LOSE.")
print("")
print("STANDING: When you STAND you stop HITTING and you let the dealer HIT. If his end value is over ")
print("21 or is less than yours you WIN. If his value is greater than yours you LOSE the round.")
print("")
print("SPLITING: When you SPLIT each of your first two cards becomes its own hand, effectively doubli")
print("-ng your chances of WINNING. The two hands go through the same process of HITTING and STANDING ")
print("for the rest of the round.")
print("")
print("BETTING: When you start your game you must bet part of the money you have. If you win the round ")
print("you get double the money back, if you lose the round you lose the money you bet, if you tie you ")
print("get back the money you initially bet. If you get a value of exactly 21, thats a blackjack and ") 
print("you get 1.5 times the money you bet back. If you lose all of your money the game ends! ")
print(".")
#instructions


valueDict = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,}
aceVal = {'Ace':11}
#dictionaries for ace and other cards


def deckCreator():
	
	
	suits = ["Clubs","Diamonds", "Spades", "Hearts"]
	numbers = ["Two of","Three of","Four of","Five of","Six of","Seven of","Eight of","Nine of","Ten of","Jack of","Queen of","King of","Ace of"]

	for i in range(13):
		initialDeck.append("%s %s" %(numbers[i],suits[0]))
		initialDeck.append("%s %s" %(numbers[i],suits[1]))	
		initialDeck.append("%s %s" %(numbers[i],suits[2]))
		initialDeck.append("%s %s" %(numbers[i],suits[3]))

#creates a deck of cards
		
def shuffleDeck(deck):
	for i in range(len(deck)):
		t = deck[i]
		s = random.randrange(len(deck))
		deck[i] = deck[s]
		deck[s] = t
	return deck

#shuffles the deck

def selectFirstWord(string):
	return string.partition(' '[0])[0]

#grabs the first word of a string, can be passed through different variables

def restart():
	global player
	global dealer
	global player2
	global newDeck
	global initialDeck
	global hD
	global p1
	global p2
	global p3
	global d2
	global d
	global p1Two
	global p2Two

	newDeck.extend(player)
	newDeck.extend(dealer)
	player =[]
	dealer =[]
	newDeck=[]
	initialDeck=[]

	if hD ==1 or hD ==2:
		newDeck.extend(player2)
		player2 =[]
		plTwo=''
		p2Two=''
		

	p1=''
	p2=''
	p3=''
	d2=''
	d=''
	hD =0
	sH1 = False
	sH2 = False
	tH1 = False
	tH2 = False
	bust = False
	bust2 = False
	fullPVal=0
	fullPVal2=0
	fullDVal=0
	dealerVal=0
	dealerValTwo=0
	playerValOne=0
	playerValTwo=0
	playerValThree=0
	player2ValOne=0
	player2ValTwo=0

	deckCreator()
	newDeck = shuffleDeck(initialDeck)
	gameFunction()

#resets all variables to work properly for the next round

def roundEP():
	print("-----------------------------------------------------------------------------------------------")
	print("_____________________________________!THE ROUND HAS ENDED!_____________________________________")
	print("-----------------------------------------------------------------------------------------------")
	print(".")

#prints a round end graphic

def newRound():

	print("Money left: $"+str(money))
	print("")
	if money ==0:
		print("GAME OVER! you lost all of your money.")
		print(".")
		print("Thank you for playing!")
		return""

	else:
		startR = input("Do you wish to start the next round? y/n: ")

		while startR.lower() != "y" and startR.lower() != "n":
			print(".")
			startR = input("Would you like to start a new round? y/n :")

		else:
			if startR.lower() == "y":
				restart()

			elif startR.lower() == "n":
				print(".")
				print("Thank you for playing!")
				return""

#Checks to see how much money a user has and either says game over or prompts them to start a new round

def blackJack():
	global fullDVal
	global fullPVal
	global money
	global bet
	roundEP()
	print("The dealers current value is "+str(fullDVal)+".")
	print("Your cards make a total value of "+str(fullPVal)+".")
	print("21 means you got a black jack, so you win this round by default!")
	money = (money + bet)
	newRound()

# gives the outcomes if the user gets blackjack 

def blackJack2():
	global hD
	global sH1
	global sH2

	if hD == 1:
		print("Thats a blackjack so you WIN your first hand!")
		sH1 = True
		print(".")
		print("You now hit your second hand.")
		hitFunc3()

	if hD == 2:
		print("Thats a blackjack so you WIN your second hand!")
		sH2 =True

		if sH1 == True:
			splitHitRes()

		elif sH1 == False:
			standFunc()

# gives the outcomes if the user gets blackjack while splitting

def hOrS():

	global newDeck
	action = input("Do you wish to hit or stand?")
	while action.lower() != "hit" and action.lower() != "stand":
		print(".")
		action = input("You can only hit or stand! Would you like to hit or stand?")
	else:
		if action.lower() == "hit":

			if hD == 0:
				p3 = ''
				newDeck = shuffleDeck(newDeck)
				hitFunc()

			elif hD ==1:
				p2 = ''
				p2Two = ''
				newDeck = shuffleDeck(newDeck)
				hitFunc2()

			elif hD ==2:
				p2Two = ''
				newDeck = shuffleDeck(newDeck)
				hitFunc3()

		elif action.lower() == "stand":
			if hD == 0:
				standFunc()

			elif hD ==1:
				p2Two = ''
				newDeck = shuffleDeck(newDeck)
				print(".")
				print("You stand your first hand, and hit your second.")
				hitFunc3()

			elif hD ==2:
				standFunc()

'''asks user to hit or stand and gives different outcomes depending on what the user decides
 as well as the situation they're in ie: split or one hand'''

def cardCalc():
	global playerValOne
	global playerValTwo
	global dealerVal
	global fullPVal
	global fullPVal2
	global fullDVal
	global action
	global dealer
	global d
	global player
	global player2
	global p1
	global p2
	global p1Two

	if selectFirstWord(d) == "Ace":
		dealerVal = aceVal[selectFirstWord(d)]
	else:
		dealerVal = valueDict[selectFirstWord(d)]

	if selectFirstWord(p1) == "Ace":
		playerValOne = aceVal[selectFirstWord(p1)]

	else:
		playerValOne = valueDict[selectFirstWord(p1)]


	if selectFirstWord(p2) == "Ace":
		playerValTwo = aceVal[selectFirstWord(p2)]

	else:
		playerValTwo = valueDict[selectFirstWord(p2)]


	if playerValOne == playerValTwo:

		fullDVal = dealerVal

		fullPVal = playerValOne 

		fullPVal2 = playerValTwo


		player2.extend(player[1])
		del player[1]

		p2 = ''

		p1Two= str(player2[0])


		splitFunc()


	else:
		fullPVal = playerValOne + playerValTwo
		fullDVal = dealerVal
		
		if fullPVal == 21:
			blackJack()
		else:
			print(".")
			print("The dealers current value is "+str(fullDVal)+".")
			print("Your two cards: " +p1+ " and "+p2+" make a total value of "+str(fullPVal)+".")
			print(".")
			hOrS()

''' obtains numerical values of the dealers first card as well 
as the players first two cards and dependent on the circumstance it will go to different places in the program '''

def hitFunc():
	global use

	use +=1

	if use == 6:
		hitEnd()

	global fullPVal
	global fullDVal
	global playerValOne
	global playerValTwo
	global playerValThree
	global action
	global newDeck
	global money
	global bet

	newDeck = shuffleDeck(newDeck)
	
	player.extend(newDeck[:1])
	del newDeck[0]
	p3 = str(player[-1])

	if selectFirstWord(p3) == "Ace":
		playerValThree = aceVal[selectFirstWord(p3)]

		if fullPVal == 21:
			blackJack()

		elif (fullPVal + playerValThree) > 21:
			playerValThree = 1
			fullPVal = fullPVal + playerValThree
			print(".")
			print("You recieve a "+p3+", making your total value "+str(fullPVal)+".")
			print("The dealers value is " +str(fullDVal)+".")
			hOrS()
		else:
			fullPVal = fullPVal + playerValThree
			print(".")
			print("You recieve a "+p3+", making your total value "+str(fullPVal)+".")
			print("The dealers value is " +str(fullDVal)+".")
			print(".")
			hOrS()

	else:
		playerValThree = valueDict[selectFirstWord(p3)]
		fullPVal = fullPVal + playerValThree

		print(".")
		print("You recieve a "+p3+", making your total value "+str(fullPVal)+".")

		if fullPVal == 21:
			blackJack()

		elif fullPVal > 21:
			roundEP()
			print("Your card value exceeds 21! The dealer wins the round! You LOSE!")
			money = (money - bet)
			print(".")
			newRound()

		else:
			print("The dealers value is " +str(fullDVal)+".")
			print(".")
			hOrS()

''' shuffles deck, takes a card from the deck and gives it to the players hand, then determines total card value
 and gives different results dependent on the situation'''


# HIT FUNCTION 2 AND 3 ONLY RUN IF THERES SPLIT OCCURING			

def hitFunc2():
	global bust 
	global sH1
	global fullPVal
	global fullDVal
	global playerValOne
	global playerValThree
	global newDeck

	newDeck = shuffleDeck(newDeck)
	
	player.extend(newDeck[:1])
	del newDeck[0]
	p2 = str(player[-1])

	if selectFirstWord(p2) == "Ace":
		playerValThree = aceVal[selectFirstWord(p2)]

		if (fullPVal + playerValThree) == 21:
			blackJack2()

		elif (fullPVal + playerValThree) > 21:
			playerValThree = 1
			fullPVal = fullPVal + playerValThree
			print(".")
			print("You recieve a "+p2+", making your total value "+str(fullPVal)+".")
			print("The dealers value is " +str(fullDVal)+".")
			hOrS()

		else:
			fullPVal = fullPVal + playerValThree
			print(".")
			print("You recieve a "+p2+", making your total value "+str(fullPVal)+".")
			print("The dealers value is " +str(fullDVal)+".")
			print(".")
			hOrS()

	else:
		playerValThree = valueDict[selectFirstWord(p2)]
		fullPVal = fullPVal + playerValThree

		print(".")
		print("You recieve a "+p2+", making your total value "+str(fullPVal)+".")
		print("The dealers value is " +str(fullDVal)+".")

		if fullPVal == 21:
			blackJack2()

		elif fullPVal > 21:
			print(".")
			print("Your card value exceeds 21! You LOSE your first hand!")
			print(".")
			print("You hit your second hand.")
			bust = True
			hitFunc3()

		else:
			print(".")
			hOrS()

''' shuffles deck, takes a card from the deck and gives it to the players first hand, then determines total card value
 and gives different results dependent on the situation'''


def hitFunc3():
	global bust2
	global bust
	global sH2
	global sH1
	global hD
	global fullPVal2
	global fullDVal
	global playerValTwo
	global playerValFour
	global newDeck

	hD =2

	newDeck = shuffleDeck(newDeck)

	player2.extend(newDeck[:1])
	del newDeck[0]
	p2Two = str(player2[-1])

	if selectFirstWord(p2Two) == "Ace":
		playerValFour = aceVal[selectFirstWord(p2Two)]

		if (fullPVal2 + playerValFour) == 21:
			blackJack2()

		elif (fullPVal2 + playerValFour) > 21:
			playerValFour = 1
			fullPVal2 = fullPVal2 + playerValFour
			print(".")
			print("You recieve a "+p2Two+", making your total value "+str(fullPVal2)+".")
			print("The dealers value is " +str(fullDVal)+".")
			hOrS()

	else:
		playerValFour = valueDict[selectFirstWord(p2Two)]
		fullPVal2 = fullPVal2 + playerValFour

		print(".")
		print("You recieve a "+p2Two+", making your total value "+str(fullPVal2)+".")
		print("The dealers value is " +str(fullDVal)+".")

		if fullPVal2 == 21:
			blackJack2()

		elif fullPVal2 > 21:
			print(".")
			print("Your card value exceeds 21! You LOSE your second hand!")
			print(".")

			bust2 = True

			if bust == True:
				splitHitRes()
			elif bust == False:
				standFunc()

		else:
			print(".")
			hOrS()

''' shuffles deck, takes a card from the deck and gives it to the players second hand, then determines total card value
 and gives different results dependent on the situation'''

def splitHitRes():
	global sH1
	global sH2
	global tH1
	global tH2
	global money
	global bet

	print(".")

	if tH1 == False and tH2 == False: 

		if sH2 == True and sH1 == True:
			roundEP()
			print("Great! You WIN both hands!")
			money += (bet*2)
			newRound()

		elif sH2 == True or sH1 == True:
			roundEP()
			print("You WIN one hand but you LOSE one hand too.")
			bet = 0
			newRound()

		else:
			roundEP()
			print("You LOSE both hands!")
			money -= (bet*2)
			newRound()

	elif tH1 == True and tH2 == False:

		if sH2 == True:
			roundEP()
			print("Your first hand is TIED with the dealer but your second hand WON!")
			money +=bet
			newRound()

		else:
			roundEP()
			print("Your first hand is TIED with the dealer but your second hand LOST!")
			money -=bet
			newRound()

	elif tH1 == False and tH2 == True:

		if sH1 == True:
			roundEP()
			print("You WON your first hand but your second hand is TIED with the dealer!")
			money +=bet
			newRound()

		else:
			roundEP()
			print("You LOST your first hand and your second hand is TIED with the dealer!")
			money -=bet
			newRound()

	elif tH1 == True and tH2 == True:
		roundEP()
		print("Both of your hands are tied with the dealer!")
		bet = 0
		newRound()

# determines based on boolean variables which hands won and which didnt in a split scenario after the dealer has finished drawing cards

def hitEnd():
	print("You have used hit the maximum amount of times, so you stand.")
	standFunc()	

# runs when a user has hit the maximum amount of times (6) and then redirects the user to the stand function		

def standEnd():
	global fullPVal
	global fullDVal
	global sH1
	global sH2
	global tH1
	global tH2
	global bust
	global bust2
	global use2
	global hD
	global money
	global bet

	use2 =0


	if fullDVal > 21:

		if hD ==2:
			print(".")
			print("The dealers card value exceeds 21 so he losses and you win!")
			sH1 = True
			sH2 = True
			splitHitRes()
		else:
			roundEP()
			print("The dealers card value exceeds 21 so he losses and you win!")
			money += bet
			newRound()

	if hD == 0:
		if fullDVal > 16:

			print(".")
			print("The dealer decides to stop dealing.")

			if fullDVal > fullPVal:
				roundEP()
				print("The dealers value is higher so you LOSE the round!")
				money -= bet
				newRound()

			elif fullDVal < fullPVal:
				roundEP()
				print("The dealers value is lower so you WIN the round!")
				money += bet
				newRound()

			else:
				roundEP()
				print("Both you and the dealer share the same card values! So you TIE in the round!")
				bet = 0
				newRound()

	elif hD == 2:
		if fullDVal > 16:

			print(".")
			print("The dealer decides to stop dealing.")

			if fullDVal > fullPVal:
				print(".")
				print("The dealers value is higher than your first hand so you LOSE that hand!")
				
			elif fullDVal < fullPVal:
				if bust == False:
					print(".")
					print("The dealers value is lower than your first hand so you WIN that hand!")
					sH1 = True

				elif bust == True:
					print(".")
					print("Your first hand already exceeded the value of 21 so it has been LOST.")

			elif fullDVal == fullPVal:
				print(".")
				print("Both you and the dealer share the same card values! So the dealer TIES with your first hand!")
				tH1 = True
			
			if fullDVal > fullPVal2:
				print(".")
				print("The dealers value is higher than your second hand so you LOSE your second hand!")
				splitHitRes()

			elif fullDVal < fullPVal2:

				if bust2 == False:
					print(".")
					print("The dealers value is lower than your second hand so you WIN that hand!")
					sH2 = True
					splitHitRes()

				elif bust2 == True:
					print(".")
					print("Your second hand already exceeded the value of 21 so it has been LOST.")
					splitHitRes()

			elif fullDVal == fullPVal2:
				print(".")
				print("Both you and the dealer share the same card values! So the dealer TIES with your second hand!")
				tH2 = True
				splitHitRes()

# compares the total card value of the dealer with the player and gives results for every possible situation

def dD():
	global d2

	if hD ==2:
		print(".")
		print("The dealer draws a "+d2+" and his value increases to "+ str(fullDVal)+ ". Your first value is " +str(fullPVal)+". Your second value is "+str(fullPVal2)+".")

		if fullDVal > 21:
			standEnd()

		elif fullDVal > 16:
			standEnd()

		else:
			newDeck = shuffleDeck(initialDeck)
			standFunc()

	elif hD ==0:
		print(".")
		print("The dealer draws a "+d2+" and his value increases to "+ str(fullDVal)+ ". Your value is " +str(fullPVal)+".")

		if fullDVal > 21:
			standEnd()

		elif fullDVal > 16:
			standEnd()

		else:
			newDeck = shuffleDeck(initialDeck)
			standFunc()

# gives the dealer paramiters, in other words it dictates if the dealer can keep drawing cards and when it should stop

def standFunc():
	global use2
	global use
	global d2

	use = 0
	use2 +=1

	if use2 == 6:
		standEnd()

	global fullPVal
	global fullDVal
	global action
	global newDeck

	print(".")
	print("The Dealer draws himself a card.")

	dealer.extend(newDeck[:1])
	del newDeck[0]
	d2 = str(dealer[-1])
    

	if selectFirstWord(d2) == "Ace":
		dealerValTwo = aceVal[selectFirstWord(d2)]

		if (fullDVal + dealerValTwo) > 21:
			dealerValTwo = 1
			fullDVal = fullDVal + dealerValTwo
			dD()
		
		else:
			fullDVal = fullDVal + dealerValTwo
			dD()
			
	else:
		dealerValTwo = valueDict[selectFirstWord(d2)]
		fullDVal = fullDVal + dealerValTwo
		dD()

#identifies dealers new card type and reacts acordingly

def splitFunc():
	global hD
	global fullPVal
	global fullPVal2
	global fullDVal

	hD =1

	print(".")
	print("The two cards that youve been given have the same value. You now have two hands!")
	print(".")
	print("The dealers current value is "+str(fullDVal)+".")
	print("Your first hand has a card value of "+str(fullPVal)+". Your second hand has a card value of "+str(fullPVal2)+".")
	print(".")
	print("NOTE: After you hit once, if you hit again you will continue to hit your first hand.")
	print(      "Only when you stand will you be able to hit your second hand. ")
	print(".")
	print("NOTE: Its strongly advised that you start by hitting when you have two hands!")
	print(".")
	hOrS()

#tells user the first two player cards each has their own hand 

def gameFunction():
	global action
	global dealer
	global d
	global player
	global p1
	global p2
	global money
	global bet

	print(".")
	startR = input("Press enter to begin.")
	while len(startR) > 0:
		print(".")
		startR = input("Press enter to begin.")

	dealer.extend(newDeck[:1])
	del newDeck[:1]

	player.extend(newDeck[:2])
	del newDeck[:2]

 
	d = str(dealer[0])
	p1 = str(player[0])
	p2 = str(player[1])

	print("Current amount of money: $"+str(money))
	print(".")
	print(".")

	bet = input("How much money do you want to bet this round? *ex: 10 for ten dollars")

	while bet.isnumeric() == False:
		bet = input("You must bet at least one dollar! How much do you want to bet?")
	else:
		bet = int(bet)

		while bet <1 or bet >money:
			print(".")
			bet = input("Thats not a valid amount! Bet within your limits! How much?")

		else:
			print(".")
			print("You bet "+str(bet)+" dollars!")

			print("-----------------------------------------------------------------------------------------------")
			print("_____________________________________!THE ROUND HAS BEGUN!_____________________________________")
			print("-----------------------------------------------------------------------------------------------")
			print(".")

			print("The dealer gives you two cards and himself one!")
			print(".")
			print("He carries a(n) "+ d +" while you have a(n) "+ p1 +" and a(n) "+p2+".")

			cardCalc()

#grabs initial cards from the deck, gets users bet amount and starts the round

deckCreator()
newDeck = shuffleDeck(initialDeck)
gameFunction()


