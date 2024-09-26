#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:42:35 2024

@author: eden
"""
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
from statsmodels.iolib.summary2 import summary_col

# Charger les données
df = pd.read_csv("/home/eden/Documents/Mémoire/final/reg/tablereg.csv")

# Variable dépendante (y)
y = df['coeff_res_tot']

#OUTLIERS#############################################################################################"
def grubbs_test(data, alpha=0.05):
    n = len(data)
    mean = np.mean(data)
    std = np.std(data, ddof=1)
    
    G = max(abs(data - mean)) / std
    
    t_value = stats.t.ppf(1 - alpha / (2*n), n-2)
    G_critical = ((n-1) * np.sqrt(t_value**2 / (n-2 + t_value**2))) / np.sqrt(n)
    
    p_value = n * (1 - stats.t.cdf(G * np.sqrt(n**2 - 2*n) / np.sqrt(n**2 - 2*n - n*G**2), n-2))
    
    return G, G_critical, p_value

def grubbs_test_outliers(data, alpha=0.05):
    outliers = []
    data_copy = data.copy()
    while True:
        G, G_critical, p_value = grubbs_test(data_copy)
        if G <= G_critical:
            break
        outlier_index = np.argmax(np.abs(data_copy - np.mean(data_copy)))
        outliers.append(data_copy.iloc[outlier_index])
        data_copy = data_copy.drop(data_copy.index[outlier_index])
    return outliers

outliers = grubbs_test_outliers(df['coeff_res_tot'])

plt.figure(figsize=(10, 6))
plt.scatter(df.index, df['coeff_res_tot'], alpha=0.5)
outlier_indices = df.index[df['coeff_res_tot'].isin(outliers)]
plt.scatter(outlier_indices, df.loc[outlier_indices, 'coeff_res_tot'], color='red', s=50)
plt.title('Scatter Plot with Grubbs Test Outliers')
plt.xlabel('Index')
plt.ylabel('coeff_res_tot')
plt.show()

print(f"Number of outliers detected: {len(outliers)}")
print(f"Outlier values: {outliers}")

#removing outliers
# Create a boolean mask for non-outlier rows
mask = ~df['coeff_res_tot'].isin(outliers)

# Create a new DataFrame without the outliers
df = df[mask].copy()

# Reset the index if needed
df = df.reset_index(drop=True)

#CALCUL DES CORRELATIONS POUR TROUVER LES VALEURS DE CONTROLE####################################
dependent_var = 'coeff_res_tot'
potential_controls = ['handi_hom', 'handi_fem', 'handi_both', 'nbenfhors', 'nbenf', 'sup_long_hom', 
                      'sup_court_hom', 'cap_hom', 'none_hom', 'sup_long_fem', 'sup_court_fem', 'cap_fem', 
                      'none_fem', 'agri_fem', 'art_fem', 'cadre_fem', 'inact_fem', 'agri_hom', 'art_hom', 
                      'cadre_hom']

correlations = {}
for var in potential_controls:
    corr, p_value = stats.pearsonr(df[dependent_var], df[var])
    correlations[var] = {'correlation': corr, 'p_value': p_value}

# Sort by absolute correlation value
sorted_correlations = sorted(correlations.items(), key=lambda x: abs(x[1]['correlation']), reverse=True)

print("Correlations with dependent variable:")
for var, stat in sorted_correlations:
    print(f"{var}: correlation = {stat['correlation']:.4f}, p-value = {stat['p_value']:.4f}")

#vizualization

# Extract variable names, correlation coefficients, and p-values
variables = [item[0] for item in sorted_correlations]
correlations = [abs(item[1]['correlation']) for item in sorted_correlations]
p_values = [item[1]['p_value'] for item in sorted_correlations]

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 12))  # Adjusted figure size for better visibility

# Set the height of each bar and the positions of the bars
height = 0.35
y = np.arange(len(variables))

# Create the horizontal bars
corr_bars = ax.barh(y - height/2, correlations, height, label='Correlation', color='blue')
p_bars = ax.barh(y + height/2, p_values, height, label='p-value', color='red')

# Customize the plot
ax.set_title('Correlation Coefficients and p-values with Dependent Variable', fontsize=16)
ax.set_ylabel('Control Variables', fontsize=12)
ax.set_xlabel('Value', fontsize=12)
ax.set_yticks(y)
ax.set_yticklabels(variables)
ax.legend()

# Add value labels on the end of each bar
def autolabel(rects):
    for rect in rects:
        width = rect.get_width()
        ax.annotate(f'{width:.3f}',
                    xy=(width, rect.get_y() + rect.get_height() / 2),
                    xytext=(3, 0),  # 3 points horizontal offset
                    textcoords="offset points",
                    ha='left', va='center', fontsize=8)

autolabel(corr_bars)
autolabel(p_bars)

# Invert y-axis to have the first variable at the top
ax.invert_yaxis()

# Adjust layout and display the plot
plt.tight_layout()
plt.show()


#TEST de WALD EMPLOI FEMININ###############################################################""
#Fit the full model
X = sm.add_constant(df[['handi_hom', 'handi_fem', 'handi_both', 'nbenfhors', 'nbenf', 'sup_long_hom', 
                      'sup_court_hom', 'cap_hom', 'none_hom', 'sup_long_fem', 'sup_court_fem', 'cap_fem', 
                      'none_fem', 'agri_fem', 'art_fem', 'cadre_fem', 'inact_fem', 'agri_hom', 'art_hom', 
                      'cadre_hom']])

y = df['coeff_res_tot']

model = sm.OLS(y, X).fit()

# Define the variables you want to test (e.g., women's employment dummies, emp_fem est la valeur de référence)
variables_to_test = ['agri_fem', 'art_fem', 'cadre_fem', 'inact_fem']

# Get the indices of these variables in the X matrix
indices = [list(X.columns).index(var) for var in variables_to_test]

# Create a constraint matrix
num_vars = len(model.params)
constraint_matrix = np.zeros((len(variables_to_test), num_vars))
for i, idx in enumerate(indices):
    constraint_matrix[i, idx] = 1

# Perform the Wald test
wald_test = model.wald_test(constraint_matrix, use_f=True, scalar=True)

print(wald_test.summary())

#TEST DE WALD EMPLOI MASCULIN##########################################################################

# Define the variables you want to test (e.g., men's employment dummies, emp_hom est la valeur de référence)
variables_to_test = ['agri_hom', 'art_hom', 'cadre_hom']

# Get the indices of these variables in the X matrix
indices = [list(X.columns).index(var) for var in variables_to_test]

# Create a constraint matrix
num_vars = len(model.params)
constraint_matrix = np.zeros((len(variables_to_test), num_vars))
for i, idx in enumerate(indices):
    constraint_matrix[i, idx] = 1

# Perform the Wald test
wald_test = model.wald_test(constraint_matrix, use_f=True, scalar=True)

print(wald_test.summary())

#TEST DE WALD HANDICAP##########################################################################

#handi_none est la valeur de référence
variables_to_test = ['handi_hom', 'handi_fem', 'handi_both']
# Get the indices of these variables in the X matrix
indices = [list(X.columns).index(var) for var in variables_to_test]

# Create a constraint matrix
num_vars = len(model.params)
constraint_matrix = np.zeros((len(variables_to_test), num_vars))
for i, idx in enumerate(indices):
    constraint_matrix[i, idx] = 1

# Perform the Wald test
wald_test = model.wald_test(constraint_matrix, use_f=True, scalar=True)

print(wald_test.summary())

#HETEROSCEDASTICITE########################################################
from statsmodels.stats.diagnostic import het_breuschpagan

_, p_value, _, _ = het_breuschpagan(model.resid, model.model.exog)
print(f"Test de Breusch-Pagan p-value: {p_value}")

import matplotlib.pyplot as plt

plt.scatter(model.fittedvalues, model.resid)
plt.xlabel("Valeurs prédites")
plt.ylabel("Résidus")
plt.title("Résidus vs Valeurs prédites")
plt.show()

####ERREUR NON NORMALES####################
_, p_value = stats.shapiro(model.resid)
print(f"Test de Shapiro-Wilk p-value: {p_value}")


fig = sm.qqplot(model.resid, line='45')
plt.title("Q-Q Plot des résidus")
plt.show()

#REGRESSION####################################################################################

# Étape 1 : Préparer les variables indépendantes et de contrôle
X = df[['ret_hom', 'ret_fem', 'ret_both',  # Variables indépendantes
        'agri_fem', 'art_fem', 'cadre_fem', 'inact_fem',  # Emploi féminin
        'agri_hom', 'art_hom', 'cadre_hom',  # Emploi masculin
        'handi_fem', 'handi_both', 'handi_hom']]  # Handicap

# Étape 2 : Ajouter une constante à X
X = sm.add_constant(X)

#Etape 3: modèle robust
model_robust = sm.OLS(y, X).fit(cov_type='HC3')

# Étape 5 : Afficher les résultats

print(model_robust.summary())

# Étape 6 : Extraire les coefficients et les p-values
coefficients = model.params
p_values = model.pvalues

# Étape 7 : Afficher les coefficients et les p-values pour les variables principales
for var in ['ret_hom', 'ret_fem', 'ret_both']:
    print(f"{var}: coefficient = {coefficients[var]:.4f}, p-value = {p_values[var]:.4f}")

print(f"R-squared: {model.rsquared:.4f}")

#MISE EN PAGE#######################################################

# Assurez-vous que ces lignes sont correctes et que df, y sont bien définis
X = df[['ret_hom', 'ret_fem', 'ret_both',  # Variables indépendantes
        'agri_fem', 'art_fem', 'cadre_fem', 'inact_fem',  # Emploi féminin
        'agri_hom', 'art_hom', 'cadre_hom',  # Emploi masculin
        'handi_fem', 'handi_both', 'handi_hom']]  # Handicap

X = sm.add_constant(X)
model_robust = sm.OLS(y, X).fit(cov_type='HC3')

# Créer un DataFrame avec les résultats
results_df = pd.DataFrame({
    'Coefficient': model_robust.params,
    'Std.Error': model_robust.bse,
    'z': model_robust.tvalues,
    'P>|z|': model_robust.pvalues
})

# Formater les valeurs
for col in results_df.columns:
    results_df[col] = results_df[col].apply(lambda x: f"{x:.4f}")

# Ajouter des étoiles pour la significativité
def add_stars(p_value):
    p = float(p_value)
    if p <= 0.01:
        return p_value + '***'
    elif p <= 0.05:
        return p_value + '**'
    elif p <= 0.1:
        return p_value + '*'
    return p_value

results_df['P>|z|'] = results_df['P>|z|'].apply(add_stars)

# Ajouter des informations supplémentaires
additional_info = pd.DataFrame({
    'Coefficient': [f"{model_robust.nobs}", f"{model_robust.rsquared:.4f}"],
    'Std.Error': ['', ''],
    'z': ['', ''],
    'P>|z|': ['', '']
}, index=['Observations', 'R-squared'])

results_df = pd.concat([results_df, additional_info])

# Afficher le tableau
print(results_df.to_string())

# Optionnel : sauvegarde en CSV pour faciliter le copier-coller
results_df.to_csv('regression_results_robust.csv')

# Afficher les coefficients et les p-values pour les variables principales
main_vars = ['ret_hom', 'ret_fem', 'ret_both']
for var in main_vars:
    coef = results_df.loc[var, 'Coefficient']
    p_val = results_df.loc[var, 'P>|z|']
    print(f"{var}: coefficient = {coef}, p-value = {p_val}")

print(f"R-squared: {model_robust.rsquared:.4f}")

