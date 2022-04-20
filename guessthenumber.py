#This is a guess the numbers game
import random
secretNumber= random.randint(1,45)
print('I am thinking of a number between 1 and 45.')

#Ask the player to guess 7 times (Changed)
for guessesTaken in range (1,8):
    print('Take a guess.')
    guess=int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break    #This condition is the correct guess!

if guess==secretNumber:
    print('Good Job! you guessed my number in  ' + str(guessesTaken) + ' guesses!')
else: print('Nope. The number I was thinking was ' + str(secretNumber))


