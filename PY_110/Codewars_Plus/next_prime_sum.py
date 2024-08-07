'''
Available at https://www.codewars.com/kata/65eb2c4c274bd91c27b38d32
Level = 5kyu

Three divisor.
Your task is to write a function that takes two integers n and m,
and returns a sorted array of all integers from n to m inclusive,
which have exactly 3 divisors (excluding 1 and the number itself).

Example:
solution(2, 20) -> [16]
16 has 3 divisors: 2, 4, 8 (1 and 16 aren't included)

Input:
n - integer (2 ≤ n ≤ 10^14)
m - integer (2 ≤ m ≤ 10^18)
NOTE: In Rust, the bounds are (2 ≤ n ≤ 2^51), (20 ≤ m ≤ 2^52).

Output:
result - array of integers

# Problem
Input:
- Integers
Output:
- List (sorted)

    Rules:
        Exp:
        - returns a sorted array of all integers from n to m inclusive, which have exactly 3 divisors (excluding 1 and the number itself)
        Implicit:
        - If there is no number, it returns an empty list.

# Example
print(solution(2, 100) == [16, 81])
print(solution(10000, 100000) == [14641, 28561, 83521])
print(solution(624, 625) == [625])
print(solution(625, 626) == [625])
print(solution(734, 735) == [])


# Data Structure:
List


# Algorithm:
    High End:
    1. Get all numbers that are divisible within the range of n and m
    2. Find the numbers that has only 3 divisors (exclusing 1 and the number)
    3 Sort the numbers and return them.

        Low end:
        1. Get input.
        2. Creat a list to store result.
        3. Iterate through the numbers in the input.
            - For each generated number in the sequence.
                - Check for exactly three Divisons.
                    - If yes, add number to list.
                    - Repeat for all numbers.

        4. Return the result.
        5. Return the sored list.
       
       Helper function to check for exacltly three divisors:
       - Get input
       - create a list to store result.
            - iterater from 2 to the input:
                - check if the current number is a divisor:
                - if yes, add number to list.
                - repeat for all numbers.

        - Check if the len of the result is == 3.
            - if yes, True
        - Return False.

# Code
'''

# Solution
def is_three_divisors(number):
    result = []

    for num in range(2, number):
        if number % num == 0:
            result.append(num)

    if len(result) == 3:
        return True
    
    return False


def solution(input1, input2):
    result = []

    for num in range(input1, input2 + 1):
        if is_three_divisors(num):
            result.append(num)

    return result

# Code Check
print(solution(2, 100) == [16, 81])
print(solution(624, 625) == [625])
print(solution(625, 626) == [625])
print(solution(734, 735) == [])

# Note!
# Time take to write PEDAC and test/debug code 12 mins 23 seconds


# other solutions
