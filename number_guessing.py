#This is a beginners project in python.
#NUMBER-GUESSING-GAME

#import required modules
import random
import math

#Reading the range for guessing the number
print("Enter the range-")
lower_limit=int(input("Enter the lower limit of the range:"))
upper_limit=int(input("Enter the upper limit of the range:"))

#Set the minimum number of guesses for the number guessing game
#formula used is: log2(upper_limit_limit+1)
guess_times=round(math.log(upper_limit-lower_limit+1,2))

#set the number to be guessed
to_guess=random.randint(lower_limit,upper_limit)

print("There are ",guess_times,"times to guess the number.")

#take a count variable
c=0

while c<=guess_times:
    #read the number guessed by user
    guessed=int(input("Enter your guess:"))

    #check if the guessed number is out of range
    if(guessed>=upper_limit and guessed<=lower_limit):
        print("Out of range!")
        c+=1 
        #increment count

    #When guess is same as the number to be guessed
    if to_guess==guessed:
        print("Congratulations!!")
        print("You have guessed it right!")
        break
        #stop guessing

    #When guess is lower than the number to be guessed
    if guessed<to_guess:
        c+=1
        print("Your guess is too low!")

    #When guess is higher than the number to be guessed
    if guessed>to_guess:
        c+=1
        print("Your guess is too high!")

if c>guess_times:
    print("Better luck next time!")