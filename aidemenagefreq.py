#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 11:10:15 2024

@author: eden
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

men = pd.read_csv("/home/eden/Documents/Mémoire/csv/menage.csv")

x_ax = ['Aide ménagère', 'Pressing', 'Livraison de repas', 'Livraison de courses']
colors = ['#0072B2', '#D55E00', '#009E73', '#CC79A7']

men_old_e = men.loc[(men['AGEPR'] >= 55) & (men['AGEPR'] <= 65) & (men['SITUAPR'] != 5)]
men_old_r = men.loc[(men['AGEPR'] >= 55) & (men['AGEPR'] <= 65) & (men['SITUAPR'] == 5)]



#non retraités
aidemen_e = men_old_e.loc[men_old_e['AIDEMEN'] == 1, 'AIDEMENH'].mean(skipna=True)
serv31_e = men_old_e.loc[(men_old_e['SERV31'] == 1) & (men_old_e['SERV31P'] == 2), 'SERV31F'].mean(skipna=True)
serv32_e = men_old_e.loc[(men_old_e['SERV32'] == 1) & (men_old_e['SERV32P'] == 2), 'SERV32F'].mean(skipna=True)
serv33_e = men_old_e.loc[(men_old_e['SERV33'] == 1) & (men_old_e['SERV32P'] == 2), 'SERV33F'].mean(skipna=True)

y_ax_e = [aidemen_e, serv31_e, serv32_e, serv33_e]

#retraites

aidemen_r = men_old_r.loc[men_old_r['AIDEMEN'] == 1, 'AIDEMENH'].mean(skipna=True)
serv31_r = men_old_r.loc[(men_old_r['SERV31'] == 1) & (men_old_r['SERV31P'] == 2), 'SERV31F'].mean(skipna=True)
serv32_r = men_old_r.loc[(men_old_r['SERV32'] == 1) & (men_old_r['SERV32P'] == 2), 'SERV32F'].mean(skipna=True)
serv33_r = men_old_r.loc[(men_old_r['SERV33'] == 1) & (men_old_r['SERV32P'] == 2), 'SERV33F'].mean(skipna=True)

y_ax_r = [aidemen_r, serv31_r, serv32_r, serv33_r]
#plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
ax1.bar(x_ax, y_ax_e, color=colors)
ax1.set_title('Non retraités')
ax1.set_ylabel('Fréquence de recours (par semaine)')
plt.setp(ax1.get_xticklabels(), rotation=70, ha="right")
for i, v in enumerate(y_ax_e):
    ax1.text(i, v, str(round(v, 2)), color='black', ha='center', va='bottom')

ax2.bar(x_ax, y_ax_r, color=colors)
ax2.set_title('Retraités')
ax2.set_ylabel('Fréquence de recours (par semaine)')
ax2.set_ylim(ax1.get_ylim())
plt.setp(ax2.get_xticklabels(), rotation=70, ha="right")
for i, v in enumerate(y_ax_r):
    ax2.text(i, v, str(round(v, 2)), color='black', ha='center', va='bottom')

plt.suptitle("Frequence moyenne de recours moyen à différents types d'aides rémunérées en fonction du statut", fontsize=16)
plt.text(0.5, 0.95, "Parmi un échantillon de ménages ayant recours à ce type d'aide au moins une fois par semaine", 
         horizontalalignment='center', verticalalignment='top', transform=plt.gcf().transFigure, fontsize=12)
plt.show()




