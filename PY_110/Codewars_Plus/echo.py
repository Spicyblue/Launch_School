''' 
Echo. 
Write a program that initializes the string word = "echo", 
the empty tuple t = (),  and the integer count = 3. 
Then, write a function to make t = ("echo", "echo", "echo", "cho", "cho", "cho", "ho", "ho", "ho", "o", "o," "o")
Each substing of the original word gets repeated count number of times.

# Problem:
#   Input: 
- String and integer
#   output: 
- Tuple of strings

#   Explcit Rule:
#   - Must have two inputs, strings, and integer count
#   Implicit rule: 
#   - Must be a program and hence involves a function definition and a function call.

# Examples and test cases

# Data Structure
list

# ALgorithms
#   High level ALgorithms:
#   - Get Input.
#   - Loop through the string form the start to the end of the string.
#   - Get the string to be added to the list.
#   - Store the resulting string a list.
#   - Convert the list to a tuple.
#   - Return it.

#      
# # Low level algorithm
#      - Define a function with two parameters.
#      - Initalize `empty_list` to `[]`
#      - Iterate over the length of `string` using a for loop.
#           - Using indexing to access from the start to end of the string and assign the return string object to `main_word`.
#                 - Use a for loop to iterate over `range(count)`.
#                        -  Append main_word string to the empty_list.
#      -  Conver list to tupple and return tupple.

# Code
'''
word =  'echo'

def convert_to_tupple(string, count):

    empty_list = []

    for index in range(len(string)):
        main_word = string[index:]

        for _ in range(count):
            empty_list.append(main_word)

    tuple_list = tuple(empty_list)

    return tuple_list

final_tuple = convert_to_tupple(word, 3)

print(final_tuple)
