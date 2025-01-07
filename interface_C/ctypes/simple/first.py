import ctypes
import os

lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "bibli.so"))

lib.afficher_message()

lib.somme.argtypes = [ctypes.c_int, ctypes.c_float]
lib.somme.restype = ctypes.c_double
print(lib.somme(3, 4))
