#============Script de la V2===========
from utils import (charger_csv_dataframe, 
                   nettoyer_dataframe, 
                   segmenter_par_pays,
                   segmenter_par_seuil_mont,
                   chiffre_affaires_par_pays,
                   tableau_croise_pays_mois,
                   exporter_top10_pays_ca)

def main():
    print("=============== Resultats des Analyses ===============")
    # charger Online Retail.csv
    dataframe = charger_csv_dataframe("Online Retail.csv")

    # nettoyage du dataframe
    df_nettoye = nettoyer_dataframe(dataframe)

    # segmenter le dataframe selon United kingdom

    df_uk = segmenter_par_pays(df_nettoye, pays = "United Kingdom")
    print(f"\nNombre de commandes en France : {len(df_uk)}")

    # Commandes dont le montant superieur à 100

    df_grosses_commandes = segmenter_par_seuil_mont(df_nettoye)
    print("\nNombre de commandes > 100 : {len(df_grosses_commandes)}")

    # calcul du chiffres d'affaires par pays
    print("\nChiffre d'Afffaires par Pays:")
    print("\n")
    print(f"{chiffre_affaires_par_pays(df_nettoye)}")

    # Creation du tableau croisé dynamique : country x mois
    print("\n Chiffre par pays à chaque Mois:")
    print("\n")
    print(tableau_croise_pays_mois(df_nettoye))


    # Export du top 10 des pays par CA
    exporter_top10_pays_ca(df_nettoye, nom_fichier= "top 10 CA par pays.xlsx")


if __name__ == "__main__":
    main()

# Fin du script V2





