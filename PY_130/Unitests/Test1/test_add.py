import unittest
from add import add

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3,4), 7, 'This fails the test')

if __name__ == '__main__':
    print('Starting test')
    unittest.main()
    print('Test ended')

