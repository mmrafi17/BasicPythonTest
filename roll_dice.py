# roll the dice with y/n
# hanya ada 2 kondisi, y/n
# selain itu akan dapet alert invalid choice
# klo pilih y bakal roll dicenya (nomor random dari 1-6)
# klo pilih n akan menyelesaikan permainannya

import random

list1 = [1, 2, 3, 4, 5, 6]

while True:
    dice = input("Roll the dice? y/n: ")
    
    if dice.lower() == 'y':
        print(random.choice(list1))
    elif dice.lower() == 'n':
        print('Thankyou')
        break
    else:
        print('Invalid Choice')



