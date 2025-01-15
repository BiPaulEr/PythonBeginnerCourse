"""
Calculus-related computations.
"""

def differentiate(f, x, h=1e-5):
    """
    Approximate the derivative of a function at a given point.

    :param f: The function to differentiate.
    :type f: callable
    :param x: The point at which to differentiate.
    :type x: float
    :param h: Step size for finite difference.
    :type h: float, optional
    :return: The approximate derivative of f at x.
    :rtype: float
    """
    return (f(x + h) - f(x - h)) / (2 * h)

def integrate(f, a, b, n=1000):
    """
    Approximate the integral of a function over an interval.

    :param f: The function to integrate.
    :type f: callable
    :param a: The start of the interval.
    :type a: float
    :param b: The end of the interval.
    :type b: float
    :param n: Number of subintervals for the approximation.
    :type n: int, optional
    :return: The approximate integral of f from a to b.
    :rtype: float
    """
    step = (b - a) / n
    return sum(f(a + i * step) * step for i in range(n))
