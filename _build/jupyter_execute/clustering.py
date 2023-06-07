#!/usr/bin/env python
# coding: utf-8

# # Quelques méthodes de classification
# ## Introduction
# La classification automatique a pour but d'obtenir une représentation simplifiée des données initiales. Elle consiste à organiser un ensemble de données en classes homogènes ou classes naturelles. 
# 
# Une définition formelle de la classification, qui puisse servir de base à un processus automatisé, amène à se poser les questions suivantes :
# - Comment les objets à classer sont-ils définis ?
# - Comment définir la notion de ressemblance entre objets ?
# - Qu'est-ce qu'une classe ?
# - Comment sont structurées les classes ?
# - Comment juger une classification par rapport à une autre ?
# 
# Pour effectuer cette classification, deux démarches sont généralement utilisées :
# - on regroupe en classes les objets qui partagent certaines caractéristiques.
# - on regroupe en classes les objets qui possèdent des caractéristiques proches. C'est cette approche qui est étudiée ici
# 
# ## Structures de classification
# ### Partition
# ```{index} Partition
# ```
# 
# ````{prf:definition} Partition
# $\Omega$ étant un ensemble fini, un ensemble $P =(P_1 ,P_2 ,\cdots  P_g )$ de parties non vides de   $\Omega$ est une partition si :
# - $(\forall k\neq l) P_k \cap P_l=\emptyset$
# - $\displaystyle\cup_{i=1}^gP_i=\Omega$
# ````
# Dans un ensemble  $\Omega$ partitionné en $g$ classes, chaque élément de l'ensemble appartient à une classe et une seule. Une manière pratique de décrire cette partition $P$ consiste à lui associer la matrice de classification ${\bf C}=(c_{ij}), i\in [\![1,n]\!], j\in [\![1,g]\!]$, avec $c_{ij}=1$ si l'individu $i$ appartient à $P_j$, et $c_{ij}=0$ sinon. Dans le cas où l'on accepte qu'un individu appartienne à plusieurs classes (avec des degrés d'appartenance), on autorise $c_{ij}$ à couvrir l'intervalle [0,1] et on parle alors de classification floue.
# ### Hiérarchie indicée
# ```{index} Hiérarchie
# ```
# 
# ````{prf:definition} Hiérarchie
# $\Omega$ étant un ensemble fini, un ensemble $H$ de parties non vides de $\Omega$ est une hiérarchie sur $\Omega$ si :
# - $\Omega \in H$
# - $(\forall x\in \Omega) \{x\}\in H$
# - $(\forall h,h'\in H) h\cap h'=\emptyset$ ou $h\subset h'$ ou $h'\subset h$
# ````
# 
# Une hiérarchie est souvent représentée par l'intermédiaire d'un indice, fonction $i$ de $H$ dans $\mathbb{R}^+$, strictement croissante vis à vis de l'inclusion et de noyau l'ensemble des singletons de $\Omega$.
# 
# ### Partition et hiérarchie
# Si $P =(P_1 \cdots,P_g)$ est une partition de $\Omega$, l'ensemble $H$ formé des classes $P_k$ de $P$, des singletons de   $\Omega$ et de l'ensemble  $\Omega$ lui-même forme une hiérarchie. Remarquons qu'inversement, il est possible d'associer à chaque niveau d'une hiérarchie indicée une partition. Une hiérarchie indicée correspond donc à un ensemble de partitions emboîtées.
# 
# ## Objectifs de la classification
# ### Difficultés de caractériser les objectifs
# L'objectif de la classification automatique est l'organisation en classes homogè\-nes\- des éléments d'un ensemble  $\Omega$. Pour définir cette notion de classes homogènes, on utilise le plus souvent une mesure de similarité (ou de dissimilarité) sur  $\Omega$. Par exemple, on peut imposer à un couple quelconque d'individus d'une même classe d'être plus "proches" que n'importe quel couple formé par un individu de la classe et un individu d'une autre classe. En pratique, cet objectif est inutilisable, et plusieurs démarches sont alors utilisées pour remplacer cet objectif trop difficile à atteindre.
# 
# ### Démarche numérique
# #### Partition
# On remplace cette condition trop exigeante par une fonction numérique (critère) qui mesure la qualité d'homogénéité d'une partition. Le problème peut paraître alors très simple. En effet, par exemple, dans le cas de la recherche d'une partition, il suffit de chercher parmi l'ensemble fini de toutes les partitions celle qui optimise le critère numérique. Malheureusement, le nombre de ces partitions étant très grand, leur énumération est impossible dans un temps raisonnable. On utilise alors des heuristiques qui donnent, non pas la meilleure solution, mais une "bonne solution", proche de la solution optimale. On parle alors d'optimisation locale. Lorsqu'il existe une structure d'ordre sur l'ensemble  $\Omega$ et que celle-ci doit être respectée par la partition, il existe un algorithme de programmation dynamique (algorithme de Fisher), qui fournit la solution optimale.
# 
# #### Hiérarchie
# Dans le cas d'une hiérarchie, on cherche à obtenir des classes d'autant plus homogènes qu'elles sont situées dans le bas de la hiérarchie. La définition d'un critère est moins facile. Nous verrons qu'il est possible de le faire en utilisant la
# notion d'ultramétrique (ultramétrique optimale).
# 
# ### Démarche algorithmique
# Il s'agit cette fois de définir directement un algorithme qui construit des classes homogènes en tenant compte de la mesure de similarité. Il est relativement facile de proposer de tels algorithmes, le problème est de pouvoir vérifier que les résultats fournis sont intéressants et répondent au problème posé. En réalité, cette démarche rejoint assez souvent la précédente. 
# 
# ### Mesure de dissimilarité et distance
# Les algorithmes de classification dépendent d'une métrique qui définit implicitement la forme des classes qui seront calculées. Si la distance euclidienne suppose une isotropie dans les axes (et donc une représentation sphérique des classes), d'autres distances ou indices de dissimilarité peuvent être utilisés.
# 
# #### Indice de dissimilarité
# On se place dans $\mathbb R^p$, et on considère $n$ individus à classer ${\bf x_1}\ldots {\bf x_n}$.
# ````{prf:definition} Dissimilarité - ultramétrique
# Une mesure de dissimilarité $d$ est une fonction de 
# 
# $
# d : \begin{array}{ccc}
# \mathbb{R}^p\times\mathbb{R}^p &\rightarrow &\mathbb{R}^+\\
# (\mathbf x_i,\mathbf x_j)&\mapsto & d_{ij} = d(\mathbf x_i,\mathbf x_j)
# \end{array}
# $
# 
# vérifiant : 
# - $(\forall i,j\in[\![1, n]\!])\ d_{ij}=d_{ji}$
# - $(\forall i\in[\![1, n]\!])\ d_{ii}= 0$
# 
# Si l'inégalité triangulaire $d_{ij}\leq d_{ik}+d_{kj}$ est de plus vérifiée pour tout $i,j,k$, alors $d$ est une distance. 
# 
# Si enfin l'inégalité ultramétrique  $d_{ij}\leq max(d_{ik}+d_{jk})$ est  vérifiée pour tout $i,j,k$, $d$ est une ultramétrique.
# ````
# A partir des mesures de dissimilarité, on déduit des mesures de similarité $s_{ij}$ le passage de l'une à l'autre se faisant par exemple par $d_{ij} = s_{max}-s_{ij}$.
# 
# #### Cas de variables qualitatives
# On suppose que les $p$ composantes des ${\bf x_i}$ sont qualitatives, et on se limite ici au cas de variables bimodales. 
# Étant donnés ${\bf x_i}=\begin{pmatrix} x_i^1\ldots x_i^p\end{pmatrix}$ et ${\bf x_j}$, on note :
# 
# - $a_{ij}$ le nombre de co-occurences entre les individus $i$ et $j$
# - $b_{ij}$ le nombre de co-absences entre les individus $i$ et $j$
# - $c_{ij}$ le nombre d'attributs présents chez $i$ et absents chez $j$
# - $d_{ij}$ le nombre d'attributs absents chez $i$ et présents chez $j$
# 
# 
# les mesures suivantes sont des exemples de dissimilarité :
# 
# - $d_{ij} = \sqrt{b_{ij}+c_{ij}}$ [distance "euclidienne" binaire]
# - $d_{ij} = \frac{(b_{ij}-c_{ij})^2}{(a_{ij}+b_{ij}+c_{ij}+d_{ij})^2}$ [différence binaire de taille]
# - $d_{ij} = \frac{(b_{ij}c_{ij})}{(a_{ij}+b_{ij}+c_{ij}+d_{ij})^2}$ [différence binaire de motif]
# - $d_{ij} = \frac{(a_{ij}+b_{ij}+c_{ij}+d_{ij})(b_{ij}+c_{ij})-(b_{ij}-c_{ij})^2}{(a_{ij}+b_{ij}+c_{ij}+d_{ij})^2}$ [différence binaire de forme]
# - $d_{ij} = \frac{(b_{ij}+c_{ij})}{4(a_{ij}+b_{ij}+c_{ij}+d_{ij})}$ [dissimilarité binaire de variance]
# - $d_{ij} = \frac{(b_{ij}+c_{ij})}{2a_{ij}+b_{ij}+c_{ij}}$ [dissimilarité binaire de Lance et Williams]
# 
# 
# #### Cas de variables quantitatives
# Dans le cas de variables quantitatives, les normes  $L_r$ : 
# 
# $\|{\bf x_i}\|_r=\left (\displaystyle\sum_{j=1}^p|x_i^j|^r\right ) ^\frac{1}{r}$
# 
# sont classiquement utilisées, et par exemple 
# 
# - $r=1$ : $\|{\bf x_i}-{\bf x_j}\|_1=\displaystyle\sum_{k=1}^p|x_i^k-x_j^k|$ est la norme $L_1$ (ou city block).
# - $r=2$ : $\|{\bf x_i}-{\bf x_j}\|_2=\sqrt{\displaystyle\sum_{k=1}^p(x_i^k-x_j^k)^2}$ est la norme $L_2$ (ou norme euclidienne).
# - $r=\infty$ : $\|{\bf x_i}-{\bf x_j}\|_\infty = \displaystyle\max_{1\leq k\leq p}\{|x_i^k-x_j^k|\}$ est la norme du max (ou norme de Tchebychev)
# 
# Si les variables ne sont pas normalisées, on peut utiliser la distance de Mahalanobis 
# 
# $d_{ij} = \displaystyle\sum_{k=1}^p\displaystyle\sum_{l=1}^pw_{kl}(x_i^k-x_j^k)(x_i^l-x_j^l)$
# 
# où la matrice des $w_{kl}$ est l'inverse de la matrice de covariance empirique. Cette distance élimine également les corrélations entre variables.
# 
# 
# Enfin, on peut utiliser une métrique issue du coefficient de corrélation, dite distance de Pearson : $d_{ij} =\sqrt{1-r^2_{ij}}$, avec
# 
# $r^2_{ij} = \frac{\left (\displaystyle\sum_{k=1}^p (x_i^k-\bar{x_i})(x_j^k-\bar{x_j})\right )^2}{\displaystyle\sum_{k=1}^p(x_i^k-\bar{x_i})^2\displaystyle\sum_{k=1}^p(x_j^k-\bar{x_j})^2}$
# 
# #### Variables de comptage
# Dans le cas particulier de variables de comptage ($x_i^k$ effectif de la classe $k$ pour l'individu $i$), une mesure naturelle de dissimilarité entre ${\bf x_i}$ et ${\bf x_j}$ est le $\chi^2$ du tableau de contingence 2$\times p$ associé. 
# 
# #### Quelle mesure choisir ?
# Une réflexion  sur le type de dissimilarité à choisir est nécessaire. Il est en particulier intéressant de répondre aux questions suivantes:
# 
# - de quelles variables initiales (qualitatives et/ou quantitatives) doit dépendre la dissimilarité? 
# - est-il souhaitable (et possible) d'obtenir des variables pertinentes supplémentaires? Si oui par mesure ? par analyse linéaire (ACP,...) ou non linéaire (manifold learning) ?
# - quelles doivent être les importances relatives des diverses variables retenues dans la constitution de la dissimilarité ?
# 
# ## Classification ascendante hiérarchique
# L'objectif est de construire une hiérarchie indicée d'un ensemble $\Omega$ sur lequel on connaît une mesure de dissimilarité $d$ telle que les points les plus proches soient regroupés dans les classes de plus petit indice. La hiérarchie est alors construite en appliquant itérativement ce principe, et l'arbre obtenu sur l'ensemble des itérations est appelé un dendrogramme. 
# 
# Il existe essentiellement
# deux approches :
# - la classification descendante : on divise $\Omega$ en classes, puis on recommence sur chacune de ces classes itérativement jusqu'à ce que les classes soient réduites à des singletons. 
# - la classification ascendante : cette fois on part de la partition de $\Omega$  où chaque classe est un singleton. On procède alors par fusions successives des classes jusqu'à obtenir une seule classe, c'est-à -dire l'ensemble  $\Omega$ lui-même. Nous insistons sur ce type de classification dans la suite.
# 
# 
# 
# ### Algorithme
# ```{index} Clustering hiérarchique
# ```
# 
# #### Construction de la hiérarchie
# $\Omega$  étant l'ensemble à classifier et $d$ une mesure de dissimilarité sur cet ensemble, on définit, à partir de $d$, une  distance $D$ entre les parties de  $\Omega$. Cette distance est en réalité une mesure de dissimilarité qui ne vérifie pas nécessairement toutes les propriétés d'une distance sur l'ensemble des parties de $\Omega$. En général, $D$ est appelé critère d'agrégation.
# L'algorithme est alors le suivant :
# 
# ```{prf:algorithm} Algorithme de clustering hiérarchique ascendant
# 
# 
# **Entrée :** Les éléments de $\Omega$
# 
# **Sortie :** Une hiérarchie
# 
# 1. Initialisation : partition des singletons 
# 2. Calcul des distances entre classes.
# 3.  Tant que le nombre de classes est $>$1
#     1. Regroupement des 2 classes les plus proches au sens de $D$
#     2. Calcul des distances entre la nouvelle classe et les anciennes classes non regroupées.
# ```
# 
# Il est facile de montrer que l'ensemble des classes définies au cours de cet algorithme forme une hiérarchie.
# 
# #### Construction de l'indice
# Après avoir défini une hiérarchie, il est nécessaire de lui associer un indice. Pour les classes du bas de la hiérarchie, c'est-à-dire les singletons, cet indice est nécessairement la valeur 0. Pour les autres classes, cet indice est généralement
# défini en associant à chacune des classes construites au cours de l'algorithme la distance $D$ qui séparait les deux classes fusionnées pour former cette nouvelle classe. Pour que cette définition conduise bien à un indice, il est nécessaire que
# les indices obtenus soient strictement croissants avec le niveau de la hiérarchie. Plusieurs difficultés peuvent alors apparaître :
# 
# - pour certains critères d'agrégation, l'indice ainsi défini n'est pas nécessaire\-ment\- croissant. On parle alors d'inversion. Par exemple, si les données sont formées par trois points du plan situés au sommet d'un triangle équilatéral de côté 1 et si on prend comme distance $D$ entre classes la distance entre les centres de gravité, on obtient une inversion.
# - lorsqu'il y a égalité de l'indice pour plusieurs niveaux emboîtés, il suffit de filtrer la hiérarchie, c'est-à-dire conserver une seule classe qui regroupe toutes les classes emboîtées ayant le même indice. 
# 
# 
# ### Critères d'agrégation
# Il existe de nombreux critères d'agrégation, mais les plus utilisés sont les suivants :
# 
# - critère du lien commun : $D_{min}(A,B)=\displaystyle\min_{i\in A,j\in B}d_{ij}$
# - critère du lien maximum: $D_{max}(A,B)=\displaystyle\max_{i\in A,j\in B}d_{ij}$
# - critère du lien moyen : $D_{moy}(A,B)=\frac{\displaystyle\sum_{i\in A}\displaystyle\sum_{j\in B}d_{ij}}{|A||B|}$
# 
# 
# 
# ![](./images/agreg.png)
# 
# 
# ### Formule de récurrence de Lance et Williams
# 
# Pour les trois critères d'agrégation précédents, il existe des relations de simplification du calcul des distances entre classes essentielles pour la mise en place pratique de l'algorithme de classification ascendante :
# 
# - $D_{min}(A,B\cup C)=min(D_{min}(A,B),D_{min}(A,C))$
# - $D_{max}(A,B\cup C)=max(D_{max}(A,B),D_{min}(A,C))$
# - $D_{moy}(A,B\cup C)=\frac{|B|D_{moy}(A,B)+|C|D_{moy}(A,C)}{|B|+|C|}$
# 
# 
# ### Critère de Ward
# ```{index} Ward ; critère
# ```
# Lorsque l'ensemble   $\Omega$ à classifier est mesuré par $p$ variables quantitatives, il est possible de lui associer un nuage de points pondérés dans $\mathbb{R}^p$ muni de la distance euclidienne $d$. Généralement, les pondérations seront toutes égales à 1. Le critère d'agrégation le plus utilisé dans cette situation est alors le critère d'inertie de Ward :
# 
# $D(A,B)=\frac{p_Ap_B}{p_A+p_B}d^2({\bf g}(A),{\bf g}(B))$
# 
# où $p_E$ représente la somme des pondérations des éléments d'une classe $E$ et ${\bf g}(E)$ est le centre de gravité d'une classe $E$.
# 
# ### Propriétés d'optimalité
# La notion de hiérarchie indicée est équivalente à la notion d'ultramétrique. La classification hiérarchique ascendante transforme donc la mesure de dissimilarité $d$ initiale en une mesure de dissimilarité $\delta$ qui possède la propriété d'être une ultramétrique. 
# 
# Le problème de la classification hiérarchique peut donc également se poser en ces termes : trouver l'ultramétrique $\delta$ la plus proche de $d$. Il reste à munir l'espace des mesures de dissimilarité sur  $\Omega$ d'une distance. On pourra utiliser, par exemple :
# 
# - $\Delta(\delta,d)=\displaystyle\sum_{i,j\in \Omega}(d_{ij}-\delta_{ij})^2$
# - $\Delta(\delta,d)=\displaystyle\sum_{i,j\in \Omega}|d_{ij}-\delta_{ij}|$
# 
# 
# ### Critère d'arrêt et partition
# ```{index} Dendrogramme
# ```
# L'ensemble des itérations peut être visualisé sous la forme d'un arbre, appelé dendrogramme. La figure suivante présente un exemple de dendrogramme en clustering hiérarchique descendant sur $X = \{a, b, c, d, e\}$. La distance $D$ n’est pas reportée
# 
# ![](./images/dendro1.png)
# 
# Le critère d'arrêt permet de déterminer la partition  de $X$ la plus appropriée. Ici encore, plusieurs choix sont possibles :
# 
# - en fixant a priori un nombre de classes
# - en fixant une borne supérieure $r$ pour $D$, et en stoppant les itérations dès que les distances calculées par les liens dépassent $r$. A noter que $r$ peut être également calculé par $r=\alpha max\{d(x,y),x,y\in X\}$ (critère dit "scale distance upper bound").
# - en coupant le dendrogramme au saut de distance $D$ maximal.
# 
# ![](./images/dendro2.png)
# 
# 
# 
# 
# ### Utilisation des méthodes
# La première difficulté est le choix de la mesure de dissimilarité sur  $\Omega$ et du critère d'agrégation. Généralement, lorsque l'on dispose de variables quantitatives, le critère conseillé est le critère d'inertie. Ensuite, il est souvent nécessaire de disposer d'outils d'aide à l'interprétation et d'outils permettant de diminuer le nombre de niveaux de hiérarchie. Il est d'autre part conseillé d'utiliser conjointement d'autres méthodes d'analyse des données comme l'Analyse en Composantes Principales vue au chapitre précédent.
# 
# ### Exemple
# On étudie ici un jeu de données correspondant aux achats dans un supermarché. On cherche à caractériser les comportements des acheteurs en fonction de leurs revenus

# In[1]:


import pandas as pd
df = pd.read_csv('./data/Mall_Customers.csv')
df.head(5)


# On affiche les données

# In[2]:


import matplotlib.pyplot as plt
plt.figure(figsize=(16,5))
plt.subplot(121)
plt.title("Score/Revenu")
plt.xlabel ("Revenu annuel (k$)")
plt.ylabel ("Score d'achat")
plt.grid(True)
plt.scatter(df['Annual Income (k$)'],df['Spending Score (1-100)'],color='blue',edgecolor='k',alpha=0.6, s=50)
plt.subplot(122)
plt.title("Distribution des âges et des scores d'achat")
plt.xlabel ("Age")
plt.ylabel ("Score d'achat")
plt.grid(True)
plt.scatter(df['Age'],df['Spending Score (1-100)'],color='red',edgecolor='k',alpha=0.6, s=50)
plt.tight_layout()


# L'objectif est de trouver des catégories de population ayant les mêmes comportements d'achat. Le nombre de classes étant inconnu, la classification héararchique va permettre de donner des indications sur le nombre de groupes.

# In[3]:


import scipy.cluster.hierarchy as sch

X = df.iloc[:,[3,4]].values
plt.figure(figsize=(15,6))
plt.title('Dendrogramme')
plt.xlabel('Clients')
plt.ylabel('Indice')
plt.hlines(y=190,xmin=0,xmax=2000,lw=2,linestyles='--')
plt.text(x=900,y=220,s='Cut',fontsize=20)
dendrogram = sch.dendrogram(sch.linkage(X, method = 'ward'))
plt.show()


# On projette ensuite le résultat de la classificatiob

# In[4]:


from sklearn.cluster import AgglomerativeClustering
model = AgglomerativeClustering(n_clusters = 5, metric = 'euclidean', linkage = 'ward')
y_model = model.fit_predict(X)
plt.figure(figsize=(12,7))
plt.scatter(X[y_model == 0, 0], X[y_model == 0, 1], s = 50, c = 'red', label = 'Radins')
plt.scatter(X[y_model == 1, 0], X[y_model == 1, 1], s = 50, c = 'blue', label = 'Prudents')
plt.scatter(X[y_model == 2, 0], X[y_model == 2, 1], s = 50, c = 'green', label = 'Riches')
plt.scatter(X[y_model == 3, 0], X[y_model == 3, 1], s = 50, c = 'orange', label = 'Dépensiers modestes')
plt.scatter(X[y_model == 4, 0], X[y_model == 4, 1], s = 50, c = 'magenta', label = 'Conscients')
plt.title('Classification',fontsize=14)
plt.xlabel ("revenu annuel (k$)",fontsize=14)
plt.ylabel ("Score (1-100)",fontsize=14)
plt.legend(loc='best')
plt.tight_layout()


# ## Recherche de partitions
# 
# ### Méthode des centres mobiles
# ```{index} Centres mobiles
# ```
# 
# ```{index} K-means
# ```
# La méthode des centres mobiles est encore connue sous le nom de méthode de réallocation-centrage ou des k-means lorsque l'ensemble à classifier est mesuré par $p$ variables. Ici, $\Omega \in \mathbb{R}^p$ est muni de sa distance euclidienne $d$. Pour simplifier la présentation, les pondérations des individus seront toutes égales à 1, mais la généralisation à des pondérations quelconques ne pose aucun problème.
# 
# #### Algorithme
# L'algorithme des centres-mobiles peut se définir ainsi :
# 
# 
# ```{prf:algorithm} Algorithme des centres mobiles
# 
# 
# **Entrée :** $\Omega$,$g$, métrique
# 
# **Sortie :** Une partition de $\Omega$
# 
# 1. Initialisation : tirage au hasard de $g$ points de  $\Omega$ (centres initiaux des $g$ classes) 
# 2.  Tant que (non convergence)
#     1. Étape E : Construction de la partition en affectant chaque point de $\Omega$ à la classe dont il est le plus près du centre (en cas d'égalité, l'affectation se fait à la classe de plus petit indice).
#     2. Étape M : Les centres de gravité de la partition qui vient d'être calculée deviennent les nouveaux centres
# ```
# 
# 
# ![](./images/kmeans1.png)
# 
# 
# L'initialisation des centres de classe étant aléatoire, il convient de répliquer l'algorithme plusieurs fois et de, par exemple, retenir la partition majoritaire. La figure suivante présente deux résultats des k-means, sur un même jeu de données (5 classes, 50 points par classes), avec une initialisation aléatoire différente.
# 
# ![](./images/kmeans2.png)
# 
# 
# 
# #### Critère et convergence
# La qualité d'un couple partition-centres est mesurée par la somme des inerties des classes par rapport à leur centre. On peut montrer qu'à chacune des deux étapes de l'algorithme, on améliore ce critère.
# 
# #### Lien avec la méthode de Ward
# La méthode des centres mobiles et la méthode de Ward optimisent toutes deux, à leur façon, le critère d'inertie intra-classe. Cette situation conduit à proposer des stratégies utilisant les deux approches comme, par exemple :
# - appliquer les centres-mobiles pour regrouper l'ensemble initial en un nombre "important" de classes
# - appliquer la méthode de Ward en partant de ces classes 
# - rechercher quelques "bons" niveaux de la hiérarchie 
# - éventuellement, appliquer de nouveau la méthode des centres-mobiles sur les partitions obtenues pour améliorer encore leur critère. 
# 
# ### Généralisation : les nuées dynamiques
# 
# ```{index} Nuées dynamiques
# ```
# 
# L'idée de base consiste à remplacer les centres   qui étaient des éléments de $\mathbb{R}^p$ jouant le rôle de représentant ou encore de noyau de la classe par des éléments de nature très diverse adaptés au problème que l'on cherche à résoudre.
# 
# #### Formalisation
# On note $L=\{\lambda_i\}$ l'ensemble des noyaux, $D:\Omega\times L\rightarrow \mathbb{R}^+$ une mesure de ressemblance entre éléments de $\Omega$ et de $L$. L'objectif est alors de trouver la partition en $g$ classes ($g$ fixé a priori) de $\Omega$ minimisant le critère $\displaystyle\sum_{k}\displaystyle\sum_{x\in P_k}D(x,\lambda_k)$
# 
# Cette minimisation est réalisée de façon alternée, comme pour les centres mobiles.
# 
# #### Choix du nombre de classes
# En général, le critère n'est pas indépendant du nombre de classes. Par exemple, le critère de l'inertie s'annule pour la partition triviale pour laquelle chaque point forme une classe. Il s'agit donc de la meilleure partition. Il est donc
# nécessaire de fixer a priori le nombre de classes. Pour résoudre ce problème très difficile, plusieurs solutions sont utilisées :
# - on a une idée du nombre de classes désirées
# - on recherche la meilleure partition pour plusieurs nombres de classes et on étudie la décroissance du critère en fonction du nombre de classes (méthode du coude)
# - on définit une fonction $f(\Omega)$ qui rend le critère indépendant du nombre de classes
# - on ajoute des contraintes supplémentaires (nombre d'individus par classe, volume d'une classe...). C'est l'option retenue par la méthode Isodata 
# - on effectue des tests statistiques sur les classes
#  
# 
# 
# 
#   
#   ### Exemple
# On génère des données

# In[5]:


from sklearn.datasets import make_blobs
import numpy as np
import matplotlib.pyplot as plt

nb_classes = 3
center = np.array(
        [[ 3,  0],[1 ,  1],[3,  4]])
cluster_std = np.array([0.8, 0.3, 1])    

X, y = make_blobs(n_samples=500,centers=center,cluster_std = cluster_std, random_state=42)
plt.figure(figsize=(5,5))
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.tight_layout()
plt.tick_params(labelbottom=False)
plt.tick_params(labelleft=False)


# Puis on applique l'algorithme des $k$-means.

# In[6]:


from sklearn.cluster import KMeans

model = KMeans(n_clusters=nb_classes,n_init=10)
    
plt.figure(figsize=(12,6))
plt.subplot(121)
plt.scatter(X[:, 0], X[:, 1],c=y, s=30,linewidths=0,cmap=plt.cm.rainbow)
plt.title("Vraies classes")
plt.tick_params(labelbottom=False)
plt.tick_params(labelleft=False)
plt.subplot(122)
model.fit(X)
plt.scatter(X[:, 0], X[:, 1], c=model.labels_, s=30,linewidths=0, cmap=plt.cm.rainbow)
plt.title("K means à {0:d} classes".format(nb_classes))
plt.tick_params(labelbottom=False)
plt.tick_params(labelleft=False)
plt.tight_layout() 
``





































 

  



