import pandas as pd
import numpy as np
import os

def generate_ventes_magasin(n=100, seed=42, output_file="ventes_magasin.csv"):
    # Seed pour rendre les données déterministes
    np.random.seed(seed)

    # Dates disponibles
    dates = pd.date_range(start="2023-01-01", end="2023-07-31").to_pydatetime().tolist()

    # PRODUITS + CATÉGORIE (3 catégories uniquement)
    produit_to_categorie = {
        # Jardinage
        "Pelle": "Jardinage",
        "Râteau": "Jardinage",
        "Tondeuse": "Jardinage",
        "Débroussailleuse": "Jardinage",

        # Quincaillerie
        "Vis métal": "Quincaillerie",
        "Boulons": "Quincaillerie",
        "Ruban adhésif": "Quincaillerie",
        "Marteau": "Quincaillerie",

        # Matériaux
        "Planche bois": "Matériaux",
        "Sac de ciment": "Matériaux",
        "Tuyau PVC": "Matériaux",
        "Peinture blanche": "Matériaux"
    }

    produits = list(produit_to_categorie.keys())

    # Choix des produits
    produits_choisis = np.random.choice(produits, n)

    # Construction de la DataFrame
    df = pd.DataFrame({
        "date_vente": np.random.choice(dates, n),
        "produduit": produits_choisis,
        "categorie": [produit_to_categorie[p] for p in produits_choisis],
        "quantite": np.random.randint(1, 21, n),
        "prix_unitaire": np.round(np.random.uniform(5.0, 150.0, n), 2),
        "magasin": np.random.choice(["Bricolage EST", "Bricolage NORD", "Bricolage SUD"], n)
    })

    # Sauvegarde CSV
    df.to_csv(output_file, index=False)
    print(f"✔ Fichier généré : {output_file}")

if __name__ == "__main__":
    output_file="ventes_magasin.csv"
    generate_ventes_magasin(output_file=os.path.join(os.path.dirname(__file__), output_file))
