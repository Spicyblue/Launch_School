import unittest
from car import Car

class CarTest(unittest.TestCase):
    def setUp(self):
        self.car = Car()
    
    def test_car_exist(self):
        self.assertTrue(self.car is not None, "Car doesn't exist")

    def test_good_wheels(self):
        self.assertEqual(4, self.car.wheels, 'Doesnt seem to have the right wheels')

    def test_name_is_none(self):
        self.assertIsNone(self.car.name, "Object name is not None")

    def test_is_instance_of_car(self):
        self.assertIsInstance(self.car, Car, "Definitely not a Car")

    def test_includes_car(self):
        lst = [1, 2, 3, 4]
        lst.append(self.car)
        self.assertIn(self.car, lst, "Can't find car in the collection")
    
    def test_raise_initialize_with_arg(self):
        with self.assertRaises(TypeError):
            car = Car(name = 'Lambo')

    def test_set_name_raises(self):
        self.assertRaises(ValueError, setattr, self.car, 'name', 1234)

    @unittest.skip('Skiping an unfinished test')
    def test_bad_wheels(self):
        self.assertEqual(2, self.car.wheels, 'Doesnt seem to have the right wheels')

if __name__ == "__main__":
    print('Test starting')
    try:
        unittest.main()
    finally:
        print('Test ended')
