'''
Not Included Object Assertions.
Write a test that will fail if 'xyz' is one of the elements in the list lst:
'''

# Solution
import unittest

class Test(unittest.TestCase):

    def test_not_included_in_collection(self):
        lst = ['notxyz', 'others']
        self.assertNotIn('xyz', lst)

if __name__ == '__main__':
    unittest.main()

## LS Solution ##

# self.assertNotIn('xyz', list)
