#Write a program that asks the user to input 10 integers. 
# Your program should count and display:

##How many of the integers are even
##How many of the integers are odd

import os

def clear_screen():
    os.system("clear")

while True:

    clear_screen()

    print("Welcome to the Even or Odd Counter!")
    even_count = 0
    odd_count = 0

    numbers = []

    for i in range(10):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)

        if num % 2 == 0:
            odd_count += 1
        else:
            even_count += 1

    print(f"You entered {odd_count} odd numbers and {even_count} even numbers")

    choice = input("Do you wish to play again? y/n: ")
    if choice != "y":
        break

