# Ask the user to input a sentence. 
# Count how many times each word appears and display the frequency of each word.

import os
import re

def clear_screen():
    os.system("clear")


while True:

    clear_screen()

    print("Enter one sentence: ")
    sentence = input()

    listed_sentence = []
    listed_sentence = re.findall(r'\b\w+\b', sentence.lower())

    print("\nOutput: ")
    word_count = {}
    for word in listed_sentence:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
        
    print("Word count:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

    print("Lets do another one? y/n: ")
    choice = input()

    if choice != "y":
        break
    
