# Ask the user to enter a number. 
# The program should say whether it is odd or even.

import os

def clear_screen():
    os.system("clear")

def determine(num):
    num = num % 2

    if num == 0:
        print("Even")

    else:
        print("Odd")



clear_screen()
print("I will tell you if your number is odd or even")
print("Enter 0 to close the program")

number = 1

while number != 0:

    number = int(input("Enter a number: "))
    determine(number)

clear_screen()
print("Thank you for using this aplication")