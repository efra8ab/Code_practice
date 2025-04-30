#Ask the used to input a list of nummber (space-separated). 
#Count how many time each number appears and display the result in the format 
# Number X appears Y times

import os

def clear_screen():
    os.system('clear')

def number_freq():
    
    numbers = {}
    
    while True:

        entry = input("next number: ")
        if entry.lower() == 'exit':
            clear_screen()
            print('list created! ')
            break 
        
        try:
            entry = int(entry)
        except ValueError:
            print('Please enter a valid integer number')
            continue

        if entry in numbers:
            numbers[entry] += 1
        else:
            numbers[entry] = 1
    
    return numbers

def print_list(numbers):
    print ('Details about your list: ')
    
    for number, count in sorted(numbers.items(), key = lambda item: [-item[1], item[0]]):
        print(f'Number {number} appears {count} times')


clear_screen()

print ("Enter a list of numbers")
print ("Enter your number and hit ENTER to add another number")
print ("Enter 'exit' if you wish to end \n")

numbers = number_freq()
print_list(numbers)
