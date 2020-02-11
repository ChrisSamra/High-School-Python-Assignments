
name = "" 
gender = ""
birth = ""
dt_obj=""
#creates name gender birth and datetime object variables

from datetime import datetime
now = datetime.now()
cyear = now.year
#imports datetime and defines "now" and "current year" variables

name = input("Welcome to Pirate Speak! What be ye moniker? :")#requests input

while len(name) <= 1: # while name input is too short or doesnt exist
  name = input("Give me ye moniker. :")#infinitley loops input request until valid input is provided

if len(name) > 1: #if input is long enough
  print("Ahoy " +name+ "!") #returns message

  gender = input("What be ye gender? Boy or Girl? :")#requests input

  while gender.lower() != "boy" and gender.lower() != "girl":# if user claims to be anything but a boy or girl
    gender = input("Thar be only a pair genders!, please choose a gender! Boy or Girl :")#infinitley loops input request until valid input is provided

if gender.lower() == "boy"  or  gender.lower() == "girl":#if input is valid
  print("So, ye be a "+gender+" eh?")#returns message

  birth = input("What be ye birthday? ddmmyyyy :")# requests input

bday = birth[2:4]
bday = int(bday)
bmonth = birth[0:2]
bmonth = int(bmonth)
byear = birth[4:8]
byear = int(byear)
#creates three variables that take the birth day month and year of the user and convert each of them into their own integers

while len(birth) < 8 or len(birth) > 8:#if input is too short or long
  birth = input("What be ye birthday? ddmmyyyy :")#infinitley loops input request until valid input is provided
 

if len(birth) == 8: #if input length is met

  yrs_till_100 = (byear + 100)#creates and defines a variable that adds 100 to the birth year of the user to get the year which he/she will be 100
  
  this_yrs_bday = (("%s, %s, %s ") %(str(bday), str(bmonth), str(cyear)))
  dt_obj = datetime.strptime(this_yrs_bday, "%m, %d, %Y ")


if dt_obj <= now:#if this years birthday has passed 

  this_yrs_bday = "%s, %s, %s " %(str(bday),  str(bmonth),  now.year + 1)
  dt_obj = datetime.strptime(this_yrs_bday, "%m, %d, %Y ")

  days_til_next_bd = abs(datetime.now() - dt_obj)#calculates the difference of days till the next birthday
  print("Ahoy "+name+ "! Ye gunna be 100 on "+str(bday)+"/" +str(bmonth)+"/" +str(yrs_till_100)+"! Ye also has "+str(days_til_next_bd)[:3]+" days till ye next birthday!")
  #gives final message
else:

  days_til_next_bd = abs(datetime.now() - dt_obj)#calculates the difference of days till the next birthday
  print("Ahoy "+name+ "! Ye gunna be 100 on "+str(bday)+"/" +str(bmonth)+"/" +str(yrs_till_100)+"! Ye also has "+str(days_til_next_bd)[:3]+" days till ye next birthday!")
  #gives final message


