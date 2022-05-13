import math


def circle(radius: float or int) -> float or int:
    """
    Function to calculate the area of a circle with a given radius
    :param radius: The numeric value of the circle's radius
    :return: The area of the circle: math.pi * (radius ** 2)
    """
    if type(radius) != int and type(radius) != float:
        raise TypeError('Not numeric input')

    if radius <= 0:
        raise ValueError('Non-positive input')

    area: float or int = math.pi * (radius ** 2)
    return area


def square(side: float or int) -> float or int:
    """
    Function to calculate the area of a square given a side length
    :param side: The numeric value of the square's side
    :return: The area of the square: side ** 2
    """
    if type(side) != int and type(side) != float:
        raise TypeError('Not numeric input')

    if side <= 0:
        raise ValueError('Non-positive input')

    area: float or int = side ** 2
    return area


def rectangle(length: float or int, width: float or int) -> float or int:
    """
    Function to calculate the area of a rectangle given its length and width
    :param length: The numeric value of the rectangle's length
    :param width: The numeric value of the rectangle's width
    :return: The area of the rectangle: length * width
    """
    if type(length) != int and type(length) != float:
        raise TypeError('Not numeric input')

    if type(width) != int and type(width) != float:
        raise TypeError('Not numeric input')

    if length <= 0:
        raise ValueError('Non-positive input')

    if width <= 0:
        raise ValueError('Non-positive input')

    area: float or int = length * width
    return area


def triangle(base: float or int, height: float or int) -> float or int:
    """
    Function to calculate the area of a triangle given its base and height
    :param base: The numeric value of the triangle's base
    :param height: The numeric value of the triangle's height
    :return: The area of the triangle: base * height / 2
    """
    if type(base) != int and type(base) != float:
        raise TypeError('Not numeric input')

    if type(height) != int and type(height) != float:
        raise TypeError('Not numeric input')

    if base <= 0:
        raise ValueError('Non-positive input')

    if height <= 0:
        raise ValueError('Non-positive input')

    area: float or int = (base * height) / 2
    return area


def trapezoid(base1: float or int, base2: float or int, height: float or int) -> float or int:
    """
    Function to calculate the area of a parallelogram given the value of its bases and height
    :param base1: The numeric value for the first base of the trapezoid
    :param base2: The numeric value for the second base of the trapezoid
    :param height: The numeric value for the height of the trapezoid
    :return: The area of the trapezoid: ((base1 + base2) / 2) * height
    """
    if type(base1) != int and type(base1) != float:
        raise TypeError('Not numeric input')

    if type(base2) != int and type(base2) != float:
        raise TypeError('Not numeric input')

    if type(height) != int and type(height) != float:
        raise TypeError('Not numeric input')

    if base1 <= 0:
        raise ValueError('Non-positive input')

    if base2 <= 0:
        raise ValueError('Non-positive input')

    if height <= 0:
        raise ValueError('Non-positive input')

    area: float or int = ((base1 + base2) / 2) * height
    return area


def parallelogram(base: float or int, height: float or int) -> float or int:
    """
    Function to calculate the area of a parallelogram given its base and height
    :param base: The numeric value of the parallelogram's length
    :param height: The numeric value of the parallelogram's width
    :return: The area of the parallelogram: base * height
    """
    if type(base) != int and type(base) != float:
        raise TypeError('Not numeric input')

    if type(height) != int and type(height) != float:
        raise TypeError('Not numeric input')

    if base <= 0:
        raise ValueError('Non-positive input')

    if height <= 0:
        raise ValueError('Non-positive input')

    area: float or int = base * height
    return area


def pentagon(side: float or int) -> float or int:
    """
    Function to calculate the area of a pentagon given a side length
    :param side: The numeric value of the pentagon's side
    :return: The area of the pentagon: apothem * 5 * side / 2
    """
    if type(side) != int and type(side) != float:
        raise TypeError('Not numeric input')

    if side <= 0:
        raise ValueError('Non-positive input')

    apothem: float or int = side / (2 * (math.tan(math.radians(180/5))))
    # The distance from the center of a side to the center of the shape

    area: float or int = (apothem * 5 * side) / 2
    return area


def hexagon(side: float or int) -> float or int:
    """
    Function to calculate the area of a hexagon given a side length
    :param side: The numeric value of the hexagon's side
    :return: The area of the hexagon: apothem * 6 * side / 2
    """
    if type(side) != int and type(side) != float:
        raise TypeError('Not numeric input')

    if side <= 0:
        raise ValueError('Non-positive input')

    apothem: float or int = side / (2 * (math.tan(math.radians(180/6))))
    # The distance from the center of a side to the center of the shape

    area: float or int = (apothem * 6 * side) / 2
    return area


def octagon(side: float or int) -> float or int:
    """
    Function to calculate the area of an octagon given a side length
    :param side: The numeric value of the octagon's side
    :return: The area of the octagon: apothem * 8 * side / 2
    """
    if type(side) != int and type(side) != float:
        raise TypeError('Not numeric input')

    if side <= 0:
        raise ValueError('Non-positive input')

    apothem: float or int = side / (2 * (math.tan(math.radians(180/8))))
    # The distance from the center of a side to the center of the shape

    area: float or int = (apothem * 8 * side) / 2
    return area


if __name__ == '__main__':
    print(circle(2.0))
    print(rectangle(2.0, 4.0))
    print(square(3.0))
    print(triangle(2.0, 5.0))
    print(trapezoid(2.0, 3.0, 2.0))
    print(parallelogram(2.0, 3.0))
    print(pentagon(5.0))
    print(hexagon(5.0))
    print(octagon(5.0))
