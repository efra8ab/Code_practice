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
    for word in set(listed_sentence):
        
        n_times = listed_sentence.count(word)
        print(f"{word}: {n_times}")
        

    print("Lets do another one? y/n: ")
    choice = input()

    if choice != "y":
        break
    
