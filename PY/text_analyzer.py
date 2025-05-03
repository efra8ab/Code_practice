#Asks the user to enter a paragraph.
##Counts and displays:
##The number of words.
##The number of unique words.
##The number of sentences (assume sentences end with ., !, or ?).

import os
import re

def clear_screen():
    os.system("clear")

def receive_input():
    sentence = input("Enter a paragraph: ")   
    return sentence

def number_words(sentence):

    listed_sentence = [word for word in re.split(r"[ ,#$%&/.!?()]+", sentence) if word]
    return len(listed_sentence)

def unique_words(sentence):

    unique_words = set([word.lower() for word in re.split(r"[ ,#$%&/.!?()]+", sentence) if word] )
    return len(unique_words)

def counting_sentences(sentence):

    return len(re.findall(r"[ .!?]+(?=\s|$)", sentence))

def repeat():

    print("Do you wish to play again? y/n")
    again = input()

    if again.lower() == "n":
        return False
    else:
        return True

clear_screen()
while True:

    listed_words = receive_input()
    
    print(f"Number of words: {number_words(listed_words)}")
    print(f"Unique words: {unique_words(listed_words)}")
    print(f"Number of sentences: {counting_sentences(listed_words)}")

    if not repeat():
        break

