#============Script de la V2===========
##DataFrame, to_datetime(InvoiceDate), retirer les lignes sans CustomerID.
#Segmenter : commandes d'un pays donné, montants > 100.
#groupby("Country") → chiffre d'affaires par pays ; pivot_table Country × mois.
#Export du top 10 des pays par CA
import pandas as pd
# Charger le fichier CSV dans un DataFrame Pandas
df = pd.read_csv("Online Retail.csv")

# InvoiceDate en datetime, retirer les lignes sans CustomerID
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df = df.dropna(subset=['CustomerID'])

# Retirer les annulations Quantity < 0 et les UnitPrice <= 0
df = df[(df['Quantity'] >= 0) & (df['UnitPrice'] > 0)]
# Créer la colonne Montant = Quantity * UnitPrice
df['Montant'] = df['Quantity'] * df['UnitPrice']

# Segmenter : commandes d'un pays donné, montants > 100
df_segment = df[(df['Country'] == 'United Kingdom') & (df['Montant'] > 100)]

# Chiffre d'affaires par pays
ca_par_pays = df.groupby('Country')['Montant'].sum().sort_values(ascending=False)

# Pivot_table Country × mois
df['Mois'] = df['InvoiceDate'].dt.to_period('M')
pivot_table = pd.pivot_table(df, values='Montant', index='Country', columns='Mois', aggfunc='sum', fill_value=0)

# Export du top 10 des pays par CA(fichier excel)
top_10_ca = ca_par_pays.head(10)
top_10_ca.to_excel("top_10_ca.xlsx")

# Affichage des résultats
print("Chiffre d'affaires par pays :")
print(ca_par_pays)
print("\nPivot_table Country × mois :")
print(pivot_table)
print("\nTop 10 des pays par chiffre d'affaires :")
print(top_10_ca)