#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:15:43 2024

@author: eden
"""

import pandas as pd

# Lire le fichier CSV
df = pd.read_csv("/home/eden/Documents/Mémoire/final/reg/tempsreg.csv", dtype=str)

# Supprimer les colonnes non désirées
columns_to_drop = df.columns[df.columns.str.startswith(('time', 'actpr', 'but', 'lieu', 'unnamed'))]
df = df.drop(columns=columns_to_drop)

# Remplacer les valeurs manquantes par 0
df = df.fillna('0')

# Convertir les colonnes en nombres flottants, puis en entiers
df = df.astype(float).round().astype(int)

# Sélectionner les lignes où couplrp est égal à 1
cpl = df.loc[df['couplrp'] == 1]

fem = cpl.loc[cpl['sexe'] == 2]
hom = cpl.loc[cpl['sexe'] == 1]

''' vérification
print(len(cpl))
print(len(fem))
print(len(hom))
'''

# Supposons que fem et hom sont vos DataFrames originaux

# Agréger les DataFrames en faisant la moyenne pour toutes les colonnes sauf 'IDMEN'
fem_aggregated = fem.groupby('IDMEN').mean().reset_index()
hom_aggregated = hom.groupby('IDMEN').mean().reset_index()

# Fusionner les DataFrames agrégés
reg = pd.merge(fem_aggregated, hom_aggregated, on='IDMEN', how='inner', suffixes=('_fem', '_hom'))



''' vérification

print(reg.shape)
print(reg.columns)
print("Nombre d'IDMEN uniques dans fem_aggregated:", fem_aggregated['IDMEN'].nunique())
print("Nombre d'IDMEN uniques dans hom_aggregated:", hom_aggregated['IDMEN'].nunique())
print("Nombre de lignes dans reg:", len(reg))

print("Doublons dans fem_aggregated:", fem_aggregated['IDMEN'].duplicated().sum())
print("Doublons dans hom_aggregated:", hom_aggregated['IDMEN'].duplicated().sum())
print(reg)
'''

# Utiliser drop() pour supprimer les colonnes 'Unnamed'
unnamed_cols = reg.columns[reg.columns.str.startswith('Unnamed')]
reg = reg.drop(columns=unnamed_cols)

#save reg
reg.to_csv("dataformatreg.csv")