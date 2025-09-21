import sqlite3
import sys

# Récupérer l’argument de la ligne de commande
titre = sys.argv[1] if len(sys.argv) > 1 else None

conn = sqlite3.connect("bibliothèque.db")
cursor = conn.cursor()

if titre:
    cursor.execute("SELECT * FROM Livres WHERE titre = ?", (titre,))
else:
    cursor.execute("SELECT * FROM Livres")

rows = cursor.fetchall()

if rows:
    for row in rows:
        print(row)
else:
    print("Aucun résultat trouvé.")

conn.close()
