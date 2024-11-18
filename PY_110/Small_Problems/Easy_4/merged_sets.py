'''
Merge Sets.
Given two lists, convert them to sets and return a new set which is the union of both sets.

# Problem
- Input: 
list 
- Output:
Set

- Rules
    Explicit:
    Sorted based on the english word for each number.
    Implicit:

# Examples

list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]
print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
# Prints True

# Data structure
List and set

# Algorithm
    - High End:
        1. Get input.
        2. Combine both lists.
        3. Return the set of the combined list.

# Code
'''

# Solution
def merge_sets(lst1, lst2):
    merged_list = lst1 + lst2
    return set(merged_list)

list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]
print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})

# Note!
# Time take to write PEDAC and test/debug code is 2 mins, 3 seconds.

## LS Answer ##
# def merge_sets(list1, list2):
#     return set(list1) | set(list2)
