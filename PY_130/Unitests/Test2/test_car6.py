import unittest
from car import Car

class CarTest(unittest.TestCase):
    def test_value_equality(self):
        car1 = Car()
        car2 = Car()

        car1.name = "Kim"
        car2.name = "Kim"

        self.assertEqual(car1, car2)  # this will pass
        self.assertIs(car1, car2)     # this will fail as it looks for object identity.

if __name__ == "__main__":
    print('Test starting')
    try:
        unittest.main()
    finally:
        print('Test ended')
