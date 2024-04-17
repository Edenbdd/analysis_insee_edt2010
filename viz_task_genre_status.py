#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 17:24:58 2024

@author: eden
"""
import pandas as pd
import matplotlib.pyplot as plt

old = pd.read_csv("/home/eden/Documents/Mémoire/données/echantillon.csv")

taches = ['Préparation des repas', 'Soin aux adultes', 'Nettoyage', 'Soin aux animaux domestiques',
            'Soin du linge', 'Jardinnage', 'Bricolage', 'Courses & Administration', 'Soin aux enfants',
            'Gestion Administrative', 'Autres']

#PLOT TEMPS CONSACRE AUX TACHES DOMESTIQUES EN MIN /JOUR SELON LE GENRE
#femmes retraitées
mean_food_fr = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 32), 'time_food_dishes'].mean()
mean_care_adult_fr = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 32), 'time_care_adult'].mean()
mean_cleaning_fr = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 32), 'time_cleaning'].mean()
mean_pets_fr = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 32), 'time_pets'].mean()
mean_laundry_fr = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 32), 'time_laundry'].mean()
mean_gardening_fr = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 32), 'time_gardening'].mean()
mean_handy_fr = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 32), 'time_handy'].mean()
mean_shopping_services_fr = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 32), 'time_shopping_services'].mean()
mean_children_fr = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 32), 'time_children'].mean()
mean_management_fr =  old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 32), 'time_371'].mean()
mean_other_care_fr = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 32), 'time_other_care'].mean()

y_axis_fr = [mean_food_fr, mean_care_adult_fr, mean_cleaning_fr, mean_pets_fr, mean_laundry_fr, 
            mean_gardening_fr, mean_handy_fr, mean_shopping_services_fr, mean_children_fr, 
            mean_management_fr, mean_other_care_fr]

#femmes en emploi
mean_food_fe = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 10), 'time_food_dishes'].mean()
mean_care_adult_fe = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 10), 'time_care_adult'].mean()
mean_cleaning_fe = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 10), 'time_cleaning'].mean()
mean_pets_fe = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 10), 'time_pets'].mean()
mean_laundry_fe = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 10), 'time_laundry'].mean()
mean_gardening_fe = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 10), 'time_gardening'].mean()
mean_handy_fe = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 10), 'time_handy'].mean()
mean_shopping_services_fe = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 10), 'time_shopping_services'].mean()
mean_children_fe = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 10), 'time_children'].mean()
mean_management_fe =  old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 10), 'time_371'].mean()
mean_other_care_fe = old.loc[(old['inc1'] == 2) & (old['ind17_1'] == 10), 'time_other_care'].mean()

y_axis_fe = [mean_food_fe, mean_care_adult_fe, mean_cleaning_fe, mean_pets_fe, mean_laundry_fe, 
            mean_gardening_fe, mean_handy_fe, mean_shopping_services_fe, mean_children_fe, 
            mean_management_fe, mean_other_care_fe]

#hommes retraités
mean_food_hr = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 32), 'time_food_dishes'].mean()
mean_care_adult_hr = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 32), 'time_care_adult'].mean()
mean_cleaning_hr = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 32), 'time_cleaning'].mean()
mean_pets_hr = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 32), 'time_pets'].mean()
mean_laundry_hr = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 32), 'time_laundry'].mean()
mean_gardening_hr = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 32), 'time_gardening'].mean()
mean_handy_hr = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 32), 'time_handy'].mean()
mean_shopping_services_hr = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 32), 'time_shopping_services'].mean()
mean_children_hr = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 32), 'time_children'].mean()
mean_management_hr =  old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 32), 'time_371'].mean()
mean_other_care_hr = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 32), 'time_other_care'].mean()

y_axis_hr = [mean_food_hr, mean_care_adult_hr, mean_cleaning_hr, mean_pets_hr, mean_laundry_hr, 
            mean_gardening_hr, mean_handy_hr, mean_shopping_services_hr, mean_children_hr, 
            mean_management_hr, mean_other_care_hr]

#hommes en emploi
mean_food_he = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 10), 'time_food_dishes'].mean()
mean_care_adult_he = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 10), 'time_care_adult'].mean()
mean_cleaning_he = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 10), 'time_cleaning'].mean()
mean_pets_he = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 10), 'time_pets'].mean()
mean_laundry_he = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 10), 'time_laundry'].mean()
mean_gardening_he = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 10), 'time_gardening'].mean()
mean_handy_he = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 10), 'time_handy'].mean()
mean_shopping_services_he = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 10), 'time_shopping_services'].mean()
mean_children_he = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 10), 'time_children'].mean()
mean_management_he =  old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 10), 'time_371'].mean()
mean_other_care_he = old.loc[(old['inc1'] == 1) & (old['ind17_1'] == 10), 'time_other_care'].mean()

y_axis_he = [mean_food_he, mean_care_adult_he, mean_cleaning_he, mean_pets_he, mean_laundry_he, 
            mean_gardening_he, mean_handy_he, mean_shopping_services_he, mean_children_he, 
            mean_management_he, mean_other_care_he]

#plot
colors = ['#E6194B', '#3CB44B', '#FFE119', '#4363D8', '#F58231', '#911EB4', '#46F0F0', '#F032E6', 
          '#BCBC8F', '#E6BEFF', '#9A6324']

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
ax1 = axes[0, 0]
ax2 = axes[0, 1]
ax3 = axes[1, 0]
ax4 = axes[1, 1]
plt.subplots_adjust(hspace=1, wspace=0.4)
#femmes retraités
ax3.bar(taches, y_axis_fr, width=0.8, color= colors)
ax3.set_title("Femmes retraitées")
ax3.set_ylabel("Temps moyen (en minutes/jour)")
plt.setp(ax3.get_xticklabels(), rotation=70, ha="right")
#femmes en emploi
ax1.bar(taches, y_axis_fe, width=0.8, color= colors)
ax1.set_ylim(ax3.get_ylim())
ax1.set_title("Femmes en emploi")
ax1.set_ylabel("Temps moyen (en minutes/jour)")
plt.setp(ax1.get_xticklabels(), rotation=70, ha="right")
#hommes en emploi
ax2.bar(taches, y_axis_he, width=0.8, color= colors)
ax2.set_ylim(ax3.get_ylim())
ax2.set_title("Hommes en emploi")
ax2.set_ylabel("Temps moyen (en minutes/jour)")
plt.setp(ax2.get_xticklabels(), rotation=70, ha="right")

#hommes retraités
ax4.bar(taches, y_axis_hr, width=0.8, color= colors)
ax4.set_ylim(ax3.get_ylim())
ax4.set_title("Hommes retraités")
ax4.set_ylabel("Temps moyen (en minutes/jour)")
plt.setp(ax4.get_xticklabels(), rotation=70, ha="right")

fig.suptitle("Temps consacré aux tâches domestiques par genre et statut", y=1, fontsize=16)
plt.show()





















