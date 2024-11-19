import unittest
import re
import random
import string
'''
Robot Name.
Write a program that manages robot factory settings.

When robots come off the factory floor, they have no name.
The first time you boot them up, a random name is generated,
such as RX837 or BC811.

Every once in a while, we need to reset a robot to its factory settings, 
which means that their name gets wiped.
The next time you ask, it will respond with a new random name.

The names must be random; they should not follow a predictable sequence.
Random names means there is a risk of collisions.
Your solution should not allow using the same name twice

'''

# Solution
'''
PEDAC
Problem:
    Input: None
    output: string

    Exp: 
    - Robots initially have no name.
    - A random name is generated first time they booth up.
    - Randon name is Two caps letter followed by 3 numbers (predictable sequence)
    - Robots name gets wiped once in a while.
    - Robot can not have same name

    imp:
    - unittest test cases show that our we need a Robot class thats doesnt 
      accept any arguments passed to its constructor.
    - The class should have a name attribute that stores the robot name. 
      Perhaps a property with a getter method name which returns the instance vaiable _name.
    - The class should have a reset method which creates a new robot name 
      that replaces the current robot name.
    
Examples:
Using unittest TestCase

Data Structure:
Class with class variables, instance variables and methods.
List and strings

Algorithm:
    Highend
    - Get a random robot name which follows the convention.
    - If asked for the name, return the robot name.
    - Reset the name only when required.

    Lowend:
    - Define a class Robot which accepts no arguments passed to the constructor.
    - Define a class variable _used_name and set to an empty list.
    - Set the instance variable _name to None.
    - Define a property @name:
        -Check if self._name is None:
            - If yes, generate the robot name and set to new_name.
            - Check if new_name exist in _used_name:
                - If yes, get a new robot_name and set to new_name.
                - Repeat until you get a new_name not in _used_name
            - Set _name to new_name
            - Add new_name to list _used_name
            - return instance variable self._name.
    - Define a instance method reset which takes no argument.
    - Clear out the names in _used_name
    - Reassign self.name to a new Robot name using the static method.
    - Define static helper method (generate_robot_name)
    - This would have no arguments.
    - Create a variable letters.
    - Randomly select two Uppercase Alphabets and assign to letters.
    - Create a varible numbers.
    - Randomly select three numbers and assign to numbers.
    - Create a variable robot_name and increment it with letter and numbers
    - Return robot_name
'''

class Robot:
    _used_name = []

    def __init__(self):
        self._name = None

    @property
    def name(self):
        if not self._name:
            new_name = self._get_robot_name()
            
            while new_name in Robot._used_name:
                new_name = self._get_robot_name()

            self._name = new_name
            Robot._used_name.append(new_name)
        return self._name

    def reset(self):
        Robot._used_name.clear()
        self._name = None
    
    @staticmethod
    def _get_robot_name():
        letters = ''.join(random.choices(string.ascii_uppercase, k=2))
        numbers = ''.join(random.choices(string.digits, k=3))
        robot_name = letters + numbers
        return robot_name

class RobotTest(unittest.TestCase):
    DIFFERENT_ROBOT_NAME_SEED = 1234
    SAME_INITIAL_ROBOT_NAME_SEED = 1000

    NAME_REGEXP = re.compile(r"^[A-Z]{2}\d{3}$")

    def test_has_name(self):
        self.assertTrue(self.NAME_REGEXP.match(Robot().name))

    def test_name_sticks(self):
        robot = Robot()
        self.assertEqual(robot.name, robot.name)

    def test_different_robots_have_different_names(self):
        random.seed(RobotTest.DIFFERENT_ROBOT_NAME_SEED)
        self.assertNotEqual(Robot().name, Robot().name)

    def test_reset_name(self):
        random.seed(RobotTest.DIFFERENT_ROBOT_NAME_SEED)
        robot = Robot()
        name1 = robot.name
        robot.reset()
        name2 = robot.name
        self.assertNotEqual(name1, name2)
        self.assertTrue(self.NAME_REGEXP.match(name2))

    def test_different_name_when_chosen_name_is_taken(self):
        random.seed(RobotTest.SAME_INITIAL_ROBOT_NAME_SEED)
        name1 = Robot().name
        random.seed(RobotTest.SAME_INITIAL_ROBOT_NAME_SEED)
        name2 = Robot().name
        self.assertNotEqual(name1, name2)

if __name__ == "__main__":
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
