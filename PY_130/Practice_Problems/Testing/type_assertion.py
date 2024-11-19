'''
Type Assertions.
Write a unittest assertion that will fail if value is not an 
instance of the Numeric class exactly. 
value should not be an instance of one of Numeric's superclasses.
'''

# Solution
import unittest

class SuperNumeric:
    def __init__(self, supernumber):
        self.supnum = supernumber

class Numeric(SuperNumeric):
    def __init__(self, number1, number2):
        self.num  = number1
        super().__init__(number2)

class Test(unittest.TestCase):
    def setUp(self):
        # This method is called before each test
        self.numeric = Numeric(10, 20)
        self.supernumeric = SuperNumeric(30)

    def test_is_Numeric(self):
        self.assertIsInstance(self.numeric, Numeric) # Will pass
    
    def test_Numeric(self):
        self.assertIsInstance(self.supernumeric, Numeric) # Will fail
if __name__ == '__main__':
    unittest.main()

## LS Solution ##

# self.assertIsInstance(value, Numeric)
