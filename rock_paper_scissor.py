# Input (Rock, Paper, or Scissors? (r/p/s))
# kalo pilih selain itu (alert: invalid choice)
# kalo pilih r/p/s dan menang, bakal di tanya..continue atau ga y/n
# klo pilih continue y, maka lanjut main
# klo pilih continue n, maka break/berhenti

import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

emojis = {ROCK: '🪨', PAPER: '📃', SCISSORS: '✂️'}
choices = tuple(emojis.keys())
# choices = (ROCK,PAPER,SCISSORS)

def get_user_choice():

    while True:
        user_choice = input('Rock, Paper, or Scissors? (r/p/s): ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print('Invalid Choice!')
            continue
        
    
def display_choice(user_choice, computer_choice):
    print(f'You choose {emojis[user_choice]}')
    print(f'Computer Choice {emojis[computer_choice]}')

def determine_winning(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Tie!')
    elif (
        (user_choice == ROCK and computer_choice == PAPER) or 
        (user_choice == PAPER and computer_choice == ROCK) or 
        (user_choice == SCISSORS and computer_choice == PAPER)):
        print('You Won')
    else:
        print('You Lose')
        
def play_game():
    while True:
        computer_choice = random.choice(choices)    
        
        user_choice = get_user_choice()
        display_choice(user_choice, computer_choice)
        determine_winning(user_choice, computer_choice)
        

        should_continue = input("Do you want to continue? y/n: ")

        if should_continue == 'n':
            break

play_game()
