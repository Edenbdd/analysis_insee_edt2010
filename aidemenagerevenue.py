#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 11:10:15 2024

@author: eden
"""

import pandas as pd
import matplotlib.pyplot as plt

men = pd.read_csv("/home/eden/Documents/Mémoire/csv/menage.csv")

x_ax = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

print(men['RG'].dtypes)

men_old_fr = men.loc[(men['AGEPR'] >= 55) & (men['AGEPR'] <= 65) & (men['RG'] != 1) & (men['RG'] != 2) & (men['RG'] != 3) & (men['RG'] != 4)]

#non retraités
men_old_e = men_old_fr.loc[(men_old_fr['SITUAPR'] != 5)]

tot_old_e1 = len(men_old_e.loc[men_old_e['MRDUC'] == 1])
aidemen_e1 = len(men_old_e.loc[(men_old_e['AIDEMEN'] == 1) & (men_old_e['MRDUC'] == 1)])
perc_aidemen_e1 = (aidemen_e1/tot_old_e1) * 100

tot_old_e2 = len(men_old_e.loc[men_old_e['MRDUC'] == 2])
aidemen_e2 = len(men_old_e.loc[(men_old_e['AIDEMEN'] == 1) & (men_old_e['MRDUC'] == 2)])
perc_aidemen_e2 = (aidemen_e2/tot_old_e2) * 100

tot_old_e3 = len(men_old_e.loc[men_old_e['MRDUC'] == 3])
aidemen_e3 = len(men_old_e.loc[(men_old_e['AIDEMEN'] == 1) & (men_old_e['MRDUC'] == 3)])
perc_aidemen_e3 = (aidemen_e3/tot_old_e3) * 100

tot_old_e4 = len(men_old_e.loc[men_old_e['MRDUC'] == 4])
aidemen_e4 = len(men_old_e.loc[(men_old_e['AIDEMEN'] == 1) & (men_old_e['MRDUC'] == 4)])
perc_aidemen_e4 = (aidemen_e4/tot_old_e4) * 100

tot_old_e5 = len(men_old_e.loc[men_old_e['MRDUC'] == 5])
aidemen_e5 = len(men_old_e.loc[(men_old_e['AIDEMEN'] == 1) & (men_old_e['MRDUC'] == 5)])
perc_aidemen_e5 = (aidemen_e5/tot_old_e5) * 100

tot_old_e6 = len(men_old_e.loc[men_old_e['MRDUC'] == 6])
aidemen_e6 = len(men_old_e.loc[(men_old_e['AIDEMEN'] == 1) & (men_old_e['MRDUC'] == 6)])
perc_aidemen_e6 = (aidemen_e6/tot_old_e6) * 100

tot_old_e7 = len(men_old_e.loc[men_old_e['MRDUC'] == 7])
aidemen_e7 = len(men_old_e.loc[(men_old_e['AIDEMEN'] == 1) & (men_old_e['MRDUC'] == 7)])
perc_aidemen_e7 = (aidemen_e7/tot_old_e7) * 100

tot_old_e8 = len(men_old_e.loc[men_old_e['MRDUC'] == 8])
aidemen_e8 = len(men_old_e.loc[(men_old_e['AIDEMEN'] == 1) & (men_old_e['MRDUC'] == 8)])
perc_aidemen_e8 = (aidemen_e8/tot_old_e8) * 100

tot_old_e9 = len(men_old_e.loc[men_old_e['MRDUC'] == 9])
aidemen_e9 = len(men_old_e.loc[(men_old_e['AIDEMEN'] == 1) & (men_old_e['MRDUC'] == 9)])
perc_aidemen_e9 = (aidemen_e9/tot_old_e9) * 100

tot_old_e10 = len(men_old_e.loc[men_old_e['MRDUC'] == 10])
aidemen_e10 = len(men_old_e.loc[(men_old_e['AIDEMEN'] == 1) & (men_old_e['MRDUC'] == 10)])
perc_aidemen_e10 = (aidemen_e10/tot_old_e10) * 100

y_ax_e = [perc_aidemen_e1, perc_aidemen_e2, perc_aidemen_e3, perc_aidemen_e4, perc_aidemen_e5, perc_aidemen_e6, perc_aidemen_e7, perc_aidemen_e8, perc_aidemen_e9, perc_aidemen_e10]

#retraites
men_old_r = men_old_fr.loc[(men_old_fr['SITUAPR'] == 5)]


tot_old_r1 = len(men_old_r.loc[men_old_r['MRDUC'] == 1])
aidemen_r1 = len(men_old_r.loc[(men_old_r['AIDEMEN'] == 1) & (men_old_r['MRDUC'] == 1)])
perc_aidemen_r1 = (aidemen_r1/tot_old_r1) * 100

tot_old_r2 = len(men_old_r.loc[men_old_r['MRDUC'] == 2])
aidemen_r2 = len(men_old_r.loc[(men_old_r['AIDEMEN'] == 1) & (men_old_r['MRDUC'] == 2)])
perc_aidemen_r2 = (aidemen_r2/tot_old_r2) * 100

tot_old_r3 = len(men_old_r.loc[men_old_r['MRDUC'] == 3])
aidemen_r3 = len(men_old_r.loc[(men_old_r['AIDEMEN'] == 1) & (men_old_r['MRDUC'] == 3)])
perc_aidemen_r3 = (aidemen_r3/tot_old_r3) * 100

tot_old_r4 = len(men_old_r.loc[men_old_r['MRDUC'] == 4])
aidemen_r4 = len(men_old_r.loc[(men_old_r['AIDEMEN'] == 1) & (men_old_r['MRDUC'] == 4)])
perc_aidemen_r4 = (aidemen_r4/tot_old_r4) * 100

tot_old_r5 = len(men_old_r.loc[men_old_r['MRDUC'] == 5])
aidemen_r5 = len(men_old_r.loc[(men_old_r['AIDEMEN'] == 1) & (men_old_r['MRDUC'] == 5)])
perc_aidemen_r5 = (aidemen_r5/tot_old_r5) * 100

tot_old_r6 = len(men_old_r.loc[men_old_r['MRDUC'] == 6])
aidemen_r6 = len(men_old_r.loc[(men_old_r['AIDEMEN'] == 1) & (men_old_r['MRDUC'] == 6)])
perc_aidemen_r6 = (aidemen_r6/tot_old_r6) * 100

tot_old_r7= len(men_old_r.loc[men_old_r['MRDUC'] == 7])
aidemen_r7 = len(men_old_r.loc[(men_old_r['AIDEMEN'] == 1) & (men_old_r['MRDUC'] == 7)])
perc_aidemen_r7 = (aidemen_r7/tot_old_r7) * 100

tot_old_r8 = len(men_old_r.loc[men_old_r['MRDUC'] == 8])
aidemen_r8 = len(men_old_r.loc[(men_old_r['AIDEMEN'] == 1) & (men_old_r['MRDUC'] == 8)])
perc_aidemen_r8 = (aidemen_r8/tot_old_r8) * 100

tot_old_r9 = len(men_old_r.loc[men_old_r['MRDUC'] == 9])
aidemen_r9 = len(men_old_r.loc[(men_old_r['AIDEMEN'] == 1) & (men_old_r['MRDUC'] == 9)])
perc_aidemen_r9 = (aidemen_r9/tot_old_r9) * 100

tot_old_r10 = len(men_old_r.loc[men_old_r['MRDUC'] == 10])
aidemen_r10 = len(men_old_r.loc[(men_old_r['AIDEMEN'] == 1) & (men_old_r['MRDUC'] == 10)])
perc_aidemen_r10 = (aidemen_r10/tot_old_r10) * 100
y_ax_r = [perc_aidemen_r1, perc_aidemen_r2, perc_aidemen_r3, perc_aidemen_r4, perc_aidemen_r5, perc_aidemen_r6, perc_aidemen_r7, perc_aidemen_r8, perc_aidemen_r9, perc_aidemen_r10]


#plot
fig, (ax1, ax2) = plt.subplots(2, 1)
plt.subplots_adjust(hspace=0.7, top = 0.85)

ax1.bar(x_ax, y_ax_e)
ax1.set_title("Non retraités")
ax1.set_ylabel("Taux de recours en %")
ax1.set_xlabel("Revenu mensuel total par unité de consommation (en décile)")
for i, v in enumerate(y_ax_e):
    ax1.text(i, v, str(round(v, 2)), color='black', ha='center', va='bottom')

ax2.bar(x_ax, y_ax_r)
ax2.set_ylim(ax1.get_ylim())
ax2.set_title("Retraités")
ax2.set_ylabel("Taux de recours en %")
ax2.set_xlabel("Revenu mensuel total par unité de consommation (en décile)")
for i, v in enumerate(y_ax_r):
    ax2.text(i, v, str(round(v, 2)), color='black', ha='center', va='bottom')

plt.suptitle("Taux de recours à une aide ménagère en fonction du revenu")
plt.show()
