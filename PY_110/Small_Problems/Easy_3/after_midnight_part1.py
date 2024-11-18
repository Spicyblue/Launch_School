'''
After Midnight (Part 1).
The time of day can be represented as the number of minutes before or after midnight.
If the number of minutes is positive, the time is after midnight.
If the number of minutes is negative, the time is before midnight.
Write a function that takes a time using this minute-based format and
returns the time of day in 24-hour format (hh:mm).
Your function should work with any integer input.

You may not use Python's datetime module.
Disregard Daylight Savings and Standard Time and other complications.

# Problem
- Input: 
Integer
- Output:
String

- Rules
    Explicit:
    If the number of minutes is positive, the time is after midnight.
    If the number of minutes is negative, the time is before midnight.
    Ouput should be in 24-hour format (hh:mm)
  
# Examples

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True

# Data structure
list or none

# Algorithm
    - High End 
        1. Get input.
        2. Define midnight.
        3. If input positive or negative:
            - Get the hour.
            - Get the minute.
        4. Return the value of hour and minute in the right format.

# Code
'''

DAY = 24
MIN = 60

# Solution
def time_of_day(minutes):

    total_mins_in_day = DAY * MIN
    midninght = 00.00
    minutes = minutes % total_mins_in_day # This keeps us within the 1440 minutes frame
    
    if minutes == int(midninght):
        hours = int(minutes)
        min = int(minutes)

    hours = minutes // MIN 
    min = minutes % MIN

    return f"{hours:02d}:{min:02d}"

# code check
print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True

# Note!
# Time take to write PEDAC and test/debug code is 39 mins, 26 seconds.

## LS Answer ##

# MINUTES_PER_HOUR = 60
# HOURS_PER_DAY = 24
# MINUTES_PER_DAY = HOURS_PER_DAY * MINUTES_PER_HOUR

# def format_time(hours, minutes):
#     return f"{hours:02d}:{minutes:02d}"

# def time_of_day(delta_minutes):
#     delta_minutes = delta_minutes % MINUTES_PER_DAY
#     hours = delta_minutes // MINUTES_PER_HOUR
#     minutes = delta_minutes % MINUTES_PER_HOUR
#     return format_time(hours, minutes)