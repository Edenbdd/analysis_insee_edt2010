#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 11:10:15 2024

@author: eden
"""

import pandas as pd
import matplotlib.pyplot as plt

men = pd.read_csv("/home/eden/Documents/Mémoire/csv/menage.csv")

x_ax = ['Aide ménagère', 'Pressing', 'Livraison de repas', 'Livraison de courses']
colors = ['#0072B2', '#D55E00', '#009E73', '#CC79A7']


#non retraités
men_old_e = men.loc[(men['AGEPR'] >= 55) & (men['AGEPR'] <= 65) & (men['SITUAPR'] != 5)]

tot_old_e = len(men_old_e)

aidemen_e = len(men_old_e.loc[(men_old_e['AIDEMEN'] == 1) & (men_old_e['AIDEMENH'] >= 1)])
serv31_e = len(men_old_e.loc[(men_old_e['SERV31'] == 1) & (men_old_e['SERV31P'] == 2)])
serv32_e = len(men_old_e.loc[(men_old_e['SERV32'] == 1) & (men_old_e['SERV32P'] == 2)])
serv33_e = len(men_old_e.loc[(men_old_e['SERV33'] == 1) & (men_old_e['SERV32P'] == 2)])

perc_aidemen_e = (aidemen_e/tot_old_e) * 100
perc_serv31_e = (serv31_e/tot_old_e) * 100
perc_serv32_e = (serv32_e/tot_old_e) * 100
perc_serv33_e = (serv33_e/tot_old_e) * 100

y_ax_e = [perc_aidemen_e, perc_serv31_e, perc_serv32_e, perc_serv33_e]

#retraites
men_old_r = men.loc[(men['AGEPR'] >= 55) & (men['AGEPR'] <= 65) & (men['SITUAPR'] == 5)]

tot_old_r = len(men_old_r)

aidemen_r = len(men_old_r.loc[(men_old_r['AIDEMEN'] == 1) & (men_old_r['AIDEMENH'] >= 1)])
serv31_r = len(men_old_r.loc[(men_old_r['SERV31'] == 1) & (men_old_r['SERV31P'] == 2)])
serv32_r = len(men_old_r.loc[(men_old_r['SERV32'] == 1) & (men_old_r['SERV32P'] == 2)])
serv33_r = len(men_old_r.loc[(men_old_r['SERV33'] == 1) & (men_old_r['SERV32P'] == 2)])

perc_aidemen_r = (aidemen_r/tot_old_r) * 100
perc_serv31_r = (serv31_r/tot_old_r) * 100
perc_serv32_r = (serv32_r/tot_old_r) * 100
perc_serv33_r = (serv33_r/tot_old_r) * 100

y_ax_r = [perc_aidemen_r, perc_serv31_r, perc_serv32_r, perc_serv33_r]
#plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.bar(x_ax, y_ax_e, color=colors)
ax1.set_title('Non retraités')
ax1.set_ylabel('Taux de recours (au moins une fois par semaine)')
plt.setp(ax1.get_xticklabels(), rotation=70, ha="right")
for i, v in enumerate(y_ax_e):
    ax1.text(i, v, str(round(v, 2)), color='black', ha='center', va='bottom')

ax2.bar(x_ax, y_ax_r, color=colors)
ax2.set_title('Retraités')
ax2.set_ylabel('Taux de recours (au moins une fois par semaine)')
ax2.set_ylim(ax1.get_ylim())
plt.setp(ax2.get_xticklabels(), rotation=70, ha="right")
for i, v in enumerate(y_ax_r):
    ax2.text(i, v, str(round(v, 2)), color='black', ha='center', va='bottom')

plt.suptitle("Taux de recours à différents types d'aides rémunérées", fontsize=14)

plt.show()




