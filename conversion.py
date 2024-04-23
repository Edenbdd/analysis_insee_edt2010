#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 16:21:32 2024

@author: eden
"""

import pyreadstat as prs

carnet, meta = prs.read_sas7bdat('/home/eden/Documents/Mémoire/lil-0695.sas7bdat/SAS/carnet.sas7bdat')
conjoint, meta1 = prs.read_sas7bdat('/home/eden/Documents/Mémoire/lil-0695.sas7bdat/SAS/conjoints.sas7bdat')
couple, meta2 = prs.read_sas7bdat('/home/eden/Documents/Mémoire/lil-0695.sas7bdat/SAS/couples.sas7bdat')
hab_menage, meta3 = prs.read_sas7bdat('/home/eden/Documents/Mémoire/lil-0695.sas7bdat/SAS/hab_menage.sas7bdat')
indiv, meta4 = prs.read_sas7bdat('/home/eden/Documents/Mémoire/lil-0695.sas7bdat/SAS/individu_fpr_tot3.sas7bdat')
menage, meta5 = prs.read_sas7bdat('/home/eden/Documents/Mémoire/lil-0695.sas7bdat/SAS/menage.sas7bdat')
qaaconjoint, meta6 = prs.read_sas7bdat('/home/eden/Documents/Mémoire/lil-0695.sas7bdat/SAS/qaaconjoints.sas7bdat')
qaacouple, meta7 = prs.read_sas7bdat('/home/eden/Documents/Mémoire/lil-0695.sas7bdat/SAS/qaacouples.sas7bdat')
semainier, meta8 = prs.read_sas7bdat('/home/eden/Documents/Mémoire/lil-0695.sas7bdat/SAS/semainiers.sas7bdat')


carnet.to_csv('carnet.csv', index=False)
conjoint.to_csv('conjoint.csv', index=False)
couple.to_csv('couple.csv', index=False)
hab_menage.to_csv('hab_menage.csv', index=False)
indiv.to_csv('indiv.csv', index=False)
menage.to_csv('menage.csv', index=False)
qaaconjoint.to_csv('qaaconjoint.csv', index=False)
qaacouple.to_csv('qaacouple.csv', index=False)
semainier.to_csv('semainier.csv', index=False)