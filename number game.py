import random 
import math 
print("Welcome to Number game")
upper =int(input("Enter the upper limit"))
lower=int(input("Enter the lower limit"))

x=random.randint(upper, lower)

print("You have only 5 chances")

count=0

while count< 5:
    count=count+1
    guess=int(input("Guess a number:-"))

    if x==guess:
        print("Congo you did it ", count,"try")
        break 
    elif x>guess:
        print("You guessed too small")
    elif x<guess:
        print("You guessed too high")

if count>= 5:
    print("The number is %d",x)
    print("Better luck next time!!")