#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 11:17:39 2024

@author: eden
"""
import matplotlib.pyplot as plt
import pandas as pd

old = pd.read_csv('/home/eden/Documents/Mémoire/données/echantillon.csv')

#BAR CHART TEMPS DE CARE POUR SON PROPRE MENAGE/ JOUR
av_care_fr = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 32), 'time_total'].mean()
av_care_fe = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 10), 'time_total'].mean()

av_care_hr = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 32), 'time_total'].mean()
av_care_he = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 10), 'time_total'].mean()

colors = ['#E6194B', '#E6194B', '#3CB44B', '#3CB44B']

x_axis_1 = ['Femmes en activité', 'Femmes retraitées', 'Hommes en activité', 'Hommes retraités']
y_axis_1 = [av_care_fe, av_care_fr, av_care_he, av_care_hr]
bars = plt.bar(x_axis_1, y_axis_1, width = 0.8, color=colors)
plt.title('Temps consacré aux tâches domestiques pour son propre ménage en fonction du genre et du statut')
plt.xticks(rotation = 70)
plt.ylabel('Temps moyen (min/jour)')
for bar in bars:
    height = round(bar.get_height())
    plt.annotate(str(height), xy=(bar.get_x() + bar.get_width()/2, height), 
                xytext=(0, 0.1), textcoords="offset points",
                ha='center', va='bottom')

plt.show()

