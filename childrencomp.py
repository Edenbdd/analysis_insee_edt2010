#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 10:35:08 2024

@author: eden
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Charger les données
df = pd.read_csv("/home/eden/Documents/Mémoire/final/children/tottempschildren.csv")

# Définir les catégories et les groupes
categories = ['Jouer', 'Prendre soin']
groupes = ['25-54 ans\n(enfants)', '55-65 ans\n(petits-enfants)']

# Données
#dataset
fy = df.loc[(df['age'] >= 25) & (df['age'] <= 54) & (df['sexe'] == 2) & (df['NENFANTS'] != 0)]
fo = df.loc[(df['age'] >= 55) & (df['age'] <= 65) & (df['sexe'] == 2)]
hy = df.loc[(df['age'] >= 25) & (df['age'] <= 54) & (df['sexe'] == 1) & (df['NENFANTS'] != 0)]
ho = df.loc[(df['age'] >= 55) & (df['age'] <= 65) & (df['sexe'] == 1)]

# Calculer les différences (femmes - hommes)
jouer = [
    (fy['children_play_self'].mean() - hy['children_play_self'].mean()) * 365 / 60,
    (fo['children_play_other'].mean() - ho['children_play_other'].mean()) * 365 / 60
]

soin = [
    (fy['children_care_self'].mean() - hy['children_care_self'].mean()) * 365 / 60,
    (fo['children_care_other'].mean() - ho['children_care_other'].mean()) * 365 / 60
]

# Paramètres du graphique
x = np.arange(len(groupes))
width = 0.35

# Créer le graphique
plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(10, 6))

# Barres pour "Jouer"
rects1 = ax.bar(x - width/2, jouer, width, label='Jouer', color='skyblue')

# Barres pour "Prendre soin"
rects2 = ax.bar(x + width/2, soin, width, label='Prendre soin', color='lightgreen')

# Personnaliser le graphique
ax.set_ylabel('Différence de temps moyen (heures/an)')
ax.set_title('Différence de temps moyen consacré aux enfants et aux petits-enfants (Femmes - Hommes)')
ax.set_xticks(x)
ax.set_xticklabels(groupes)
ax.legend()

# Ajouter une ligne horizontale à y=0
ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)

# Ajouter les valeurs sur les barres
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.1f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3 if height > 0 else -3),  # Ajustement vertical selon le signe
                    textcoords="offset points",
                    ha='center', va='bottom' if height > 0 else 'top')

autolabel(rects1)
autolabel(rects2)

# Ajuster la mise en page
fig.tight_layout()

# Afficher le graphique
plt.show()
