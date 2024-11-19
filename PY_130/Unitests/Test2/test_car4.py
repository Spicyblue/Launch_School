import unittest
from car import Car

class CarTest(unittest.TestCase):
    def test_car_exist(self):
        car = Car()
        self.assertTrue(car is not None, "Car doesn't exist")

    def test_good_wheels(self):
        car = Car()
        self.assertEqual(4, car.wheels, 'Doesnt seem to have the right wheels')

    def test_name_is_none(self):
        car = Car()
        self.assertIsNone(car.name, "Object name is not None")

    def test_is_instance_of_car(self):
        car = Car()
        self.assertIsInstance(car, Car, "Definitely not a Car")

    def test_includes_car(self):
        car = Car()
        lst = [1, 2, 3, 4]
        lst.append(car)
        self.assertIn(car, lst, "Can't find car in the collection")

    @unittest.skip('Skiping an unfinished test')
    def test_bad_wheels(self):
        car = Car()
        self.assertEqual(2, car.wheels, 'Doesnt seem to have the right wheels')

if __name__ == "__main__":
    print('Test starting')
    try:
        unittest.main()
    finally:
        print('Test ended')
