import sqlite3

# Données à insérer
livres = [
    ("Les Misérables", "Victor Hugo", 1862),
    ("Le Petit Prince", "Antoine de Saint-Exupéry", 1943),
    ("Candide", "Voltaire", 1759),
]

conn = sqlite3.connect("bibliothèque.db")
cursor = conn.cursor()

# Insertion des données
cursor.executemany(
    "INSERT INTO Livres (titre, auteur, annee_publication) VALUES (?, ?, ?)",
    livres
)

print("3 livres insérés dans la table.")

conn.commit()
conn.close()
