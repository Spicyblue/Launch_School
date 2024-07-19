'''
Reversed Lists
Write a function that takes a list as an argument and reverses its elements, in place.
That is, mutate the list passed into the function.
The returned object should be the same object used as the argument.
You may not use the list.reverse method nor may you use a slice ([::-1]).

# Problem
- Input: 
list
- Output:
list

- Rules
    Explicit:
    The function reverses the list argument in place.
    he returned object should be the same object used as the argument.

# Examples
list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True

# Data structure
list

# Algorithm
    - High End 
        1. Get input.
        2. Create a start counter starting at 0.
        3. Create a end counter starting at -1.
        4. Iterate through the input till and stop at the midpoint.
            - moved the element at the idex of the start to the index of the end.
            - move the element at the index of the end to the index of the start.
            - increase start counter by 1.
            - decrease end counter by 1.
            - repeat till the midpoint.
        5. Return the reversed list.

# Code
'''

# Solution
def reverse_list(lst):
    start = 0
    end = -1
    midpoint = len(lst) // 2

    while start < midpoint:
        lst[start], lst[end] = lst[end] , lst[start]
        start += 1
        end -= 1
    
    return lst

# Code Check
list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True


# Note!
# Time take to write PEDAC and test/debug code is 27 mins, 58 seconds.
# This took more time than i had anticipated because I was having diffulties with the
# writing the correcct code for switching the elements at the start and end index first
# and then the element in the end and last next.. This means i was resetting the initial change i had made
# unknowlingly. Unsderstanding what was going on was key to improving my code. Good exercise.

## LS Answer ##
# def reverse_list(lst):
#     first = 0
#     last = -1

#     while first < (len(lst) // 2):
#         lst[first], lst[last] = lst[last], lst[first]
#         first += 1
#         last -= 1

#     return lst

# # Solution 
# def reverse_list(lst):
#     n = len(lst)
#     for idx in range(n // 2):
#         lst[idx], lst[-(idx + 1)] = lst[-(idx + 1)], lst[idx]

#     return lst