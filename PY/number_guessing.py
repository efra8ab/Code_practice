#Generate a random number between 1 and 10. 
# The user tries to guess it. 
# The program tells them if they got it right or not.

import os
import random

def clear_screen():
    os.system("clear")

while True:
    secret_number = random.randint(1, 10)
    counter = 0
    clear_screen()
    
    while True:
        guess = int(input("Guess the secret number: "))

        if guess != secret_number:
            counter += 1
            print("try again...")
        else:
            break
        
    clear_screen()
    print(f"You did it!, the secret number was {secret_number} ")
    print(f"It only took you {counter} tries")
    again = input("Do you want to play again? (Y/N)")

    if again == "N":
        break

