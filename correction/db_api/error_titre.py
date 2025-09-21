import sqlite3

conn = sqlite3.connect("bibliothèque.db")
cursor = conn.cursor()

try:
    # Tentative d'insertion sans titre (NULL)
    cursor.execute(
        "INSERT INTO Livres (titre, auteur, annee_publication) VALUES (?, ?, ?)",
        (None, "Auteur Inconnu", 2000)
    )
    conn.commit()
except sqlite3.IntegrityError as e:
    print("Erreur d'intégrité :", e)
finally:
    conn.close()
