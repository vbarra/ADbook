#!/usr/bin/env python
# coding: utf-8

# # TP long

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')


# ## Jeu de données
# L'objectif de ce jeu de données est de prédire une maladie rénale à partir de mesures effectuées sur des individus.
# Les données ont été recueillies sur une période de deux mois en Inde et comportent 25 caractéristiques
# 1. Age(en années)
# 2. Pression sanguine (mm/Hg)
# 3. Densité (qualitative ordinale, parmi sg - (1.005,1.010,1.015,1.020,1)
# 4. Albumine (qualitative ordinale, parmi (0,1,2,3,4,5))
# 5. Sucre  (qualitative ordinale, parmi (0,1,2,3,4,5))
# 6. Globules rouge (qualitative nominale parmi (normal,abnormal))
# 7. Cellules Pus (qualitative nominale parmi (normal,abnormal))
# 8. Amas de cellules Pus (qualitative nominale parmi (présent,absent))
# 9. Bactérie (qualitative nominale parmi (présent,absent))
# 10. Glucose (mgs/dl)
# 11. Urée dans le sang (mgs/dl)
# 12. Créatinine (mgs/dl)
# 13. Sodium (mEq/L)
# 14. Potassium (mEq/L)
# 15. Hémoglobine (gms)
# 16. Volume cellulaire
# 17. Comptage globules blancs
# 18. Comptage globules rouge
# 19. Hypertension (qualitative nominale parmi (oui,non))
# 20. Diabète (qualitative nominale parmi (oui,non))
# 21. Maladie coronarienne (qualitative nominale parmi (oui,non))
# 22. Appetit (qualitative nominale parmi (normal,pauvre))
# 23. Oedeme (qualitative nominale parmi (oui,non))
# 24. Anémie (qualitative nominale parmi (oui,non))
# 25. Classe (malade : ckd, pas malade : notckd)d)

# In[2]:


data = pd.read_csv('../data/dataTP.csv')


# In[3]:


data.head()


# In[4]:


data.info()


# ## 1. Analyse exploratoire

# ### Nettoyage des données
# Les données, comme tout jeu de données réel, comporte de nombreuses imperfections :
# - données manquantes (Nan) dans les données
# - erreurs de lecture du fichier initial dans plusieurs colonnes (un '\t' est encore présent, comme par exemple dans la colonne `Classe`('ckd\t' à la place de 'ckd'))
# - possiblement données aberrantes.
# 
# Il est de plus nécessaire de faire les pré-traitements habituels pour assurer une analyse de données pertinente :
# - gestion des variables qualitatives
# - normalisation
# - gestion des variables entières / flottantes
# 
# Votre premier travail consiste donc à régler tous ces points pour obtenir un fichier de données propre. Vous devez donc mettre en jeu des techniques d'[imputation](https://scikit-learn.org/stable/modules/impute.html), de [normalisation](https://scikit-learn.org/stable/modules/preprocessing.html) ou encore de gestion de [données aberrantes](https://scikit-learn.org/stable/modules/outlier_detection.html).

# ### 1.1. Analyse univariée / bivariée
# Vous explorerez ici les caractéristiques des variables (statistique univariée) et des relations entre couples de variables (statistiques bivariée) :
# - [distribution des variables](https://seaborn.pydata.org/generated/seaborn.distplot.html), [boxplot](https://seaborn.pydata.org/generated/seaborn.boxplot.html),...
# - [corrélations](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html), [relations entre variables](sns.PairGrid),...
# 
# Vous en déduirez des actions à prendre sur ces variables (suppression d'une colonne, application d'une fonction mathématique à une colonne,...)

# ### 1.2. Sélection / extraction de variables
# #### 1.2.1. Sélection de variables
# Vous appliquerez ici les méthodes classiques de [sélection de variables](https://scikit-learn.org/stable/modules/feature_selection.html) sur les variables (éventuellement pré traitées par le point 1.1.) pour en extraire un jeu de données à $d<<25$ variables initiales à analyser.
# #### 1.2.2. Extraction de variable
# Vous analyserez le jeu de données (éventuellement pré traitées par le point 1.1.) à l'aide d'une [ACP](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html) et en déduirez $d<<25$ nouvelles variables à analyser

# ### 2. Problème de classification
# Le premier problème qui nous intéresse est de pouvoir construire un modèle de classification non supervisée et de comparer ses résultats à la "vraie" classification proposée dans le dernière colonne.
# Vous construirez donc des modèles de [classification](https://scikit-learn.org/stable/modules/clustering.html) à partir des éléments vus en cours , optimiserez les paramètres de ces algorithmes (nombre de classes dans les k-means par exemple) et évaluerez leur performance.
# Vous travaillerez d'une part sur les variables retenues par sélection de variables, et d'autre part sur les variables calculées par extraction de variables. Vous comparerez les résultats de classification obtenus.

# ### 3. Problème de régression
# Le second problème concerne la [régression linéaire](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html) d'une ou plusieurs des colonnes en fonction des autres régression. Vous vous intéresserez donc à :
# - la régression simple de la colonne 12 en fonction des autres colonnes
# - la régression multiple des colonnes 16, 17 et 18 en fonction des autres colonnes
#  
