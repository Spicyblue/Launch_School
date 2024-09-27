import unittest
from car import Car

class CarTest(unittest.TestCase):
    def test_wheels(self):
        car = Car()
        self.assertEqual(4, car.wheels, 'Doesnt seem to have the right wheels')

if __name__ == "__main__":
    print('Test starting')
    try:
        unittest.main()
    finally:
        print('Test ended')