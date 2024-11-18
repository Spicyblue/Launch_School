'''
Reverse Engineering.

Write a class such that the following code prints the results indicated by the comments:

my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz

'''

# Solution

class Transform:

    def __init__(self, string):
        self.string = string

    def uppercase(self):
        return self.string.upper()

    @classmethod
    def lowercase(cls, string):
        return string.lower()

my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz

## LS Solution ##

# class Transform:
#     def __init__(self, data):
#         self.data = data

#     def uppercase(self):
#         return self.data.upper()

#     @classmethod
#     def lowercase(cls, str_):
#         return str_.lower()