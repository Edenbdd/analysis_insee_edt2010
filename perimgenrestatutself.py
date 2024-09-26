#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 06:36:34 2024

@author: eden
"""

import pandas as pd
import matplotlib.pyplot as plt

df =  pd.read_csv("/home/eden/Documents/Mémoire/final/tottempsperimetre.csv")

#dataframe
fe = df.loc[(df['sexe'] == 2) & (df['situa'] != 5) & (df['couplrp'] == 1)]
fr = df.loc[(df['sexe'] == 2) & (df['situa'] == 5) & (df['couplrp'] == 1)]
me = df.loc[(df['sexe'] == 1) & (df['situa'] != 5) & (df['couplrp'] == 1)]
mr = df.loc[(df['sexe'] == 1) & (df['situa'] == 5) & (df['couplrp'] == 1)]
#list
x_axis = ["Femmes non retraitées", "Femmes retraitées", "Hommmes non retraités", "Hommes retraités"]
data = [fe, fr, me, mr]
res_self = []
int_self = []
broad_self = []

#loop
for d in data:
    mean = d['res_self'].mean()
    res_self.append(mean)
for d in data:
    mean = d['int_self'].mean()
    int_self.append(mean)
for d in data:
    mean = d['broad_self'].mean()
    broad_self.append(mean)


#plot
plt.style.use('ggplot')

fig, ax = plt.subplots(figsize=(10, 6))

# Largeur des barres
bar_width = 0.2

# Positions des barres sur l'axe x
x = range(len(x_axis))
x1 = [i - bar_width for i in x]
x2 = x
x3 = [i + bar_width for i in x]

# Tracé des barres
ax.bar(x1, res_self, width=bar_width, label='périmètre restreint')
ax.bar(x2, int_self, width=bar_width, label='périmètre intermédiaire')
ax.bar(x3, broad_self, width=bar_width, label='périmètre élargi')

# Ajout des étiquettes sur l'axe x
ax.set_xticks(x)
ax.set_xticklabels(x_axis)

# Ajout des étiquettes sur l'axe y
ax.set_ylabel('Temps moyen (en min/jour)')

# Ajout des valeurs au-dessus des barres
for i, v in enumerate(res_self):
    ax.text(x1[i] - 0.1, v + 0.5, str(round(v, 1)), color='black', fontweight='bold')
for i, v in enumerate(int_self):
    ax.text(x2[i] - 0.1, v + 0.5, str(round(v, 1)), color='black', fontweight='bold')
for i, v in enumerate(broad_self):
    ax.text(x3[i] - 0.1, v + 0.5, str(round(v, 1)), color='black', fontweight='bold')

# Ajout de la légende
ax.legend()
plt.title("Temps moyen consacré au travail domestique en fonction du genre")
# Affichage du graphique
plt.show()
