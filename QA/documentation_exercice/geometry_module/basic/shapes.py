"""
Shape-related computations.
"""

def area_circle(radius):
    """
    Calculate the area of a circle.

    :param radius: The radius of the circle.
    :type radius: float
    :return: The area of the circle.
    :rtype: float
    """
    from math import pi
    return pi * radius**2

def perimeter_rectangle(length, width):
    """
    Calculate the perimeter of a rectangle.

    :param length: The length of the rectangle.
    :type length: float
    :param width: The width of the rectangle.
    :type width: float
    :return: The perimeter of the rectangle.
    :rtype: float
    """
    return 2 * (length + width)
