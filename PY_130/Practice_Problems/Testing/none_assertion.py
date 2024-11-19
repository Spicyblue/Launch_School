'''
None Assertions.
Write a unittest assertion that will fail if value is not None.
'''

# Solution
import unittest

class Test(unittest.TestCase):

    def test_none(self):
        value = None
        self.assertEqual(None, value, 'Value is not None ')
        self.assertIsNone(value)

if __name__ == '__main__':
    unittest.main()

## LS Solution ##

# self.assertIsNone(value)

