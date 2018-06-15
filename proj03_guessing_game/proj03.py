# Name:
# Date:


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
mode = raw_input("Chose a dificulty mode. (Easy, Normal, Hard, Extreme) ")
if mode == "Easy":
    a = 10
elif mode == "Normal":
    a = 25
elif mode == "Hard":
    a = 50
elif mode == "Extreme":
    a = 100
else:
    a = 100000
import random
x = random.randint(1, a)
y = int(raw_input("Guess a number from 1 to " + str(a) + " or enter " + str(a + 1) + " to exit."))
while y < x or y > x and y < a + 1:
    if y > x:
        print "Your number is too high!"
        y = int(raw_input("Guess another number from 1 to " + str(a) + " or enter " + str(a + 1) + " to exit."))
    elif y < x:
        print "Your number is too low!"
        y = int(raw_input("Guess another number from 1 to " + str(a) + " or enter " + str(a + 1) + " to exit."))
if y == x:
    print "Congrats, You have guessed the number!"
else:
    print "You were lame and quit the game."
