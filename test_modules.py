import unittest
from modules import *


class TestEthanMarco(unittest.TestCase):
    def test_circle(self):
        self.assertAlmostEqual(circle(1),  3.14159, delta=0.001)
        self.assertAlmostEqual(circle(.1), 0.031459, delta=0.001)

        with self.assertRaises(TypeError):
            circle('1')

        with self.assertRaises(ValueError):
            circle(-1)
            circle(0)

    def test_square(self):
        self.assertEqual(square(10),  100)
        self.assertAlmostEqual(square(.1), 0.01, delta=0.001)

        with self.assertRaises(TypeError):
            square('1')

        with self.assertRaises(ValueError):
            square(-1)
            square(0)

    def test_rectangle(self):
        self.assertEqual(rectangle(10, 15),  150)
        self.assertAlmostEqual(rectangle(.5, 10), 5, delta=0.001)
        self.assertAlmostEqual(rectangle(10, .2), 2, delta=0.001)
        self.assertAlmostEqual(rectangle(.5, .2), 0.1, delta=0.001)

        with self.assertRaises(TypeError):
            rectangle('10', '15')
            rectangle('10', 15)
            rectangle(10, '15')

        with self.assertRaises(ValueError):
            rectangle(-10, 15)
            rectangle(10, -15)
            rectangle(-10, -15)
            rectangle(0, 15)
            rectangle(10, 0)
            rectangle(0, 0)

    def test_triangle(self):
        self.assertEqual(triangle(10, 15),  75)
        self.assertAlmostEqual(triangle(.5, 10), 2.5, delta=0.001)
        self.assertAlmostEqual(triangle(10, .2), 1, delta=0.001)
        self.assertAlmostEqual(triangle(.5, .2), 0.05, delta=0.001)

        with self.assertRaises(TypeError):
            triangle('10', '15')
            triangle('10', 15)
            triangle(10, '15')

        with self.assertRaises(ValueError):
            triangle(-10, 15)
            triangle(10, -15)
            triangle(-10, -15)
            triangle(0, 15)
            triangle(10, 0)
            triangle(0, 0)


if __name__ == '__main__':
    unittest.main()
