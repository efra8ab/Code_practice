#Write a program that asks the user to input a sentence. The program should then:
##Count how many words the sentence has.
##Display the longest word.
##Display the average word length (rounded to 2 decimal places).

import os
import re

def clear_screen():
    os.system("Clear")

def sentence_input():
    
    sentence = input("Enter a sentence: ")
    listed_words = [word for word in re.split(r"[ ,.!#$%&/?()]+", sentence) if word]    
    return listed_words

def counting_words(word_list):

    return len(word_list)

def largest_word(word_list):
    
    largest = max(word_list, key=len)
    return largest

def average_size(word_list):
    
    total_char = sum(len(word) for word in word_list)
    return round(total_char/len(word_list), 2)


listed_words = sentence_input()
print(f"Your sentence has: {counting_words(listed_words)} words")
print(f"The largest word is: {largest_word(listed_words)}")
print(f"The average word has: {average_size(listed_words)} characters")


