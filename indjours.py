#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:13:09 2024

@author: eden
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

indiv = pd.read_csv("/home/eden/Documents/Mémoire/csv/indiv.csv")
#DATA SET DOM TOM A ENLEVER
old = indiv.loc[(indiv['age'] <= 65) & (indiv['age'] >= 55)]
old_fe = old.loc[(indiv['sexe'] == 2) & (indiv['situa'] != 5)]
old_fr = old.loc[(indiv['sexe'] == 2) & (indiv['situa'] == 5)]
old_me = old.loc[(indiv['sexe'] == 1) & (indiv['situa'] != 5)]
old_mr = old.loc[(indiv['sexe'] == 1) & (indiv['situa'] == 5)]



def calculate_percentages(df, col_name, col_prefix):
    """
    Calcule les pourcentages pour les différentes catégories d'une colonne donnée.
    
    Paramètres:
    df (pandas.DataFrame): Le DataFrame contenant les données.
    col_name (str): Le nom de la colonne à analyser.
    col_prefix (str): Le préfixe de la colonne à utiliser pour les sous-catégories.
    
    Retourne:
    tuple: Quatre listes contenant les pourcentages pour les catégories "obl", "agr", "corv" et "dep".
    """
    total = df.loc[(df[col_name]) == 1].shape[0]
    
    obl = df.loc[(df[f"{col_prefix}P"] == 2)].shape[0]
    agr = df.loc[(df[f"{col_prefix}P"] == 3)].shape[0]
    corv = df.loc[(df[f"{col_prefix}P"] == 1)].shape[0]
    dep = df.loc[(df[f"{col_prefix}P"] == 4)].shape[0]
    
    per_obl = (obl / total) * 100
    per_agr = (agr / total) * 100
    per_corv = (corv / total) * 100
    per_dep = (dep / total) * 100
    
    return [per_obl, per_agr, per_corv, per_dep]


#Homme non retraités
# courses
per_men1_obl_me, per_men1_agr_me, per_men1_corv_me, per_men1_dep_me = calculate_percentages(old_me, 'MEN1', 'MEN1')
# cuisine
per_men2_obl_me, per_men2_agr_me, per_men2_corv_me, per_men2_dep_me = calculate_percentages(old_me, 'MEN2', 'MEN2')
# cuisine recep
per_men3_obl_me, per_men3_agr_me, per_men3_corv_me, per_men3_dep_me = calculate_percentages(old_me, 'MEN3', 'MEN3')
# vaisselle
per_men4_obl_me, per_men4_agr_me, per_men4_corv_me, per_men4_dep_me = calculate_percentages(old_me, 'MEN4', 'MEN4')
# ménage
per_men5_obl_me, per_men5_agr_me, per_men5_corv_me, per_men5_dep_me = calculate_percentages(old_me, 'MEN5', 'MEN5')
# repassage
per_men6_obl_me, per_men6_agr_me, per_men6_corv_me, per_men6_dep_me = calculate_percentages(old_me, 'MEN6', 'MEN6')
# bricolage
per_men7_obl_me, per_men7_agr_me, per_men7_corv_me, per_men7_dep_me = calculate_percentages(old_me, 'MEN7', 'MEN7')
# jardinage
per_men8_obl_me, per_men8_agr_me, per_men8_corv_me, per_men8_dep_me = calculate_percentages(old_me, 'MEN8', 'MEN8')

#hommes retraités
per_men1_obl_mr, per_men1_agr_mr, per_men1_corv_mr, per_men1_dep_mr = calculate_percentages(old_mr, 'MEN1', 'MEN1')
per_men2_obl_mr, per_men2_agr_mr, per_men2_corv_mr, per_men2_dep_mr = calculate_percentages(old_mr, 'MEN2', 'MEN2')
per_men3_obl_mr, per_men3_agr_mr, per_men3_corv_mr, per_men3_dep_mr = calculate_percentages(old_mr, 'MEN3', 'MEN3')
per_men4_obl_mr, per_men4_agr_mr, per_men4_corv_mr, per_men4_dep_mr = calculate_percentages(old_mr, 'MEN4', 'MEN4')
per_men5_obl_mr, per_men5_agr_mr, per_men5_corv_mr, per_men5_dep_mr = calculate_percentages(old_mr, 'MEN5', 'MEN5')
per_men6_obl_mr, per_men6_agr_mr, per_men6_corv_mr, per_men6_dep_mr = calculate_percentages(old_mr, 'MEN6', 'MEN6')
per_men7_obl_mr, per_men7_agr_mr, per_men7_corv_mr, per_men7_dep_mr = calculate_percentages(old_mr, 'MEN7', 'MEN7')
per_men8_obl_mr, per_men8_agr_mr, per_men8_corv_mr, per_men8_dep_mr = calculate_percentages(old_mr, 'MEN8', 'MEN8')

#femmes retraités
per_men1_obl_fr, per_men1_agr_fr, per_men1_corv_fr, per_men1_dep_fr = calculate_percentages(old_fr, 'MEN1', 'MEN1')
per_men2_obl_fr, per_men2_agr_fr, per_men2_corv_fr, per_men2_dep_fr = calculate_percentages(old_fr, 'MEN2', 'MEN2')
per_men3_obl_fr, per_men3_agr_fr, per_men3_corv_fr, per_men3_dep_fr = calculate_percentages(old_fr, 'MEN3', 'MEN3')
per_men4_obl_fr, per_men4_agr_fr, per_men4_corv_fr, per_men4_dep_fr = calculate_percentages(old_fr, 'MEN4', 'MEN4')
per_men5_obl_fr, per_men5_agr_fr, per_men5_corv_fr, per_men5_dep_fr = calculate_percentages(old_fr, 'MEN5', 'MEN5')
per_men6_obl_fr, per_men6_agr_fr, per_men6_corv_fr, per_men6_dep_fr = calculate_percentages(old_fr, 'MEN6', 'MEN6')
per_men7_obl_fr, per_men7_agr_fr, per_men7_corv_fr, per_men7_dep_fr = calculate_percentages(old_fr, 'MEN7', 'MEN7')
per_men8_obl_fr, per_men8_agr_fr, per_men8_corv_fr, per_men8_dep_fr = calculate_percentages(old_fr, 'MEN8', 'MEN8')

#femmes non retraités
per_men1_obl_fe, per_men1_agr_fe, per_men1_corv_fe, per_men1_dep_fe = calculate_percentages(old_fe, 'MEN1', 'MEN1')
per_men2_obl_fe, per_men2_agr_fe, per_men2_corv_fe, per_men2_dep_fe = calculate_percentages(old_fe, 'MEN2', 'MEN2')
per_men3_obl_fe, per_men3_agr_fe, per_men3_corv_fe, per_men3_dep_fe = calculate_percentages(old_fe, 'MEN3', 'MEN3')
per_men4_obl_fe, per_men4_agr_fe, per_men4_corv_fe, per_men4_dep_fe = calculate_percentages(old_fe, 'MEN4', 'MEN4')
per_men5_obl_fe, per_men5_agr_fe, per_men5_corv_fe, per_men5_dep_fe = calculate_percentages(old_fe, 'MEN5', 'MEN5')
per_men6_obl_fe, per_men6_agr_fe, per_men6_corv_fe, per_men6_dep_fe = calculate_percentages(old_fe, 'MEN6', 'MEN6')
per_men7_obl_fe, per_men7_agr_fe, per_men7_corv_fe, per_men7_dep_fe = calculate_percentages(old_fe, 'MEN7', 'MEN7')
per_men8_obl_fe, per_men8_agr_fe, per_men8_corv_fe, per_men8_dep_fe = calculate_percentages(old_fe, 'MEN8', 'MEN8')



## Hommes non retraités (me)
corv_list_me = [per_men1_corv_me, per_men2_corv_me, per_men3_corv_me, per_men4_corv_me, per_men5_corv_me, per_men6_corv_me, per_men7_corv_me, per_men8_corv_me]
dep_list_me = [per_men1_dep_me, per_men2_dep_me, per_men3_dep_me, per_men4_dep_me, per_men5_dep_me, per_men6_dep_me, per_men7_dep_me, per_men8_dep_me]
obl_list_me = [per_men1_obl_me, per_men2_obl_me, per_men3_obl_me, per_men4_obl_me, per_men5_obl_me, per_men6_obl_me, per_men7_obl_me, per_men8_obl_me]
agr_list_me = [per_men1_agr_me, per_men2_agr_me, per_men3_agr_me, per_men4_agr_me, per_men5_agr_me, per_men6_agr_me, per_men7_agr_me, per_men8_agr_me]

# Hommes retraités (mr)
corv_list_mr = [per_men1_corv_mr, per_men2_corv_mr, per_men3_corv_mr, per_men4_corv_mr, per_men5_corv_mr, per_men6_corv_mr, per_men7_corv_mr, per_men8_corv_mr]
dep_list_mr = [per_men1_dep_mr, per_men2_dep_mr, per_men3_dep_mr, per_men4_dep_mr, per_men5_dep_mr, per_men6_dep_mr, per_men7_dep_mr, per_men8_dep_mr]
obl_list_mr = [per_men1_obl_mr, per_men2_obl_mr, per_men3_obl_mr, per_men4_obl_mr, per_men5_obl_mr, per_men6_obl_mr, per_men7_obl_mr, per_men8_obl_mr]
agr_list_mr = [per_men1_agr_mr, per_men2_agr_mr, per_men3_agr_mr, per_men4_agr_mr, per_men5_agr_mr, per_men6_agr_mr, per_men7_agr_mr, per_men8_agr_mr]

# Femmes retraitées (fr)
corv_list_fr = [per_men1_corv_fr, per_men2_corv_fr, per_men3_corv_fr, per_men4_corv_fr, per_men5_corv_fr, per_men6_corv_fr, per_men7_corv_fr, per_men8_corv_fr]
dep_list_fr = [per_men1_dep_fr, per_men2_dep_fr, per_men3_dep_fr, per_men4_dep_fr, per_men5_dep_fr, per_men6_dep_fr, per_men7_dep_fr, per_men8_dep_fr]
obl_list_fr = [per_men1_obl_fr, per_men2_obl_fr, per_men3_obl_fr, per_men4_obl_fr, per_men5_obl_fr, per_men6_obl_fr, per_men7_obl_fr, per_men8_obl_fr]
agr_list_fr = [per_men1_agr_fr, per_men2_agr_fr, per_men3_agr_fr, per_men4_agr_fr, per_men5_agr_fr, per_men6_agr_fr, per_men7_agr_fr, per_men8_agr_fr]

# Femmes non retraitées (fe)
corv_list_fe = [per_men1_corv_fe, per_men2_corv_fe, per_men3_corv_fe, per_men4_corv_fe, per_men5_corv_fe, per_men6_corv_fe, per_men7_corv_fe, per_men8_corv_fe]
dep_list_fe = [per_men1_dep_fe, per_men2_dep_fe, per_men3_dep_fe, per_men4_dep_fe, per_men5_dep_fe, per_men6_dep_fe, per_men7_dep_fe, per_men8_dep_fe]
obl_list_fe = [per_men1_obl_fe, per_men2_obl_fe, per_men3_obl_fe, per_men4_obl_fe, per_men5_obl_fe, per_men6_obl_fe, per_men7_obl_fe, per_men8_obl_fe]
agr_list_fe = [per_men1_agr_fe, per_men2_agr_fe, per_men3_agr_fe, per_men4_agr_fe, per_men5_agr_fe, per_men6_agr_fe, per_men7_agr_fe, per_men8_agr_fe]

# Créer la figure avec 4 sous-graphiques
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))

def autolabel(rects, ax):
    """Ajoute la valeur de chaque barre au-dessus d'elle."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{:.2f}%'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

# Hommes non retraités (me)
data_me = {
    'Activités': ['Courses', 'Cuisine quotidienne', 'Cuisine de réception', 'Vaisselle', 'Ménage', 'Repassage', 'Bricolage', 'Jardinage'],
    "Corvée": corv_list_me,
    'Cela dépend': dep_list_me,
    "Obligation": obl_list_me,
    'Agréable': agr_list_me
}
df_me = pd.DataFrame(data_me)
x = np.arange(len(data_me['Activités']))
width = 0.2
rects1 = ax1.bar(x - 0.3, df_me['Corvée'], width, label='Corvée')
rects2 = ax1.bar(x - 0.1, df_me['Cela dépend'], width, label='Cela dépend')
rects3 = ax1.bar(x + 0.1, df_me['Obligation'], width, label="Obligation qui n'est \npas gênante")
rects4 = ax1.bar(x + 0.3, df_me['Agréable'], width, label='Agréable')
"""
autolabel(rects1, ax1)
autolabel(rects2, ax1)
autolabel(rects3, ax1)
autolabel(rects4, ax1)
"""
ax1.set_xlabel('Activités')
ax1.set_ylabel('Pourcentage (%)')
ax1.set_ylim(0, 100)
ax1.set_title('Hommes non retraités')
ax1.set_xticks(x)
ax1.set_xticklabels(data_me['Activités'])
ax1.tick_params(axis='x', rotation=70)
ax1.legend(loc='upper left')

# Hommes retraités (mr)
data_mr = {
    'Activités': ['Courses', 'Cuisine quotidienne', 'Cuisine de réception', 'Vaisselle', 'Ménage', 'Repassage', 'Bricolage', 'Jardinage'],
    "Corvée": corv_list_mr,
    'Cela dépend': dep_list_mr,
    "Obligation": obl_list_mr,
    'Agréable': agr_list_mr
}
df_mr = pd.DataFrame(data_mr)
x = np.arange(len(data_mr['Activités']))
width = 0.2

rects1 = ax2.bar(x - 0.3, df_mr['Corvée'], width, label='Corvée')
rects2 = ax2.bar(x - 0.1, df_mr['Cela dépend'], width, label='Cela dépend')
rects3 = ax2.bar(x + 0.1, df_mr['Obligation'], width, label="Obligation qui n'est \npas gênante")
rects4 = ax2.bar(x + 0.3, df_mr['Agréable'], width, label='Agréable')
"""
autolabel(rects1, ax2)
autolabel(rects2, ax2)
autolabel(rects3, ax2)
autolabel(rects4, ax2)
"""
ax2.set_xlabel('Activités')
ax2.set_ylabel('Pourcentage (%)')
ax2.set_ylim(0, 100)
ax2.set_title('Hommes retraités')
ax2.set_xticks(x)
ax2.set_xticklabels(data_mr['Activités'])
ax2.tick_params(axis='x', rotation=70)
ax2.legend(loc='upper left')

# Femmes retraitées (fr)
data_fr = {
    'Activités': ['Courses', 'Cuisine quotidienne', 'Cuisine de réception', 'Vaisselle', 'Ménage', 'Repassage', 'Bricolage', 'Jardinage'],
    "Corvée": corv_list_fr,
    'Cela dépend': dep_list_fr,
    "Obligation": obl_list_fr,
    'Agréable': agr_list_fr
}
df_fr = pd.DataFrame(data_fr)
x = np.arange(len(data_fr['Activités']))
width = 0.2

rects1 = ax4.bar(x - 0.3, df_fr['Corvée'], width, label='Corvée')
rects2 = ax4.bar(x - 0.1, df_fr['Cela dépend'], width, label='Cela dépend')
rects3 = ax4.bar(x + 0.1, df_fr['Obligation'], width, label="Obligation qui n'est \npas gênante")
rects4 = ax4.bar(x + 0.3, df_fr['Agréable'], width, label='Agréable')
"""
autolabel(rects1, ax4)
autolabel(rects2, ax4)
autolabel(rects3, ax4)
autolabel(rects4, ax4)
"""
ax4.set_xlabel('Activités')
ax4.set_ylabel('Pourcentage (%)')
ax4.set_ylim(0, 100)
ax4.set_title('Femmes retraitées')
ax4.set_xticks(x)
ax4.set_xticklabels(data_fr['Activités'])
ax4.tick_params(axis='x', rotation=70)
ax4.legend(loc='upper left')

# Femmes non retraitées (fe)
data_fe = {
    'Activités': ['Courses', 'Cuisine quotidienne', 'Cuisine de réception', 'Vaisselle', 'Ménage', 'Repassage', 'Bricolage', 'Jardinage'],
    "Corvée": corv_list_fe,
    'Cela dépend': dep_list_fe,
    "Obligation": obl_list_fe,
    'Agréable': agr_list_fe
}
df_fe = pd.DataFrame(data_fe)
x = np.arange(len(data_fe['Activités']))
width = 0.2

rects1 = ax3.bar(x - 0.3, df_fe['Corvée'], width, label='Corvée')
rects2 = ax3.bar(x - 0.1, df_fe['Cela dépend'], width, label='Cela dépend')
rects3 = ax3.bar(x + 0.1, df_fe['Obligation'], width, label="Obligation qui n'est \npas gênante")
rects4 = ax3.bar(x + 0.3, df_fe['Agréable'], width, label='Agréable')
"""
autolabel(rects1, ax3)
autolabel(rects2, ax3)
autolabel(rects3, ax3)
autolabel(rects4, ax3)
"""
ax3.set_xlabel('Activités')
ax3.set_ylabel('Pourcentage (%)')
ax3.set_ylim(0, 100)
ax3.set_title('Femmes non retraitées')
ax3.set_xticks(x)
ax3.set_xticklabels(data_fe['Activités'])
ax3.tick_params(axis='x', rotation=70)
ax3.legend(loc='upper left')

plt.suptitle("Ressenti face aux tâches domestiques")
plt.tight_layout()
plt.show()





















