'''
Available at https://www.codewars.com/kata/6584b7cac29ca91dd9124009
Level = 7kyu

Lojban Number.
Counting in Lojban, an artificial language developed over the last forty years, 
is easier than in most languages. The numbers from zero to nine are:

1 pa 4 vo 7 ze
2 re 5 mu 8 bi 0 no
3 ci 6 xa 9 so
Larger numbers are created by gluing the digits together. For example, 123 is pareci.

Write a program that reads in a Lojban string (representing a number less than or equal to 1,000,000) 
and outputs it in numbers.

Example:
renonore  Lojban string
2002  Number
Input/Output
[input] string representing the number in Lojban pareci
Constraints: Lojban number ≤ 1,000,000
[output] integer representing the Lojban number 123

# Problem
- Input: 
    String representing the number in Lojban pareci
- Output: 
    Integer representing the Lojban number 123
    
- Explicit rules:
    1. Value of string input should not be more than 1,000, 000
- Implicit rules:
    - The order of the string matters as seen from test cases.

Qusestion:
What should the program return for an empty String
What should the program do for strings not in present in the language

# Examples / Test Cases
Example:
renonore  # Lojban string
2002  # Number

# Data Structure:
Use Dictionary to store language string as Key and language number as value

# Algorithm
# High Level: V1
- Create function that takes a string input
- Validate input is string
- Split string into substring of length 2'
- For each substring, Check for their language value and get them as string.
- convert strings to interger.

# Steve Algo

P
    - input =  Lojban string
    - output = integer
    - reqs
        ex
        imp
E
D
A
    v1
    - split string into substrings of length 2
    - convert substring into integer-as-string
    - join integer-strings into long string
    - convert to integer and return
    
    v2
    - use a comprehension to create the list of substrings
        - method: use range() to generate list of starting-indexes, starting
            with zero, stepping by two, and ending with the len(list) minus one (non-inclusive).
            Example indexes for string `pavoze` ==> [0, 2, 4]
    - use comprehension to iterate thru list-of-substrings and convert to integer-string
    - join integer-strings-list into long string
    - convert to integer and return
C
'''

my_dict = {
    'pa' : '1',
    'vo' : '4',
    'ze' : '7',
    're' : '2',
    'mu' : '5',
    'bi' : '8',
    'ci' : '3',
    'xa' : '6',
    'so' : '9',
    'no' : '0',
}

# Goz Code
def lojban_string_to_integer(lojban_string):
    if type(lojban_string) is not str:
        print('This is not a valid lojban word')
    
    sublist = [lojban_string [index: index + 2 ] for index in range(0, len(lojban_string), 2)]

    lojban_number = ''

    for items in sublist:
        lojban_number += my_dict[items]

    return int(lojban_number)
    
test = 'renonore'

print(lojban_string_to_integer(test))

# Steven Code
def convert_lojban(lojban):

    substrings = [lojban[starting_idx: starting_idx + 2] 
                  for starting_idx 
                  in range(0, len(lojban)-1, 2)]
    converted = [my_dict[substr]
                 for substr
                 in substrings]
    return int(''.join(converted))
