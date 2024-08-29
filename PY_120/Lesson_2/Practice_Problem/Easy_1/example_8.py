'''
Example 8.

Suppose you have an object named my_obj and that you want to call
a method named foo using my_obj as the caller.
How can you see where Python will look for the method.
You don't need to determine the actual method location;
just identifying the search sequence is sufficient.

'''

# Solution.

# The method resolution order (MRO) shows how python will search for the method name 
# `foo` using `my_obj` as the caller. It will first search the class of `my_obj` 
# and if it doesnt find the method, it searches up the inheritance class (if there is an inheritance).
# Finally it searches the parent class `object` and if it doesnt find anything, it throws an error.

## LS Solution ##

# The class.mro method is defined by the class class, a superclass of all Python classes.
# It returns the method resolution order (MRO) for the class that invokes it.
# Thus. if we want the MRO of a Vehicle class, we can call Vehicle.mro().
# We don't have a class, however. 
# Fortunately, it's easy to determine the class of an object;
# query the __class__ variable associated with all objects. 
# Thus, we write my_obj.__class__.mro() to call the mro method.

# The output of mro() is a bit ugly to look at. If you want to print it more cleanly,
# you can use a for loop and the __name__ variable:

# for klass in my_obj.__class__.mro():
#     print(klass.__name__)

# The MRO is also called the lookup chain, since Python will look for a method starting in the first class in the chain, then the second class, and so on until it gets to the ultimate superclass, object.
# If the method appears nowhere in the chain, Python will raise an AttributeError.