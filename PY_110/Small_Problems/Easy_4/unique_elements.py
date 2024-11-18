'''
Unique Elements.
From two list arguments, determine the elements that are unique to the first list.
The return value should be a set.

# Problem
- Input: 
List
- Output:
Set

- Rules
    Explicit:
    Return value should be a set
    Implicit:

# Examples

list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})

# Data structure
Dictionary and list

# Algorithm
    - High End:
        1. Get input.
        2. Create an empty set to add the result.
        3. Iterate through the first list.
           - Check if the element is not in the second list, 
           - Add element to set.
           - Repeat for all element.
        4. Return set.

# Code
'''

# Solution
def unique_from_first(lst1, lst2):
    result = set()

    for ele in lst1:
        if ele not in lst2:
            result.add(ele)

    return result

# code check
list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})

# Note!
# Time take to write PEDAC and test/debug code is 4 mins, 59 seconds.

## LS Answer ##
# def unique_from_first(list1, list2):
#     return set(list1) - set(list2)