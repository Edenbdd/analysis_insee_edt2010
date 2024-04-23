#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 15:06:26 2024

@author: eden
"""

#import
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#dataframe
indiv = pd.read_csv("/home/eden/Documents/Mémoire/csv/indiv.csv")
men = pd.read_csv("/home/eden/Documents/Mémoire/csv/menage.csv")

#virer les dom
men = men[['IDMEN', 'RG']]
indiv.rename(columns={'idmen':'IDMEN'}, inplace=True)
indiv = pd.merge(indiv, men, on='IDMEN', how='left')

#DATA SET DOM TOM A ENLEVER
old = indiv.loc[(indiv['age'] <= 65) & (indiv['age'] >= 55) & (indiv['RG'] != 1) & (indiv['RG'] != 2) & (indiv['RG'] != 3) & (indiv['RG'] != 4)]
old_fe = old.loc[(old['sexe'] == 2) & (old['situa'] != 5)]
old_fr = old.loc[(old['sexe'] == 2) & (old['situa'] == 5)]
old_me = old.loc[(old['sexe'] == 1) & (old['situa'] != 5)]
old_mr = old.loc[(old['sexe'] == 1) & (old['situa'] == 5)]

def percent(df, col_name):
    total = len(df)
    per_men = len(df.loc[df[col_name] == 1]) /total * 100
    return per_men
    

## Hommes non retraités (me)
per_men1_me = percent(old_me, 'MEN1')
per_men2_me = percent(old_me, 'MEN2')
per_men3_me = percent(old_me, 'MEN3')
per_men4_me = percent(old_me, 'MEN4')
per_men5_me = percent(old_me, 'MEN5')
per_men6_me = percent(old_me, 'MEN6')
per_men7_me = percent(old_me, 'MEN7')
per_men8_me = percent(old_me, 'MEN8')
y_axis_me = [per_men1_me, per_men2_me, per_men3_me, per_men4_me, per_men5_me, per_men6_me, per_men7_me, per_men8_me]
# Hommes retraités (mr)
per_men1_mr = percent(old_mr, 'MEN1')
per_men2_mr = percent(old_mr, 'MEN2')
per_men3_mr = percent(old_mr, 'MEN3')
per_men4_mr = percent(old_mr, 'MEN4')
per_men5_mr = percent(old_mr, 'MEN5')
per_men6_mr = percent(old_mr, 'MEN6')
per_men7_mr = percent(old_mr, 'MEN7')
per_men8_mr = percent(old_mr, 'MEN8')
y_axis_mr = [per_men1_mr, per_men2_mr, per_men3_mr, per_men4_mr, per_men5_mr, per_men6_mr, per_men7_mr, per_men8_mr]
# Femmes retraitées (fr)
per_men1_fr = percent(old_fr, 'MEN1')
per_men2_fr = percent(old_fr, 'MEN2')
per_men3_fr = percent(old_fr, 'MEN3')
per_men4_fr = percent(old_fr, 'MEN4')
per_men5_fr = percent(old_fr, 'MEN5')
per_men6_fr = percent(old_fr, 'MEN6')
per_men7_fr = percent(old_fr, 'MEN7')
per_men8_fr = percent(old_fr, 'MEN8')
y_axis_fr = [per_men1_fr, per_men2_fr, per_men3_fr, per_men4_fr, per_men5_fr, per_men6_fr, per_men7_fr, per_men8_fr]
# Femmes non retraitées (fe)
per_men1_fe = percent(old_fe, 'MEN1')
per_men2_fe = percent(old_fe, 'MEN2')
per_men3_fe = percent(old_fe, 'MEN3')
per_men4_fe = percent(old_fe, 'MEN4')
per_men5_fe = percent(old_fe, 'MEN5')
per_men6_fe = percent(old_fe, 'MEN6')
per_men7_fe = percent(old_fe, 'MEN7')
per_men8_fe = percent(old_fe, 'MEN8')
y_axis_fe = [per_men1_fe, per_men2_fe, per_men3_fe, per_men4_fe, per_men5_fe, per_men6_fe, per_men7_fe, per_men8_fe]

# Créer la figure avec 4 sous-graphiques

plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(12, 8))

x = np.arange(8)
width = 0.2

ax.bar(x - 0.4, y_axis_me, width, label='Hommes non retraités', color='#ADD8E6')
ax.bar(x - 0.2, y_axis_mr, width, label='Hommes retraités', color='#1E90FF')
ax.bar(x, y_axis_fe, width, label='Femmes non retraitées', color='#90EE90')
ax.bar(x + 0.2, y_axis_fr, width, label='Femmes retraitées', color='#4D7A3F')

ax.set_ylabel('Pourcentage (%)')
ax.set_xticks(x)
ax.set_xticklabels(['Courses', 'Cuisine quotidienne', 'Cuisine de réception', 'Vaisselle', 'Ménage', 'Repassage', 'Bricolage', 'Jardinage'])
ax.tick_params(axis='x', rotation=70)
ax.set_ylim(0, 100)
ax.legend()

leg = ax.legend()
for text in leg.get_texts():
    text.set_color("grey")

plt.suptitle("Pourcentage de personnes ayant effectué une tâche domestique dans la semaine passée", fontsize=16, color="grey")
plt.tight_layout()
plt.show()




















