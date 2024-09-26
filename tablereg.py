#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:48:53 2024

@author: eden
"""

import pandas as pd


# Lire le fichier CSV
reg = pd.read_csv("/home/eden/Documents/Mémoire/final/reg/dataformatreg.csv", dtype=int)

#s'assurer qu'il n'y aura pas de division par 0

# Colonnes à vérifier et remplacer
colonnes_a_verifier = ['res_tot_fem',	'int_tot_fem',	'broad_tot_fem', 'res_tot_hom',	'int_tot_hom',
                       'broad_tot_hom']
# Remplacer les 0 par 10 dans les colonnes spécifiées
reg[colonnes_a_verifier] = reg[colonnes_a_verifier].replace(0, 10)

   

#temps fem tot - hom tot
reg['diff_int_tot'] = reg['int_tot_fem'] - reg['int_tot_hom']
reg['diff_res_tot'] = reg['res_tot_fem'] - reg['res_tot_hom']
reg['diff_broad_tot'] = reg['broad_tot_fem'] - reg['broad_tot_hom']


#coef fem tot/hom tot
reg['coeff_int_tot'] = reg['int_tot_fem'] / reg['int_tot_hom']
reg['coeff_res_tot'] = reg['res_tot_fem'] / reg['res_tot_hom']
reg['coeff_broad_tot'] = reg['broad_tot_fem'] / reg['broad_tot_hom']


#colonnes retraités
reg['ret_hom'] = ((reg['situa_hom'] == 5) & (reg['situa_fem'] != 5)).astype(int)
reg['ret_fem'] = ((reg['situa_fem'] == 5) & (reg['situa_hom'] != 5)).astype(int)
reg['ret_both'] = ((reg['situa_fem'] == 5) & (reg['situa_hom'] == 5)).astype(int)
reg['ret_not'] = ((reg['situa_fem'] != 5) & (reg['situa_hom'] != 5)).astype(int)

#rename enfants
reg = reg.rename(columns={'NENFANTS_fem':'nbenf'})
reg = reg.rename(columns={'NENFHORS_fem':'nbenfhors'})

#handicap
reg['handi_hom'] = ((reg['handicap_fem'] != 1) & (reg['handicap_hom'] == 1)).astype(int)
reg['handi_fem'] = ((reg['handicap_fem'] == 1) & (reg['handicap_hom'] != 1)).astype(int)
reg['handi_both'] = ((reg['handicap_fem'] == 1) & (reg['handicap_hom'] == 1)).astype(int)
reg['handi_not'] = ((reg['handicap_fem'] != 1) & (reg['handicap_hom'] != 1)).astype(int)

#études hom
reg['sup_long_hom'] = reg['dip14_hom'].isin([10, 12, 20]).astype(int)
reg['sup_court_hom'] = reg['dip14_hom'].isin([30, 31, 33]).astype(int)
reg['bac_hom'] = reg['dip14_hom'].isin([41, 42, 44]).astype(int)
reg['cap_hom'] = reg['dip14_hom'].isin([43, 50]).astype(int)
reg['none_hom'] = reg['dip14_hom'].isin([60, 70, 71]).astype(int)

#études fem
reg['sup_long_fem'] = reg['dip14_fem'].isin([10, 12, 20]).astype(int)
reg['sup_court_fem'] = reg['dip14_fem'].isin([30, 31, 33]).astype(int)
reg['bac_fem'] = reg['dip14_fem'].isin([41, 42, 44]).astype(int)
reg['cap_fem'] = reg['dip14_fem'].isin([43, 50]).astype(int)
reg['none_fem'] = reg['dip14_fem'].isin([60, 70, 71]).astype(int)

#cs 24 fem
reg['agri_fem'] = reg['cs24_fem'].isin([10, 71]).astype(int)
reg['art_fem'] = reg['cs24_fem'].isin([72, 21, 22, 23]).astype(int)
reg['cadre_fem'] = reg['cs24_fem'].isin([73, 31, 32, 36, 41, 46, 47, 48]).astype(int)
reg['empl_fem'] = reg['cs24_fem'].isin([51, 55, 56, 61, 66, 69, 76]).astype(int)
reg['inact_fem'] = reg['cs24_fem'].isin([81, 82]).astype(int)

#cs 24 hom
reg['agri_hom'] = reg['cs24_hom'].isin([10, 71]).astype(int)
reg['art_hom'] = reg['cs24_hom'].isin([72, 21, 22, 23]).astype(int)
reg['cadre_hom'] = reg['cs24_hom'].isin([73, 31, 32, 36, 41, 46, 47, 48]).astype(int)
reg['empl_hom'] = reg['cs24_hom'].isin([51, 55, 56, 61, 66, 69, 76]).astype(int)
reg['inact_hom'] = reg['cs24_hom'].isin([81, 82]).astype(int)

print(reg.columns)

#vérification
colonnes_a_verifier2 = ["coeff_int_tot", "coeff_res_tot", "coeff_broad_tot"]
for colonne in colonnes_a_verifier2:
    zeros_count = (reg[colonne] == 0).sum()
    if zeros_count > 0:
        print(f"La colonne '{colonne}' contient {zeros_count} valeur(s) égale(s) à 0.")
    else:
        print(f"La colonne '{colonne}' ne contient aucune valeur égale à 0.")
   

#cleaning
supp = ['Unnamed: 0', 'IDMEN', 'idind_fem', 'sexe_fem', 'age_fem', 'situa_fem',
       'cs24_fem', 'couplrp_fem', 'handicap_fem', 'dip14_fem', 'RG_fem',
       'res_self_fem', 'res_other_fem', 'int_self_fem', 'int_other_fem', 'broad_self_fem',
       'broad_other_fem', 'idind_hom', 'sexe_hom', 'age_hom',
       'situa_hom', 'cs24_hom', 'couplrp_hom', 'handicap_hom', 'dip14_hom',
       'RG_hom', 'NENFHORS_hom', 'NENFANTS_hom', 'res_self_hom',
       'res_other_hom', 'int_self_hom', 'int_other_hom',
       'broad_self_hom', 'broad_other_hom']
reg_clean = reg.drop(columns=supp)

#save data reg
reg_clean.to_csv("tablereg.csv")