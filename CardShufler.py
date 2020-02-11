def cardshufler():
	loopTime=input("how many times do you want Shuffler	-	")#times suffler will suffle
	cardGroup1 = ["c1","c2","c3","c4","c5","c6","c7","c8","c9","c10","cjacks","cqueen","cking","d1","d2","d3","d4","d5","d6","d7","d8","d9","d10","djacks","dqueen","dking"]#splits cards in to two groups equal in size
	cardGroup2 = ["h1","h2","h3","h4","h5","h6","h7","h8","h9","h10","hjacks","hqueen","hking","s1","s2","s3","s4","s5","s6","s7","s8","s9","s10","sjacks","squeen","sking"]
	cardReturn = []#decleration list that will be returned cards
	loopCoditon = True
	while loopCoditon:#condtion if user wants to contiue shuffling or not
		for i1 in range(int(loopTime)):
			cardReturn=[]
			for i2 in range(26):#loop that suffles cards
				cardReturn.append(cardGroup1[25-i2])
				cardReturn.append(cardGroup2[25-i2])
			cardGroup1=cardReturn[:27]
			cardGroup2=cardReturn[26:]
		print(cardReturn)#retruns the suffled deck
		loopCoditon =  input("do you want to shuffle again.(y/n)	-	").lower() == "y"#asks user if they want to reshufle
		if loopCoditon:
			loopTime = input("how many times do you want Shuffler	-	")
	print("Thank you for using card Shuffler")

cardshufler()