#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 17:40:15 2024

@author: eden
"""

import pandas as pd


carnet = pd.read_csv("/home/eden/Documents/Mémoire/csv/carnet.csv")
indiv = pd.read_csv("/home/eden/Documents/Mémoire/csv/indiv.csv")
men = pd.read_csv("/home/eden/Documents/Mémoire/csv/menage.csv")

carnet = carnet[carnet.columns[carnet.columns.str.startswith('actpr') | 
                               carnet.columns.str.startswith('but') | 
                               carnet.columns.str.startswith('lieudet')].tolist() + ['idind']]

indiv = indiv[["idind", "idmen", "sexe", "age", "situa", "cs24", "couplrp", "handicap", "dip14"]]
men = men[["IDMEN", "RG", "NENFHORS", "NENFANTS"]]


#nettoyer carnet

carnet = carnet.drop(carnet.columns[carnet.columns.str.startswith('butv')], axis=1)
carnet = carnet.drop(carnet.columns[carnet.columns.str.startswith('actprv')], axis=1)
carnet = carnet.drop(carnet.columns[carnet.columns.str.startswith('lieudetv')], axis=1)

indiv.rename(columns={'idmen':'IDMEN'}, inplace=True)
indiv = pd.merge(indiv, men, on="IDMEN", how="left")

merged = pd.merge(carnet, indiv, on="idind", how="left")
print(len(merged))
old = merged.loc[(merged['age'] >= 55) & (merged['age'] <= 65) & (merged['RG'] != 1) & (merged['RG'] != 2) & (merged['RG'] != 3) & (merged['RG'] != 4)] 
print(len(old))
old.to_csv("echantillonreg.csv")