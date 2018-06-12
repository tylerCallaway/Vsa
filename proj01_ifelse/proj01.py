# Name:Tyler
# Date:

# proj01: A Simple Program

# Part I:
# This program asks the user for his/her name and grade.
#Then, it prints out a sentence that says the number of years until they graduate.

name = (raw_input("What is your name?"))
grade= int(raw_input("What grade are you in?"))

print str(name) + ", you have "+ str(12- grade) + " years left in school"

name= (raw_input("What is your name?"))
name= name[0].upper() + name [1:100].lower()

print "Your name is " + str(name)

# Part II:
# This program asks the user for his/her name and birth month.
# Then, it prints a sentence that says the number of days and months until their birthday


current_day= 11
current_month= 6

month = int(raw_input("Please state your birth month by number."))
day = int(raw_input("Please state the day of your birth."))
if month > current_month:
    month_till= (month-current_month)
else:
    month_till=(current_month-month)

if day>current_day:
    day_till=(day-current_day)
elif day<current_day:
    day_till= (current_day-day)
else:
    day_till=(day-current_day)

print("Your birthday is ") + str (month_till) + " months away."
print("Your birthday is ") + str (day_till) + " days away."

# If you complete extensions, describe your extensions here!

age= int(raw_input("What is your age?"))
if age < 3:
    print "You can watch G rated movies."
else:
    print "You can watch PG movies."
elif age <17 or age >13:
    print "You can watch PG-13 movies."
elif age > 17:
print "You can watch R rated movies."