#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 11:43:53 2024

@author: eden
"""

import matplotlib.pyplot as plt
import pandas as pd

old = pd.read_csv('/home/eden/Documents/Mémoire/données/echantillon.csv')

#BAR CHART TEMPS DE CARE POUR SON PROPRE MENAGE/ JOUR SELON 3 PERIMETRES DU TRAVAIL DOMESTIQUE
x_axis = ['Restraint', 'Intermédiaire', 'Elargi']
colors = ['#001F3F', '#FF6B00', '#006D5B']

#femmes en activités
core_fe = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 10), 'core'].mean()
int_fe = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 10), 'intermediate'].mean()
broad_fe = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 10), 'broad'].mean()
y_axis_fe = [core_fe, int_fe, broad_fe]

#hommes en activités
core_he = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 10), 'core'].mean()
int_he = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 10), 'intermediate'].mean()
broad_he = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 10), 'broad'].mean()
y_axis_he = [core_he, int_he, broad_he]

#femmes retraitées
core_fr = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 32), 'core'].mean()
int_fr = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 32), 'intermediate'].mean()
broad_fr = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 32), 'broad'].mean()
y_axis_fr = [core_fr, int_fr, broad_fr]

#hommes retraités
core_hr = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 32), 'core'].mean()
int_hr = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 32), 'intermediate'].mean()
broad_hr = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 32), 'broad'].mean()
y_axis_hr = [core_hr, int_hr, broad_hr]

#plot
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
ax1 = axes[0, 0]
ax2 = axes[0, 1]
ax3 = axes[1, 0]
ax4 = axes[1, 1]
plt.subplots_adjust(hspace=0.8, wspace=0.4)

bar3 = ax3.bar(x_axis, y_axis_fr, color=colors)
ax3.set_xlabel('Périmètre du Travail Domestique')
ax3.set_ylabel('Temps (minutes/jour)')
ax3.set_title("Femmes retraitées")
plt.setp(ax3.get_xticklabels(), rotation=70, ha="right")
for bar in bar3:
    height = round(bar.get_height())
    ax3.annotate(str(height), xy=(bar.get_x() + bar.get_width()/2, height), 
                xytext=(0, 0.1), textcoords="offset points",
                ha='center', va='bottom')

bar1 = ax1.bar(x_axis, y_axis_fe, color=colors)
ax1.set_xlabel('Périmètre du Travail Domestique')
ax1.set_ylabel('Temps (minutes/jour)')
ax1.set_title("Femmes en activité")
ax1.set_ylim(ax3.get_ylim())
plt.setp(ax1.get_xticklabels(), rotation=70, ha="right")
plt.setp(ax3.get_xticklabels(), rotation=70, ha="right")
for bar in bar1:
    height = round(bar.get_height())
    ax1.annotate(str(height), xy=(bar.get_x() + bar.get_width()/2, height), 
                xytext=(0, 0.1), textcoords="offset points",
                ha='center', va='bottom')


bar2 = ax2.bar(x_axis, y_axis_he, color=colors)
ax2.set_xlabel('Périmètre du Travail Domestique')
ax2.set_ylabel('Temps (minutes/jour)')
ax2.set_title("Hommes en activité")
ax2.set_ylim(ax3.get_ylim())
plt.setp(ax2.get_xticklabels(), rotation=70, ha="right")
plt.setp(ax3.get_xticklabels(), rotation=70, ha="right")
for bar in bar2:
    height = round(bar.get_height())
    ax2.annotate(str(height), xy=(bar.get_x() + bar.get_width()/2, height), 
                xytext=(0, 0.1), textcoords="offset points",
                ha='center', va='bottom')



bar4 = ax4.bar(x_axis, y_axis_hr, color=colors)
ax4.set_xlabel('Périmètre du Travail Domestique')
ax4.set_ylabel('Temps (minutes/jour)')
ax4.set_title("Hommes retraités")
ax4.set_ylim(ax3.get_ylim())
plt.setp(ax4.get_xticklabels(), rotation=70, ha="right")
plt.setp(ax3.get_xticklabels(), rotation=70, ha="right")
for bar in bar4:
    height = round(bar.get_height())
    ax4.annotate(str(height), xy=(bar.get_x() + bar.get_width()/2, height), 
                xytext=(0, 0.1), textcoords="offset points",
                ha='center', va='bottom')



plt.suptitle("Temps consacré au travail domestique en fonction du genre et du statut", fontsize=16)
plt.show()












