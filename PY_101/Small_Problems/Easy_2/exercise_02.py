# Greeting a user
# Write a program that asks for user's name, then greets the user. 
# If the user appends a ! to their name, the computer will yell the greeting (print it using all uppercase).
# Example
#  What is your name? Sue
# Hello Sue.
# What is your name? Bob!
# HELLO BOB! WHY ARE WE YELLING?


# solution

name = input('What is your name? ').strip()

if name.endswith("!"):
    print(f'HELLO {name.upper()} WHY ARE WE YELLING?')
else:
    print(f'Hello {name.title()}')