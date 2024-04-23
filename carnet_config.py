#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 17:40:15 2024

@author: eden
"""

import pandas as pd
import matplotlib.pyplot as plt

carnet = pd.read_csv("/home/eden/Documents/Mémoire/csv/carnet.csv")
indiv = pd.read_csv("/home/eden/Documents/Mémoire/csv/indiv.csv")
men = pd.read_csv("/home/eden/Documents/Mémoire/csv/menage.csv")


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
carnet = carnet.drop(carnet.columns[carnet.columns.str.startswith('lieudet')], axis=1)
carnet = carnet.drop(carnet.columns[carnet.columns.str.startswith('pres')], axis=1)
carnet = carnet.drop(carnet.columns[carnet.columns.str.startswith('stiglitz')], axis=1)

indiv.rename(columns={'idmen':'IDMEN'}, inplace=True)
indiv = pd.merge(indiv, men, on="IDMEN", how="left")

merged = pd.merge(carnet, indiv, on="idind", how="left")
print(len(merged))
old = merged.loc[(merged['age'] >= 55) & (merged['age'] <= 65) & (merged['RG'] != 1) & (merged['RG'] != 2) & (merged['RG'] != 3) & (merged['RG'] != 4)] 
print(len(old))
old.to_csv("echantillon.csv")