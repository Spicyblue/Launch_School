'''
Exception Assertions.
Write a unittest assertion that will fail 
unless employee.hire raises a NoExperienceError exception.
'''

# Solution
import unittest

class NoExperienceError(Exception):
    pass

class Employee:
    def __init__(self, experience=0):
        self.experience = experience

    def hire(self):
        if self.experience < 1:
            raise NoExperienceError("Employee has no experience")
        return "Employee hired successfully"

class TestEmployee(unittest.TestCase):
    def setUp(self):
        # This method is called before each test
        self.employee_no_experience = Employee()
        self.employee_with_experience = Employee(2)

    def test_hire_no_experience(self):
        with self.assertRaises(NoExperienceError):
            self.employee_no_experience.hire()

    def test_hire_with_experience(self):

        self.assertEqual(self.employee_with_experience.hire(), "Employee hired successfully")

if __name__ == '__main__':
    unittest.main()

## LS Solution ##

# with self.assertRaises(NoExperienceError):
#     employee.hire()
