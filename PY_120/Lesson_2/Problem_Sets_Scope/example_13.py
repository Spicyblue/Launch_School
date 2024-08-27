'''
Example 13.

Consider the following code:

class Tree:
    def __init__(self):
        self.type = "Generic Tree"

class Pine(Tree):
    def __init__(self):
        super().__init__()
        self.type = "Pine Tree"

Answer the following question without running the code.

When an instance of Pine is created, what value will its type attribute have? Why?

'''

# Solution

class Tree:
    def __init__(self):
        self.type = "Generic Tree"

class Pine(Tree):
    def __init__(self):
        super().__init__()
        self.type = "Pine Tree"

# When an instance of `Pine` is created, its attribute `type`` will have a value of
# the string literal `"Pine Tree"`. 
# This is becuase the type attribute within the `Pine` class 
# overrides that of the parent class `Tree` and will always be return when it is being accessed.

## LS Solution ##   
# Subclasses and superclasses share instance variables. 
# Based on the code in Pine.__init__, we'll first call Tree.__init__
# where that shared variable will be set to 'Generic Tree'. 
# However, when execution returns to Pine.__init__, 
# self.type will be reassigned to 'Pine Tree'.