#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 11:07:51 2024

@author: eden
"""

import pandas as pd

df = pd.read_csv("/home/eden/Documents/Mémoire/final/children/echantillonchildren.csv", dtype=str)
df = df.copy()
activites = {
    '311': 'Cuisine : préparation et cuisson des aliments, épluchage',
    '312': 'Lavage de la vaisselle + rangement de la vaisselle, débarrasser la table',
    '313': 'Mettre la table, servir le repas',
    '322': 'Rangement des courses, chargement et déchargement de la voiture',
    '323': 'Rangement et nettoyage extérieur',
    '324': 'Ménage et rangement (intérieur de la maison)',
    '331': "Lavage du linge (y c. le trier, le mettre dans / sortir de la machine à laver, l'étendre)",
    '332': "Repassage",
    '334': "Couture, tricot, crochet, cirage et lavage des chaussures",
    '335': "Rangement des vêtements, préparer son sac, sa valise",
    '341': "Chauffage, eau (couper le bois, charger le charbon, allumer le feu)",
    '342': "Gestion du ménage : faire ses comptes, courrier administratif",
    '343': "Autres activités d'entretien de la maison",
    '351': "Achats de biens de consommation, shopping",
    '352': "Achats de services marchands (hors soins personnels)",
    '361': "Recours aux services administratifs (banques, avocats, notaires, démarches administratives (CAF)…). Hors recherche d'emploi.",
    '371': "Gros travaux de construction : maçonnerie, plomberie, menuiserie, charpente, carrelage…",
    '372': "Aménagement et décoration de la maison (petits travaux)",
    '373': "Entretien et réparation d'objets, d'appareils",
    '374': "Réparations et travaux d'entretien relatifs aux voitures, 2 roues et bateaux",
    '382': "Jardinage",
    '383': "S'occuper des animaux domestiques : animaux de basse-cour et autres animaux à usage productif (hors travail professionnel)",
    '384': "S'occuper des animaux de compagnie",
    '385': "Promener le chien, sortir un animal de compagnie",
    '411': "S'occuper d'enfants de son ménage (hors soins médicaux)",
    '412': "Accompagner un enfant de son ménage, l'attendre (hors trajets)",
    '413': "Soins médicaux aux enfants de son ménage, à domicile",
    '414': "Autres : bisous, câlins, gronderies… à un enfant de son ménage",
    '421': "Surveillance des devoirs et leçons",
    '422': "Conversations, lectures non scolaires",
    '423': 'Jeux et activités à domicile',
    '424': 'Jeux et activités hors du domicile',
    '431': 'Soins aux adultes de son ménage : aide pour activités personnelles ou physiologiques (toilette,repas, habillement',
    '432': 'Accompagner, tenir compagnie à un adulte de son ménage',
    '433': 'Autres aides à un membre adulte de son ménage',
    '419': "S'occuper d'enfants (y c. accompagner, soins médicaux, câlins…), pour un autre ménage",
    '429': "Jeux et instruction (activités incluses dans 421 à 424), pour un autre ménage",
    '439': "Soins aux adultes d'un autre ménage"
    }

buts = {
       '1.0': "personnel ou pour son ménage",
       '2.0': "professionnel",
       '3.0': "aide à un autre ménage",
       '4.0': "bénévole"}

trajets = {
    '812': "Autres trajets (hors trajets pendant le travail)",
    '813': "trajets liés aux enfants",
    '819': "trajets pour un autre ménage"
    }

# Supposons que df est votre DataFrame initial
# activites et buts sont vos dictionnaires existants

df = df.fillna('0')
for col in df.columns:
    if col.startswith('but'):
       df[col] = df[col].astype(str)


# Créer les nouvelles colonnes pour chaque combinaison activité-but
for act_code, act_description in activites.items():
    for but_code, but_description in buts.items():
        column_name = f'time_{act_code}_{but_code}'
        df[column_name] = 0


# Parcourir les colonnes d'activités et de buts
act_columns = [col for col in df.columns if col.startswith('act')]
but_columns = [col for col in df.columns if col.startswith('but')]


#calcul des temps
for index, row in df.iterrows():
    for act_col, but_col in zip(act_columns, but_columns):
        act_code = row[act_col]
        but_code = row[but_col]
        # Vérifier si l'activité et le but sont dans les dictionnaires respectifs
        if act_code in activites and but_code in buts:
                df.loc[index, f'time_{act_code}_{but_code}'] += 10
        else:
                pass
            
#trajets
df['time_trajet_self'] = 0
for i, row in df.iterrows():
    for nb in range(1, 145): 
        if ((row[f'actpr{nb}'] == '812') | (row[f'actpr{nb}'] == '813')) & (row[f'lieudet{nb}'] == '24'):
                df.loc[i, 'time_trajet_self'] += 10

df['time_trajet_other'] = 0
for i, row in df.iterrows():
    for nb in range(1, 145): 
        if ((row[f'actpr{nb}'] == '819') & (row[f'lieudet{nb}'] == '24')):
                df.loc[i, 'time_trajet_other'] += 10
        
df['time_trajet_tot'] = df['time_trajet_self'] + df['time_trajet_other']

#PERIMETRE
#res soi même
df['res_self'] = df['time_311_1.0'] + df['time_312_1.0'] + df['time_323_1.0'] + df['time_324_1.0'] + df['time_331_1.0'] + df['time_332_1.0'] + \
    df['time_335_1.0'] + df['time_341_1.0'] + df['time_342_1.0'] + df['time_343_1.0'] + df['time_411_1.0'] + df['time_412_1.0'] \
        + df['time_413_1.0'] + df['time_414_1.0'] + df['time_431_1.0'] + df['time_432_1.0'] + df['time_433_1.0'] 
        
#res autrui
df['res_other'] = df['time_311_3.0'] + df['time_312_3.0'] + df['time_323_3.0'] + df['time_324_3.0'] + df['time_331_3.0'] + df['time_332_3.0'] + \
    df['time_335_3.0'] + df['time_341_3.0'] + df['time_342_3.0'] + df['time_343_3.0'] + df['time_419_3.0'] + df['time_439_3.0'] 

#res tot
df['res_tot'] = df['res_self'] + df['res_other']

#int soi même
df['int_self'] = df['res_self'] + df['time_322_1.0'] + df['time_334_1.0'] + df['time_351_1.0'] + df['time_352_1.0'] + \
    df['time_361_1.0'] + df['time_371_1.0'] + df['time_372_1.0'] + df['time_373_1.0'] + df['time_374_1.0'] + df['time_382_1.0'] \
        + df['time_421_1.0'] + df['time_422_1.0'] + df['time_423_1.0'] + df['time_424_1.0']

#int autrui
df['int_other'] = df['res_other'] + df['time_322_3.0'] + df['time_334_3.0'] + df['time_351_3.0'] + df['time_352_3.0'] + \
    df['time_361_3.0'] + df['time_371_3.0'] + df['time_372_3.0'] + df['time_373_3.0'] + df['time_374_3.0'] + df['time_382_3.0'] \
        + df['time_414_3.0'] + df['time_429_3.0']

#int tot
df['int_tot'] = df['int_self'] + df['int_other']

#broad soi même
df['broad_self'] = df['int_self'] + df['time_383_1.0'] + df['time_384_1.0'] + df['time_385_1.0'] + df['time_trajet_self']

#broad autrui
df['broad_other'] = df['int_other'] + df['time_383_3.0'] + df['time_384_3.0'] + df['time_385_3.0'] + df['time_trajet_other']

#broad tot
df['broad_tot'] = df['broad_self'] + df['broad_other']

#TASKS
#préparation repas
df['food_self'] = df['time_311_1.0'] + df['time_312_1.0'] + df['time_313_1.0']
df['food_other'] = df['time_311_3.0'] + df['time_312_3.0'] + df['time_313_3.0']
df['food_tot'] = df['food_self'] + df['food_other']

#soin aux adultes
df['adult_self'] = df['time_431_1.0'] + df['time_432_1.0'] + df['time_433_1.0']
df['adult_other'] = df['time_439_3.0']
df['adult_tot'] = df['adult_self'] + df['adult_other']

#ménage
df['cleaning_self'] = df['time_323_1.0'] + df['time_322_1.0'] + df['time_324_1.0'] + df['time_343_1.0']
df['cleaning_other'] = df['time_323_3.0'] + df['time_322_3.0'] + df['time_324_3.0'] + df['time_343_3.0']
df['cleaning_tot'] = df['cleaning_self'] + df['cleaning_other']

#animaux
df['pets_self'] = df['time_383_1.0'] + df['time_384_1.0'] + df['time_385_1.0']
df['pets_other'] = df['time_383_3.0'] + df['time_384_3.0'] + df['time_385_3.0']
df['pets_tot'] = df['pets_self'] + df['pets_other']

#linge
df['linge_self'] = df['time_331_1.0'] + df['time_332_1.0'] + df['time_334_1.0'] + df['time_335_1.0']
df['linge_other'] = df['time_331_3.0'] + df['time_332_3.0'] + df['time_334_3.0'] + df['time_335_3.0']
df['linge_tot'] = df['linge_self'] + df['linge_other']

#jardin
df['jardin_self'] =  df['time_382_1.0']
df['jardin_other'] =  df['time_382_3.0']
df['jardin_tot'] = df['jardin_self'] + df['jardin_other']

#bricolage
df['brico_self'] = df['time_371_1.0'] + df['time_372_1.0'] + df['time_373_1.0'] + df['time_374_1.0']
df['brico_other'] = df['time_371_3.0'] + df['time_372_3.0'] + df['time_373_3.0'] + df['time_374_3.0']
df['brico_tot'] = df['brico_self'] + df['brico_other']

#courses
df['shop_self'] = df['time_351_1.0'] + df['time_352_1.0'] + df['time_361_1.0']
df['shop_other'] = df['time_351_3.0'] + df['time_352_3.0'] + df['time_361_3.0']
df['shop_tot'] = df['shop_self'] + df['shop_other']

#SOINS aux enfants
df['children_care_self'] = df['time_411_1.0'] + df['time_412_1.0'] + df['time_413_1.0'] + df['time_414_1.0']
df['children_care_other'] = df['time_419_3.0'] 
df['children_care_tot'] = df['children_care_self'] + df['children_care_other']

#ACTIVITES avec enfants
df['children_play_self'] = df['time_421_1.0'] + df['time_422_1.0'] + df['time_423_1.0'] + df['time_424_1.0']
df['children_play_other'] = df['time_429_3.0']
df['children_play_tot'] = df['children_play_self'] + df['children_play_other']

#TOT avec enfants
df['children_tot_self'] = df['children_care_self'] + df['children_play_self']
df['children_tot_other'] = df['children_care_other'] + df['children_play_other']
df['children_tot_tot'] = df['children_tot_self'] + df['children_tot_other'] 

#gestion
df['gestion_self'] =  df['time_342_1.0']
df['gestion_other'] =  df['time_342_3.0']
df['gestion_tot'] = df['gestion_self'] + df['gestion_other']

#autres
df['other_self'] = df['time_341_1.0']
df['other_other'] = df['time_341_3.0']
df['other_tot'] = df['other_self'] + df['other_other']

    
df.to_csv("tottempschildren.csv")





