import random, sys
print('ROCK, PAPER, SCISSORS')

#These variables keep track of the number of wins losses, and ties.
wins = 0
losses = 0
ties = 0

while True: # The main game loop
    print('%s Wins, %s Losses, % Ties' %(wins, losses, ties))
    while True: # The player input loop
        print('Enter y9our move: (r)ock (p)aper (s)cissors or (q)uit')
        player_move= input()
        if player_move == 'q':
            sys.exit() #Quit the program
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break #Break out of the player input loop
        print ('Type one of r,p,s, or q')

        #Display what the player chose:

    if player_move == 'r':
        print('ROCK vs...')
    
    elif player_move =='p':
        print('PAPER vs...')
    elif player_move == 's':
        print ('SCISSORS vs...')
    
    #Display what the computer chose
    random_number = random.randomint(1,3)
    if random_number ==1:
        computer_move = 'r'
        print('ROCK')
    elif random_number == 2:
        computer_move = 'p'
        print('PAPER')
    elif random_number == 3:
        computerMove = 's'
        print ('SCISSORS')