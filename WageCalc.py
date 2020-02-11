print("Welcome to The Wage Calculator!")
#obtain wage
hour_rate = input("What is your hourly rate? *$00.00*	-	")

while not hour_rate[0] == "$":
	hour_rate = input("What is your hourly rate? *$00.00*	-	")

#obtain hours
hours = input("How Many hours did you work this month? *000*	-	")

while hours == "":
	hours = input("How Many hours did you work this month? *000*	-	")

hour_rate = float(hour_rate[1:])
hours = float(hours)
#icome calc
icomeBeforeTaxs = hour_rate * hours

#decduct calc
deduct = icomeBeforeTaxs*0.0495 +icomeBeforeTaxs* 0.0188

#fainal calc
income = icomeBeforeTaxs - deduct

print("Your money this month is $"+str(income))


# Chris and Hasin CS 20