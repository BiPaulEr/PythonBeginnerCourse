import ctypes
import os

# Charger la bibliothèque
lib = ctypes.CDLL("")

# Définir la structure Python correspondant à Monster


# Définir les types de la fonction


# Créer un tableau de monstres
monsters = [
    Monster(b"Dragon", 50, 30),
    Monster(b"Goblin", 20, 10),
    Monster(b"Troll", 40, 15)
]

# Convertir en tableau C
ArrayType = Monster * len(monsters)
c_array = ArrayType(*monsters)

# Appeler la fonction C
lib.boost_monsters(c_array, len(monsters))

# Afficher le résultat
for m in c_array:
    print(f"{m.name.decode()} -> Health: {m.health}, Mana: {m.mana}")
