import ctypes
import os

# Charger la bibliothèque compilée
stats = ctypes.CDLL("")

# Définir les types de la fonction
stats.sum_and_max_and_min.argtypes = [

]
stats.sum_and_max_and_min.restype = None

# Liste de nombres à analyser
data = [10, 5, 7, 3, 9, 12, 4]

# Préparer les variables pour le résultat
sum_result = 
max_result = 
min_result = 

# Convertir la liste en tableau C
ArrayType = ctypes.c_int * len(data)
c_array = ArrayType(*data)

# Appeler la fonction C
****

print(f"Somme : {sum_result.value}")
print(f"Maximum : {max_result.value}")
print(f"Minimum : {min_result.value}")

