# Name:
# Date:

# proj02: sum

# Write a program that prompts the user to enter numbers, one per line,
# ending with a line containing 0, and keep a running sum of the numbers.
# Only print out the sum after all the numbers are entered
# (at least in your final version). Each time you read in a number,
# you can immediately use it for your sum,
# and then be done with the number just entered.

#Example:
# Enter a number to sum, or 0 to indicate you are finished: 4
# Enter a number to sum, or 0 to indicate you are finished: 5
# Enter a number to sum, or 0 to indicate you are finished: 2
# Enter a number to sum, or 0 to indicate you are finished: 10
# Enter a number to sum, or 0 to indicate you are finished: 0
#The sum of your numbers is: 21

user_input = int(raw_input("Please state a number."))

sum = 0 + int(user_input)
while int(user_input) > 0:
    print "Your sum is " + str(sum)
    user_input=raw_input("Please state a number, enter 0 when finished.")
    sum= sum + int(user_input)