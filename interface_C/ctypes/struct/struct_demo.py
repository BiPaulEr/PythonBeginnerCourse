import ctypes
import os

lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "bibli.so"))

class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_float)]

lib.modify_point.argtypes = [ctypes.POINTER(Point)]

point = Point(5, 2.5)

lib.modify_point(ctypes.byref(point))

print(f"Modified Point x: {point.x}, y: {point.y}")