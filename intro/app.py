# Rock, paper, scisor basic game

import random

def get_choices():
    player_selection = input('Enter a choice (rock, paper or scissors): ')
    options = ['rock', 'paper', 'scissor']
    computer_selection = random.choice(options)
    choices = {'player': player_selection, 'computer': computer_selection}

    return choices


def check_win(player_option, computer_option):
    # With f before a string we can get variable values into the string
    print(f"You chose {player_option}, computer chose {computer_option}")

    if (player_option == computer_option):
        return 'Tied players'

    elif (player_option == 'rock'):
        if computer_option == 'scissors':
            return 'Rock smashes scissors! You win!!'
        else:
            return 'Paper covers rock! You lose.'
        
    elif (player_option == 'paper'):
        if computer_option == 'rock':
            return 'Paper covers rock! You win!!'
        else:
            return 'Scissors cuts paper! You lose.'
        
    elif (player_option == 'scissors'):
        
        if computer_option == 'paper':
            return 'Scissors cuts paper! You win!!'
        else:
            return 'Rock smashes scissors! You lose.'
    

choices = get_choices()
result = check_win(choices['player'], choices['computer'])
print(result)
