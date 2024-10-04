'''
Equality Assertions.
Write a unittest assertion that will fail if value.lower does not return 'xyz'.
'''

# Solution
import unittest

class TestBolean(unittest.TestCase):

    def test_boolean(self):
        self.value = 'GXYZ'
        self.assertEqual(self.value.lower(), 'xyz', 'Objects are not the same ')

if __name__ == '__main__':
    unittest.main()

## LS Solution ##

# self.assertEqual('xyz', value.lower())