# Rapport — 5 découvertes majeures (V2 — Online Retail)

*Données : 397 884 lignes après nettoyage (sur 541 909 initiales), 4 338 clients uniques, 37 pays.*

## 1. Le Royaume-Uni écrase toutes les autres géographies

Le Royaume-Uni représente **82 % du chiffre d'affaires total** (7,31 M sur 8,91 M au total), ce qui confirme que le site est avant tout un acteur domestique britannique malgré une présence dans 37 pays.

## 2. Les Pays-Bas sont le 2ᵉ marché, loin devant les autres pays européens

Hors UK, les Pays-Bas arrivent en tête avec **285 446 de CA**, suivis de l'Irlande (EIRE, 265 546), de l'Allemagne (228 867) et de la France (209 024). Un écart notable puisque le 5ᵉ pays (Australie) tombe déjà à 138 521 — le marché est concentré sur une poignée de pays.

## 3. Une saisonnalité nette avec un pic avant Noël

Le CA mensuel grimpe fortement à partir de septembre 2011 et culmine en **novembre 2011 (1,16 M)**, avant de retomber en décembre — cohérent avec des achats de fin d'année passés en amont des fêtes plutôt que juste avant.

## 4. Le panier moyen par pays ne suit pas le classement du CA

Le Royaume-Uni domine en CA total, mais ce sont les **Pays-Bas (121 en moyenne par ligne de commande), l'Australie (117) et le Japon (117)** qui ont le panier moyen le plus élevé. Ces marchés ont peu de clients mais achètent en plus grosses quantités par commande.

## 5. Les produits les plus vendus sont des articles de déco/emballage à petit prix unitaire

Le produit le plus vendu en quantité est *"PAPER CRAFT, LITTLE BIRDIE"* (80 995 unités), suivi de pots de rangement en céramique et d'articles de déco à petit prix. Le volume de vente vient donc surtout d'articles peu chers achetés en grande quantité, plutôt que de produits chers achetés à l'unité.

---

*Chiffres calculés à partir du DataFrame nettoyé (CustomerID non nul, annulations et prix ≤ 0 exclus), via les fonctions `ca_par_pays`, `pivot_pays_mois` et des `groupby` complémentaires dans `utils.py`.*
