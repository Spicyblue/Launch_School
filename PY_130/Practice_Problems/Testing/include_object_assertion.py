'''
Included Object Assertions.
Write a unittest assertion that will fail if the 'xyz' is not in the list lst.
'''

# Solution
import unittest

class Test(unittest.TestCase):

    def test_object_in_collection(self):
        lst = ['xyz', 'notxyz', 'others']
        self.assertIn('xyz', lst)

if __name__ == '__main__':
    unittest.main()

## LS Solution ##

# self.assertIn('xyz', lst)
