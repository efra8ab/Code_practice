#Ask the user to input a number N and then print all the prime numbers between 1 and N, inclusive

import os


def clear_screen():
    os.system('clear')

#using algorithm 
def manual_prime_check(num):
    if num <= 1:
        return False
    
    for i in range (2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_prime(num):
    clear_screen()
    print(f"Prime numbers between 0 - {num}")
    for i in range(2, num + 1):
        if manual_prime_check(i):
            print(f"{i}")

while True:
    clear_screen()

    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Please enter a valid integer")
        exit()

    is_prime(num)

    response = input("\nDo you want to check another number? (y/n):")
    if response.lower() == "n":
        break



