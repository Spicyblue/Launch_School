'''
Combining Lists.
Write a function that takes two lists as arguments and
returns a set that contains the union of the values from the two lists.
You may assume that both arguments will always be lists.

# Problem
- Input: 
List
- Output:
Set

- Rules
    Explicit:
    Argument is always list
    Implicit:
    Do not mutate any of the list argument

# Examples
print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True

# Data structure
List

# Algorithm
    - High End 
        1. Get input.
        2. Add list 2 to list 1 in a new list
        3. return the set of new list

# Code
'''

# Solution
def union(lst1, lst2):

    lst = lst1 + lst2

    return set(lst)

# code check
print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True

# Note!
# Time take to write PEDAC and test/debug code is 4 mins, 1 seconds.


## LS Answer ##

# def copy_non_dups_to(result_set, lst):
#     for value in lst:
#         result_set.add(value)

# def union(list1, list2):
#     result_set = set()
#     copy_non_dups_to(result_set, list1)
#     copy_non_dups_to(result_set, list2)
#     return result_set

# Solution 2
# def union(list1, list2):
#     return set(list1).union(set(list2))