import os
import re

def clear_screen():
    os.system("clear")

def word_filter():
    sentence = input('Enter your sentence: ')
    length = input('Enter a maximum length for each word:')

    sentence_list = []

    sentence_list = re.split(r"[ ,.!?/\;:]+", sentence)

    filtered_words = []
    for word in sentence_list:
        if len(word) <= int(length):
            filtered_words.append(word)
        else:
            filtered_words.append('_')

    print(' '.join(filtered_words))


clear_screen()
word_filter()
