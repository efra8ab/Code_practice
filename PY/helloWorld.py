#Print “Hello, World!” and then ask the user for their name. 
# Print a greeting using the name.

import os

def clear_screen():
    os.system("clear")

clear_screen()

print("Hello World")
name = input("What is your name?: ")

clear_screen()
print(f"Hello {name}!")
