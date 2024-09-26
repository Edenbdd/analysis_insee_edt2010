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

indiv = indiv[["idind", "idmen", "age", "situa", "sexe", "couplrp"]]
men = men[["IDMEN", "RG"]]
#men.rename(columns={"IDMEN" : "idmen"}, inplace=True)

"""
print(carnet.columns)
print(len(carnet))
print(indiv.columns)
print(len(indiv))
print(carnet['idcar'])
"""
#nettoyer carnet
carnet = carnet.drop(carnet.columns[carnet.columns.str.startswith('ordi')], axis=1)
carnet = carnet.drop(carnet.columns[carnet.columns.str.startswith('pres')], axis=1)
carnet = carnet.drop(carnet.columns[carnet.columns.str.startswith('stiglitzv')], axis=1)
carnet = carnet.drop(carnet.columns[carnet.columns.str.startswith('actse')], axis=1)
carnet = carnet.drop(carnet.columns[carnet.columns.str.startswith('butv')], axis=1)
carnet = carnet.drop(carnet.columns[carnet.columns.str.startswith('actprv')], axis=1)

indiv.rename(columns={'idmen':'IDMEN'}, inplace=True)
indiv = pd.merge(indiv, men, on="IDMEN", how="left")

merged = pd.merge(carnet, indiv, on="idind", how="left")
print(len(merged))
old = merged.loc[(merged['age'] >= 55) & (merged['age'] <= 65) & (~merged['RG'].isin([1, 2, 3, 4])) & (merged['couplrp'] == 1)] 
print(len(old))
old.to_csv("echantillon.csv")