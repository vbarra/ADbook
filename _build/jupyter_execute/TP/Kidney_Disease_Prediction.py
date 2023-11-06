#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# For Filtering the warnings
import warnings
warnings.filterwarnings('ignore')


# # Jeu de données
# L'objectif de ce jeu de données est de prédire une maladie rénale à partir de 25 mesures.
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
# 25. Classe (malade : ckd, pas malade notckd
#  	25.Class (nominal)		
# 		class - (ckd,notckd)

# The data needs cleaning: in that it has NaNs and the numeric features need to be forced to floats. Basically, we were instructed to get rid of ALL ROWS with Nans, with no threshold - meaning, any row that has even one NaN, gets deleted.

# In[2]:


# gestion données manquantes + normalisation + sélection de variables
# classification (25e arg)
# peut on faire de la régression sur le 14 ?


# In[3]:


data = pd.read_csv('kidney_disease.csv')


# In[4]:


data.head()


# ckd=chronic kidney disease

# In[5]:


data.info()


# In[6]:


data.classification.unique()


# In[7]:


data.classification=data.classification.replace("ckd\t","ckd") 


# In[8]:


data.classification.unique()


# In[9]:


data.drop('id', axis = 1, inplace = True)


# In[10]:


data.head()


# In[11]:


data['classification'] = data['classification'].replace(['ckd','notckd'], [1,0])


# In[12]:


data.head()


# In[13]:


data.isnull().sum()


# In[14]:


df = data.dropna(axis = 0)
print(f"Before dropping all NaN values: {data.shape}")
print(f"After dropping all NaN values: {df.shape}")


# In[15]:


df.head()


# In[16]:


df.index = range(0,len(df),1)
df.head()


# In[17]:


for i in df['wc']:
    print(i)


# In[18]:


df['wc']=df['wc'].replace(["\t6200","\t8400"],[6200,8400])


# In[19]:


for i in df['wc']:
    print(i)


# In[20]:


df.info()


# In[21]:


df['pcv']=df['pcv'].astype(int)
df['wc']=df['wc'].astype(int)
df['rc']=df['rc'].astype(float)
df.info()


# In[22]:


object_dtypes = df.select_dtypes(include = 'object')
object_dtypes.head()


# In[23]:


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


# In[24]:


df=df.replace(dictonary)


# In[25]:


df.head()


# In[26]:


import seaborn as sns
plt.figure(figsize = (20,20))
sns.heatmap(df.corr(), annot = True, fmt=".2f",linewidths=0.5)


# In[27]:


df.corr()


# In[28]:


X = df.drop(['classification', 'sg', 'appet', 'rc', 'pcv', 'hemo', 'sod'], axis = 1)
y = df['classification']


# In[29]:


X.columns


# In[30]:


from sklearn.model_selection import train_test_split


# In[31]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)


# In[32]:


from sklearn.ensemble import RandomForestClassifier


# In[33]:


model = RandomForestClassifier(n_estimators = 20)
model.fit(X_train, y_train)


# In[34]:


from sklearn.metrics import confusion_matrix, accuracy_score


# In[35]:


confusion_matrix(y_test, model.predict(X_test))


# In[36]:


print(f"Accuracy is {round(accuracy_score(y_test, model.predict(X_test))*100, 2)}%")


# In[37]:


import pickle
pickle.dump(model, open('kidney.pkl', 'wb'))


# In[ ]:




