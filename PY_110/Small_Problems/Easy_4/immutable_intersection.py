'''
Immutable Intersection.
Transform two lists into frozen sets and find their common elements.

# Problem
- Input: 
list 
- Output:
Frozenset

- Rules
    Explicit:
    Frozen sets contains common elements.
    Implicit:


# Examples
list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})
print(intersection(list1, list2) == expected_result) # True

# Data structure
list and frozenset.

# Algorithm
    - High End:
        1. Get input.
        2. Convert input to sets and find their intersection.
        3. Convert the intersection to frozenset.
        3. Return frozenset.

# Code
'''

# Solution
def intersection(lst1, lst2):
    intersect = set.intersection(set(lst1), set(lst2))

    return frozenset(intersect)

# code check
list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})
print(intersection(list1, list2) == expected_result) # True

# Note!
# Time take to write PEDAC and test/debug code is 1 mins, 26 seconds.

## LS Answer ##
# def intersection(list1, list2):
#     return frozenset(list1) & frozenset(list2)
