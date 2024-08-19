'''
Exercise 1
For each of the following pairs of classes, 
try to determine whether they have an "is-a" or "has-a" relationship or neither.

First Class     Second Class
Car             Engine
Teacher         Student
Flag            Color
Apple           Orange
Ship            Vessel
Structure       Home
Shape           Circle

'''

# solution

# First Class     Second Class      Relationship
# Car             Engine            has - a
# Teacher         Student           has - a
# Flag            Color             has - a
# Apple           Orange            neither
# Ship            Vessel            is - a 
# Structure       Home              has - a, is - a
# Shape           Circle            is - a



## LS Answer ##
# A car can have an engine, so this is a has-a relationship.

# A teacher is not generally a student, and a student is not generally a teacher.
# However, a teacher can have a student, or a student can have a teacher. 
# No matter how you look at it, this is a has-a relationship.

# A flag is not a color, nor is a color a flag.
# However, a flag can have several colors, so this is a has-a relationship.

# An apple is not an orange, nor is an orange an apple. 
# Likewise, apples don't have oranges, and oranges don't have apples. 
# This is neither an is-a nor a has-a relationship.

# A ship is a vessel, so this is an is-a relationship.

# A house is a structure, so this is an is-a relationship. 
# A house can also have multiple structures associated with it: a garage, a tool shed, an outhouse, etc. 
# That means this relation can also be seen as a has-a relationship from the house's perspective.

# A circle is a shape, so this is an is-a relationship.

# Some of the class names in this exercise may have multiple meanings.
# For instance, we use the shipping-based definition for vessels. 
# However, vessels are also defined as containers like bottles and kettles. 
# If we use the container definition, there is no relationship between a ship and a vessel. 
# The correct answers may vary based on how you interpreted the class names.