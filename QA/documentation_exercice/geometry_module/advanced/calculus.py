"""
Calculus-related geometric computations.
"""

def arc_length(f, a, b, n=1000):
    """
    Approximate the arc length of a curve between two points.

    :param f: The function representing the curve y = f(x).
    :type f: callable
    :param a: The starting x-coordinate.
    :type a: float
    :param b: The ending x-coordinate.
    :type b: float
    :param n: Number of subintervals for the approximation.
    :type n: int, optional
    :return: The approximate arc length of the curve.
    :rtype: float
    """
    from math import sqrt
    step = (b - a) / n
    return sum(sqrt(1 + (f(a + i * step + step / 2) - f(a + i * step))**2 / step**2) * step for i in range(n))

def surface_area_sphere(radius):
    """
    Calculate the surface area of a sphere.

    :param radius: The radius of the sphere.
    :type radius: float
    :return: The surface area of the sphere.
    :rtype: float
    """
    from math import pi
    return 4 * pi * radius**2
