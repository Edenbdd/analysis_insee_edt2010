#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 11:29:29 2024

@author: eden
"""

import pandas as pd


edt = pd.read_csv("/home/eden/Documents/Mémoire/données/Csv/efile_fr.csv")
ind = pd.read_csv("/home/eden/Documents/Mémoire/données/Csv/indfile_fr.csv")

#changer en string pour préserver les nombres indiquer
edt = edt.astype('string')
ind = ind.astype('string')
#print(edt.dtypes)
#print(ind.dtypes)

#créer une colonne avec un id unique pour chaque personne
edt['uniq'] = edt['PID'] + edt['HID']
ind['uniq'] = ind['PID'] + ind['HID']
#print(edt['uniq'].head())
#print(ind['uniq'].head())

#fusionner
merged = pd.merge(edt, ind, on='uniq', how='left')
#print(merged.index)
#print(merged.columns)

#repasser l'âge en int
merged['inc2'] = merged['inc2'].astype('int64')

#créer et sauvergarder un df avec seulement les personnes entre 55 et 65 ans
old = merged[(merged['inc2'] >= 55) & (merged['inc2'] <= 65)]
#print(old.index)
#print(old.head)
#print(old.columns)
#old.to_csv('echantillon.csv', index=False)
#print(old['inc2'].head(25))

#clean certaines colonnes pour rendre le tableau lisible sur excel + enregistrer
old = old.loc[:, ~old.columns.str.contains('Mcom|Scom|Alone|Wpartner|Wparent|Wchild|Wother')]
#old.to_csv('echantillon.csv', index=False)
#print(old.columns)

#créer un dictionnaire avec les noms des activités
activities = {
    '300': "Unspecified household and family care",
    '311': 'Food preparation, baking and preserving',
    '312': 'Dish washing',
    '321': 'Cleaning dwelling',
    '322': 'Cleaning garden',
    '323': 'Heating and water',
    '324': 'Arranging household goods and materials',
    '329': 'Other or unspecified household upkeep',
    '331': 'Laundry',
    '332': 'Ironing',
    '333': 'Handicraft and producing textiles',
    '341': 'Gardening',
    '342': 'Tending domestic animals',
    '343': 'Caring for pets',
    '344': 'Walking the dog',
    '351': 'House construction and renovation',
    '352': 'Repairs of dwelling',
    '353': 'Making, repairing and maintaining equipment',
    '354': 'Vehicle maintenance',
    '361': 'Shopping',
    '362': 'Commercial and administrative services',
    '363': 'Personal services',
    '371': 'Household management',
    '381': 'Physical care and supervision of child',
    '382': 'Teaching the child',
    '383': 'Reading, playing and talking with child',
    '384': 'Accompanying child',
    '391': 'Physical care and supervision of adult',
    '392': 'Other help of a dependent adult household member',
    '399': 'Help to a non dependent adult household member',
    '421':	'Construction and repairs as help',
    '422':	'Help in employment and farming',
    '423':	'Care of own children living in another household',
    '424':	'Other childcare as help to another household',
    '425':	'Help to an adult of another household',
    '429':	'Other or unspecified informal help to another household'
    }

#print(old.dtypes)
old = old.fillna('0')
#créer les nouvelles colonnes
for activity, name in activities.items():
    old[f'time_{activity}'] = 0
#print(old.columns)
#parcourir chaque ligne et compte le nombre d'apparition pour avoir le temps consacrer à chaque activité (min)
for i, row in old.iterrows():
    for j, col in enumerate(old.columns):
        for activity, name in activities.items():
            if row[col] == activity:
                old.loc[i, f'time_{activity}'] += 9
            else:
                pass



#CREATION DE COLONNE PAR TYPE D ACTIVITE (POUR SON PROPRE MENAGE)
old['time_food_dishes'] = old['time_311'] + old['time_312']
old['time_care_adult'] = old['time_391'] + old['time_392'] + old['time_399']
old['time_cleaning'] = old['time_321'] + old['time_323'] + old['time_324'] + old['time_329']
old['time_pets'] = old['time_342'] + old['time_344'] + old['time_343']
old['time_laundry'] = old['time_331'] + old['time_332'] + old['time_333']
old['time_gardening'] = old['time_341'] + old['time_322'] 
old['time_handy'] = old['time_351'] + old['time_352'] + old['time_353'] + old['time_354']
old['time_shopping_services'] = old['time_361'] + old['time_362'] + old['time_363'] 
old['time_children'] = old['time_381'] + old['time_382'] + old['time_383'] + old['time_384']
old['time_other_care'] = old['time_300']

#CREATION DE COLONNE SELON LE HALO
old['time_total'] = old['time_food_dishes'] + old['time_care_adult'] + old['time_cleaning'] + old['time_pets'] + old['time_laundry'] + old['time_gardening'] + old['time_handy'] +old['time_shopping_services'] + old['time_children'] + old['time_other_care']
old['core'] = old['time_food_dishes'] + old['time_care_adult'] + old['time_cleaning'] + old['time_laundry'] + old['time_381'] + old['time_382'] + old['time_384'] 
old['intermediate'] = old['core'] + old['time_383'] + old['time_shopping_services'] + old['time_gardening'] + old['time_handy']
old['broad'] = old['intermediate'] + old['time_pets'] + old['time_other_care'] #+ trajet ? voir méthodo détaillée

#pb de doublon -> il va falloir pondérer, cf méthodologie de l'INSEE
#print(old['uniq'].value_counts())


#SAVE
old.to_csv('echantillon.csv', index=False)










