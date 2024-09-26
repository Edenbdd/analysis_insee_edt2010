#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 11:07:51 2024

@author: eden
"""

import pandas as pd
import numpy as np

df = pd.read_csv("/home/eden/Documents/Mémoire/final/pref/echantillon.csv", dtype=str)
df = df.copy()

# REGOURPER LES ACTIVITES ##############################""
    
# Repos
repos = ['111', '112', '113']
# Soins personnels
soins_personnels = ['121', '122', '123', '124', '131', '132', '133', '151']
#Repas
repas = ['141', '142', '143', '144', '145', '146']
# Travail et Etudes
travail = ['211', '212', '213', '214', '221', '223', '231', '232', '233', '234', '241', '251', '261', '262', '263', '264', '271', '272']
# Loisirs
loisirs = ['381', '510', '511', '512', '513', '514', '521', '522', '523', '524', '531', '532', '533', '541', '542', '612', '613', '614', '615', '616', '617', '619', '621', '622', '623', '624', '625', '626', '627', '631', '632', '633', '634', '635', '636', '637', '638', '641', '651', '653', '654', '655', '656', '658', '661', '662', '663', '664', '665', '667', '668', '669', '671', '672', '673', '674', '678']
# Trajets et autres
trajets_et_autres = [ '341', '344', '810', '811', '812', '813', '819']
# Préparation repas
food = ['311', '312', '313']
# Soin aux adultes
adult = ['431', '432', '433', '439']
# Ménage
cleaning = ['323', '322', '324', '343']
# Animaux
pets = ['383', '384', '385']
# Linge
linge = ['331', '332', '334', '335']
# Jardin
jardin = ['382']
# Bricolage
brico = ['371', '372', '373', '374']
# Courses
shop = ['351', '352', '361']
# Soins aux enfants
children_care = ['411', '412', '413', '414', '419']
# Activités avec enfants
children_play = ['421', '422', '423', '424', '429']
# Total avec enfants (combinaison de soins et activités)
children_tot = children_care + children_play
# Gestion
gestion = ['342']
# Restreint
res = ['311', '312', '323', '324', '331', '332', '335', '341', '342', '343', '411', '412', '413', '414', '431', '432', '433', '419', '439']
# Intermédiaire
int_activities = res + ['322', '334', '351', '352', '361', '371', '372', '373', '374', '382', '421', '422', '423', '424', '429']
#Broad
# Broad (basé sur la définition donnée)
broad = int_activities + pets + trajets_et_autres
#catégories:
categories = {
        'repos': repos,
        'soins_personnels': soins_personnels,
        'repas': repas,
        'travail': travail,
        'loisirs': loisirs,
        'trajets_et_autres': trajets_et_autres,
        'food': food,
        'adult': adult,
        'cleaning': cleaning,
        'pets': pets,
        'linge': linge,
        'jardin': jardin,
        'brico': brico,
        'shop': shop,
        'children_care': children_care,
        'children_play': children_play,
        'children_tot': children_tot,
        'gestion': gestion,
        'res': res,
        'int_activities': int_activities,
        'broad': broad
    }


#ISOLER L ECHANTILLON STIGLITZT########################################""
# 1. Identifier les colonnes stiglitz
stiglitz_columns = [col for col in df.columns if col.startswith('stiglitz')]

print(len(df))
# Afficher le nombre de colonnes stiglitz trouvées
print(f"Nombre de colonnes stiglitz trouvées : {len(stiglitz_columns)}")

# 2. Exclure les lignes avec toutes les colonnes stiglitz vides
df_filtered = df.dropna(subset=stiglitz_columns, how='all')

# Afficher le nombre de lignes restantes
print(f"Nombre de lignes restantes : {len(df_filtered)}")


# Dictionnaire de correspondance entre les codes et les notes
note_mapping = {1: -3, 2: -2, 3: -1, 4: 0, 5: 1, 6: 2, 7: 3}

def calculate_category_mean(row, category, act_prefix='actpr', stiglitz_prefix='stiglitz'):
    category_ratings = []
    
    # Parcourir les 144 moments possibles de la journée
    for i in range(1, 145):
        act_col = f'{act_prefix}{i}'
        stig_col = f'{stiglitz_prefix}{i}'
        
        # Vérifier si les colonnes d'activité et de stiglitz existent pour ce moment
        if act_col in row.index and stig_col in row.index:
            act_value = str(row[act_col]).strip()
            stig_code = row[stig_col]
            
            # Vérifier si l'activité appartient à la catégorie et si le code stiglitz est valide
            if act_value in category and pd.notna(stig_code):
                try:
                    # Convertir le code stiglitz en entier
                    stig_code = int(float(stig_code))
                    if stig_code in note_mapping:
                        # Convertir le code en note réelle
                        real_note = note_mapping[stig_code]
                        category_ratings.append(real_note)
                    else:
                        print(f"Code stiglitz invalide : {stig_code}")
                except ValueError:
                    print(f"Valeur non numérique trouvée : {stig_code}")
    
    # Calculer la moyenne des notes pour cette catégorie
    return np.mean(category_ratings) if category_ratings else np.nan

# Appliquer la fonction à chaque catégorie pour chaque ligne du DataFrame
for category_name, category_codes in categories.items():
    df_filtered[f'mean_{category_name}'] = df_filtered.apply(lambda row: calculate_category_mean(row, category_codes), axis=1)

# Afficher un résumé des nouvelles colonnes de moyenne
print(df_filtered[[col for col in df_filtered.columns if col.startswith('mean_')]].describe())

    
df_filtered.to_csv("tempspref.csv")





