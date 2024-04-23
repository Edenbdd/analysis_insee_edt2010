#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 15:23:26 2024

@author: eden
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

men = pd.read_csv("/home/eden/Documents/Mémoire/csv/menage.csv")

x_ax = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

#HANDICAPES
men_old = men.loc[(men['AGEPR'] >= 55) & (men['AGEPR'] <= 65) & (men['RG'] != 1) & (men['RG'] != 2) & (men['RG'] != 3) & (men['RG'] != 4)]


#non retraités
men_old_eh = men_old.loc[(men_old['SITUAPR'] != 5)]


tot_old_e1h = len(men_old_eh.loc[men_old_eh['MRDUC'] == 1])
aidemen_e1h = len(men_old_eh.loc[(men_old_eh['AIDEMEN'] == 1) & (men_old_eh['MRDUC'] == 1) & (men_old_eh['HANDIC1E'] == 1)])
perc_aidemen_e1h = (aidemen_e1h/tot_old_e1h) * 100

tot_old_e2h = len(men_old_eh.loc[men_old_eh['MRDUC'] == 2])
aidemen_e2h = len(men_old_eh.loc[(men_old_eh['AIDEMEN'] == 1) & (men_old_eh['MRDUC'] == 2) & (men_old_eh['HANDIC1E'] == 1)])
perc_aidemen_e2h = (aidemen_e2h/tot_old_e2h) * 100

tot_old_e3h = len(men_old_eh.loc[men_old_eh['MRDUC'] == 3])
aidemen_e3h = len(men_old_eh.loc[(men_old_eh['AIDEMEN'] == 1) & (men_old_eh['MRDUC'] == 3) & (men_old_eh['HANDIC1E'] == 1)])
perc_aidemen_e3h = (aidemen_e3h/tot_old_e3h) * 100

tot_old_e4h = len(men_old_eh.loc[men_old_eh['MRDUC'] == 4])
aidemen_e4h = len(men_old_eh.loc[(men_old_eh['AIDEMEN'] == 1) & (men_old_eh['MRDUC'] == 4) & (men_old_eh['HANDIC1E'] == 1)])
perc_aidemen_e4h = (aidemen_e4h/tot_old_e4h) * 100

tot_old_e5h = len(men_old_eh.loc[men_old_eh['MRDUC'] == 5])
aidemen_e5h = len(men_old_eh.loc[(men_old_eh['AIDEMEN'] == 1) & (men_old_eh['MRDUC'] == 5) & (men_old_eh['HANDIC1E'] == 1)])
perc_aidemen_e5h = (aidemen_e5h/tot_old_e5h) * 100

tot_old_e6h = len(men_old_eh.loc[men_old_eh['MRDUC'] == 6])
aidemen_e6h = len(men_old_eh.loc[(men_old_eh['AIDEMEN'] == 1) & (men_old_eh['MRDUC'] == 6) & (men_old_eh['HANDIC1E'] == 1)])
perc_aidemen_e6h = (aidemen_e6h/tot_old_e6h) * 100

tot_old_e7h = len(men_old_eh.loc[men_old_eh['MRDUC'] == 7])
aidemen_e7h = len(men_old_eh.loc[(men_old_eh['AIDEMEN'] == 1) & (men_old_eh['MRDUC'] == 7) & (men_old_eh['HANDIC1E'] == 1)])
perc_aidemen_e7h = (aidemen_e7h/tot_old_e7h) * 100

tot_old_e8h = len(men_old_eh.loc[men_old_eh['MRDUC'] == 8])
aidemen_e8h = len(men_old_eh.loc[(men_old_eh['AIDEMEN'] == 1) & (men_old_eh['MRDUC'] == 8) & (men_old_eh['HANDIC1E'] == 1)])
perc_aidemen_e8h = (aidemen_e8h/tot_old_e8h) * 100

tot_old_e9h = len(men_old_eh.loc[men_old_eh['MRDUC'] == 9])
aidemen_e9h = len(men_old_eh.loc[(men_old_eh['AIDEMEN'] == 1) & (men_old_eh['MRDUC'] == 9) & (men_old_eh['HANDIC1E'] == 1)])
perc_aidemen_e9h = (aidemen_e9h/tot_old_e9h) * 100

tot_old_e10h = len(men_old_eh.loc[men_old_eh['MRDUC'] == 10])
aidemen_e10h = len(men_old_eh.loc[(men_old_eh['AIDEMEN'] == 1) & (men_old_eh['MRDUC'] == 10) & (men_old_eh['HANDIC1E'] == 1)])
perc_aidemen_e10h = (aidemen_e10h/tot_old_e10h) * 100

y_ax_eh = [perc_aidemen_e1h, perc_aidemen_e2h, perc_aidemen_e3h, perc_aidemen_e4h, perc_aidemen_e5h, perc_aidemen_e6h, perc_aidemen_e7h, perc_aidemen_e8h, perc_aidemen_e9h, perc_aidemen_e10h]

#retraites
men_old_rh = men_old.loc[(men_old['SITUAPR'] == 5)]


tot_old_r1h = len(men_old_rh.loc[men_old_rh['MRDUC'] == 1])
aidemen_r1h = len(men_old_rh.loc[(men_old_rh['AIDEMEN'] == 1) & (men_old_rh['MRDUC'] == 1) & (men_old_rh['HANDIC1E'] == 1)])
perc_aidemen_r1h = (aidemen_r1h/tot_old_r1h) * 100

tot_old_r2h = len(men_old_rh.loc[men_old_rh['MRDUC'] == 2])
aidemen_r2h = len(men_old_rh.loc[(men_old_rh['AIDEMEN'] == 1) & (men_old_rh['MRDUC'] == 2) & (men_old_rh['HANDIC1E'] == 1)])
perc_aidemen_r2h = (aidemen_r2h/tot_old_r2h) * 100

tot_old_r3h = len(men_old_rh.loc[men_old_rh['MRDUC'] == 3])
aidemen_r3h = len(men_old_rh.loc[(men_old_rh['AIDEMEN'] == 1) & (men_old_rh['MRDUC'] == 3) & (men_old_rh['HANDIC1E'] == 1)])
perc_aidemen_r3h = (aidemen_r3h/tot_old_r3h) * 100

tot_old_r4h = len(men_old_rh.loc[men_old_rh['MRDUC'] == 4])
aidemen_r4h = len(men_old_rh.loc[(men_old_rh['AIDEMEN'] == 1) & (men_old_rh['MRDUC'] == 4) & (men_old_rh['HANDIC1E'] == 1)])
perc_aidemen_r4h = (aidemen_r4h/tot_old_r4h) * 100

tot_old_r5h = len(men_old_rh.loc[men_old_rh['MRDUC'] == 5])
aidemen_r5h = len(men_old_rh.loc[(men_old_rh['AIDEMEN'] == 1) & (men_old_rh['MRDUC'] == 5) & (men_old_rh['HANDIC1E'] == 1)])
perc_aidemen_r5h = (aidemen_r5h/tot_old_r5h) * 100

tot_old_r6h = len(men_old_rh.loc[men_old_rh['MRDUC'] == 6])
aidemen_r6h = len(men_old_rh.loc[(men_old_rh['AIDEMEN'] == 1) & (men_old_rh['MRDUC'] == 6) & (men_old_rh['HANDIC1E'] == 1)])
perc_aidemen_r6h = (aidemen_r6h/tot_old_r6h) * 100

tot_old_r7h = len(men_old_rh.loc[men_old_rh['MRDUC'] == 7])
aidemen_r7h = len(men_old_rh.loc[(men_old_rh['AIDEMEN'] == 1) & (men_old_rh['MRDUC'] == 7) & (men_old_rh['HANDIC1E'] == 1)])
perc_aidemen_r7h = (aidemen_r7h/tot_old_r7h) * 100

tot_old_r8h = len(men_old_rh.loc[men_old_rh['MRDUC'] == 8])
aidemen_r8h = len(men_old_rh.loc[(men_old_rh['AIDEMEN'] == 1) & (men_old_rh['MRDUC'] == 8) & (men_old_rh['HANDIC1E'] == 1)])
perc_aidemen_r8h = (aidemen_r8h/tot_old_r8h) * 100

tot_old_r9h = len(men_old_rh.loc[men_old_rh['MRDUC'] == 9])
aidemen_r9h = len(men_old_rh.loc[(men_old_rh['AIDEMEN'] == 1) & (men_old_rh['MRDUC'] == 9) & (men_old_rh['HANDIC1E'] == 1)])
perc_aidemen_r9h = (aidemen_r9h/tot_old_r9h) * 100

tot_old_r10h = len(men_old_rh.loc[men_old_rh['MRDUC'] == 10])
aidemen_r10h = len(men_old_rh.loc[(men_old_rh['AIDEMEN'] == 1) & (men_old_rh['MRDUC'] == 10) & (men_old_rh['HANDIC1E'] == 1)])
perc_aidemen_r10h = (aidemen_r10h/tot_old_r10h) * 100

y_ax_rh = [perc_aidemen_r1h, perc_aidemen_r2h, perc_aidemen_r3h, perc_aidemen_r4h, perc_aidemen_r5h, perc_aidemen_r6h, perc_aidemen_r7h, perc_aidemen_r8h, perc_aidemen_r9h, perc_aidemen_r10h]


#NONHANDICAPES
#non retraités
men_old_e = men_old.loc[(men_old['SITUAPR'] != 5)]


tot_old_e1 = len(men_old_e.loc[men_old_e['MRDUC'] == 1])
aidemen_e1 = len(men_old_e.loc[(men_old_e['AIDEMEN'] == 1) & (men_old_e['MRDUC'] == 1) & (men_old_e['HANDIC1E'] != 1)])
perc_aidemen_e1 = (aidemen_e1/tot_old_e1) * 100

tot_old_e2 = len(men_old_e.loc[men_old_e['MRDUC'] == 2])
aidemen_e2 = len(men_old_e.loc[(men_old_e['AIDEMEN'] == 1) & (men_old_e['MRDUC'] == 2) & (men_old_e['HANDIC1E'] != 1)])
perc_aidemen_e2 = (aidemen_e2/tot_old_e2) * 100

tot_old_e3 = len(men_old_e.loc[men_old_e['MRDUC'] == 3])
aidemen_e3 = len(men_old_e.loc[(men_old_e['AIDEMEN'] == 1) & (men_old_e['MRDUC'] == 3) & (men_old_e['HANDIC1E'] != 1)])
perc_aidemen_e3 = (aidemen_e3/tot_old_e3) * 100

tot_old_e4 = len(men_old_e.loc[men_old_e['MRDUC'] == 4])
aidemen_e4 = len(men_old_e.loc[(men_old_e['AIDEMEN'] == 1) & (men_old_e['MRDUC'] == 4) & (men_old_e['HANDIC1E'] != 1)])
perc_aidemen_e4 = (aidemen_e4/tot_old_e4) * 100

tot_old_e5 = len(men_old_e.loc[men_old_e['MRDUC'] == 5])
aidemen_e5 = len(men_old_e.loc[(men_old_e['AIDEMEN'] == 1) & (men_old_e['MRDUC'] == 5) & (men_old_e['HANDIC1E'] != 1)])
perc_aidemen_e5 = (aidemen_e5/tot_old_e5) * 100

tot_old_e6 = len(men_old_e.loc[men_old_e['MRDUC'] == 6])
aidemen_e6 = len(men_old_e.loc[(men_old_e['AIDEMEN'] == 1) & (men_old_e['MRDUC'] == 6) & (men_old_e['HANDIC1E'] != 1)])
perc_aidemen_e6 = (aidemen_e6/tot_old_e6) * 100

tot_old_e7 = len(men_old_e.loc[men_old_e['MRDUC'] == 7])
aidemen_e7 = len(men_old_e.loc[(men_old_e['AIDEMEN'] == 1) & (men_old_e['MRDUC'] == 7) & (men_old_e['HANDIC1E'] != 1)])
perc_aidemen_e7 = (aidemen_e7/tot_old_e7) * 100

tot_old_e8 = len(men_old_e.loc[men_old_e['MRDUC'] == 8])
aidemen_e8 = len(men_old_e.loc[(men_old_e['AIDEMEN'] == 1) & (men_old_e['MRDUC'] == 8) & (men_old_e['HANDIC1E'] != 1)])
perc_aidemen_e8 = (aidemen_e8/tot_old_e8) * 100

tot_old_e9 = len(men_old_e.loc[men_old_e['MRDUC'] == 9])
aidemen_e9 = len(men_old_e.loc[(men_old_e['AIDEMEN'] == 1) & (men_old_e['MRDUC'] == 9) & (men_old_e['HANDIC1E'] != 1)])
perc_aidemen_e9 = (aidemen_e9/tot_old_e9) * 100

tot_old_e10 = len(men_old_e.loc[men_old_e['MRDUC'] == 10])
aidemen_e10 = len(men_old_e.loc[(men_old_e['AIDEMEN'] == 1) & (men_old_e['MRDUC'] == 10) & (men_old_e['HANDIC1E'] != 1)])
perc_aidemen_e10 = (aidemen_e10/tot_old_e10) * 100

y_ax_e = [perc_aidemen_e1, perc_aidemen_e2, perc_aidemen_e3, perc_aidemen_e4, perc_aidemen_e5, perc_aidemen_e6, perc_aidemen_e7, perc_aidemen_e8, perc_aidemen_e9, perc_aidemen_e10]

#retraites
men_old_r = men_old.loc[(men_old['SITUAPR'] == 5)]

tot_old_r1 = len(men_old_r.loc[men_old_r['MRDUC'] == 1])
aidemen_r1 = len(men_old_r.loc[(men_old_r['AIDEMEN'] == 1) & (men_old_r['MRDUC'] == 1) & (men_old_r['HANDIC1E'] != 1)])
perc_aidemen_r1 = (aidemen_r1/tot_old_r1) * 100

tot_old_r2 = len(men_old_r.loc[men_old_r['MRDUC'] == 2])
aidemen_r2 = len(men_old_r.loc[(men_old_r['AIDEMEN'] == 1) & (men_old_r['MRDUC'] == 2) & (men_old_r['HANDIC1E'] != 1)])
perc_aidemen_r2 = (aidemen_r2/tot_old_r2) * 100

tot_old_r3 = len(men_old_r.loc[men_old_r['MRDUC'] == 3])
aidemen_r3 = len(men_old_r.loc[(men_old_r['AIDEMEN'] == 1) & (men_old_r['MRDUC'] == 3) & (men_old_r['HANDIC1E'] != 1)])
perc_aidemen_r3 = (aidemen_r3/tot_old_r3) * 100

tot_old_r4 = len(men_old_r.loc[men_old_r['MRDUC'] == 4])
aidemen_r4 = len(men_old_r.loc[(men_old_r['AIDEMEN'] == 1) & (men_old_r['MRDUC'] == 4) & (men_old_r['HANDIC1E'] != 1)])
perc_aidemen_r4 = (aidemen_r4/tot_old_r4) * 100

tot_old_r5 = len(men_old_r.loc[men_old_r['MRDUC'] == 5])
aidemen_r5 = len(men_old_r.loc[(men_old_r['AIDEMEN'] == 1) & (men_old_r['MRDUC'] == 5) & (men_old_r['HANDIC1E'] != 1)])
perc_aidemen_r5 = (aidemen_r5/tot_old_r5) * 100

tot_old_r6 = len(men_old_r.loc[men_old_r['MRDUC'] == 6])
aidemen_r6 = len(men_old_r.loc[(men_old_r['AIDEMEN'] == 1) & (men_old_r['MRDUC'] == 6) & (men_old_r['HANDIC1E'] != 1)])
perc_aidemen_r6 = (aidemen_r6/tot_old_r6) * 100

tot_old_r7 = len(men_old_r.loc[men_old_r['MRDUC'] == 7])
aidemen_r7 = len(men_old_r.loc[(men_old_r['AIDEMEN'] == 1) & (men_old_r['MRDUC'] == 7) & (men_old_r['HANDIC1E'] != 1)])
perc_aidemen_r7 = (aidemen_r7/tot_old_r7) * 100


tot_old_r8 = len(men_old_r.loc[men_old_r['MRDUC'] == 8])
aidemen_r8 = len(men_old_r.loc[(men_old_r['AIDEMEN'] == 1) & (men_old_r['MRDUC'] == 8) & (men_old_r['HANDIC1E'] != 1)])
perc_aidemen_r8 = (aidemen_r8/tot_old_r8) * 100

tot_old_r9 = len(men_old_r.loc[men_old_r['MRDUC'] == 9])
aidemen_r9 = len(men_old_r.loc[(men_old_r['AIDEMEN'] == 1) & (men_old_r['MRDUC'] == 9) & (men_old_r['HANDIC1E'] != 1)])
perc_aidemen_r9 = (aidemen_r9/tot_old_r9) * 100

tot_old_r10 = len(men_old_r.loc[men_old_r['MRDUC'] == 10])
aidemen_r10 = len(men_old_r.loc[(men_old_r['AIDEMEN'] == 1) & (men_old_r['MRDUC'] == 10) & (men_old_r['HANDIC1E'] != 1)])
perc_aidemen_r10 = (aidemen_r10/tot_old_r10) * 100
y_ax_r = [perc_aidemen_r1, perc_aidemen_r2, perc_aidemen_r3, perc_aidemen_r4, perc_aidemen_r5, perc_aidemen_r6, perc_aidemen_r7, perc_aidemen_r8, perc_aidemen_r9, perc_aidemen_r10]


#plot
x = np.arange(10)
width = 0.35
color1 = '#0077B6'
color2 = '#FF9900'

fig, (ax1, ax2) = plt.subplots(2, 1)
plt.subplots_adjust(hspace=0.7, top=0.8)

# Premier graphique : Non Retraités
rects1 = ax1.bar(x_ax, y_ax_e, width, label='Personnes valides', color=color1)
rects2 = ax1.bar(x_ax, y_ax_eh, width, bottom=y_ax_e, label='Personnes atteintes de handicap', color=color2)
ax1.set_title("Non Retraités")
ax1.set_ylabel("Taux de recours en %")
ax1.set_xlabel("Revenu mensuel total par unité de consommation (en décile)")
for i, (v1, v2) in enumerate(zip(y_ax_e, y_ax_eh)):
    total = v1 + v2
    ax1.text(i, total + 2, str(round(total, 2)), color='black', ha='center', va='bottom')

# Deuxième graphique : Retraités
rects1 = ax2.bar(x_ax, y_ax_r, width, color=color1)
rects2 = ax2.bar(x_ax, y_ax_rh, width, bottom=y_ax_r, color=color2)
ax2.set_title("Retraités")
ax2.set_ylabel("Taux de recours en %")
ax2.set_xlabel("Revenu mensuel total par unité de consommation (en décile)")
for i, (v1, v2) in enumerate(zip(y_ax_r, y_ax_rh)):
    total = v1 + v2
    ax2.text(i, total + 2, str(round(total, 2)), color='black', ha='center', va='bottom')

plt.legend()
plt.suptitle("Taux de recours à une aide ménagère en fonction du revenu")
plt.show()
