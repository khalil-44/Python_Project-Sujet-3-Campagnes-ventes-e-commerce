# ===========================================================================
# VFinale.py
# Application finale du projet "Campagnes & ventes e-commerce" (Online Retail)
#
# Contrainte : pas de nouvelle fonction definie ici. On reutilise uniquement
# les fonctions deja ecrites en V1 et V2 (dans utils.py) ; tout le reste
# (graphiques, menu) est ecrit en sequentiel, directement dans la boucle.
#
# Menu :
#   1. CA par pays        -> tableau top 10 + barres (CA) + boxplot (paniers)
#   2. Ventes par mois     -> courbe CA/mois + histogramme des montants
#   3. Top produits        -> tableau des produits les plus vendus
#   4. Exporter            -> export Excel du top 10 pays + du top produits
#   5. Quitter
# ===========================================================================

import os
import matplotlib.pyplot as plt

from utils import (
    # V1 - fondations NumPy (sans pandas)
    lire_fichier_csv,
    extraire_Quantity_UnitPrice,
    filtrer_quantites_unitprices,
    calculer_montant,
    calculer_stats,
    # V2 - exploration pandas
    charger_csv_dataframe,
    nettoyer_dataframe,
    chiffre_affaires_par_pays,
    tableau_croise_pays_mois,
    exporter_top10_pays_ca,
)

NOM_FICHIER_DONNEES = "Online Retail.csv"
DOSSIER_EXPORT = "exports"

# ===========================================================================
# ETAPE 1 : Stats rapides V1 (NumPy, sans pandas)
# ===========================================================================
print("=" * 50)
print(" ONLINE RETAIL - PIPELINE COMPLET (V1 + V2 + Finale)")
print("=" * 50 + "\n")

print("--- Statistiques rapides (V1 - NumPy, sans pandas) ---")
lignes = lire_fichier_csv(NOM_FICHIER_DONNEES)
tableau = extraire_Quantity_UnitPrice(lignes)
tableau_filtre = filtrer_quantites_unitprices(tableau)
tableau_final = calculer_montant(tableau_filtre)
panier_moyen, quantite_mediane, montant_total = calculer_stats(tableau_final)

print(f"  Lignes valides (V1)   : {len(tableau_final)} / {len(lignes)}")
print(f"  Panier moyen          : {panier_moyen:.2f} £")
print(f"  Quantité médiane      : {quantite_mediane:.2f}")
print(f"  Montant total         : {montant_total:,.2f} £\n")

# ===========================================================================
# ETAPE 2 : Chargement + nettoyage V2 (pandas)
# ===========================================================================
print("Chargement et nettoyage des données (V2 - pandas)...")
df = charger_csv_dataframe(NOM_FICHIER_DONNEES)
df_propre = nettoyer_dataframe(df)
print(f"-> {len(df_propre)} lignes après nettoyage (sur {len(df)} lignes brutes).\n")

# ===========================================================================
# ETAPE 3 : Menu interactif
# ===========================================================================
os.makedirs(DOSSIER_EXPORT, exist_ok=True)

while True:
    print("\n" + "=" * 50)
    print(" ANALYSE DES VENTES - ONLINE RETAIL")
    print("=" * 50)
    print("1. CA par pays")
    print("2. Ventes par mois")
    print("3. Top produits")
    print("4. Exporter")
    print("5. Quitter")

    choix = input("Votre choix (1-5) : ").strip()
    match choix:
        # -----------------------------------------------------------------
        # OPTION 1 : CA par pays -> tableau + barres + boxplot des paniers
        # -----------------------------------------------------------------
        case "1":
            print("\n--- Chiffre d'affaires par pays (Top 10) ---")
            ca = chiffre_affaires_par_pays(df_propre).head(10)
            for pays, valeur in ca.items():
                print(f"  {pays:<20} {valeur:>15,.2f} £")

            # Graphique 1 : barres du CA par pays
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.bar(ca.index, ca.values, color="#4C72B0")
            ax.set_title(f"Chiffre d'affaires - Top {len(ca)} pays")
            ax.set_xlabel("Pays")
            ax.set_ylabel("Chiffre d'affaires (£)")
            ax.tick_params(axis="x", rotation=45)
            for label in ax.get_xticklabels():
                label.set_ha("right")
            fig.tight_layout()
            plt.show()

            # Graphique 2 : boxplot des paniers (montant par facture) pour ces pays
            top_pays = ca.index.tolist()
            paniers = df_propre.groupby(["Country", "InvoiceNo"])["Montant"].sum().reset_index()
            paniers_top = paniers[paniers["Country"].isin(top_pays)]
            data = [
                paniers_top.loc[paniers_top["Country"] == pays, "Montant"].values
                for pays in top_pays
            ]
            fig, ax = plt.subplots(figsize=(11, 6))
            ax.boxplot(data, labels=top_pays, showfliers=True)
            ax.set_title(f"Distribution des paniers par pays (Top {len(top_pays)} par CA)")
            ax.set_xlabel("Pays")
            ax.set_ylabel("Montant du panier (£)")
            ax.set_yscale("log")
            ax.tick_params(axis="x", rotation=45)
            for label in ax.get_xticklabels():
                label.set_ha("right")
            fig.tight_layout()
            plt.show()

        # -----------------------------------------------------------------
        # OPTION 2 : Ventes par mois -> courbe CA/mois + histogramme montants
        # -----------------------------------------------------------------
        case "2":
            print("\n--- Chiffre d'affaires par mois ---")
            pivot = tableau_croise_pays_mois(df_propre)
            total_par_mois = pivot.sum(axis=0)
            for mois, valeur in total_par_mois.items():
                print(f"  {str(mois):<10} {valeur:>15,.2f} £")

            # Graphique 3 : courbe du CA par mois
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(total_par_mois.index.astype(str), total_par_mois.values, marker="o", color="#DD8452")
            ax.set_title("Chiffre d'affaires par mois")
            ax.set_xlabel("Mois")
            ax.set_ylabel("Chiffre d'affaires (£)")
            ax.tick_params(axis="x", rotation=45)
            for label in ax.get_xticklabels():
                label.set_ha("right")
            ax.grid(True, alpha=0.3)
            fig.tight_layout()
            plt.show()

            # Graphique 4 : histogramme des montants de commande (par facture)
            paniers = df_propre.groupby(["Country", "InvoiceNo"])["Montant"].sum().reset_index()
            montants = paniers["Montant"]
            montants_affiches = montants[(montants >= 0) & (montants <= 1000)]
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.hist(montants_affiches, bins=40, color="#55A868", edgecolor="white")
            ax.set_title("Distribution des montants de commande (entre 0£ et 1000£)")
            ax.set_xlabel("Montant de la commande (£)")
            ax.set_ylabel("Nombre de commandes")
            ax.grid(True, alpha=0.3)
            fig.tight_layout()
            plt.show()

        # -----------------------------------------------------------------
        # OPTION 3 : Top produits (par CA et par quantité)
        # -----------------------------------------------------------------
        case "3":
            print("\n--- Top 10 produits par chiffre d'affaires ---")
            top_ca = (
                df_propre.groupby(["StockCode", "Description"])["Montant"]
                .sum()
                .sort_values(ascending=False)
                .head(10)
            )
            for (code, description), valeur in top_ca.items():
                print(f"  [{code}] {description[:40]:<40} {valeur:>12,.2f} £")

            print("\n--- Top 10 produits par quantité vendue ---")
            top_qte = (
                df_propre.groupby(["StockCode", "Description"])["Quantity"]
                .sum()
                .sort_values(ascending=False)
                .head(10)
            )
            for (code, description), valeur in top_qte.items():
                print(f"  [{code}] {description[:40]:<40} {valeur:>10,.0f} unités")

        # -----------------------------------------------------------------
        # OPTION 4 : Exporter les tableaux en Excel
        # -----------------------------------------------------------------
        case "4":
            chemin_pays = os.path.join(DOSSIER_EXPORT, "top10_pays_ca.xlsx")
            exporter_top10_pays_ca(df_propre, chemin_pays)
            print(f"-> Export top 10 pays : {chemin_pays}")

            top_ca = (
                df_propre.groupby(["StockCode", "Description"])["Montant"]
                .sum()
                .sort_values(ascending=False)
                .head(10)
            )
            chemin_produits = os.path.join(DOSSIER_EXPORT, "top10_produits.xlsx")
            top_ca.to_excel(chemin_produits)
            print(f"-> Export top 10 produits : {chemin_produits}")

            chemin_pivot = os.path.join(DOSSIER_EXPORT, "ca_pays_x_mois.xlsx")
            tableau_croise_pays_mois(df_propre).to_excel(chemin_pivot)
            print(f"-> Export tableau croisé pays x mois : {chemin_pivot}")

        # -----------------------------------------------------------------
        # OPTION 5 : Quitter
        # -----------------------------------------------------------------
        case "5":
            print("Au revoir !")
            break

        case _:
            print("Choix invalide, merci de saisir un nombre entre 1 et 5.")