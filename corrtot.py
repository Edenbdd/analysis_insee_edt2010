#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 10:31:03 2024

@author: eden
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données
df = pd.read_csv("/home/eden/Documents/Mémoire/final/reg/tablereg.csv")

#INT TOT HOM / INT TOT FEM
# Créer le scatter plot
plt.figure(figsize=(10, 8))
sns.scatterplot(x='int_tot_fem', y='int_tot_hom', data=df)

# Ajouter une ligne de référence y=x
min_val = min(df['int_tot_fem'].min(), df['int_tot_hom'].min())
max_val = max(df['int_tot_fem'].max(), df['int_tot_hom'].max())
plt.plot([min_val, max_val], [min_val, max_val], 'r--', label='y=x')

# Personnaliser le graphique
plt.title('Scatter plot de int_tot_hom en fonction de int_tot_fem')
plt.xlabel('int_tot_fem')
plt.ylabel('int_tot_hom')
plt.legend()

# Afficher le graphique
plt.tight_layout()
plt.show()

# Calculer la corrélation
correlation = df['int_tot_hom'].corr(df['int_tot_fem'])
print(f"Corrélation entre int_tot_hom et int_tot_fem : {correlation:.4f}")

#diff int tot
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Charger les données
df = pd.read_csv("/home/eden/Documents/Mémoire/final/reg/tablereg.csv")

# Créer une figure avec plusieurs sous-graphiques
fig, axes = plt.subplots(2, 2, figsize=(16, 14))
fig.suptitle("Visualisation de diff_int_tot", fontsize=16)

# 1. Histogramme
sns.histplot(df['diff_int_tot'], kde=True, ax=axes[0, 0])
axes[0, 0].set_title("Histogramme avec courbe de densité")
axes[0, 0].set_xlabel("diff_int_tot")

# 2. Boîte à moustaches
sns.boxplot(y=df['diff_int_tot'], ax=axes[0, 1])
axes[0, 1].set_title("Boîte à moustaches")
axes[0, 1].set_ylabel("diff_int_tot")

# 3. Graphique de densité
sns.kdeplot(df['diff_int_tot'], shade=True, ax=axes[1, 0])
axes[1, 0].set_title("Graphique de densité")
axes[1, 0].set_xlabel("diff_int_tot")

# 4. Q-Q plot
stats.probplot(df['diff_int_tot'], dist="norm", plot=axes[1, 1])
axes[1, 1].set_title("Q-Q Plot")

plt.tight_layout()
plt.show()

# Statistiques descriptives
print(df['diff_int_tot'].describe())

# Calculer et afficher le pourcentage de valeurs positives et négatives
total = len(df['diff_int_tot'])
positives = (df['diff_int_tot'] > 0).sum()
negatives = (df['diff_int_tot'] < 0).sum()
zeros = (df['diff_int_tot'] == 0).sum()

print(f"\nPourcentage de valeurs positives : {positives/total*100:.2f}%")
print(f"Pourcentage de valeurs négatives : {negatives/total*100:.2f}%")
print(f"Pourcentage de valeurs nulles : {zeros/total*100:.2f}%")
