'''
Available at https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python
Level = 6kyu

Ordered string.
Your task is to sort a given string. Each word in the string will contain a single number.
This number is the position the word should have in the result.
Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
If the input string is empty, return an empty string.
The words in the input String will only contain valid consecutive numbers.

# Problem:
Input:
- String
Output:
- String

    Rules:
        Exp:
        - This number is the position the word should have in the result.
        - Numbers can be from 1 to 9. So 1 will be the first word (not 0).

# Example
print(order("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est")
print(order("4of Fo1r pe6ople g3ood th5e the2") == "Fo1r the2 g3ood 4of th5e pe6ople")
print(order("") == "")

# Data Structure:
List

# Alg:
    High End:
    1. Get a list of string.
    2. Sort them based on the number.
    3. Get back the sorted string.

        Low end:
        1. Get input.
        2. Split input into list.
        3. Iterate through the list and sort the based on the number:
            - Helper sort function.
            - Get String
            - Iterate through the stirng:
                - Check if stirng is a number.
                - Return the integer value of the number.

        4. Sort the list pased on the sort helper function.
        5. Return the sored list.

# Code 
'''

# Solution
def get_number(string):
    number = 0

    for char in string:
        if char.isnumeric():
            number = char

    return number

def order(string):
    string_lst = string.split(' ')
    sorted_stirng = sorted(string_lst, key = get_number)
    sorted_stirng = " ".join(sorted_stirng)

    return sorted_stirng

# Code Check
print(order("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est")
print(order("4of Fo1r pe6ople g3ood th5e the2") == "Fo1r the2 g3ood 4of th5e pe6ople")
print(order("") == "")

# Note!
# Time take to write PEDAC and test/debug code 12 mins 23 seconds
