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

def jour(df, col_name):
    total = len(df.loc[df[col_name] == 1])
    men_sem = len(df.loc[df[f"{col_name}J"] == 1])
    men_we = len(df.loc[df[f"{col_name}J"] == 2])
    men_de = len(df.loc[df[f"{col_name}J"] == 3])
    per_men_sem = men_sem/total * 100
    per_men_we = men_we/total * 100
    per_men_de = men_de/total * 100
    return [per_men_sem, per_men_we, per_men_de]
    

## Hommes non retraités (me)
per_men1_sem_me, per_men1_we_me, per_men1_de_me = jour(old_me, 'MEN1')
per_men2_sem_me, per_men2_we_me, per_men2_de_me = jour(old_me, 'MEN2')
per_men3_sem_me, per_men3_we_me, per_men3_de_me = jour(old_me, 'MEN3')
per_men4_sem_me, per_men4_we_me, per_men4_de_me = jour(old_me, 'MEN4')
per_men5_sem_me, per_men5_we_me, per_men5_de_me = jour(old_me, 'MEN5')
per_men6_sem_me, per_men6_we_me, per_men6_de_me = jour(old_me, 'MEN6')
per_men7_sem_me, per_men7_we_me, per_men7_de_me = jour(old_me, 'MEN7')
per_men8_sem_me, per_men8_we_me, per_men8_de_me = jour(old_me, 'MEN8')

# Hommes retraités (mr)
per_men1_sem_mr, per_men1_we_mr, per_men1_de_mr = jour(old_mr, 'MEN1')
per_men2_sem_mr, per_men2_we_mr, per_men2_de_mr = jour(old_mr, 'MEN2')
per_men3_sem_mr, per_men3_we_mr, per_men3_de_mr = jour(old_mr, 'MEN3')
per_men4_sem_mr, per_men4_we_mr, per_men4_de_mr = jour(old_mr, 'MEN4')
per_men5_sem_mr, per_men5_we_mr, per_men5_de_mr = jour(old_mr, 'MEN5')
per_men6_sem_mr, per_men6_we_mr, per_men6_de_mr = jour(old_mr, 'MEN6')
per_men7_sem_mr, per_men7_we_mr, per_men7_de_mr = jour(old_mr, 'MEN7')
per_men8_sem_mr, per_men8_we_mr, per_men8_de_mr = jour(old_mr, 'MEN8')

# Femmes retraitées (fr)
per_men1_sem_fr, per_men1_we_fr, per_men1_de_fr = jour(old_fr, 'MEN1')
per_men2_sem_fr, per_men2_we_fr, per_men2_de_fr = jour(old_fr, 'MEN2')
per_men3_sem_fr, per_men3_we_fr, per_men3_de_fr = jour(old_fr, 'MEN3')
per_men4_sem_fr, per_men4_we_fr, per_men4_de_fr = jour(old_fr, 'MEN4')
per_men5_sem_fr, per_men5_we_fr, per_men5_de_fr = jour(old_fr, 'MEN5')
per_men6_sem_fr, per_men6_we_fr, per_men6_de_fr = jour(old_fr, 'MEN6')
per_men7_sem_fr, per_men7_we_fr, per_men7_de_fr = jour(old_fr, 'MEN7')
per_men8_sem_fr, per_men8_we_fr, per_men8_de_fr = jour(old_fr, 'MEN8')

# Femmes non retraitées (fe)
per_men1_sem_fe, per_men1_we_fe, per_men1_de_fe = jour(old_fe, 'MEN1')
per_men2_sem_fe, per_men2_we_fe, per_men2_de_fe = jour(old_fe, 'MEN2')
per_men3_sem_fe, per_men3_we_fe, per_men3_de_fe = jour(old_fe, 'MEN3')
per_men4_sem_fe, per_men4_we_fe, per_men4_de_fe = jour(old_fe, 'MEN4')
per_men5_sem_fe, per_men5_we_fe, per_men5_de_fe = jour(old_fe, 'MEN5')
per_men6_sem_fe, per_men6_we_fe, per_men6_de_fe = jour(old_fe, 'MEN6')
per_men7_sem_fe, per_men7_we_fe, per_men7_de_fe = jour(old_fe, 'MEN7')
per_men8_sem_fe, per_men8_we_fe, per_men8_de_fe = jour(old_fe, 'MEN8')



# Créer la figure avec 4 sous-graphiques
plt.style.use('ggplot')

# Créer la figure avec 4 sous-graphiques
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))

# Hommes non retraités (me)
x = np.arange(8)
width = 0.2

rects1 = ax1.bar(x - 0.2, [per_men1_sem_me, per_men2_sem_me, per_men3_sem_me, per_men4_sem_me, per_men5_sem_me, per_men6_sem_me, per_men7_sem_me, per_men8_sem_me], width, label='Semaine')
rects2 = ax1.bar(x, [per_men1_we_me, per_men2_we_me, per_men3_we_me, per_men4_we_me, per_men5_we_me, per_men6_we_me, per_men7_we_me, per_men8_we_me], width, label='Week-end')
rects3 = ax1.bar(x + 0.2, [per_men1_de_me, per_men2_de_me, per_men3_de_me, per_men4_de_me, per_men5_de_me, per_men6_de_me, per_men7_de_me, per_men8_de_me], width, label='Les deux')
ax1.set_title('Hommes non retraités',  color='grey')
ax1.set_ylabel('Pourcentage (%)')
ax1.set_ylim(0, 100)
ax1.set_xticks(x)
ax1.set_xticklabels(['Courses', 'Cuisine quotidienne', 'Cuisine de réception', 'Vaisselle', 'Ménage', 'Repassage', 'Bricolage', 'Jardinage'])
ax1.tick_params(axis='x', rotation=70)
ax1.legend()

# Hommes retraités (mr)
rects1 = ax2.bar(x - 0.2, [per_men1_sem_mr, per_men2_sem_mr, per_men3_sem_mr, per_men4_sem_mr, per_men5_sem_mr, per_men6_sem_mr, per_men7_sem_mr, per_men8_sem_mr], width, label='Semaine')
rects2 = ax2.bar(x, [per_men1_we_mr, per_men2_we_mr, per_men3_we_mr, per_men4_we_mr, per_men5_we_mr, per_men6_we_mr, per_men7_we_mr, per_men8_we_mr], width, label='Week-end')
rects3 = ax2.bar(x + 0.2, [per_men1_de_mr, per_men2_de_mr, per_men3_de_mr, per_men4_de_mr, per_men5_de_mr, per_men6_de_mr, per_men7_de_mr, per_men8_de_mr], width, label='Les deux')
ax2.set_title('Hommes retraités',  color='grey')
ax2.set_ylabel('Pourcentage (%)')
ax2.set_ylim(0, 100)
ax2.set_xticks(x)
ax2.set_xticklabels(['Courses', 'Cuisine quotidienne', 'Cuisine de réception', 'Vaisselle', 'Ménage', 'Repassage', 'Bricolage', 'Jardinage'])
ax2.tick_params(axis='x', rotation=70)
ax2.legend()

# Femmes retraitées (fr)
rects1 = ax4.bar(x - 0.2, [per_men1_sem_fr, per_men2_sem_fr, per_men3_sem_fr, per_men4_sem_fr, per_men5_sem_fr, per_men6_sem_fr, per_men7_sem_fr, per_men8_sem_fr], width, label='Semaine')
rects2 = ax4.bar(x, [per_men1_we_fr, per_men2_we_fr, per_men3_we_fr, per_men4_we_fr, per_men5_we_fr, per_men6_we_fr, per_men7_we_fr, per_men8_we_fr], width, label='Week-end')
rects3 = ax4.bar(x + 0.2, [per_men1_de_fr, per_men2_de_fr, per_men3_de_fr, per_men4_de_fr, per_men5_de_fr, per_men6_de_fr, per_men7_de_fr, per_men8_de_fr], width, label='Les deux')
ax4.set_title('Femmes retraitées',  color='grey')
ax4.set_ylabel('Pourcentage (%)')
ax4.set_ylim(0, 100)
ax4.set_xticks(x)
ax4.set_xticklabels(['Courses', 'Cuisine quotidienne', 'Cuisine de réception', 'Vaisselle', 'Ménage', 'Repassage', 'Bricolage', 'Jardinage'])
ax4.tick_params(axis='x', rotation=70)
ax4.legend()

# Femmes non retraitées (fe)
rects1 = ax3.bar(x - 0.2, [per_men1_sem_fe, per_men2_sem_fe, per_men3_sem_fe, per_men4_sem_fe, per_men5_sem_fe, per_men6_sem_fe, per_men7_sem_fe, per_men8_sem_fe], width, label='Semaine')
rects2 = ax3.bar(x, [per_men1_we_fe, per_men2_we_fe, per_men3_we_fe, per_men4_we_fe, per_men5_we_fe, per_men6_we_fe, per_men7_we_fe, per_men8_we_fe], width, label='Week-end')
rects3 = ax3.bar(x + 0.2, [per_men1_de_fe, per_men2_de_fe, per_men3_de_fe, per_men4_de_fe, per_men5_de_fe, per_men6_de_fe, per_men7_de_fe, per_men8_de_fe], width, label='Les deux')
ax3.set_title('Femmes non retraitées', color='grey')
ax3.set_ylabel('Pourcentage (%)')
ax3.set_ylim(0, 100)
ax3.set_xticks(x)
ax3.set_xticklabels(['Courses', 'Cuisine quotidienne', 'Cuisine de réception', 'Vaisselle', 'Ménage', 'Repassage', 'Bricolage', 'Jardinage'])
ax3.tick_params(axis='x', rotation=70)
ax3.legend()

for ax in [ax1, ax2, ax3, ax4]:
    leg = ax.legend()
    for text in leg.get_texts():
        text.set_color('grey') 

plt.suptitle("Répartition des tâches domestiques par jour de la semaine", fontsize=16, color='grey')
plt.tight_layout()
plt.show()




















