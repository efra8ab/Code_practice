#Create a game where the program randomly selects a number between 1 and 100. The user has 10 attempts to guess it.
##After each guess, tell the user if the number is higher or lower.
##Keep track of how many guesses it took.
##If the user guesses it, congratulate them and display their score (based on number of attempts).
##If they fail, reveal the number.

import os
import random

def clear_screen():
    os.system("clear")

def generate_random_num():
    secret_number = random.randint(1, 100)
    return secret_number

def guess_number(secret_number):

    print("Guess a number between 1 and 100!, you only have 10 shots")
    shots = 0

    while shots != 10:

        try: 
            guess = int(input("take a guess: "))
        except ValueError:
            print("Enter a valid value!")
            continue
        
        if guess > secret_number:
            print(f"\nlower...{9 - shots} shots left")
            shots += 1
        
        elif guess < secret_number:
            print(f"\nHigher...{9 - shots} shots left")
            shots += 1
        
        elif guess == secret_number:
            clear_screen()
            print(f"You did it!, the secret number was {secret_number}")
            print(f"It only took you {shots} shots")
            return True
        

    print(f"""You failed! 
          The secret number was {secret_number}""")
    
def play_again():

    print("Do you wish to play again? (y/n)")
    again = input()

    if again.lower() == "n":
        return False
    else :
        return True

while True:
    clear_screen()
    guess_number(generate_random_num())
    if not play_again():
        break

    


