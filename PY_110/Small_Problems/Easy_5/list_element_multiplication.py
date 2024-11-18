'''
List Element Multiplication.
Given two lists of integers of the same length, 
return a new list where each element is the product of the corresponding elements from the two lists.

# Problem
- Input: 
String
- Output:
List

- Rules
    Explicit:
    New list where each element is the product of the corresponding elements from the two lists.
    Implicit:

# Examples

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True

# Data structure
List

# Algorithm
    - High End:
        1. Get input.
        2. Create a list to store the result.
        3. Iterate through the input.
            - Access both list elemenet at the same index and multiply them.
            - Add the result to the list.
            - Repeat for all item.
        4. Return list.
        
# Code
'''

# Solution
def multiply_items(lst1, lst2):

    result = []

    for idx in range(len(lst1)):
        sum  = lst1[idx] * lst2[idx]
        result.append(sum)

    return result

# code check
list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True

# Note!
# Time take to write PEDAC and test/debug code is 5 mins, 21 seconds.

## LS Answer ##
# def multiply_items(list1, list2):
#     result = []
#     for i in range(len(list1)):
#         result.append(list1[i] * list2[i])

#     return result
# Solution 2
# def multiply_items(list1, list2):
#     return [num1 * num2 for num1, num2 in zip(list1, list2)]
