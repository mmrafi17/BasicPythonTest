# kondisinya ada lebih dari 1:
# n = 10
# 1. 11 -100 (too high)
# 2. 1 - 9 (too low)
# 3. 10 ( )


import random

number_to_guess = random.randint(1, 100)
print(number_to_guess)

while True:
    try:
        guess = int(input("Guess the number between 1 to 100: "))
        if guess < number_to_guess:
            print("Number is too Low")
        elif guess > number_to_guess:
            print("Number is too high")
        else:
            print("Congratulation! You guessed the number.")
            break
    except ValueError:
        print("Please enter a valid number!")

