'''
Rotation (Part 1).
Write a function that rotates a list by moving the first element to the end of the list.
Do not modify the original list; return a new list instead.
If the input is an empty list, return an empty list.
If the input is not a list, return None.
Review the test cases below, then implement the solution accordingly.

# Problem:
- Input:
List
- Output:
List

- Rules
    Explicit:
    Move the first element to the end of the list.
    Do not modify the original list; return a new list instead.
    If the input is an empty list, return an empty list
    If the input is not a list, return None.

# Examples:
# All of these examples should print True
print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])

# Data structure
List

# Algorithm
    - High End 
        1. Get input.
        2. Check if input type is list, if not, return None.
        3. Check is list is empty, if empty, return list. 
        4. Get list input from second element till end and assign to result.
        5. Add the first element of the last position of result.
        6. Return result.

# Code
'''

# Solution
def rotate_list(lst):
    if type(lst) is not list:
        return None

    if lst == []:
        return lst

    result  = lst [1 : ]
    result.append(lst[0])

    return result

#code check
print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# Solution 2:
def rotate_list2(lst):
    if type(lst) is not list:
        return None

    if lst == []:
        return lst
    
    result = []

    for idx in range(1, len(lst)):
        result.append(lst[idx])

    result.append(lst[0])

    return result

print(rotate_list2([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list2(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list2(['a']) == ['a'])
print(rotate_list2([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list2([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list2([]) == [])

# Note!
# Time take to write PEDAC and test/debug code is 12 mins, 45 seconds.
# Better to use isinstance(argument, datatype) for checking if an argument is of currect datatype.

## LS Answer ##
# def rotate_list(lst):
#     if not isinstance(lst, list):
#         return None

#     if len(lst) == 0:
#         return []

#     return lst[1:] + [lst[0]]
