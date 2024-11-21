import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(5, 5), 10)
        self.assertEqual(self.calc.add(10, 11), 21)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(17, 6), 11)
        self.assertEqual(self.calc.subtract(99, 78), 21)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 3), 9)
        self.assertEqual(self.calc.multiply(4, 9), 36)

    def test_divide(self):
        self.assertEqual(self.calc.divide(100, 5), 20)
        self.assertEqual(self.calc.divide(200, 20), 10)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(4, 2), 0)
        self.assertEqual(self.calc.modulo(11, 4), 3)


    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()