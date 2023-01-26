# This is a guess the number game for simple coding.
import random


# after importing the random number library, we need to make a function to use it.
random_number = random.randrange(1, 10)  # grab any number starting with 1
n = 0
while n != random_number:  # begin the loop!
    n = int(input("Guess a number between 1 and 10"))  # input fxn provides prompt for user
    if n < random_number:
        print("Sorry, guess again. Too low.")
    elif n > random_number:
        print("Sorry, guess again. Too high.")
    else:
        break
print('Hurray, congrats! You have guessed the number correctly')
