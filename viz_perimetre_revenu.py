#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 12:58:31 2024

@author: eden
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

old = pd.read_csv('/home/eden/Documents/Mémoire/données/echantillon.csv')

#VALEURS
#général
colors = ['#E60049', '#0BB4FF', '#50E991']
category = ['Premier', 'Deuxième', 'Troisième', 'Quatrième', 'Cinquième']
xlabel = 'Quintiles'
ylabel = 'Temps (min/jour)'

#femmes actives
#core
core_fe1 = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 10) & (old['HHQ9_1'] == 1), 'core'].mean()
core_fe2 = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 10) & (old['HHQ9_1'] == 2), 'core'].mean()
core_fe3 = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 10) & (old['HHQ9_1'] == 3), 'core'].mean()
core_fe4 = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 10) & (old['HHQ9_1'] == 4), 'core'].mean()
core_fe5 = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 10) & (old['HHQ9_1'] == 5), 'core'].mean()
core_fe = [core_fe1, core_fe2, core_fe3, core_fe4, core_fe5]
#intermediate
int_fe1 = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 10) & (old['HHQ9_1'] == 1), 'intermediate'].mean()
int_fe2 = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 10) & (old['HHQ9_1'] == 2), 'intermediate'].mean()
int_fe3 = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 10) & (old['HHQ9_1'] == 3), 'intermediate'].mean()
int_fe4 = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 10) & (old['HHQ9_1'] == 4), 'intermediate'].mean()
int_fe5 = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 10) & (old['HHQ9_1'] == 5), 'intermediate'].mean()
int_fe = [int_fe1, int_fe2, int_fe3, int_fe4, int_fe5]
#broad
broad_fe1 = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 10) & (old['HHQ9_1'] == 1), 'broad'].mean()
broad_fe2 = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 10) & (old['HHQ9_1'] == 2), 'broad'].mean()
broad_fe3 = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 10) & (old['HHQ9_1'] == 3), 'broad'].mean()
broad_fe4 = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 10) & (old['HHQ9_1'] == 4), 'broad'].mean()
broad_fe5 = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 10) & (old['HHQ9_1'] == 5), 'broad'].mean()
broad_fe = [broad_fe1, broad_fe2, broad_fe3, broad_fe4, broad_fe5]

#homme actif
#core
core_he1 = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 10) & (old['HHQ9_1'] == 1), 'core'].mean()
core_he2 = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 10) & (old['HHQ9_1'] == 2), 'core'].mean()
core_he3 = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 10) & (old['HHQ9_1'] == 3), 'core'].mean()
core_he4 = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 10) & (old['HHQ9_1'] == 4), 'core'].mean()
core_he5 = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 10) & (old['HHQ9_1'] == 5), 'core'].mean()
core_he = [core_he1, core_he2, core_he3, core_he4, core_he5]
#intermediate
int_he1 = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 10) & (old['HHQ9_1'] == 1), 'intermediate'].mean()
int_he2 = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 10) & (old['HHQ9_1'] == 2), 'intermediate'].mean()
int_he3 = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 10) & (old['HHQ9_1'] == 3), 'intermediate'].mean()
int_he4 = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 10) & (old['HHQ9_1'] == 4), 'intermediate'].mean()
int_he5 = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 10) & (old['HHQ9_1'] == 5), 'intermediate'].mean()
int_he = [int_he1, int_he2, int_he3, int_he4, int_he5]
#broad
broad_he1 = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 10) & (old['HHQ9_1'] == 1), 'broad'].mean()
broad_he2 = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 10) & (old['HHQ9_1'] == 2), 'broad'].mean()
broad_he3 = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 10) & (old['HHQ9_1'] == 3), 'broad'].mean()
broad_he4 = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 10) & (old['HHQ9_1'] == 4), 'broad'].mean()
broad_he5 = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 10) & (old['HHQ9_1'] == 5), 'broad'].mean()
broad_he = [broad_he1, broad_he2, broad_he3, broad_he4, broad_he5]

#femmes retraitées
#core
core_fr1 = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 32) & (old['HHQ9_1'] == 1), 'core'].mean()
core_fr2 = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 32) & (old['HHQ9_1'] == 2), 'core'].mean()
core_fr3 = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 32) & (old['HHQ9_1'] == 3), 'core'].mean()
core_fr4 = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 32) & (old['HHQ9_1'] == 4), 'core'].mean()
core_fr5 = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 32) & (old['HHQ9_1'] == 5), 'core'].mean()
core_fr = [core_fr1, core_fr2, core_fr3, core_fr4, core_fr5]
#intermediate
int_fr1 = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 32) & (old['HHQ9_1'] == 1), 'intermediate'].mean()
int_fr2 = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 32) & (old['HHQ9_1'] == 2), 'intermediate'].mean()
int_fr3 = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 32) & (old['HHQ9_1'] == 3), 'intermediate'].mean()
int_fr4 = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 32) & (old['HHQ9_1'] == 4), 'intermediate'].mean()
int_fr5 = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 32) & (old['HHQ9_1'] == 5), 'intermediate'].mean()
int_fr = [int_fr1, int_fr2, int_fr3, int_fr4, int_fr5]
#broad
broad_fr1 = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 32) & (old['HHQ9_1'] == 1), 'broad'].mean()
broad_fr2 = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 32) & (old['HHQ9_1'] == 2), 'broad'].mean()
broad_fr3 = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 32) & (old['HHQ9_1'] == 3), 'broad'].mean()
broad_fr4 = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 32) & (old['HHQ9_1'] == 4), 'broad'].mean()
broad_fr5 = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 32) & (old['HHQ9_1'] == 5), 'broad'].mean()
broad_fr = [broad_fr1, broad_fr2, broad_fr3, broad_fr4, broad_fr5]

#hommes retraités
#core
core_hr1 = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 32) & (old['HHQ9_1'] == 1), 'core'].mean()
core_hr2 = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 32) & (old['HHQ9_1'] == 2), 'core'].mean()
core_hr3 = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 32) & (old['HHQ9_1'] == 3), 'core'].mean()
core_hr4 = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 32) & (old['HHQ9_1'] == 4), 'core'].mean()
core_hr5 = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 32) & (old['HHQ9_1'] == 5), 'core'].mean()
core_hr = [core_hr1, core_hr2, core_hr3, core_hr4, core_hr5]
#intermediate
int_hr1 = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 32) & (old['HHQ9_1'] == 1), 'intermediate'].mean()
int_hr2 = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 32) & (old['HHQ9_1'] == 2), 'intermediate'].mean()
int_hr3 = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 32) & (old['HHQ9_1'] == 3), 'intermediate'].mean()
int_hr4 = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 32) & (old['HHQ9_1'] == 4), 'intermediate'].mean()
int_hr5 = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 32) & (old['HHQ9_1'] == 5), 'intermediate'].mean()
int_hr = [int_hr1, int_hr2, int_hr3, int_hr4, int_hr5]
#broad
broad_hr1 = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 32) & (old['HHQ9_1'] == 1), 'broad'].mean()
broad_hr2 = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 32) & (old['HHQ9_1'] == 2), 'broad'].mean()
broad_hr3 = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 32) & (old['HHQ9_1'] == 3), 'broad'].mean()
broad_hr4 = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 32) & (old['HHQ9_1'] == 4), 'broad'].mean()
broad_hr5 = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 32) & (old['HHQ9_1'] == 5), 'broad'].mean()
broad_hr = [broad_hr1, broad_hr2, broad_hr3, broad_hr4, broad_hr5]



# Créer la figure et les sous-graphiques
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))

# Définir la largeur des barres et leur espacement
bar_width = 0.25
spacing = 0.1
x_pos = np.arange(len(category))

# Tracer les barres sur chaque sous-graphique
ax3.bar(x_pos - bar_width - spacing, core_fr, width=bar_width)
ax3.bar(x_pos - spacing, int_fr, width=bar_width)
ax3.bar(x_pos + bar_width - spacing, broad_fr, width=bar_width)
ax3.set_xticks(x_pos)
ax3.set_xticklabels(category, rotation=70, ha="right", fontsize=8)
ax3.set_xlabel(xlabel)
ax3.set_ylabel(ylabel)
ax3.set_title("Femmes retraitées")

ax1.bar(x_pos - bar_width - spacing, core_fe, width=bar_width)
ax1.bar(x_pos - spacing, int_fe, width=bar_width)
ax1.bar(x_pos + bar_width - spacing, broad_fe, width=bar_width)
ax1.set_xticks(x_pos)
ax1.set_xticklabels(category, rotation=70, ha="right", fontsize=8)
ax1.set_xlabel(xlabel)
ax1.set_ylabel(ylabel)
ax1.set_title("Femmes en activité")
ax1.set_ylim(ax3.get_ylim())

ax2.bar(x_pos - bar_width - spacing, core_he, width=bar_width)
ax2.bar(x_pos - spacing, int_he, width=bar_width)
ax2.bar(x_pos + bar_width - spacing, broad_he, width=bar_width)
ax2.set_xticks(x_pos)
ax2.set_xticklabels(category, rotation=70, ha="right", fontsize=8)
ax2.set_xlabel(xlabel)
ax2.set_ylabel(ylabel)
ax2.set_title("Hommes en activité")
ax2.set_ylim(ax3.get_ylim())

ax4.bar(x_pos - bar_width - spacing, core_hr, width=bar_width, label='Périmètre restreint')
ax4.bar(x_pos - spacing, int_hr, width=bar_width, label='Périmètre intermédiaire')
ax4.bar(x_pos + bar_width - spacing, broad_hr, width=bar_width, label='Périmètre élargi')
ax4.set_xticks(x_pos)
ax4.set_xticklabels(category, rotation=70, ha="right", fontsize=8)
ax4.set_xlabel(xlabel)
ax4.set_ylabel(ylabel)
ax4.set_title("Hommes retraités")
ax4.set_ylim(ax3.get_ylim())

fig.legend(loc='center')
plt.subplots_adjust(hspace=0.8, wspace=0.4)
plt.suptitle("Temps consacré au travail domestique en fonction du niveau de revenu", fontsize=16)
plt.show()













