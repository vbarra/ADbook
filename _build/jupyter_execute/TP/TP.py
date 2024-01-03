#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')


# # Jeu de données
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


data = pd.read_csv('data.csv')


# In[23]:


data.head()


# In[24]:


data.info()


# ## Analyse exploratoire

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
# Votre premier travail consiste donc à régler tous ces points pour obtenir un fichier de données propre. Vous devez donc mettre en jeu des techniques d'[imputation](https://scikit-learn.org/stable/modules/impute.html), de [normalisation](https://scikit-learn.org/stable/modules/preprocessing.html) ou encore de gestion de [données aberrantes](https://scikit-learn.org/stable/modules/outlier_detection.html)

# ### Analyse univariée / bivariée

# ### Sélection / extraction de variables

# ### Problème de classification
# Le premier problème qui nous intéresse est de pouvoir construire un modèle de classification non supervisée et de comparer ses résultats à la "vraie" classification proposée dans le dernière colonne.
# Vous construirez donc des modèles de classification à partir des éléments vus en cours (https://scikit-learn.org/stable/modules/clustering.html), optimiserez les paramètres de ces algorithmes (nombre de classes dans les k-means par exemple) et évaluerez leur performance.

# ### Problème de régression
# Le second problème conerne la régression d'une ou plusieurs des colonnes en fonction des autres régression. Vous vous intéresserez donc à :
# - la régression simple de la colonne 12 en fonction des autres colonnes
# - la régression multiple des colonnes 16, 17 et 18 en fonction des autres colonnes
#  

# In[25]:


data.classification.unique()


# In[26]:


data.classification=data.classification.replace("ckd\t","ckd") 


# In[27]:


data.classification.unique()


# In[28]:


data.drop('id', axis = 1, inplace = True)


# In[29]:


data.head()


# In[30]:


data['classification'] = data['classification'].replace(['ckd','notckd'], [1,0])


# In[31]:


data.head()


# In[32]:


data.isnull().sum()


# In[33]:


df = data.dropna(axis = 0)
print(f"Before dropping all NaN values: {data.shape}")
print(f"After dropping all NaN values: {df.shape}")


# In[34]:


df.head()


# In[35]:


df.index = range(0,len(df),1)
df.head()


# In[36]:


for i in df['wc']:
    print(i)


# In[37]:


df['wc']=df['wc'].replace(["\t6200","\t8400"],[6200,8400])


# In[38]:


for i in df['wc']:
    print(i)


# In[39]:


df.info()


# In[40]:


df['pcv']=df['pcv'].astype(int)
df['wc']=df['wc'].astype(int)
df['rc']=df['rc'].astype(float)
df.info()


# In[41]:


object_dtypes = df.select_dtypes(include = 'object')
object_dtypes.head()


# In[42]:


dictonary = {
        "rbc": {
        "abnormal":1,
        "normal": 0,
    },
        "pc":{
        "abnormal":1,
        "normal": 0,
    },
        "pcc":{
        "present":1,
        "notpresent":0,
    },
        "ba":{
        "notpresent":0,
        "present": 1,
    },
        "htn":{
        "yes":1,
        "no": 0,
    },
        "dm":{
        "yes":1,
        "no":0,
    },
        "cad":{
        "yes":1,
        "no": 0,
    },
        "appet":{
        "good":1,
        "poor": 0,
    },
        "pe":{
        "yes":1,
        "no":0,
    },
        "ane":{
        "yes":1,
        "no":0,
    }
}


# In[43]:


df=df.replace(dictonary)


# In[44]:


df.head()


# In[45]:


import seaborn as sns
plt.figure(figsize = (20,20))
sns.heatmap(df.corr(), annot = True, fmt=".2f",linewidths=0.5)


# In[46]:


df.corr()


# In[47]:


X = df.drop(['classification', 'sg', 'appet', 'rc', 'pcv', 'hemo', 'sod'], axis = 1)
y = df['classification']


# In[48]:


X.columns


# In[49]:


from sklearn.model_selection import train_test_split


# In[50]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)


# In[51]:


from sklearn.ensemble import RandomForestClassifier


# In[52]:


model = RandomForestClassifier(n_estimators = 20)
model.fit(X_train, y_train)


# In[53]:


from sklearn.metrics import confusion_matrix, accuracy_score


# In[54]:


confusion_matrix(y_test, model.predict(X_test))


# In[55]:


print(f"Accuracy is {round(accuracy_score(y_test, model.predict(X_test))*100, 2)}%")


# In[56]:


import pickle
pickle.dump(model, open('kidney.pkl', 'wb'))


# In[ ]:




