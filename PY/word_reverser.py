#Write a program that asks the user to input a sentence, 
# and then prints each word in reverse order, not reversed letters.

import os

def clear_screen():
    os.system("clear")

while True:

    clear_screen()

    print("Enter a sentence:")
    sentence = input()
    words = sentence.split()
    words.reverse()

    reversed_words = " ".join(words)

    print(f"\nYour reversed sentence is:\n{reversed_words}")

    choice = input("\nDo you want to try with another sentence? y/n:")

    if choice != "y":
        break
