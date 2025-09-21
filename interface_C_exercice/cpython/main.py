#import de la librairie

# Création d’une liste de monstres (dictionnaires Python)
monsters_list = [
    {"name": "Dragon", "health": 50, "mana": 30},
    {"name": "Goblin", "health": 20, "mana": 10},
    {"name": "Troll", "health": 40, "mana": 15}
]

# Appel de la fonction C pour booster les monstres


# Afficher le résultat
for m in monsters_list:
    print(f"{m['name']} -> Health: {m['health']}, Mana: {m['mana']}")
