# Projet Fil Rouge — Analyse des ventes e-commerce (Online Retail)

**Formation Python 360° · Commission Scientifique nationale — ASEGUIM**
**Sujet 3 : Campagnes & ventes e-commerce**

## Contexte

Ce dépôt contient le projet réalisé par le groupe 5 composé de  3 étudiants dans le
cadre de la formation Python orientée analyse de données. L'objectif est de
charger, nettoyer, analyser et visualiser un vrai jeu de données de
transactions e-commerce, à travers trois livrables progressifs (V1, V2,
Finale).

## Jeu de données

**[Online Retail — UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/352/online+retail)**
≈ 541 909 lignes de transactions d'un site de vente en ligne britannique
(déc. 2010 – déc. 2011).

| Colonne | Description |
|---|---|
| `InvoiceNo` | numéro de facture (préfixe `C` = annulation) |
| `StockCode`, `Description` | produit |
| `Quantity` | quantité (peut être négative sur annulation) |
| `InvoiceDate` | date et heure de la commande |
| `UnitPrice` | prix unitaire |
| `CustomerID` | identifiant client (souvent manquant) |
| `Country` | pays du client |

> Le fichier source est fourni ici au format `Online Retail.xlsx`. Les scripts
> attendent un fichier `Online Retail.csv` (séparateur `;`, encodage UTF-8) :
> pensez à exporter/convertir le fichier Excel en CSV avant de lancer les
> scripts (Excel → *Enregistrer sous* → CSV UTF-8, séparateur point-virgule).

## Structure du dépôt

```
.
├── README.md              # ce fichier
├── Online Retail.xlsx      # jeu de données brut (source UCI)
├── Online Retail.csv        # jeu de données converti (à générer, non versionné)
├── utils.py                 # toutes les fonctions réutilisables (V1, V2, ...)
├── ScripV1.py                # script principal - Livrable V1 (NumPy)
├── ScriptV2.py                # script principal - Livrable V2 (pandas)
├── Vfinale.py                  # script principal - Livrable Finale (data-viz + appli menu)
├── top 10 CA par pays.xlsx     # export généré par la V2
└── exports/                     # exports générés par la Finale (option 4 du menu)
    ├── top10_pays_ca.xlsx
    ├── top10_produits.xlsx
    └── ca_pays_x_mois.xlsx
```

## Prérequis

- Python 3.9+
- Bibliothèques : `numpy`, `pandas`, `openpyxl`

Installation :

```bash
pip install numpy pandas openpyxl
```

## Livrables

### V1 — Fondations Python & NumPy (25 %)

Lecture du CSV sans pandas, conversion des colonnes `Quantity` et
`UnitPrice` en tableaux NumPy, création de la colonne `Montant`, filtrage
des annulations (`Quantity < 0`) et des prix nuls, puis calcul de
statistiques descriptives (panier moyen, quantité médiane, montant total).

Exécution :

```bash
python ScripV1.py
```

Sortie attendue :

```
Panier moyen: ...
Quantité médiane: ...
Montant total: ...
```

### V2 — Exploration pandas (35 %)

Chargement dans un DataFrame, nettoyage (dates, `CustomerID` manquants,
annulations), segmentation (par pays, par seuil de montant), calcul du
chiffre d'affaires par pays (`groupby`), tableau croisé Country × Mois
(`pivot_table`), et export du top 10 des pays par chiffre d'affaires.

Exécution :

```bash
python ScriptV2.py
```

Génère le fichier `top 10 CA par pays.xlsx`.

### Finale — Data-viz & application (40 %)

Application interactive en ligne de commande qui réutilise uniquement les
fonctions déjà écrites en V1 et V2 (aucune nouvelle fonction dans `utils.py`) :
au lancement, elle recalcule les statistiques rapides V1 (NumPy) puis charge
et nettoie les données (V2 - pandas), avant d'ouvrir un menu.

Exécution :

```bash
python Vfinale.py
```

Menu proposé :

| Option | Action |
|---|---|
| **1. CA par pays** | Tableau du top 10 pays par CA + graphique en barres + boxplot (échelle log) des paniers par pays |
| **2. Ventes par mois** | Tableau du CA par mois + courbe du CA par mois + histogramme des montants de commande (0–1000 £) |
| **3. Top produits** | Top 10 produits par chiffre d'affaires et top 10 par quantité vendue |
| **4. Exporter** | Export Excel dans `exports/` : top 10 pays (`top10_pays_ca.xlsx`), top 10 produits (`top10_produits.xlsx`), tableau croisé pays × mois (`ca_pays_x_mois.xlsx`) |
| **5. Quitter** | Fin de l'application |

Les 4 graphiques Matplotlib demandés dans le cahier des charges sont donc
couverts : barres (CA par pays), courbe (CA par mois), histogramme
(montants de commande) et boxplot (paniers par pays).

## Organisation du code

Toutes les fonctions sont centralisées dans `utils.py` et importées dans les
scripts principaux (`ScripV1.py`, `ScriptV2.py`, `Vfinale.py`), afin de garder
chaque script court, lisible et focalisé sur l'enchaînement des étapes. La
Finale ne redéfinit aucune nouvelle fonction : les graphiques et le menu sont
écrits de façon séquentielle directement dans `Vfinale.py`, au-dessus des
briques V1/V2 déjà validées.

## Auteurs
BAH THIERNO AMADOU KALIL
CHESAN CRISTOPHER
N'DEYE MARIAME BANGOURA
