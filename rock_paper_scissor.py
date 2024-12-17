# Input (Rock, Paper, or Scissors? (r/p/s))
# kalo pilih selain itu (alert: invalid choice)
# kalo pilih r/p/s dan menang, bakal di tanya..continue atau ga y/n
# klo pilih continue y, maka lanjut main
# klo pilih continue n, maka break/berhenti

import random

while True:
    emojis = {'r': '🪨', 'p': '📃', 's': '✂️'}
    choices = ('r','p','s')
    user_choice = input('Rock, Paper, or Scissors? (r/p/s): ').lower()

    if user_choice not in choices:
        print('Invalid Choice!')
        continue
    
    computer_choice = random.choice(choices)    
    print(f'You choose {emojis[user_choice]}')
    print(f'Computer Choice {emojis[computer_choice]}')

    if user_choice == computer_choice:
        print('Tie!')
    elif (
        (user_choice == 'r' and computer_choice == 'p') or 
        (user_choice == 'p' and computer_choice == 'r') or 
        (user_choice == 's' and computer_choice == 'p')):
        print('You Won')
    else:
        print('You Lose')

    should_continue = input("Do you want to continue? y/n: ")

    if should_continue == 'n':
        break



