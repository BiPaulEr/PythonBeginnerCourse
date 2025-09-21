import ctypes
import os

# Charger la bibliothèque compilée
stats = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "stats.so"))

# Définir les types de la fonction
stats.sum_and_max_and_min.argtypes = [
    ctypes.POINTER(ctypes.c_int), # array
    ctypes.c_int,                 # length
    ctypes.POINTER(ctypes.c_int), # sum
    ctypes.POINTER(ctypes.c_int),  # max
    ctypes.POINTER(ctypes.c_int)  # min
]
stats.sum_and_max_and_min.restype = None

# Liste de nombres à analyser
data = [10, 5, 7, 3, 9, 12, 4]

# Préparer les variables pour le résultat
sum_result = ctypes.c_int(0)
max_result = ctypes.c_int(0)
min_result = ctypes.c_int(0)

# Convertir la liste en tableau C
ArrayType = ctypes.c_int * len(data)
c_array = ArrayType(*data)

# Appeler la fonction C
stats.sum_and_max_and_min(c_array, len(data), ctypes.byref(sum_result), ctypes.byref(max_result), ctypes.byref(min_result))

print(f"Somme : {sum_result.value}")
print(f"Maximum : {max_result.value}")
print(f"Minimum : {min_result.value}")

