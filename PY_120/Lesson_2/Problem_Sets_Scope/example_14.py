'''
Example 14.

Consider the following code:

class A:
  def __init__(self):
      self.var_a = "A class variable"

class B(A):
    def __init__(self):
        self.var_b = "B class variable"

b = B()
print(b.var_a)
Without running this code, what will happen if you were to run it? Why?

'''

# Solution

class A:
  def __init__(self):
      self.var_a = "A class variable"

class B(A):
    def __init__(self):
        self.var_b = "B class variable"

b = B()
print(b.var_a)

# The code will raise an AttributeError if you were to run it.
# Since B.__init__ doesn't call super().__init__,
# b knows nothing about the var_a instance variable.
# var_a never gets initialized.

## LS Solution ##   
# The code will raise an AttributeError if you were to run it.
# Since B.__init__ doesn't call super().__init__,
# b knows nothing about the var_a instance variable.a