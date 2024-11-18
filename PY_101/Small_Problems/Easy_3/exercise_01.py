# Repeat Yourself
# Write a function that takes two arguments, a string and a positive integer, 
# then prints the string as many times as the integer indicates.

# Solution

def repeat(string_input, no_of_time):
    for _ in range(no_of_time):
        print(string_input)

repeat('Hello', 3)
