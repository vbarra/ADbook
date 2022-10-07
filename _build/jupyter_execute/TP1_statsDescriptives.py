#!/usr/bin/env python
# coding: utf-8

# # TP Statistiques descriptives
# 

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# ## Statistique monovariée
# 
# Le tableau suivant donne les notes (sur 10) obtenues à un examen par un groupe d'élèves. 
# $\begin{array}{c|c}
# Nom & Note \\
#   \hline
# Alain &6\\
# Raymond &5\\
# Jean-Joseph &9\\
# Eglantine &3\\
# Isidore &3\\
# Mauricette &1\\
# Sylvère &9\\
# Pétunia &6\\
# Philemon &5\\
# Archibald &6\\
# Théodule &5\\
# Marguerite &6\\
# Proserpine &5\\
# Alphonse &7\\
# Géraud &5\\
# Basile &10\\
# Fantine &2\\
# Sidonie &1\\
# Thérèse &1\\
# Yves &1
# \end{array}$

# In[2]:


notes = np.array([6, 5, 9, 3, 3, 1, 9, 6, 5, 6, 5, 6, 5, 7, 5, 10, 2, 1, 1, 1])


# Donner les différentes modalités possibles

# In[3]:


#TODO


# Calculer les effectifs cumulés de chaque modalité. 

# In[4]:


#TODO


# Calculer les effectifs par modalité, les fréquences et les fréquences cumulées des notes

# In[5]:


#TODO



# Représenter avec un (ou plusieurs) graphique(s) adapté(s) la répartition des notes

# In[6]:


#TODO


# En déduire (et afficher) la fonction de répartition empirique des notes.

# In[7]:


#TODO


# En utilisant la fonction [boxplot](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.boxplot.html), tracer la boîte à moustache des notes. 

# In[8]:


#TODO


# Calculer les éléments caractéristiques (indicateurs de tendance, de dispersion) des notes.

# In[9]:


#TODO


# ## Statistique bivariée
# 
# ### Cas de variables quantitatives
# 
# On donne le fichier de données suivant

# In[10]:


X=np.loadtxt('./bivariee.txt',delimiter=',')
plt.figure(figsize=(12,8))

plt.subplot(2,2,2)
plt.plot(X[:,0],X[:,1],'ob')
plt.axis([0,1,0,2])
plt.title('Nuage de points')
plt.xlabel('X')
plt.ylabel('Y')

plt.subplot(4,2,6)
plt.subplots_adjust(hspace=0.4, wspace=0.3)
plt.boxplot(X[:,0],0,'+',0)
plt.axis([0,1,0.75,1.25])
plt.title('Boite à moustache pour X')

plt.subplot(2,4,2)
plt.boxplot(X[:,1],0,'+',1)
a = plt.axis()
plt.axis([a[0], a[1], 0, 2])
plt.title('Boite à moustache pour Y')
plt.show()


# Calculer la covariance entre les deux variables. Conclusion ?

# In[11]:


#TODO


# Calculer la corrélation entre les deux variables. Conclusion ?

# In[12]:


#TODO


# ### Cas de variables qualitatives
# 
# On s'intéresse à un fichier décrivant la réussite d'étudiants en mathématiques (données décrites [ici](https://archive.ics.uci.edu/ml/datasets/Student+Performance)) 

# In[13]:


import pandas as pd
result = pd.read_csv('./student.csv',delimiter=';')


# In[19]:


print(result)


# On regarde les deux premières colonnes des données (code de l'école et genre de l'étudiant)

# In[20]:


x = result.values[:,0]
g = result.values[:,1]


# Construire le tableau de contingence de ces deux variables

# In[21]:


#TODO


# Construire le tableau théorique associé en supposant l’indépendance des deux variables.

# In[22]:


#TODO


# Calculer la distance du $\chi^2$ entre les variables $x$ et $g$. Ces deux variables sont elles liées ou sont elles indépendantes ?

# In[23]:


#TODO


# On s’intéresse maintenant à la septième variable $ne$ qui code le niveau d’éducation des mères de la manière suivante :
# - 0 - none,
# - 1 - primary education (4th grade),
# - 2 - 5th to 9th grade,
# - 3 - secondary education
# - 4 - higher education
# 
# Récupérer cette variable et calculer les effectifs de chacune des modalités. Calculer le tableau de contingence  entre les variables $x$ et $ne$

# In[24]:


#TODO


# In[25]:


#TODO


# In[26]:





# Les effectifs étant trop faibles, fusionner les deux premières colonnes

# In[27]:


#TODO


# Construire le tableau théorique, en supposant l'indépendance des variables

# In[28]:


#TODO


# Calculer la distance du $\chi^2$ entre les variables $x$ et $ne$. Ces deux variables sont elles liées ou sont elles indépendantes ? Que peut on en déduire sur le choix de l’école ?

# In[29]:


#TODO

