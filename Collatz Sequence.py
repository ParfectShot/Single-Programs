# Collatz sqeuence ends always with "1"

print("Enter an Integer : ")

# Exception Handling
try:
    number=int(input())
except ValueError:
    print("Enter an Integer Value")

# User Input
number=int(input())

#Function creating collatz sequence
def collatz(number):

    if number % 2 == 0:
        print(number//2)
        return number//2
    if number % 2 == 1:
        print(3*number+1)
        return 3*number+1


a = collatz(number)

#Loop generating collatz sequence
while a != 1:
    a = collatz(a)
