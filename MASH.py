#This is a game of MANSION, APARTMENT, SHACK, HOUSE
import random, sys
import time

love = []
job =[]


print ('Let\'s play a schoolyard classic, MASH!')

print ("Please enter 4 crushes, one at a time")
for loveNames in range (1,5):
    love_answer = input()
    love.append(love_answer)
print ('Your crushes are ' + ','.join(love) + ' .')

print ('Please tell me 4 jobs you may want to have.')
for jobTypes in range (1,5):
    job_answer = input()
    job.append(job_answer)
    
print('Your job prospects are ' + ','.join(job) )

print ('I am thinking')
print('....')
print('...')
time.sleep(3)


home=['house', 'flat', 'mansion', 'shack']

psychicNumber = random.randint(0,3)

print ('You will marry ' + love[psychicNumber] + '. Your job will be working as a ' + job[psychicNumber] + 
'. You will live in a ' + home[psychicNumber] + ' and have ' + str(random.randint(1,9)) + ' kid(s)' )



