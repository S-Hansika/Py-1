import random
x= random.randint(0,9)
chance= 0
while chance<5:
    guess= int(input("Guess any number from 0-9 :  "))
    chance= chance+1
    if guess>x:
        print("You guessed too high, lower down your expectations")
    elif guess<x:
        print("Your guess is too low, increase your standards")
    else:
        break

if guess==x:
    print("You finally guessed it right in "+ str(chance) + " tries!")
elif not chance<5: 
    print("You couldn't guess the number, the number was "+ str(x))


