import unittest
'''
Clock.
Create a clock that is independent of date.
You should be able to add minutes to and subtract minutes from the time represented by a given Clock object.
Note that you should not mutate Clock objects when adding and subtracting minutes 
-- create a new Clock object.
Two clock objects that represent the same time should be equal to each other.
You may not use any built-in date or time functionality; just use arithmetic operations.

'''

# Solution
'''
PEDAC
Problem:
    Input: Integers
    output: string

    Exp: 
    - Clock is independent of date.
    - Clock objects should be able to add and substract minutes from clock object.
    - Create a new clock object when peroforming any manipulation.
    - Two clock objects that represent the same time should be equal to each other.

    imp:
    - unittest test cases show that our we need a Clock class thats doesnt accept any arguments passed to its constructor.
    - The class should have an at method which takes in an two arguments (hour and seconds)
    - Clock objects can perform addition and substaction with integers which return a new clock.
    
Examples:
Using unittest TestCase

Data Structure:
Class with class variables and methods.

Algorithm:
    Highend
    - Get clock with time and seconds always starting at 00:00
    - Perform any clock arithemtics
    - Return the clock object as string of hours and time

    Lowend:
    - A bit too complex to explain. Hope the code helps.
'''
class Clock:
    def __init__(self, hours=0, minutes=0):
        # This calculation converts everything to minutes 
        # uses modulo to ensure it's within a 24-hour period.
        self.all_minutes = (hours * 60 + minutes) % (24 * 60)

    @classmethod
    def at(cls, hour=0, minute=0):
        return cls(hour, minute)

    def __str__(self):
        hours, minutes = divmod(self.all_minutes, 60)
        return f"{hours:02d}:{minutes:02d}"

    def __eq__(self, other):
        if not isinstance(other, Clock):
            return NotImplemented
        return self.all_minutes == other.all_minutes

    def __add__(self, minutes):
        return Clock(0, self.all_minutes + minutes)

    def __sub__(self, minutes):
        return Clock(0, self.all_minutes - minutes)

class ClockTest(unittest.TestCase):
    def test_on_the_hour(self):
        self.assertEqual('08:00', str(Clock.at(8)))
        self.assertEqual('09:00', str(Clock.at(9)))

    def test_past_the_hour(self):
        self.assertEqual('11:09', str(Clock.at(11, 9)))

    def test_add_a_few_minutes(self):
        clock = Clock.at(10) + 3
        self.assertEqual('10:03', str(clock))

    def test_adding_does_not_mutate(self):
        old_clock = Clock.at(10)
        new_clock = old_clock + 3
        self.assertIsNot(new_clock, old_clock)

    def test_subtract_fifty_minutes(self):
        clock = Clock.at(0) - 50
        self.assertEqual('23:10', str(clock))

    def test_subtracting_does_not_mutate(self):
        old_clock = Clock.at(10)
        new_clock = old_clock - 50
        self.assertIsNot(new_clock, old_clock)

    def test_add_over_an_hour(self):
        clock = Clock.at(10) + 61
        self.assertEqual('11:01', str(clock))

    def test_wrap_around_at_midnight(self):
        clock = Clock.at(23, 30) + 60
        self.assertEqual('00:30', str(clock))

    def test_add_more_than_a_day(self):
        clock = Clock.at(10) + 3061
        self.assertEqual('13:01', str(clock))

    def test_subtract_a_few_minutes(self):
        clock = Clock.at(10, 30) - 5
        self.assertEqual('10:25', str(clock))

    def test_subtract_minutes(self):
        clock = Clock.at(10) - 90
        self.assertEqual('08:30', str(clock))

    def test_wrap_around_at_negative_midnight(self):
        clock = Clock.at(0, 30) - 60
        self.assertEqual('23:30', str(clock))

    def test_subtract_more_than_a_day(self):
        clock = Clock.at(10) - 3061
        self.assertEqual('06:59', str(clock))

    def test_equivalent_clocks(self):
        clock1 = Clock.at(15, 37)
        clock2 = Clock.at(15, 37)
        self.assertEqual(clock1, clock2)

    def test_non_equivalent_clocks(self):
        clock1 = Clock.at(15, 37)
        clock2 = Clock.at(15, 36)
        clock3 = Clock.at(14, 37)
        self.assertNotEqual(clock1, clock2)
        self.assertNotEqual(clock1, clock3)

    def test_wrap_around_backwards(self):
        clock1 = Clock.at(0, 30) - 60
        clock2 = Clock.at(23, 30)
        self.assertEqual(clock1, clock2)

if __name__ == '__main__':
    unittest.main()

# # LS Solution ##
# import random
# import string

# class Robot:
#     _names = set()

#     def __init__(self):
#         self._name = None

#     @property
#     def name(self):
#         if not self._name:
#             while True:
#                 potential_name = self._generate_name()
#                 if potential_name not in Robot._names:
#                     break
#             self._name = potential_name
#             Robot._names.add(self._name)
#         return self._name

#     def reset(self):
#         Robot._names.discard(self._name)
#         self._name = None

#     def _generate_name(self):
#         letters = ''.join(random.choices(string.ascii_uppercase, k=2))
#         numbers = ''.join(random.choices(string.digits, k=3))
#         return letters + numbers
