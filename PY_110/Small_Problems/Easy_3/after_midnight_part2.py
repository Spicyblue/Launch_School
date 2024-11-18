'''
After Midnight (Part 2)
As seen in the previous exercise, the time of day can be represented as the number of minutes before or after midnight.
If the number of minutes is positive, the time is after midnight.
If the number of minutes is negative, the time is before midnight.
Write two functions that each take a time of day in 24 hour format,
and return the number of minutes before and after midnight, respectively.
Both functions should return a value in the range 0 through 1439.

You may not use Python's datetime module.
Disregard Daylight Savings and Standard Time and other irregularities.

# Problem
- Input: 
Integer
- Output:
String

- Rules
    Explicit:
    If the number of minutes is positive, the time is after midnight.
    If the number of minutes is negative, the time is before midnight.
    Two functions which both should return a value in the range 0 through 1439.
   
# Examples
print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True

# Data structure
list

# Algorithm
    - High End 
        1. Get input.
        2. Get total mins in a day.
        3. Split string into hour and minutes.
        4. Get total mins from hour and minutes.
        5. Check if total mins falls within total mins in a day.
        6. Return total mins.

# Code
'''

# Solution
DAY = 24
MIN = 60

def get_int_hour_min(string):
    hour_min = string.split(':')
    hour, min = hour_min
    hour = int(hour)
    min = int(min)

    return hour, min

def after_midnight(time_str):
    total_min_in_day = DAY * MIN
    hour, min = get_int_hour_min(time_str)
    total_min = (hour * 60) + min
    total_min = total_min % total_min_in_day

    return total_min

def before_midnight(time_str):
    total_min_in_day = DAY * MIN
    hour, min = get_int_hour_min(time_str)
    total_min = (hour * 60) + (min * -1) 
    total_min = total_min % total_min_in_day
    
    return total_min

# code check 
print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34")== 754)    # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True

# Note!
# Time take to write PEDAC and test/debug code is 24 mins, 17 seconds.

# HOURS_PER_DAY = 24
# MINUTES_PER_HOUR = 60
# MINUTES_PER_DAY = HOURS_PER_DAY * MINUTES_PER_HOUR

# def after_midnight(time_str):
#     hours, minutes = [int(unit) for unit in time_str.split(":")]
#     return ((hours * MINUTES_PER_HOUR) + minutes) % MINUTES_PER_DAY

# def before_midnight(time_str):
#     delta_minutes = MINUTES_PER_DAY - after_midnight(time_str)
#     if delta_minutes == MINUTES_PER_DAY:
#         delta_minutes = 0

#     return delta_minutes
