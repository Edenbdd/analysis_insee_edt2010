#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 11:31:40 2024

@author: eden
"""
import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
df = pd.read_csv("/home/eden/Documents/Mémoire/final/pref/tempspref.csv")

# Convertir la colonne 'sexe' en numérique
df['sexe'] = pd.to_numeric(df['sexe'], errors='coerce')

# Liste des catégories dans l'ordre souhaité pour l'affichage
ordered_categories = ['gestion', 'cleaning',  'adult', 'linge', 'travail',
         'shop', 'trajets_et_autres', 'food', 'soins_personnels', 
         'children_care',  'jardin', 'brico',
        'repos',  'repas', 'loisirs', 'children_play', 'pets',
]

# Dictionnaire de correspondance entre les noms de catégories et les étiquettes
label_dict = {
    'repos': 'Repos',
    'soins_personnels': 'Soins et hygiène',
    'repas': 'Repas',
    'travail': 'Activité ¨professionelle',
    'loisirs': 'Loisirs',
    'food': 'Préparation des repas',
    'adult': 'Soins aux adultes',
    'cleaning': 'Ménage/Nettoyage',
    'pets': 'Animaux',
    'linge': 'Linge',
    'jardin': 'Jardinage',
    'brico': 'Bricolage',
    'shop': 'Courses',
    'children_care': 'Soins aux enfants',
    'children_play': 'Activités avec enfants',
    'gestion': 'Gestion du foyer',
    'trajets_et_autres': 'Trajets et autres'
}

# Créer la liste des étiquettes dans l'ordre des catégories
labels = [label_dict[cat] for cat in ordered_categories]

# Sélectionner les colonnes de moyennes pour ces catégories
mean_columns = [f'mean_{cat}' for cat in ordered_categories]

# Convertir toutes les colonnes de moyennes en numérique
for col in mean_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Calculer les moyennes pour chaque catégorie par genre
means_hommes = df[df['sexe'] == 1][mean_columns].mean()
means_femmes = df[df['sexe'] == 2][mean_columns].mean()

# Créer le graphique
plt.figure(figsize=(12, len(ordered_categories)*0.5))
plt.style.use('ggplot')

# Créer les barres pour chaque genre
y_pos = range(len(ordered_categories))
plt.barh(y_pos, means_hommes, height=0.4, label='Hommes', color='#90EE90', alpha=0.8)
plt.barh([y + 0.4 for y in y_pos], means_femmes, height=0.4, label='Femmes', color='#003366', alpha=0.8)


# Configurer les étiquettes de l'axe y avec les nouveaux labels
plt.yticks([y + 0.2 for y in y_pos], labels)

# Personnaliser le graphique
plt.xlabel('Satisfaction moyenne (-3 à +3)')
plt.title('Satisfaction moyennne par catégorie d\'activité en fonction du genre')
plt.legend()

# Ajuster la mise en page
plt.tight_layout()

# Afficher le graphique
plt.show()



