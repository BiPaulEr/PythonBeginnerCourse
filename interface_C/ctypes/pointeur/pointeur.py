import ctypes
import os

lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "bibli.so"))

lib.modification_ptr_int.argtypes = [ctypes.POINTER(ctypes.c_int)]
variable_int = ctypes.c_int(0)

lib.modification_ptr_int(ctypes.byref(variable_int))

python_value = variable_int.value
print(python_value)
