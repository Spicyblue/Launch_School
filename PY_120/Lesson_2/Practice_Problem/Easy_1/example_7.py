'''
Example 6.

Suppose you have the Oracle class and from above and a RoadTrip class
that inherits from the Oracle class, as shown below:

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

class RoadTrip(Oracle):
    def choices(self):
        return [
            'visit Vegas',
            'fly to Fiji',
            'romp in Rome',
            'go on a Scrabble cruise',
            'get hopelessly lost',
        ]

What will happen when you run the following code?

trip = RoadTrip()
print(trip.predict_the_future())

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

class RoadTrip(Oracle):
    def choices(self):
        return [
            'visit Vegas',
            'fly to Fiji',
            'romp in Rome',
            'go on a Scrabble cruise',
            'get hopelessly lost',
        ]

trip = RoadTrip()
print(trip.predict_the_future())

# When we run the following code, it will print one of 5 choices from the instance method `choices` 
# of the class `RoadTrip`.
# This is because the calling object `trip` is of the classs `RoadTrip`
# and it can call the instance method `predict_the_future` because it inherits the class `Oracle`.
# However, the instance method `choices` of the class `RoadTrip` gets used when `predict_the_future` is called.

## LS Solution ##

#This code will print one of 5 messages:
# You will visit Vegas.
# You will fly to Fiji.
# You will romp in Rome.
# You will go on a Scrabble cruise.
# You will get hopelessly lost.

# Each time you run this code, it will print one of those messages.
# It will make that choice randomly.

# Why does this happen? 
# Doesn't self.choices in predict_the_future look in the Oracle class for a choices method? 
# The answer is no. Since we're calling predict_the_future on an instance of RoadTrip,
# every time Python tries to resolve a method name using self.
# it first looks in the class of the calling object.
# Even though we called choices from with a method in the Oracle class,
# self refers to the RoadTrip class.
# Thus, Python first looks for RoadTrip.choices before falling back to Oracle.choices.
# To see the difference, change the name of the RoadTrip.choices to RoadTrip.chooses and rerun the program.
