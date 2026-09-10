# Icii on passera nos instructions pour le script V1
# En 1er lieu, on va importer le module utils.py pour pouvoir utiliser les fonctions qu'il contient

from utils import (lire_fichier_csv, 
                   extraire_Quantity_UnitPrice, 
                   filtrer_quantites_unitprices, 
                   calculer_montant, 
                   calculer_stats)

def main():
    # Lecture du fichier CSV
    nom_fichier = "Online Retail.csv"
    lignes = lire_fichier_csv(nom_fichier)

    # Extraction des colonnes Quantity et UnitPrice et création de la colonne Montant
    Tableau = extraire_Quantity_UnitPrice(lignes)

    # Filtrage des Quantites < 0 et des UnitPrices <= 0
    Tableau_filtre = filtrer_quantites_unitprices(Tableau)

    # Calcul de la colonne Montant
    Tableau_final = calculer_montant(Tableau_filtre)

    # Calcul des statistiques
    panier_moyen, quantite_mediane, montant_total = calculer_stats(Tableau_final)

    # Affichage des résultats
    print(f"Panier moyen: {panier_moyen:.2f}")
    print(f"Quantité médiane: {quantite_mediane:.2f}")
    print(f"Montant total: {montant_total:.2f}")

if __name__ == "__main__":
    main()

# Fin du scriptV1.py
