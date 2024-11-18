'''
Example 1.

Which of the following are objects in Python? If they are objects,
 how can you find out what class they belong to?

True
'hello'
[1, 2, 3, 'happy days']
142
{1, 2, 3}
1.2345

'''

# Solution

# All of the above are objects in python and you can
#  find out what class they belong to using the the function `type` 
# or the __class__ magic variable on the object.

## LS Solution ##
# All of them are objects! All values in Python are an object,
#  so you never need to ask yourself "is this value an object?"
# because the answer every time will be "Yes!"

# You can determine what class an object belongs 
# to in Python by asking the object what its class is by
#  using the __class__ magic variable on the object, as you can see below:

# print(True.__class__)                        # <class 'bool'>
# print('hello'.__class__)                     # <class 'str'>
# print([1, 2, 3, 'happy days'].__class__)     # <class 'list'>
# print({1, 2, 3}.__class__)                   # <class 'set'>
# print((142).__class__)                       # <class 'int'>
# print(1.2345.__class__)                      # <class 'float'>

# Note that we must put parenthesis around an integer
# before using the __class__ variable; that's necessary 
# to distinguish the integer 142 from 142.something, which is not a number. 
# This is not necessary with floating point numbers like 1.2345.

# If you just want the class name without the clutter,
# you can use .__class__.__name__ instead:

# print(True.__class__.__name__)                      # bool
# print('hello'.__class__.__name__)                   # str
# print([1, 2, 3, 'happy days'].__class__.__name__)   # list
# print({1, 2, 3}.__class__.__name__)                 # set
# print((142).__class__.__name__)                     # int
# print(1.2345.__class__.__name__)                    # float
