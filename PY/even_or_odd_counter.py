#Write a program that asks the user to input 10 integers. 
# Your program should count and display:

##How many of the integers are even
##How many of the integers are odd

import os

def clear_screen():
    os.system("clear")

def odd_even_count():
    print("Welcome to the Even or Odd Counter!")
    even_count = 0
    odd_count = 0

    numbers = []

    for i in range(10):
        while True:
            try:
                num = int(input(f"Enter number {i + 1}: "))
                break
            except ValueError:
                print("Enter a valid number!")
        
        numbers.append(num)

        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print(f"\nNumbers entered {numbers}")

    print(f"You entered {odd_count} odd numbers and {even_count} even numbers")

while True:

    clear_screen()

    odd_even_count()

    choice = input("Do you wish to play again? y/n: ")
    if choice != "y":
        break

