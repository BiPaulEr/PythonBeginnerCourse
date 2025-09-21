import sqlite3

# Connexion à la base de données (ou création si elle n'existe pas)
conn = sqlite3.connect("bibliothèque.db")
cursor = conn.cursor()

# Création de la table Livres
cursor.execute("""
CREATE TABLE IF NOT EXISTS Livres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titre TEXT NOT NULL,
    auteur TEXT NOT NULL,
    annee_publication INTEGER
)
""")

print("Table Livres créée (si elle n’existait pas déjà).")

# Sauvegarde et fermeture
conn.commit()
conn.close()
