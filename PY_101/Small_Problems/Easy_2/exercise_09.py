# How Old is Teddy?
# Build a program that randomly generates and prints Teddy's age. 
# To get the age, you should generate a random number between 20 and 100, inclusive.
#Further Exploration
# Modify this program to ask for a name, then print the age for that person. 
# For an extra challenge, use "Teddy" as the name if no name is entered.

# Solution

import random

def ask_name():
    name = input('Enter a name: ')

    return name

def get_teddy_age():
    age = random.randint(20, 100)
    return age

def display_teddy_new_age(name_input, age_input):
    if name_input == "":
        name_input = 'Teddy'
    print(f'{name_input} is {age_input} years old')

def main():
    new_name = ask_name()
    new_age = get_teddy_age()
    display_teddy_new_age(new_name, new_age)

main()
