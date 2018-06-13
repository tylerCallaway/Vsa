# coding=utf-8
# Name:
# Date:

"""
proj04

practice with lists

"""

#Part I
#Take a list, say for example this one:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.

for list in range(0, 5):
    print list



#Part II
# Take two lists, say for example these two:
b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that creates and prints a list that contains only the elements
# that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

for item in b:
    for item_c in c:
        if item == item_c:
            print item



#Part III
# Take a list, say for example this one:

d = ["b", "a", "f", "y", "a", "t", "_", "p", "a", "R"]
# and write a program that replaces all “a” with “*”.

g = "a"
for g in d:
    if g == "a":
        print "*"
    else:
        print g







#Part IV
#Ask the user for a string, and print out whether this string is a palindrome or not.

j = str(raw_input("Please enter a word."))
list_one = []
list_two = []
str = j
for letter in str:
    list_one.append(letter)
    list_two.append(letter)
list_two.reverse()
print list_one
print list_two

if list_one == list_two:
    print "Your word is a palindrome."
else:
    print "This is not a palandrome."