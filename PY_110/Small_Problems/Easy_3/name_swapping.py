'''
Name Swapping
Write a function that takes a string argument consisting of a first name, a space, and a last name. 
The function should return a new string consisting of the last name, a comma, a space, and the first name.
You may assume that the names don't include middle names, initials, or suffixes ("Jr.", "Sr.").

Further Exploration
Suppose the named person has one or more middle names?
Refactor the current solution so it can accommodate this.
The middle names should be listed after the first name:

# Problem
- Input: 
string
- Output:
string

- Rules
    Explicit:
    String argument consisting of a first name, a space, and a last name.
    new string consisting of the last name, a comma, a space, and the first name and other names.

# Examples

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True

print(swap_name('Karl Oskar Henriksson Ragvals')
                == "Ragvals, Karl Oskar Henriksson")  # True

# Data structure
list

# Algorithm
    - High End 
        1. Get input.
        2. Convert string to list and unpack list.
        3. Use indexing to access the correct elementin the list required.
        3. Return result with the right format.

# Code
'''

# Solution
def swap_name(string):
    
    list_of_names = string.split(' ')
    last_name = list_of_names[-1]
    other_names  = " ".join(list_of_names [ : -1])

    return f"{last_name}, {other_names}"

# Code Check
print(swap_name('Joe Roberts') == "Roberts, Joe")   # True
print(swap_name('Karl Oskar Henriksson Ragvals')
                == "Ragvals, Karl Oskar Henriksson")  # True

# Note!
# Time take to write PEDAC and test/debug code is 4 mins, 46 seconds.

## LS Answer ##
# def swap_name(name):
#     return ', '.join(name.split()[::-1])