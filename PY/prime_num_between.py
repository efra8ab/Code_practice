#Ask the user to input a number N and then print all the prime numbers between 1 and N, inclusive

import os
from sympy import *

def clear_screen():
    os.system('clear')
    

def prime_check(num):
    num = abs(num)
    for i in range (2, num + 1):
        if isprime(i):
            print(f"{i}")

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid integer")
    exit()

clear_screen()
prime_check(num)



