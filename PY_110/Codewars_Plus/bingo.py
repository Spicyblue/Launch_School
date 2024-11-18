'''
Available at https://www.codewars.com/kata/57f625992f4d53c24200070e
Level = 6kyu

Bingo.
Time to win the lottery!
Given a lottery ticket (ticket), represented by an array of 2-value arrays, you must find out if you've won the jackpot.

Example ticket:
[ [ 'ABC', 65 ], [ 'HGR', 74 ], [ 'BYHT', 74 ] ]

To do this, you must first count the 'mini-wins' on your ticket.
Each subarray has both a string and a number within it.
If the character code of any of the characters in the string matches the number, you get a mini win.
Note you can only have one mini win per sub array.
Once you have counted all of your mini wins, compare that number to the other input provided (win).
If your total is more than or equal to (win), return 'Winner!'. Else return 'Loser!'.
All inputs will be in the correct format. Strings on tickets are not always the same length.

# Problem:
Input:
- Nested list
Output:
- String

    Rules:
        Exp:
        - Each subarray has both a string and a number within it
        - If the character code of any of the characters in the string matches the number, you get a mini win.
        - Note you can only have one mini win per sub array
        - If your total is more than or equal to (win), return 'Winner!'. Else return 'Loser!'.

# Example
print(bingo([['ABC', 65], ['HGR', 74], ['BYHT', 74]], 2), 'Loser!')
print(bingo([['ABC', 65], ['HGR', 74], ['BYHT', 74]], 1), 'Winner!')
print(bingo([['HGTYRE', 74], ['BE', 66], ['JKTY', 74]], 3), 'Loser!')


# Date Structure:
None

# Alg:
    High End:
    1. Compare the current ticket with the with the number
    2. Get how many wins are present.
    3. Return winner or looser based on conditions.

        Low end:
        1. Get input.
        2. Set mini_win to 0.
        3. Iterate though the outermost list:
            Iterate throught the inner list.
                - Check if any of the character code of the current element is equall to the number.
                - if yes, increase mini_win by 1.
                - repeat for all the element in the inner array

        4. Check if mini_win is greater or equall to second input.
            - If yes, return winner.
            - If not, return looser. 

# Code
'''

# Solution
def bingo(nested_lst, integer):
    mini_win = 0

    for ticket, num in nested_lst:
        for char in ticket:
            if ord(char) == num:
                mini_win += 1

    if mini_win >= integer:
        return 'Winner!'

    return 'Loser!'

# Code Check
print(bingo([['ABC', 65], ['HGR', 74], ['BYHT', 74]], 2) == 'Loser!')
print(bingo([['ABC', 65], ['HGR', 74], ['BYHT', 74]], 1) == 'Winner!')
print(bingo([['HGTYRE', 74], ['BE', 66], ['JKTY', 74]], 3) == 'Loser!')

# Note!
# Time take to write PEDAC and test/debug code 27 mins 53 seconds
