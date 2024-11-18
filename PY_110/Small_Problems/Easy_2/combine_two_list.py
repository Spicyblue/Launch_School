'''
Combine Two Lists.
Write a function that combines two lists passed as arguments and
returns a new list that contains all elements from both list arguments,
with each element taken in alternation.
You may assume that both input lists are non-empty,
and that they have the same number of elements.

Further Exploration
Can you solve this problem using the zip function?

# Problem
- Input: 
List
- Output:
List

- Rules
    Explicit:
    A new list that contains all elements from both list arguments, with each element taken in alternation.
    Both input lists are non-empty, and that they have the same number of elements.

# Examples
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True

# Data structure
list

# Algorithm
    - High End 
        1. Get input.
        2. Create an empty list to hold result
        3. Iterate through the list 
            - Add element from list 1 to empty list
            - Add element from list 2 to empts list.
            - repeat until all elements from list 1 and list 2 are added
        3. Return new list

# Code
'''

# Solution
def interleave(lst1, lst2):

    result = [] 

    for index in range(len(lst1)):
        result.append(lst1[index])
        result.append(lst2[index])

    return result

# Solution 2 using zip method (Further exploration)
# def interleave(lst1, lst2):

#     tup_list = zip(lst1, lst2)

#     result = []

#     for item in tup_list:
#         result.extend(item)

#     return result
            
# code check
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      #

# Note!
# Time take to write PEDAC and test/debug code is 9 mins, 04 seconds.

## LS Answer ##
# def interleave(list1, list2):
#     new_list = []
#     for idx in range(len(list1)):
#         new_list.extend([list1[idx], list2[idx]])

#     return new_list