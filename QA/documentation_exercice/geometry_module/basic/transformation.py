"""
Geometric transformations.
"""

def translate(point, dx, dy):
    """
    Translate a point by a given distance.

    :param point: A tuple (x, y) representing the point.
    :type point: tuple
    :param dx: Distance to translate along the x-axis.
    :type dx: float
    :param dy: Distance to translate along the y-axis.
    :type dy: float
    :return: The translated point as a tuple (x, y).
    :rtype: tuple
    """
    x, y = point
    return x + dx, y + dy

def scale(point, factor):
    """
    Scale a point by a given factor.

    :param point: A tuple (x, y) representing the point.
    :type point: tuple
    :param factor: Scaling factor.
    :type factor: float
    :return: The scaled point as a tuple (x, y).
    :rtype: tuple
    """
    x, y = point
    return x * factor, y * factor
