'''
Example 6.

Without running the following code, can you determine what the following code will do? 
Explain why you will get those results.

import random

class Oracle:
    def predict_the_future(self):
        return f'You will {random.choice(self.choices()}.'

    def choices(self):
        return [
            'eat a nice lunch',
            'take a nap soon',
            'stay at work late',
            'adopt a cat',
        ]

oracle = Oracle()
print(oracle.predict_the_future())

'''

# Solution.
import random

class Oracle:
    def predict_the_future(self):
        return f'You will {random.choice(self.choices())}.'

    def choices(self):
        return [
            'eat a nice lunch',
            'take a nap soon',
            'stay at work late',
            'adopt a cat',
        ]

oracle = Oracle()
print(oracle.predict_the_future())

# The following code snippet first imports a module module and then
# creats a class Oracle with two instance methods.
# Next object `oracle` created class the the instance method `predict_the_future`. 
# This method uses the random module method `choices` to 
# always randomly select an object within the returned 
# list in the `oracle` instance method `choice`.
# Hence, a new returned value is passed  to the instance method `predict_the_future` every time 
# `random.choice(self.choices())` is called. 
# This will finally output the string `You will` + the randomly returned object selected
# from the instance method `choices``


## LS Solution ##

# This code will print one of 4 messages:
# You wil eat a nice lunch.
# You wil take a nap soon.
# You wil stay at work late.
# You wil adopt a cat.
# Each time you run this code, it will print one of those messages. It will make that choice randomly.
