'''
Multiply Lists
Write a function that takes two list arguments,
each containing a list of numbers, 
and returns a new list that contains the product of each pair of
numbers from the arguments that have the same index.
You may assume that the arguments contain the same number of elements.

# Problem
- Input: 
List
- Output:
list

- Rules
    Explicit:
    Takes two list argumentsas input.
    Returns a new list that contains the product of each pair of numbers 
    from the arguments that have the same index.
    Positions must be maintained.
    Arguments contain same number of elements.
  
# Examples
list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True


# Data structure
list

# Algorithm
    - High End 
        1. Get input.
        2. Create an empty list to store result.
        3. Iterate through the list 
            - multiply the value of the elements at the same position of both list
            - Add result of multiplication to empty list.
            - repeat for all elements in both lists.
        4. Return result

# Code
'''

# Solution
def multiply_list(lst1, lst2):

    result = []

    for idx in range(len(lst1)):
        answer = lst1[idx] * lst2[idx]
        result.append(answer)

    return result
            
# code check
list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True

# Note!
# Time take to write PEDAC and test/debug code is 8 mins, 20 seconds.

## LS Answer ##
# def multiply_list(numbers1, numbers2):
#     result = []

#     for i in range(len(numbers1)):
#         result.append(numbers1[i] * numbers2[i])

#     return result
# Solution 2
# def multiply_list(numbers1, numbers2):
#     return [a * b for a, b in zip(numbers1, numbers2)]
