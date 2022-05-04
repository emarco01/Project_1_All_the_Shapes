import math


def circle(radius):
    if type(radius) != int and type(radius) != float:
        raise TypeError('Not numeric input')

    if radius <= 0:
        raise ValueError('Non-positive input')

    area = math.pi * (radius ** 2)
    return area


def square(side):
    if type(side) != int and type(side) != float:
        raise TypeError('Not numeric input')

    if side <= 0:
        raise ValueError('Non-positive input')

    area = side ** 2
    return area


def rectangle(length, width):
    if type(length) != int and type(length) != float:
        raise TypeError('Not numeric input')

    if type(width) != int and type(width) != float:
        raise TypeError('Not numeric input')

    if length <= 0:
        raise ValueError('Non-positive input')

    if width <= 0:
        raise ValueError('Non-positive input')

    area = length * width
    return area


def triangle(base, height):
    if type(base) != int and type(base) != float:
        raise TypeError('Not numeric input')

    if type(height) != int and type(height) != float:
        raise TypeError('Not numeric input')

    if base <= 0:
        raise ValueError('Non-positive input')

    if height <= 0:
        raise ValueError('Non-positive input')

    area = (base * height) / 2
    return area


if __name__ == '__main__':
    print(circle(2.0))
    print(rectangle(2.0, 4.0))
    print(square(3.0))
    print(triangle(2.0, 5.0))
