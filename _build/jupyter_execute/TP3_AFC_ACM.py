#!/usr/bin/env python
# coding: utf-8

# In[1]:


try:
    import seaborn numpy matplotlib pandas mca 
except ModuleNotFoundError: 
    get_ipython().system('pip3 install --quiet seaborn numpy matplotlib pandas mca')


# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# # TP AFC / ACM

# # Exercice 1 : Analyse Factorielle des Correspondances
# Le fichier de données est un tableau d'effectifs, croisant l'origine sociale des sondés (CSP, version simplifiée) avec les médias d'informations utilisés

# In[80]:


media = pd.read_table("./data/mediaCSP.txt", header=0, index_col=0, delimiter="\t", encoding="utf-8")
print(media)


# ## ===== Votre travail : =====
# Vous avez à disposition un fichier ca.py, permettant de réaliser les calculs relatifs à une analyse factorielle des correspondances. L'objectif est de répondre aux questions suivantes : 
# - Quelle est la structure des moyens d'information choisis selon la CSP ? (profils lignes).
# - La structure est-elle différente d’une CSP à l’autre ?
# - Les médias sont-ils différents en termes de CSP ? (profils colonnes)
# - Existe-t-il des relations entre CSP et médias  (des CSP ont-elles une préférences pour certains médias ? Certains médias attirent-ils des catégories particulières de CSP ?)

# ### Analyse Factorielle des correspondances
# 
# On créé une instance de l'objet CA, que l'on applique sur le tableau des valeurs

# In[81]:


from ca import CA
afc = CA(row_labels=media.index,col_labels=media.columns)
afc.fit(media.values)


# ### Valeurs propres
# En utilisant l'attribut $eig\_$ et la fonction plot_eigenvalues (ligne 294 du fichier $base.py$),afficher et interpréter les valeurs propres issues de l'analyse factorielle (nombre, contribution des facteurs...)

# In[82]:


#TODO


# In[83]:


#TODO


# 

# ### Analyse des profils lignes
# On affiche ici, pour chaque modalité ligne, la distribution des individus colonnes

# In[84]:


data = np.apply_along_axis(arr=media.values,axis=1,func1d=lambda x:x/np.sum(x))
data_cum = data.cumsum(axis=1)
labels = list(media.index)
colors = plt.get_cmap('RdYlGn')(np.linspace(0.15, 0.85, data.shape[1]))

fig, ax = plt.subplots(figsize=(9.2, 5))
ax.invert_yaxis()
ax.xaxis.set_visible(False)
ax.set_xlim(0, np.sum(data, axis=1).max())

for i, (colname, color) in enumerate(zip(list(afc.col_labels_short_.values), colors)):
    widths = data[:,i]
    starts = data_cum[:,i] - widths
    ax.barh(labels, widths, left=starts, height=0.5,label=colname, color=color)
    xcenters = starts + widths / 2

    r, g, b, _ = color
    text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
    for y, (x, c) in enumerate(zip(xcenters, widths)):

        ax.text(x, y, str(float(round(c,2))), ha='center', va='center',
                    color=text_color)
ax.legend(ncol=len(afc.col_labels_short_.values), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')

plt.show()


# En utilisant l'attribut row\_coord\_, afficher les coordonnées des modalités lignes par facteur. Calculer la moyenne pondérée et la variance des coordonnées des modalités lignes sur le premier facteur. Qu'obtenez-vous ?

# In[85]:


#TODO


# In[86]:


#TODO


# Moyenne :  1.3877787807814457e-17  égale à 0
# 
# Variance :  0.013857286816774693 égale à la valeur propre associée

# En utilisant la fonction mapping\_row (ligne 389, ficher base.py), représenter les individus lignes dans le premier plan factoriel (qui restitue 94.5\% de l'information disponible). Analyser le résultat

# In[87]:


#TODO


# ### Calcul de la distance du $\chi^2$
# La distance du $\chi^2$ entre les modalités lignes dans l’espace initial devient distance euclidienne dans l’espace factoriel. Comme en ACP, la restitution est parfaite lorsque tous les facteurs sont pris en compte, et approchée si une partie est utilisée. La précision dépend alors d’une part de la qualité de restitution du repère factoriel choisi, d’autre part de la qualité de représentation des modalités impliquées dans le calcul (les $cos^2$).

# In[88]:


f,ax = plt.subplots(1, 2,figsize=(10,4))

for l in range(0,2):

    # Distances entre modalités sur le l-eme facteur
    plt.subplot(1,2,l+1)
    distPairesLigF1 = np.zeros(shape=(data.shape[l],data.shape[l]))
    for i in range(data.shape[l]-1):
        for j in range(i+1,data.shape[l]):
            distPairesLigF1[i,j] = np.sum((afc.row_coord_[i,0]-afc.row_coord_[j,0])**2) 
    sns.heatmap(distPairesLigF1,vmin=0,vmax=np.max(distPairesLigF1),linewidth=0.1,cmap= 'Greens',xticklabels=media.index,yticklabels=media.index)
    plt.title("Distance sur le facteur "+str(l+1))
f.subplots_adjust(wspace=0.9)


# ### Analyse des profils colonnes
# Faire la même analsye sur les profils colonnes. Interpréter les résultats

# In[89]:


#TODO


# ### Analyse de l'association lignes-colonnes
# Au-delà de la comparaison des profils, l’intérêt majeur de l’AFC est d’identifier les associations entre les modalités lignes et colonnes : est ce que les agriculteurs s'informent plus par la radio que les autres ? Est ce que la presse magazine attire plus les cadres ?
# 
# Avant de s’intéresser aux relations entre les modalités, il faut déjà vérifier qu’il existe bien une liaison exploitable entre les variables en ligne et colonne du tableau de contingence. La statistique du $\chi^2$ de l'écart à l'indépendance permet de le faire
# 
# Faire un test du $\chi^2$ (voir le cours statistiques bivariées), en utilisant la fonction [$scipy.stats.chi2.cdf$](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2.html) du module $scipy$. Conclure.

# In[90]:


#TODO


# Le test conduit au rejet de l'hypothèse nulle : les variables lignes et colonnes sont donc manifestement fortement liées.

# 
# 
# Pour approfondir la nature des relations entre les modalités lignes et colonnes du tableau, on peut calculer l'indice d'attraction / répulsion, défini par 
# $$\frac{P(Y=y_k, X=x_l)}{P(Y=y_k)P(X=x_l)}$$
# 
# où $x_l$ et $y_k$ sont les profils ligne et colonne. En pratique, cet indice est calculé comme le rapport entre les effectifs observés et théoriques : s'il est supérieur à 1, il y a une attraction ; sinon il y a répulsion entre les modalités.
# 
# Calculer cet indice, effectuer uin test du $\chi^2$ et conclure.

# In[91]:


#TODO


# ### Représentation simultanée lignes/colonnes
# 
# En utilisant la fonction $mapping$ (ligne 329 du fichier base.py), projeter sur le premier plan factoriel les individus ligne et colonne. Interpreter.

# In[92]:


#TODO


# Comme en ACP où il est possible de reconstituer approximativement les données originelles à partir des coordonnées factorielles des individus, on peut approcher le tableau des indices d’attraction-répulsion $i_{kl}$ à partir des coordonnées factorielles des modalités lignes et colonnes : en reconstruisant à partir des $P$ premiers facteurs, si $F_{kp}$ ett $G_{lp}$ sont les coordonnées factorielles des modalités lignes et colonnes
# 
# $i_{kl} = 1+\displaystyle\sum_{p=1}^P \frac{F_{kp}G_{lp}}{\sqrt{\lambda_p}}$
# 
# Ainsi : 
# - Deux modalités s’attirent (resp. se repoussent) si leurs coordonnées sont de même signe (resp. de signe contraire) sur les axes factoriels.
# - Le trait est d’autant plus marqué que les valeurs des coordonnées sont élevées (en valeur absolue) c.-à-d. que les points sont situés aux extrémités des facteurs.
# - Les  coordonnées doivent être relativisées par le pouvoir de restitution du facteur ($\lambda_h$).
# 
# Calculer l'approximation des inices d'attraction-répulsion à parit des données du premier facteur (P=1). Interpréter.
# 
# 

# In[93]:


#TODO


# # Exercice 2 : Analyse des Correspondances Multiples
# Ici on s'intéresse à 6 traits de caractères de 27 races de chien, et on souhaite analyser le tableau par ACM

# In[5]:


chiens = pd.read_table("./data/chiens.txt", header=0, index_col=0, delimiter="\t", encoding="utf-8")
print(chiens)  


# On récupère les variables actives : on s'intéresse à un sous-ensemble de cardinal $k$ de variables du jeu de données (vous pouvez changer les variables utilisées).

# In[8]:


var_chiens = chiens[['Taille','Velocite','Affection']] 

print(var_chiens)


# ## Analyse des individus
# 
# Dans la suite, on travaille sur le tableau disjonctif complet des données (variables transformées en indicatrices 0/1).

# In[67]:


#codage en 0/1 des propriétés des chiens : tableau disjonctif complet
X = pd.get_dummies(var_chiens,prefix='',prefix_sep='')
n,p =  X.shape
print(X)


# ## ===== Votre travail : =====
# Vous avez à disposition un fichier mca.py, permettant de réaliser les calculs relatifs à une analyse des correspondances multiples
# Faire une analyse en composantes multiples de ces données et plus précisément : 
# - Déterminer l'importance des axes principaux calculés lors de l'ACP (attribut $eig\_$, descripion ligne 74 de mca.py).
# - Déterminer les contributions des points lignes à la variance des axes (attribut r$ow\_contrib\_$, descripion ligne 86 de mca.py)
# - Déterminer les contributions des points colonnes à la variance de l'axe (attribut $col\_contrib\_$, descripion ligne 90 de mca.py)
# - Déterminer la qualité de représentation des des points lignes et colonnes (attributs $row\_cos2\_$ et $col\_cos2\_$, descripion lignes 94 et 97 de mca.py)
# - Tracer la projection des points lignes et colonnes (fonctions $mapping$, $mapping\_row$ et $mapping\_col$ de mca.py) sur les plans princpaux
# - Commenter l'ensemble de vos analyses
# 

# Calculer la distance entre individus : on utilise dans ce cas la distance du Chi2 sur modalités catégorielles (voir chapitre 1 du cours) qui met en valeur les différences entre les modalités rares 
# 

# In[68]:


#profil individu moyen
ind_moy = np.sum(X.values,axis=0)/(n*p) 

distchi2 = np.zeros(shape=(n,n))

#TODO : calcul de la distance 

plt.figure(figsize=(10,10))
sns.heatmap(distchi2,vmin=0,vmax=np.max(distchi2),linewidth=0.1,cmap= 'Greens',xticklabels=chiens.index,yticklabels=chiens.index)


# Ainsi, par exemple, le Basset a plus de caractères en commun avec le Caniche qu’avec le Beauceron.

# Calculer la distance à l'origine (profil moyen). Interpréter 

# In[69]:


#profil moyen des variables-modalités
moda_moy = np.ones(X.shape[0])/n

distO = np.zeros(shape=(1,n))

#TODO : calcul de la distance

sns.heatmap(distO,vmin=0,vmax=np.max(distO),linewidth=0.1,cmap= 'Greens',xticklabels=X.index)


# Ainsi par exemple, le Pointer est plus proche du chien moyen que le Cocker.

# ### Analyse des colonnes
# L’analyse des associations entre les modalités revient à travailler sur les profils colonnes. Le tableau de données est normalisé par les sommes en colonne. Le profil moyen est égal au poids des observations 

# In[70]:


#somme en colonne
somme_col = np.sum(X.values,axis=0) 

n,p =  X.shape

#On utilise la distance du Chi2 sur modalités catégorielles qui met en valeur les différences entre les modalités rares 
dist = np.zeros(shape=(p,p))

for i in range(p-1):
    for j in range(i,p):
        dist[i,j] = dist[j,i] = np.sum(n*((X.values[:,i]/somme_col[i]-X.values[:,j]/somme_col[j])**2))

plt.figure(figsize=(10,10))
sns.heatmap(dist,vmin=0,vmax=np.max(dist),linewidth=0.1,cmap= 'Greens',xticklabels=X.columns,yticklabels=chiens.columns)



# Calculer la distance à l'origine, qui  donne une information sur la fréquence de la modalité dans la base. Elle est définie par la disance du $\chi^2$ au profil moyen. Interpréter 

# In[71]:


#profil moyen des variables-modalités
moda_moy = np.ones(X.shape[0])/n

distO = np.zeros(shape=(1,p))

#TODO calcul distance

sns.heatmap(distO,vmin=0,vmax=np.max(distO),linewidth=0.1,cmap= 'Greens',xticklabels=X.columns)


# Ainsi, Veloc+ est moins présent que Veloc- dans les exemples.

# ### ACM

# On créé une instance de l'objet MCA (défini dans mca.py) et on estime le modèle des correspondances multiples sur les données $X$
# 

# In[52]:


from mca import MCA
acm = MCA(row_labels=var_chiens.index, var_labels=var_chiens.columns)
acm.fit(var_chiens.values)


# ### Analyse des valeurs propres
# 
# L’objectif de l’Analyse des Correspondances Multiples est de décomposer l'information sur une succession d’axes factoriels orthogonaux. Le nouveau système de représentation est calculé pour préserver au mieux les distances entre individus. L nombre maximum de facteurs est $p-k$, où $p$ est la somme du nombre de modalités des variables (le nombre de colonnes de $X$), et $k$ le nombre de variables initiales.
# 
# De même que pour l'analyse facrtorielle, calculer les valeurs propres et interpréter les facteurs.

# In[72]:


#TODO


# ### Représentation graphique

# 
# 2 types de graphiques peuvent être réalisés :
# - Les mappings classiques qui représentent les points lignes et colonnes sur un plan factoriel
# - Des graphiques qui permettent d'interpréter rapidement les axes : on choisit un axe factoriel et on observe quels sont les points lignes et colonnes qui présentent les plus fortes contributions et cos2 pour cet axe
# 

# In[73]:


f, (ax1, ax2,ax3) = plt.subplots(1, 3,figsize=(16,4))
acm.mapping(ax1,num_x_axis=1, num_y_axis=2)
acm.mapping_row(ax2,num_x_axis=1, num_y_axis=2)
acm.mapping_col(ax3,num_x_axis=1, num_y_axis=2)
f.subplots_adjust(wspace=0.52)
plt.tight_layout()


# In[74]:


f, (ax1, ax2,ax3) = plt.subplots(1, 3,figsize=(16,4))
acm.mapping(ax1,num_x_axis=1, num_y_axis=3)
acm.mapping_row(ax2,num_x_axis=1, num_y_axis=3)
acm.mapping_col(ax3,num_x_axis=1, num_y_axis=3)
f.subplots_adjust(wspace=0.52)
plt.tight_layout()


# ### Analyse du 1er axe
# 
# On utilise les formules de $cos^2$ pour mesurer la qualité de la projection des individus et des modalités sur les axes factoriels.
# En pratique, si deux individus sont bien projetés alors s’ils sont proches en projections, ils sont effectivement proches dans leur espace d’origine et on peut alors interprèter leur proximité :
# 
# — La proximité entre deux individus s’interprète en terme de distance (du $\chi^2$) : deux individus se ressemblent s’ils ont choisis les mêmes modalités. 
# 
# — La proximité entre deux modalités de deux variables différentes s’interprète en terme de distance (du $\chi^2$) : deux modalités se ressemblent si elles sont possédées par les mêmes individus. 

# On peut exhiber les coordonnées des individus sur les facteurs. Par exemple sur le premier facteur

# In[75]:


print(pd.DataFrame(acm.row_coord_[:,0],index=var_chiens.index))


# et de même pour les modalités

# In[79]:


print(pd.DataFrame(acm.col_coord_[:,0],index=X.columns))



# Calculer la moyenne des  coordonnées pour chaque variable. Qu'observez-vous ?

# In[31]:


#TODO 


# En utillisant les fonctions plot\_row\_contrib et plot\_row\_cos2 (voir fichier base.py), interpréter la contribution des individus aux deux premiers facteurs.

# In[32]:


#TODO


# ### Analyse du deuxième axe

# In[34]:


#TODO


# In[ ]:




