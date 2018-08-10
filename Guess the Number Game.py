# This is a Guess the Number Game

import random

secret=random.randint(1,21)

#Asking the User to enter the no.

print("I am thinking of a number between 1-20")
print("Take a Guess..(Only Six Chances)")


# Asking the user to enter upto 6 times max
for i in range(1,7):
    number = int(input())

    if number<secret:
        print("A little high")


    elif number>secret:
        print("A little low")


    else:
        break
# Printing the conclusion
if number==secret:
    print("You guessed it in " + str(i) + " guesses")
    print("Number is : "+str(secret))
else:
    print("Better Luck next time :)")
