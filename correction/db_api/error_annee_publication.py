import sqlite3

conn = sqlite3.connect("bibliothèque.db")
cursor = conn.cursor()

try:
    # Tentative d'insertion avec une année non numérique (chaîne)
    cursor.execute(
        "INSERT INTO Livres (titre, auteur, annee_publication) VALUES (?, ?, ?)",
        ("Livre Test", "Auteur Test", "année_invalide")
    )
    conn.commit()
except sqlite3.OperationalError as e:
    print("Erreur opérationnelle :", e)
except sqlite3.IntegrityError as e:
    print("Erreur d'intégrité :", e)
finally:
    conn.close()
