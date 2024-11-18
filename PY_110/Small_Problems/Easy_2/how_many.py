'''
How Many?
Write a function that counts the number of occurrences of each element in a given list.
Once counted, print each element alongside the number of occurrences.
Consider the words case sensitive e.g. ("suv" != "SUV").

Further Exploration
Try to solve the problem when words are case insensitive,
e.g. "suv" and "SUV" represent the same vehicle type.

# Problem
- Input: 
list of strings
- Output:
string 

- Rules
    Explicit:
    Counts the number of occurrences of each element in a given list.
    Print each element alongside the number of occurrences.
    Consider the words case sensitive e.g. ("suv" != "SUV").
  
# Examples
vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck', 'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)
Expected Output
# your output sequence may appear in a different sequence
car => 4
truck => 3
SUV => 1
motorcycle => 2

# Data structure
list and set. Dictionaries can also be used.

# Algorithm
    - High End 
        1. Get input.
        2. Create a set of the input.
        3. Iterate to the list.
            - print the element and the count in the right format.
            - repeat for all elements.
        4. Return 

# Code
'''

# Solution
def count_occurrences(lst):
    
    # further exploration
    cleaned_lst = [item.casefold() for item in lst]

    unique_items = set(cleaned_lst)
    
    for item in unique_items:
        print(f'{item} ==> {cleaned_lst.count(item)}')
    
    return

# code check
vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck', 'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)

# Note!
# Time take to write PEDAC and test/debug code is 6 mins, 21 seconds.

## LS Answer ##
# def print_occurrences(occurrences):
#     for item, count in occurrences.items():
#         print(f"{item} => {count}")

# def count_occurrences(elements):
#     occurrences = {}

#     for item in elements:
#         occurrences[item] = occurrences.get(item, 0) + 1

#     print_occurrences(occurrences)
