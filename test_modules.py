import unittest
from modules import *


class TestEthanMarco(unittest.TestCase):
    """
    Class that represents all the unit tests run on modules.py.
    """
    def test_circle(self) -> None:
        """
        Method that uses value, TypeError, and ValueError tests, to test if the parameters are positive, numeric values,
        and if the correct value of the area is found for the circle function.
        """
        self.assertAlmostEqual(circle(1),  3.14159, delta=0.001)
        self.assertAlmostEqual(circle(.1), 0.031459, delta=0.001)

        with self.assertRaises(TypeError):
            circle('1')

        with self.assertRaises(ValueError):
            circle(-1)
            circle(0)

    def test_square(self) -> None:
        """
        Method that uses value, TypeError, and ValueError tests, to test if the parameters are positive, numeric values,
        and if the correct value of the area is found for the square function.
        """
        self.assertEqual(square(10),  100)
        self.assertAlmostEqual(square(.1), 0.01, delta=0.001)

        with self.assertRaises(TypeError):
            square('1')

        with self.assertRaises(ValueError):
            square(-1)
            square(0)

    def test_rectangle(self) -> None:
        """
        Method that uses value, TypeError, and ValueError tests, to test if the parameters are positive, numeric values,
        and if the correct value of the area is found for the rectangle function.
        """
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

    def test_triangle(self) -> None:
        """
        Method that uses value, TypeError, and ValueError tests, to test if the parameters are positive, numeric values,
        and if the correct value of the area is found for the triangle function.
        """
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

    def test_trapezoid(self) -> None:
        """
        Method that uses value, TypeError, and ValueError tests, to test if the parameters are positive, numeric values,
        and if the correct value of the area is found for the trapezoid function.
        """
        self.assertEqual(trapezoid(10, 14, 10),  120)
        self.assertAlmostEqual(trapezoid(.1, 14, 10), 70.5, delta=0.001)
        self.assertAlmostEqual(trapezoid(10, .14, 10), 50.7, delta=0.001)
        self.assertAlmostEqual(trapezoid(10, 14, .1), 1.2, delta=0.001)
        self.assertAlmostEqual(trapezoid(.1, .14, 10), 1.2, delta=0.001)
        self.assertAlmostEqual(trapezoid(.1, 14, .1), 0.705, delta=0.001)
        self.assertAlmostEqual(trapezoid(.1, .14, .1), 0.012, delta=0.001)
        self.assertAlmostEqual(trapezoid(10, .14, .1), .507, delta=0.001)

        with self.assertRaises(TypeError):
            trapezoid('10', '14', '10')
            trapezoid('10', 14, 10)
            trapezoid(10, '14', 10)
            trapezoid(10, 14, '10')
            trapezoid('10', '14', 10)
            trapezoid('10', 14, '10')
            trapezoid(10, '14', '10')

        with self.assertRaises(ValueError):
            trapezoid(-10, -14, -10)
            trapezoid(-10, 14, 10)
            trapezoid(10, -14, 10)
            trapezoid(10, 14, -10)
            trapezoid(-10, -14, 10)
            trapezoid(-10, 14, -10)
            trapezoid(10, -14, -10)
            trapezoid(0, 0, 0)
            trapezoid(10, 0, 0)
            trapezoid(0, 14, 0)
            trapezoid(0, 0, 10)
            trapezoid(10, 14, 0)
            trapezoid(10, 0, 10)
            trapezoid(0, 14, 10)

    def test_parallelogram(self) -> None:
        """
        Method that uses value, TypeError, and ValueError tests, to test if the parameters are positive, numeric values,
        and if the correct value of the area is found for the parallelogram function.
        """
        self.assertEqual(parallelogram(10, 15),  150)
        self.assertAlmostEqual(parallelogram(.5, 10), 5.0, delta=0.001)
        self.assertAlmostEqual(parallelogram(10, .2), 2, delta=0.001)
        self.assertAlmostEqual(parallelogram(.5, .2), 0.1, delta=0.001)

        with self.assertRaises(TypeError):
            parallelogram('10', '15')
            parallelogram('10', 15)
            parallelogram(10, '15')

        with self.assertRaises(ValueError):
            parallelogram(-10, 15)
            parallelogram(10, -15)
            parallelogram(-10, -15)
            parallelogram(0, 15)
            parallelogram(10, 0)
            parallelogram(0, 0)

    def test_pentagon(self) -> None:
        """
        Method that uses value, TypeError, and ValueError tests, to test if the parameters are positive, numeric values,
        and if the correct value of the area is found for the pentagon function.
        """
        self.assertAlmostEqual(pentagon(10), 172.048, delta=0.001)
        self.assertAlmostEqual(pentagon(.1), 0.017, delta=0.001)

        with self.assertRaises(TypeError):
            pentagon('1')

        with self.assertRaises(ValueError):
            pentagon(-1)
            pentagon(0)

    def test_hexagon(self):
        """
        Method that uses value, TypeError, and ValueError tests, to test if the parameters are positive, numeric values,
        and if the correct value of the area is found for the hexagon function.
        """
        self.assertAlmostEqual(hexagon(10), 259.808, delta=0.001)
        self.assertAlmostEqual(hexagon(.1), 0.026, delta=0.001)

        with self.assertRaises(TypeError):
            hexagon('1')

        with self.assertRaises(ValueError):
            hexagon(-1)
            hexagon(0)

    def test_octagon(self) -> None:
        """
        Method that uses value, TypeError, and ValueError tests, to test if the parameters are positive, numeric values,
        and if the correct value of the area is found for the octagon function.
        """
        self.assertAlmostEqual(octagon(10), 482.843, delta=0.001)
        self.assertAlmostEqual(octagon(.1), 0.048, delta=0.001)

        with self.assertRaises(TypeError):
            octagon('1')

        with self.assertRaises(ValueError):
            octagon(-1)
            octagon(0)


if __name__ == '__main__':
    unittest.main()
