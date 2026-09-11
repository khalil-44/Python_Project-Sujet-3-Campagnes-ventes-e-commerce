# Ce module contiendra l'ensemble des fonctions à reutiliser dans les différents scripts
import csv
import numpy as np
import pandas as pd
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


# ===================================================================
#===================Fonctions pour la V2 DU Projet====================================
#DataFrame, to_datetime(InvoiceDate), retirer les lignes sans CustomerID.
#Segmenter : commandes d'un pays donné, montants > 100.
#groupby("Country") → chiffre d'affaires par pays ; pivot_table Country × mois.
#Export du top 10 des pays par CA.

#fonction 5: qui va charger le fichier CSV dans un DataFrame Pandas 
def charger_csv_dataframe(nom_fichier):
    df = pd.read_csv(nom_fichier, sep=';', encoding='utf-8')
    return df

#fonction 6: nettoyer le dataframe : convertir la colonne InvoiceDate en datetime, retirer les lignes sans CustomerID
# retirer les annulations Quantity < 0 et les UnitPrice <= 0
# Creer la colonne Montant = Quantity * UnitPrice
def nettoyer_dataframe(df):
    df = df.copy()  # on crée une copie du DataFrame pour éviter de modifier l'original
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')  # convertir la colonne InvoiceDate en datetime
    df = df.dropna(subset=['CustomerID'])  # retirer les lignes sans CustomerID
    df = df[(df['Quantity'] >= 0) & (df['UnitPrice'] > 0)]  # retirer les annulations Quantity < 0 et les UnitPrice <= 0
    df['Montant'] = df['Quantity'] * df['UnitPrice']  # creer la colonne Montant = Quantity * UnitPrice
    return df

#fonction 7: segmenter le dataframe : commandes d'un pays donné, montants > 100
def segmenter_dataframe(df, pays, montant_min=100):
    df_segment = df[(df['Country'] == pays) & (df['Montant'] > montant_min)]  # segmenter le dataframe
    return df_segment

# fonction 8: calculer le chiffre d'affaires par pays
def chiffre_affaires_par_pays(df):
    ca_par_pays = df.groupby('Country')['Montant'].sum().sort_values(ascending=False)  # groupby("Country") → chiffre d'affaires par pays
    return ca_par_pays
# fonction 9: créer un tableau croisé dynamique Country × mois
def tableau_croise_pays_mois(df):
    df=df.copy()  # on crée une copie du DataFrame pour éviter de modifier l'original
    df['Mois'] = df['InvoiceDate'].dt.to_period('M')  # extraire le mois de la colonne InvoiceDate
    pivot_table = pd.pivot_table(df, values='Montant', index='Country', columns='Mois', aggfunc='sum', fill_value=0)  # pivot_table Country × mois
    return pivot_table

# fonction 10: exporter un fichier excel du top 10 des pays par chiffre d'affaires depuis le dataframe
def exporter_top10_pays_ca(df, nom_fichier):
    top10_pays = chiffre_affaires_par_pays(df).head(10)  # on récupère le top 10 des pays par chiffre d'affaires
    file_exported =top10_pays.to_excel(nom_fichier, index=True)  # on exporte le top 10 des pays par chiffre d'affaires dans un fichier excel
    return file_exported

########### Fin des fonctions pour la V2 DU Projet ############