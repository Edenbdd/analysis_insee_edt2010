#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:13:09 2024

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
old_me = indiv.loc[(indiv['age'] <= 65) & (indiv['age'] >= 55) & (indiv['RG'] != 1) & (indiv['RG'] != 2) & (indiv['RG'] != 3) & (indiv['RG'] != 4)]


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



corv_list_me = [per_men1_corv_me, per_men2_corv_me, per_men3_corv_me, per_men4_corv_me, per_men5_corv_me, per_men6_corv_me, per_men7_corv_me, per_men8_corv_me]
dep_list_me = [per_men1_dep_me, per_men2_dep_me, per_men3_dep_me, per_men4_dep_me, per_men5_dep_me, per_men6_dep_me, per_men7_dep_me, per_men8_dep_me]
obl_list_me = [per_men1_obl_me, per_men2_obl_me, per_men3_obl_me, per_men4_obl_me, per_men5_obl_me, per_men6_obl_me, per_men7_obl_me, per_men8_obl_me]
agr_list_me = [per_men1_agr_me, per_men2_agr_me, per_men3_agr_me, per_men4_agr_me, per_men5_agr_me, per_men6_agr_me, per_men7_agr_me, per_men8_agr_me]

# Créer la figure avec 4 sous-graphiques

def autolabel(rects, ax):
    """Ajoute la valeur de chaque barre au-dessus d'elle."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{:.2f}%'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

fig, ax = plt.subplots(figsize=(12, 8))

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
rects1 = plt.bar(x - 0.3, df_me['Corvée'], width, label='Corvée')
rects2 = plt.bar(x - 0.1, df_me['Cela dépend'], width, label='Cela dépend')
rects3 = plt.bar(x + 0.1, df_me['Obligation'], width, label="Obligation qui n'est \npas gênante")
rects4 = plt.bar(x + 0.3, df_me['Agréable'], width, label='Agréable')
"""
autolabel(rects1, ax1)
autolabel(rects2, ax1)
autolabel(rects3, ax1)
autolabel(rects4, ax1)
"""
ax.set_xlabel('Activités')
ax.set_ylabel('Pourcentage (%)')
ax.set_ylim(0, 100)
ax.set_xticks(x)
ax.set_xticklabels(data_me['Activités'])
ax.tick_params(axis='x', rotation=70)
ax.legend(loc='upper left')

leg = ax.legend()
for text in leg.get_texts():
    text.set_color('black')


plt.suptitle("Ressenti face aux tâches domestiques", color="grey", fontsize=16)
plt.tight_layout()
plt.show()





















