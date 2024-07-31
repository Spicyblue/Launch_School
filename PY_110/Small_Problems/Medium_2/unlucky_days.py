'''
Unlucky Days
Some people believe that Fridays that fall on the 13th day of the month are unlucky days.
Write a function that takes a year as an argument and returns the number of Friday the 13ths in that year.
You may assume that the year is greater than 1752, which is when the United Kingdom adopted the modern Gregorian Calendar.
You may also assume that the same calendar will remain in use for the foreseeable future.

# Problem
- Input: 
Integer
- Output:
String

- Rules
    Explicit:
    The year is greater than 1752.
    You may also assume that the same calendar will remain in use for the foreseeable future.


    Implicit:

# Examples
print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True

# Data structure
List

# Algorithm
    - High End:
        1. Get input.
        2. Iterate over all the months of the given year.
        3. For each month, get the day that falls on the 13th.
        4. Count the 13ths that fall on a Friday.
        5. Return the count.

# Code
'''

# Solution
import datetime
def friday_the_13ths(year):
    thirteenths = [datetime.date(year, month, 13)
                   for month in range(1, 13)]

    count = 0
    for day in thirteenths:
        if day.weekday() == 4: # note that Monday is 0 and Sunday is 7
            count += 1

    return count

# code check
print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True

# Note!

'''
Quite an intresting way to play with the date time module.
Might be intresting to look more into this.
This solution takes advantage of Python's datetime module to create date objects that correspond to the 13th of each month.
Using a list comprehension, it creates a list of these date objects for every month of the given year.

We then check the weekday of each 13th day of a month.
If it's a Friday (represented by the integer 4), we increment the count variable.
After checking all the dates, the function returns the final count.

Note that the date.weekday method in Python's datetime module returns an integer between 0 (Monday) and 6 (Sunday).
'''

## LS Answer ##

# import datetime

# def friday_the_13ths(year):
#     thirteenths = [datetime.date(year, month, 13)
#                    for month in range(1, 13)]

#     count = 0
#     for day in thirteenths:
#         if day.weekday() == 4:
#             count += 1

#     return count
