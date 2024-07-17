'''
Searching 101.
Write a program that solicits six (6) numbers from the user and prints a
message that describes whether the sixth number appears among the first five.

Further exploration.
Suppose we alter the problem to look for a number that satisfies a condition 
(e.g., a number greater than 25) instead of a specific number? 
Would the current solution still work? Why or why not?

# Problem
    - Input : 
    User input number
    - Output: 
    Number and string

    -Explicit:
    - Only numbers are input
    - Valid if last input is present in previous input, else 
    - Only six input is accepted.

# Examples
Example 1

Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 17

17 is in 25,15,20,17,23.

Example 2
Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 18

18 isn't in 25,15,20,17,23.

# Data Structure:
List

# Algorithm
    - High  level
        1. Ask user to enter a valid number (Assuming all inputs are numbers).
        2. Add number to a empty list.
        3. Repeat 1 and 2 until 6 numbers are present in the list.
            -If 6 input are present in the list, go to 4.
        4. Check if the last number is present in the previous 5 inputs.
            - If yes, print that the number in present in the list.
            - If not, print that number is not present.

# Code 
'''

# Solution
def check_sixth_number():

    input_result = []
    number_position = ['1st', '2nd', '3rd', '4th', '5th', 'last']

    for idx in range(len(number_position)):
        number = input(F"Enter the {number_position[idx]} number: ").strip()
        input_result.append(number)

    last_number = input_result[-1]
    previous_numbers = input_result[ : -1]

    # modification for further exploration
    for last_number in previous_numbers:
        if int(last_number) > 25:
            found = True
            break
    
    if found and (last_number in previous_numbers) :
        print("\n")
        print(F"There is a number in {",".join(previous_numbers)} greater than 25 ")
    
    if last_number in previous_numbers:
        print("\n")
        print(f"{str(last_number)} is in {",".join(previous_numbers)}.")
        return
    
    print("\n")
    print(f"{str(last_number)} isn't in {",".join(previous_numbers)}.")

# code check
check_sixth_number()

# Note!
# Time take to write PEDAC and test/debug code is 27 mins, 23 seconds.

# Further Exploration:
# Took additional 5 mins!


### LS Answer ###
# numbers = []

# numbers.append(input("Enter the 1st number: "))
# numbers.append(input("Enter the 2nd number: "))
# numbers.append(input("Enter the 3rd number: "))
# numbers.append(input("Enter the 4th number: "))
# numbers.append(input("Enter the 5th number: "))
# last_number = input("Enter the last number: ")

# numbers_list = ','.join(numbers)

# if last_number in numbers:
#     print(f"{last_number} is in {numbers_list}.")
# else:
#     print(f"{last_number} isn't in {numbers_list}.")
