'''
Boolean Assertions.
Write a unittest assertion that will fail if value % 2 != 0 is not True.
'''

# Solution
import unittest

class TestBolean(unittest.TestCase):

    def test_boolean(self):
        self.value = 10
        self.assertTrue(self.value % 2 != 0, 'Modulus is zero')

if __name__ == '__main__':
    unittest.main()

## LS Solution ##

# self.assertTrue(value % 2 != 0, 'value is not odd')