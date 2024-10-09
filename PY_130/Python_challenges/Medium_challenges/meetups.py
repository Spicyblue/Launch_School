import unittest
from datetime import date
import calendar
'''
Meetups.
Meetups are a great way to meet people who share a common interest. Typically, meetups happen monthly on the same day of the week. For example, a meetup's meeting may be set as:

The first Monday of January 2021
The third Tuesday of December 2020
The teenth Wednesday of December 2020
The last Thursday of January 2021

In this program, we'll construct objects that represent a meetup date.
Each object takes a month number (1-12) and a year (e.g., 2021).
Your object should be able to determine the exact date of the meeting in the specified month and year.
For instance, if you ask for the 2nd Wednesday of May 2021,
the object should be able to determine that the meetup for that month will occur on the 12th of May, 2021.

The descriptors that may be given are strings:
'first', 'second', 'third', 'fourth', 'fifth', 'last', and 'teenth'.
The case of the strings is not important;
that is, 'first' and 'fIrSt' are equivalent.
Note that "teenth" is a made up word.
There was a meetup whose members realized that there are exactly 7 days that end in '-teenth'.
Therefore, it's guaranteed that each day of the week (Monday, Tuesday, ...) will have exactly one date that is the "teenth" of that day in every month.
That is, every month has exactly one "teenth" Monday,
one "teenth" Tuesday, etc.
The fifth day of the month may not happen every month,
but some meetup groups like that irregularity.

The days of the week are given by the strings 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', and 'Sunday'. Again, the case of the strings is not important.

'''

# Solution
'''
PEDAC
Problem:
    Input: Integers
    output: Strings

    Exp: 
    - Meetup occurs monthly on same day of the week.
    - Meetup objects takes a month and a year.
    - Meetup object should be able to determine the exact date of the meeting in the specified month and year
    - Descriptors that may be given are strings.
    - Every month has exactly one "teenth" day in the weeek.
    - The fifth day of the month may not happen every month.

    imp:
    - unittest test cases show that our we need Meetup class thats accept two arguments passed to its constructor.
    - The class should have a day instance method which takes in an two arguments which returns the exact date in specific format (y.d.m)
    - If a meetupdate doesnt exists, return None.
    
Examples:
Using unittest TestCase

Data Structure:
Class with class variables and methods.

Algorithm:
    Highend
    - Get Meetups with year and day.
    - Get the exact date for the meetup
    - Return the exact date.

    Lowend:
    - Create a Meetup class which accepts two arguments
    - Set the arguments passed  to instance variable _year and _month respectively.
    - Create a day instance method that accepts the weekday and schedule of the meetup.
    - Set the instance variable _day to None
    - Using the calendar module, access proerty day_name which returns calendar object
        - Convert this calendar object to a list and set to a variable weekdays
    - Convert the weekday to its corresponding integer (0 for Monday, 1 for Tuesday, etc.) using the calendar.day_name list.
    - Define a list of valid schedules.
    - Convert the input schedule to lowercase for case-insensitive comparison.
    - Get all the days of the specified weekday in the month using a list comprehension.
    - Depending on the schedule, we return the appropriate date (helper method). Set this to meetup_date.
    - Return meet_up date.

    - Helper method _get_date.
    - Define a instance method which accepts three arguments, day, schedule and list of schedules.
        - For 'teenth' schedule, we find the first day between 13 and 19 and return the date
        - For 'last', we use the last day in our list and return the date.
        - For others ('first', 'second', etc.), we use the day at the corresponding index and return the date.
        - If the requested day doesn't exist, we return None.
'''

class Meetup:
    def __init__(self, year, month):
        self._year = year
        self._month = month

    def day(self, weekday, schedule):
        self._day = None
        weekdays = list(calendar.day_name)
        weekday = weekdays.index(weekday.capitalize())
        
        schedules = ['first', 'second', 'third', 'fourth', 'fifth', 'last', 'teenth']
        schedule = schedule.lower()
        
        if schedule not in schedules:
            raise ValueError

        days = [day for day in 
                range(1, calendar.monthrange(self._year, self._month)[1] + 1)
                if date(self._year, self._month, day).weekday() == weekday]

        meetup_date = self._get_date(days, schedule, schedules)
        return meetup_date

    def _get_date(self, days, schedule, schedules):
        if schedule == 'teenth':
            self._day = next(day for day in days if 13 <= day <= 19)
            return date(self._year, self._month, self._day)

        elif schedule == 'last':
            self._day = days[-1]
            return date(self._year, self._month, self._day)

        else:
            index = schedules.index(schedule)
            if index < len(days):
                self._day = days[index]
                return date(self._year, self._month, self._day)
            else:
                return None

class MeetupTest(unittest.TestCase):

    def test_second_tuesday_of_december_2013(self):
        meetup = Meetup(2013, 12)
        self.assertEqual(date(2013, 12, 10), meetup.day('Tuesday', 'second'))

    def test_second_wednesday_of_january_2014(self):
        meetup = Meetup(2014, 1)
        self.assertEqual(date(2014, 1, 8), meetup.day('Wednesday', 'second'))

    def test_second_thursday_of_february_2014(self):
        meetup = Meetup(2014, 2)
        self.assertEqual(date(2014, 2, 13), meetup.day('Thursday', 'second'))

    def test_second_friday_of_march_2014(self):
        meetup = Meetup(2014, 3)
        self.assertEqual(date(2014, 3, 14), meetup.day('Friday', 'second'))

    def test_second_saturday_of_april_2014(self):
        meetup = Meetup(2014, 4)
        self.assertEqual(date(2014, 4, 12), meetup.day('Saturday', 'second'))

    def test_second_sunday_of_may_2014(self):
        meetup = Meetup(2014, 5)
        self.assertEqual(date(2014, 5, 11), meetup.day('Sunday', 'second'))

    def test_third_monday_of_june_2014(self):
        meetup = Meetup(2014, 6)
        self.assertEqual(date(2014, 6, 16), meetup.day('Monday', 'third'))

    def test_third_tuesday_of_july_2014(self):
        meetup = Meetup(2014, 7)
        self.assertEqual(date(2014, 7, 15), meetup.day('Tuesday', 'third'))

    def test_third_wednesday_of_august_2014(self):
        meetup = Meetup(2014, 8)
        self.assertEqual(date(2014, 8, 20), meetup.day('Wednesday', 'third'))

    def test_third_thursday_of_september_2014(self):
        meetup = Meetup(2014, 9)
        self.assertEqual(date(2014, 9, 18), meetup.day('Thursday', 'third'))

    def test_third_friday_of_october_2014(self):
        meetup = Meetup(2014, 10)
        self.assertEqual(date(2014, 10, 17), meetup.day('Friday', 'third'))

    def test_third_saturday_of_november_2014(self):
        meetup = Meetup(2014, 11)
        self.assertEqual(date(2014, 11, 15), meetup.day('Saturday', 'third'))

    def test_third_sunday_of_december_2014(self):
        meetup = Meetup(2014, 12)
        self.assertEqual(date(2014, 12, 21), meetup.day('Sunday', 'third'))

    def test_fourth_monday_of_january_2015(self):
        meetup = Meetup(2015, 1)
        self.assertEqual(date(2015, 1, 26), meetup.day('Monday', 'fourth'))

    def test_fourth_tuesday_of_february_2015(self):
        meetup = Meetup(2015, 2)
        self.assertEqual(date(2015, 2, 24), meetup.day('Tuesday', 'fourth'))

    def test_fourth_wednesday_of_march_2015(self):
        meetup = Meetup(2015, 3)
        self.assertEqual(date(2015, 3, 25), meetup.day('Wednesday', 'fourth'))

    def test_fourth_thursday_of_april_2015(self):
        meetup = Meetup(2015, 4)
        self.assertEqual(date(2015, 4, 23), meetup.day('Thursday', 'fourth'))

    def test_fourth_friday_of_may_2015(self):
        meetup = Meetup(2015, 5)
        self.assertEqual(date(2015, 5, 22), meetup.day('Friday', 'fourth'))

    def test_fourth_saturday_of_june_2015(self):
        meetup = Meetup(2015, 6)
        self.assertEqual(date(2015, 6, 27), meetup.day('Saturday', 'fourth'))

    def test_fourth_sunday_of_july_2015(self):
        meetup = Meetup(2015, 7)
        self.assertEqual(date(2015, 7, 26), meetup.day('Sunday', 'fourth'))

    def test_fifth_monday_of_august_2015(self):
        meetup = Meetup(2015, 8)
        self.assertEqual(date(2015, 8, 31), meetup.day('Monday', 'fifth'))

    def test_fifth_tuesday_of_september_2015(self):
        meetup = Meetup(2015, 9)
        self.assertEqual(date(2015, 9, 29), meetup.day('Tuesday', 'fifth'))

    def test_fifth_wednesday_of_october_2015(self):
        meetup = Meetup(2015, 10)
        self.assertIsNone(meetup.day('Wednesday', 'fifth'))

    def test_fifth_thursday_of_november_2015(self):
        meetup = Meetup(2015, 11)
        self.assertIsNone(meetup.day('Thursday', 'fifth'))

    def test_fifth_friday_of_december_2015(self):
        meetup = Meetup(2015, 12)
        self.assertIsNone(meetup.day('Friday', 'fifth'))

    def test_fifth_saturday_of_january_2016(self):
        meetup = Meetup(2016, 1)
        self.assertEqual(date(2016, 1, 30), meetup.day('Saturday', 'fifth'))

    def test_fifth_sunday_of_february_2016(self):
        meetup = Meetup(2016, 2)
        self.assertIsNone(meetup.day('Sunday', 'fifth'))

    def test_fifth_monday_of_february_2016(self):
        meetup = Meetup(2016, 2)
        self.assertEqual(date(2016, 2, 29), meetup.day('Monday', 'fifth'))

    def test_last_monday_of_march_2016(self):
        meetup = Meetup(2016, 3)
        self.assertEqual(date(2016, 3, 28), meetup.day('Monday', 'last'))

    def test_last_tuesday_of_april_2016(self):
        meetup = Meetup(2016, 4)
        self.assertEqual(date(2016, 4, 26), meetup.day('Tuesday', 'last'))

    def test_last_wednesday_of_may_2016(self):
        meetup = Meetup(2016, 5)
        self.assertEqual(date(2016, 5, 25), meetup.day('Wednesday', 'last'))

    def test_last_thursday_of_june_2016(self):
        meetup = Meetup(2016, 6)
        self.assertEqual(date(2016, 6, 30), meetup.day('Thursday', 'last'))

    def test_last_friday_of_july_2016(self):
        meetup = Meetup(2016, 7)
        self.assertEqual(date(2016, 7, 29), meetup.day('Friday', 'last'))

    def test_last_saturday_of_august_2016(self):
        meetup = Meetup(2016, 8)
        self.assertEqual(date(2016, 8, 27), meetup.day('Saturday', 'last'))

    def test_last_sunday_of_september_2016(self):
        meetup = Meetup(2016, 9)
        self.assertEqual(date(2016, 9, 25), meetup.day('Sunday', 'last'))

    def test_last_sunday_of_february_2015(self):
        meetup = Meetup(2015, 2)
        self.assertEqual(date(2015, 2, 22), meetup.day('Sunday', 'last'))

    def test_teenth_monday_of_october_2016(self):
        meetup = Meetup(2016, 10)
        self.assertEqual(date(2016, 10, 17), meetup.day('Monday', 'teenth'))

    def test_teenth_tuesday_of_november_2016(self):
        meetup = Meetup(2016, 11)
        self.assertEqual(date(2016, 11, 15), meetup.day('Tuesday', 'teenth'))

    def test_teenth_wednesday_of_december_2016(self):
        meetup = Meetup(2016, 12)
        self.assertEqual(date(2016, 12, 14), meetup.day('Wednesday', 'teenth'))

    def test_teenth_thursday_of_january_2017(self):
        meetup = Meetup(2017, 1)
        self.assertEqual(date(2017, 1, 19), meetup.day('Thursday', 'teenth'))

    def test_teenth_friday_of_february_2017(self):
        meetup = Meetup(2017, 2)
        self.assertEqual(date(2017, 2, 17), meetup.day('Friday', 'teenth'))

    def test_teenth_saturday_of_march_2017(self):
        meetup = Meetup(2017, 3)
        self.assertEqual(date(2017, 3, 18), meetup.day('Saturday', 'teenth'))

    def test_teenth_sunday_of_april_2017(self):
        meetup = Meetup(2017, 4)
        self.assertEqual(date(2017, 4, 16), meetup.day('Sunday', 'teenth'))

if __name__ == '__main__':
    unittest.main()

# # LS Solution ##
# from datetime import date, timedelta

# class Meetup:
#     DAY_OF_WEEK = {
#         'sunday': 6,
#         'monday': 0,
#         'tuesday': 1,
#         'wednesday': 2,
#         'thursday': 3,
#         'friday': 4,
#         'saturday': 5,
#     }

#     SCHEDULE_START_DAY = {
#         'first': 1,
#         'second': 8,
#         'third': 15,
#         'fourth': 22,
#         'fifth': 29,
#         'teenth': 13,
#         'last': None,
#     }

#     def __init__(self, year, month):
#         self.year = year
#         self.month = month
#         if self.month == 12:
#             self.days_in_month = (date(self.year + 1, 1, 1) - timedelta(days=1)).day
#         else:
#             self.days_in_month = (date(self.year, self.month + 1, 1) - timedelta(days=1)).day

#     def day(self, weekday, schedule):
#         weekday = weekday.lower()
#         schedule = schedule.lower()

#         first_possible_day = self.first_day_to_search(schedule)
#         last_possible_day = min(first_possible_day + 6, self.days_in_month)

#         day_of_week = self.DAY_OF_WEEK[weekday]

#         for day in range(first_possible_day, last_possible_day + 1):
#             current_date = date(self.year, self.month, day)
#             if current_date.weekday() == day_of_week:
#                 return current_date
#         return None

#     def first_day_to_search(self, schedule):
#         return self.SCHEDULE_START_DAY[schedule] or (self.days_in_month - 6)