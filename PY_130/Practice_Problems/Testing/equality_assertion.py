'''
Equality Assertions.
Write a unittest assertion that will fail if value.lower does not return 'xyz'.
'''

# Solution
import unittest

class Test(unittest.TestCase):

    def test_equality(self):
        value = 'XYZ'
        self.assertEqual('xyz', value.lower(), 'Objects are not the same ')

if __name__ == '__main__':
    unittest.main()

## LS Solution ##

# self.assertEqual('xyz', value.lower())