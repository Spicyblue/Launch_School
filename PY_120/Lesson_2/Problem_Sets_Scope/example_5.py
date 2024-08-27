'''
Example 5.

Define a Student class that has a class variable named school_name.
You should initialize the school name to 'Oxford'.
After defining the class, instantiate an instance of
the Student class and print the school name using that instance.

'''

# Solution

class Student:

    def __init__(self, school_name):
        self._school_name = school_name

oxford = Student('Oxford')
print(oxford._school_name)      # Outputs Oxford

## LS Solution ##
# class Student:
#     school_name = 'Oxford'

# student = Student()
# print(student.__class__.school_name)     # Oxford
# print(student.school_name)               # Oxford