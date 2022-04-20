#This program says hello and asks for my name.
from os import lseek


print('Hello world!')
print('What is your name?')  # ask for their name
myName = input()
print('What is your favorite animal?') # ask for their favorite animal
myAnimal = input()
print('It is good to meet you, ' + myName + '.  ' + myAnimal + 's are the cutest!')
print('The length of your name is:')
print(len(myName))
print('The length of your favorite animal is')
print(len(myAnimal))
print('What is your age?')  # ask for their age
myAge = input()
print('Whaaa! You don\'t look a day over ' + str(int(myAge) - 13) + '!' )
