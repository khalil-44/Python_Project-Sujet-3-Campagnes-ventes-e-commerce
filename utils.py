# Ce module contiendra l'ensemble des fonctions à reutiliser dans les différents scripts
import csv
import numpy as np
# fonction 1: qui servira à la leecture du fichier CSV "Online Retail.csv"
def lire_fichier_csv(nom_fichier):
    
    with open(nom_fichier, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        lignes = [row for row in reader]
        return lignes
           
# fonction 2: qui servira à la conversion des colonnes Quantity et UnitPrice en tableaux NumPy et création de la colonne Montant = Quantity * UnitPrice
# Pour cela on extrait les colonnes Quantity et UnitPrice du fichier CSV PUIS on les convertit en tableaux NumPy et on calcule la colonne Montant
def extraire_Quantity_UnitPrice(lignes, nom_colonne_quantity='Quantity',nom_colonne_unitprice='UnitPrice'):
     colones_2d =[]
     for ligne in lignes:
         try:                                 # permet de gérer les erreurs si les colonnes ne sont pas présentes ou si les valeurs ne sont pas convertibles en int ou float
             q=int(ligne[nom_colonne_quantity])    
             p=float(ligne[nom_colonne_unitprice])
         except (KeyError, TypeError, ValueError):
             continue
         colones_2d.append([q,p])# on ajoute les valeurs converties à la liste colones_2d
         Tableau = np.array(colones_2d) # on convertit la liste en tableau NumPy(de 2 dimensions)
     return Tableau 
# La conversion est terminée
# Maintenant on va filtrer les Quantites < 0 et les UnitPrice <= 0 après on cree la colonne Montant = Quantity * UnitPrice

# fonction 3: qui servira à Filtrer les Quantites < 0 et les UnitPrice <= 0
def filtrer_quantites_unitprices(Tableau):
    quantites = Tableau[:, 0]  # on récupère la première colonne (Quantity)
    unit_prices = Tableau[:, 1]  # on récupère la deuxième colonne (UnitPrice)
    mask = (quantites >= 0) & (unit_prices > 0)  # on crée un masque pour filtrer les valeurs
    Tableau = Tableau[mask]  # on applique le masque pour filtrer le tableau
    return Tableau

# fonction 4: qui servira à créer la colonne Montant en multipliant les Quantites filtrées par les UnitPrices filtrés
# et rajouter la colonne Montant au tableau NumPy
def calculer_montant(Tableau):
    Montant = Tableau[:, 0] * Tableau[:, 1]  # on calcule la colonne Montant
    Tableau = np.column_stack((Tableau, Montant))  # on ajoute la colonne Montant au tableau NumPy
    return Tableau


# Maintenant on procède aux calculs des premiers Stats notamment:

# 1-Panier moyen ; 2-Quantité mediane ; 3-Montant Total 

def calculer_stats(Tableau):
    panier_moyen = np.mean(Tableau[:, 2])  # on calcule le panier moyen
    quantite_mediane = np.median(Tableau[:, 0])  # on calcule la quantité médiane
    montant_total = np.sum(Tableau[:, 2])  # on calcule le montant total
    return panier_moyen, quantite_mediane, montant_total
