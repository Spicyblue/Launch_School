'''
Cute Angles.
Write a function that takes a floating point number representing
an angle between 0 and 360 degrees and returns a string
representing that angle in degrees, minutes, and seconds.
You should use a degree symbol (°) to represent degrees,
a single quote (') to represent minutes, and a double quote (") to represent seconds.
There are 60 minutes in a degree, and 60 seconds in a minute.
Note: You can use the following constant to represent the degree symbol:

Further Exploration
Our solution only works with positive numbers in the range of 0 to 360 (inclusive). 
Can you refactor it so that it works with any positive or negative number?

DEGREE = "\u00B0"

# Problem
- Input: 
floating point number
- Output:
string representing that angle in degrees, minutes, and seconds.

- Rules
    Explicit:
    Use a degree symbol (°) to represent degrees.
    Use a single quote to represent minutes.
    Use a double quote to represnt seconds.
    There are 60 minutes in a degree, and 60 seconds in a minute.

# Examples
# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

# Data structure
None

# Algorithm
    - High End 
        1. Get input.
        2. Create a variable for degree, minutes and seconds.
        3. Get the degree value by using int function on the input.
        4. Get minute value by using modulo divsion by 1 on the float of the input.
            - multiply by 60.
        5. Get minute value by using modulo divsion by 1 on the float of minutes.
            - multiply by 60.
        6. Use f string to return result with the right formats.

# Code
'''
# Solution
DEGREE = "\u00B0"
DEGREE_MULTIPLIER = 60


def dms(gps):
    # Further exploration
    if gps % 360 == 0 and gps > 0:
        gps = 360
    else:
        gps = gps % 360

    deg = int(gps)
    print(deg)

    minutes = (float(gps) % 1) * DEGREE_MULTIPLIER
    min = int(minutes)

    seconds = (minutes % 1) * DEGREE_MULTIPLIER
    sec = int(seconds)

    return f"{deg}{DEGREE}{min :02d}'{sec :02d}\""

# code check
print(dms(30)== "30°00'00\"")
print(dms(76.73)== "76°43'48\"")
print(dms(254.6)== "254°35'59\"")
print(dms(93.034773)== "93°02'05\"")
print(dms(0)== "0°00'00\"")
print(dms(360)== "360°00'00\"" or dms(360)== "0°00'00\"")

# further exploration code check
print(dms(-1))   # 359°00'00"
print(dms(400))  # 40°00'00"
print(dms(-40))  # 320°00'00"
print(dms(-420)) # 300°00'00"

# Note!
# Time take to write PEDAC and test/debug code is 32 mins, 59 seconds.
# It was very tricky to understand how the modulo operator works with decimal.

## LS Answer ##

# DEGREE = "\u00B0"
# MINUTES_PER_DEGREE = 60
# SECONDS_PER_MINUTE = 60
# SECONDS_PER_DEGREE = MINUTES_PER_DEGREE * SECONDS_PER_MINUTE

# def pad_zeroes(number):
#     num_string = str(number)
#     if len(num_string) < 2:
#         return '0' + num_string
#     else:
#         return num_string

# def dms(degrees_float):
#     degrees_int = int(degrees_float)
#     minutes = int((degrees_float - degrees_int) * MINUTES_PER_DEGREE)
#     seconds = int(
#         (degrees_float - degrees_int - (minutes / MINUTES_PER_DEGREE)) *
#         SECONDS_PER_DEGREE
#     )

#     return (f"{degrees_int}{DEGREE}"
#             f"{pad_zeroes(minutes)}'"
#             f'{pad_zeroes(seconds)}"')