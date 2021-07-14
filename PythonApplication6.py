import random

while True:

    options = ['rock', 'paper', 'scissors']
    player_choice = input('Type one of the options:\n rock \n paper \n scissors \n ')
    computer_choice = random.choice(options)


    if player_choice == 'rock' and computer_choice == 'rock':
        print('draw')
    elif player_choice == 'rock' and computer_choice == 'paper':
        print('You lost')
    elif player_choice == 'rock' and computer_choice == 'scissors':
        print('You won')



    if player_choice == 'paper' and computer_choice == 'rock':
        print('You won')
    elif player_choice == 'paper' and computer_choice == 'paper':
        print('draw')
    elif player_choice == 'paper' and computer_choice == 'scissors':
        print('You lost')



    if player_choice == 'scissors' and computer_choice == 'rock':
        print('You lost')
    elif player_choice == 'scissors' and computer_choice == 'paper':
        print('You won')
    elif player_choice == 'scissors' and computer_choice == 'scissors':
        print('draw')
    
    if input('Do you want to play again? yes/no ') == 'no':
        break