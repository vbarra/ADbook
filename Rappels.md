---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
# Rappels


## Expérience aléatoire

### Définitions
````{prf:definition} Expérience aléatoire
:label: expalea
Une **expérience aléatoire** est une expérience dont on ne peut prévoir le résultat a priori. Répétée dans des conditions identiques, elle peut donner lieu à des résultats différents.
````

````{prf:example}
- Le lancé de dé
- les côtes exactes d'une pièce fabriquée dans un atelier
````

````{prf:definition} Issue
:label: issue
On appelle **issue** d'une expérience aléatoire l'un des résultats possibles de cette expérience
````


````{prf:definition} Univers des possibles
:label: univers
On appelle **univers des possibles** d'une expérience aléatoire l'ensemble  $\Omega$ des issues de cette expérience.
````

````{prf:example}
Lorsque l'on joue à pile ou face avec une pièce de monnaie, l'expérience a deux issues possibles et $\Omega = \{P,F\}$.
````
L'univers des possibles n'est pas défini de manière unique, mais dépend de l'usage de l'experience. Par exemple, pour le lancer de deux dés, on peut être intéressé par :
- le résultat du lancer, dans ce cas $\Omega = \{(1,1), (1,2), \cdots (6,6)\}$
- la somme des deux faces et $\Omega = [\![2,12]\!]$

```{index} Evènement
``` 
````{prf:definition} Evènement
:label: evenement
Etant donnée une expérience aléatoire, un **évènement** est une assertion vraie ou fausse suivant l'issue de l'expérience. C'est donc un sous-ensemble $E$ de $\Omega$.
````

````{prf:example}
- Dans l'expérience du lancer de deux dés, on peut s'intéresser à l'évènement "la somme des deux faces est paire" ou encore  "la somme est supérieure à 7".
- Si l'expérience considérée concerne les jobs effectués sur une machine on peut considérer :
1. $\Omega=\mathbb{N}$ et l'évènement "le nombre de jobs ne dépasse pas 10" : $E=[\![0,5]\!]$
2. $\Omega=\mathbb{R}^*$ et  l'évènement "le job dure plus de 15 s" et $E=]15,+\infty[$
````
Il existe certains évènements particuliers : 
- l'évènement dit certain : c'est l'univers des possibles (par exemple "la somme des deux faces d'un lancer de deux dés est inférieure ou égale à 12")
- l'évènement impossible ("la somme des deux faces d'un lancer de deux dés est supérieure ou égale à 20")
- l'évènement simple : tout singleton de $\Omega$
- l'évènement composé : tout sous-ensembme de $\Omega$ de cardinalité au moins égale à 2.

### Notation et opérations sur les évènements
Les évènements peuvent être interprétés soit d'un point de vue ensembliste (Diagrammes de Venn), soit de manière équivalente d'un point de vue probabiliste.

| **Notation**                      | **Interprétation probabiliste**           |
|-------------------------------|---------------------------------------|
| $\omega$                      | issue possible, évènement élémentaire |
| $A$                           | évènement                             |
| $\omega\in A$                  | $\omega$ réalise $A$                  |
| $A\subset B$                  | $A$ implique $B$                      |
| $A\cup B$                     | $A$ ou $B$                            |
| $A\cap B$                     | $A$ et $B$                            |
| $\bar A$                      | contraire de $A$                      |
| $\emptyset$                   | évènement impossible                  |
| $\Omega$                      | évènement certain                     |
| $A\cap B=\emptyset$           | $A$ et $B$ incompatibles              |
| $A\setminus B = A\cap \bar B$ | $A$ et pas $B$                        |






## Probabilités
### Objectif
L'objectif des probabilités est de donner une **mesure** à la chance qu'a un évènement de se réaliser lors d'une expérience aléatoire. Pour ce faire, on définit une fonction $P:\Omega\rightarrow [0,1]$ vérifiant certains axiomes et propriétés.

```{index} Tribu
``` 

````{prf:definition} Tribu
:label: tribu
Soit $T$ une famille d'évènements. Pour que $T$ soit probabilisable, il faut que :
- $\emptyset\in T, \Omega\in T$
- Si $A_i$ est une suite dans $T$ alors $\cup_iA_i\in T$ et $\cap_iA_i\in T$
- Si $A\in T$ alors $\bar A\in T$

$T$ est une **tribu** et $(\Omega,T)$ est un **espace probabilisable**.
````
En pratique, on choisit souvent la tribu engendrée par une famille de $n$ d'évènements $A_i$, qui est l'ensemble des parties de $\Omega$ obtenues en effectuant l'union de $k$ évènements $A_i,i\in [\![1,n]\!]$.

````{prf:example}
Dans le cas du lancer d'un dé, $\Omega = \{1,2,3,4,5,6\}$, et : 
- la tribu engendrée par la famille d'évènements $\{\{1,3,5\},\{2,4,6\}\}$ est $\{\emptyset,\{1,3,5\},\{2,4,6\},\Omega\}$.
- la tribu engendrée par la famille d'évènements $\{\{1\},\{2\},\{3\},\{4\},\{5\},\{6\}\}$ est l'ensemble des parties de $\Omega$. Plus généralement, si $\Omega$ est dénombrable, cette tribu est appelée **tribu discrète**.
````
On peut également s'intéresser, si $\Omega=\mathbb R$, à la tribu engendrée par les ouverts de $\mathbb{R}$, on parle alors de **tribu borélienne**

### Probabilité
```{margin} A. Kolmogorov
![](./images/kolmogorov.jpeg)
```
```{index} Probabilité
``` 
```{prf:axiom} Axiomatique de Kolmogorov
:label: axiomKolmo
On appelle **probabilité** sur $(\Omega,T)$ une application $P$ de $T$ dans [0,1] vérifiant :
- $(\forall A\in T)\; P(A)\in[0,1]$
- $P(\Omega)=1$
- Pour toute famille dénombrable $(A_i)$ d'évènements disjoints $P(\displaystyle\bigcup_i A_i) = \displaystyle\sum_iP(A_i)$
```
````{prf:property}
- $P(\emptyset)=0$
- $(\forall A)\; P(\bar A)=1-P(A)$
- $(\forall A,B)\; P(A\setminus B) = P(A)-P(A\bigcap B)$
- $(\forall A,B)\; P(A\bigcup B) = P(A+P(B))-P(A\bigcap B)$
- $(\forall A,B)$ si $A\subset B$ alors $P(A)\leq P(B)$
- Pour toute famille dénombrable $(A_i)$ d'évènements quelconques $P(\displaystyle\bigcup_i A_i) \leq \displaystyle\sum_iP(A_i)$
````
### Conditionnement
Les probabilités **conditionnelles** intègrent une information supplémentaire sous la forme de l'observation de la réalisation d'un évènement donné.
```{index} Probabilité ; conditionnelle
``` 
````{prf:definition} Probabilité conditionnelle
Soit $B$ un évènement de probabilité non nulle. On appelle **probabilité conditionnelle** de $A$ sachant $B$ le rapport 

$P(A\mid B) = \frac{P(A\bigcap B)}{P(B)}$
````
$P(A\mid B)$ représente la probabilité que $A$ se réalise sachant que $B$ est réalisé. 

Remarquons que l'on peut écrire $P(A\bigcap B) = P(A\mid B)P(B) = P(B\mid A)P(A)$.

````{prf:example}
7\% des français sont atteints d'un cancer du poumon. 70\% des malades sont des fumeurs et 50\% des français fument. On recherche la probabilité d'être atteint d'un cancer du poumon lorsque l'on est fumeur.
L'évènement $A$ est "avoir un cancer du poumon", et $B$ est "être fumeur". D'après les données on a $P(A)$=0.07, $P(B)$ = 0.5 et $P(B\mid A)$ = 0.7. 
On a alors $P(A\mid B) = \frac{P(A\bigcap B)}{P(B)}$ avec $P(A\bigcap B)=P(B\mid A)P(A)$ d'où

$P(B\mid A)=\frac{P(B\mid A)P(A)}{P(B}$ = 0.098
````

### Indépendance
```{index} Indépendance
``` 
````{prf:definition} Indépendance
Deux évènements $A$ et $B$ sont dits **indépendants** si et seulement si $P(A\mid B) = P(A)$.
````
On a alors bien évidemment $P(A\bigcap B) = P(A)P(B)$.

```{prf:remark}
:class: dropdown
La notion d'indépendance est directement rattachée à $P$ : $A$ et $B$ peuvent être indépendants pour une probabilité donnée, mais pas pour une autre.
```
On peut généraliser la notion d'indépendance à une famille d'évènements $(A_i)_{i\in[\![1,n]\!]}$ : on dira que les $A_i$ sont **mutuellement indépendants** si pour tout $I\subset [\![1,n]\!]$

$P\left (\displaystyle\bigcap_{i\in I} A_i\right ) = \displaystyle\prod_{i\in I} P(A_i)$

L'indépendance mutuelle est plus forte que l'indépendance deux à deux.

```{prf:remark}
:class: dropdown
La notion d'indépendance n'est pas une notion purement ensembliste. Deux évènements peuvent être indépendants pour une loi de probabilité et pas pour une autre. 
```

### Théorème des probabilités totales

```{prf:theorem}
Soit $B_i$ un système complet d'évènements (qui forment donc une partition de $\Omega$). Pour tout évènement $A$, on peut écrire 

$P(A) = \displaystyle\sum_i P(A\bigcap B_i) = \displaystyle\sum_i P(A| B_i) P(B_i)$
```


### Règle de Bayes

A partir de l'égalité $P(A\bigcap B) = P(A|B)P(B)=P(B|A)P(A)$, on définit la règle de Bayes

$(\forall A,B)\quad P(B|A)=\frac{P(A|B)P(B)}{P(A)}$


Si $B_i$ est un système complet d'évènements, on a de plus 

$P(B_i|A)= \frac{P(A|B_i)P(B_i)}{P(A)} = \frac{P(A|B_i)P(B_i)}{\displaystyle\sum_k P(A|B_k)P(B_k)}$


````{prf:example}
Un fabricant de boulons a trois usines de fabrication situées à Amiens, Besançon et Clermont-Ferrand. Amiens fournit 25\% de la production, Besançon 20\% et Clermont-Ferrand 55\%. Les boulons de 5mm représentent 20\% des boulons produits à Amiens, 30\% à Besançon et 15\% à Clermont-Ferrand. On répond à la question suivante : sachant que le boulon acheté a une taille de 5mm, quelle est la probabilité qu'il soit produit à Clermont-Ferrand ?

On note $B_1$ (respectivement $B_2,B_3$) l'évènement "Le boulon est produit à Amiens (resp. Besançon, Clermont-Ferrand)". On note également $A$ l'évènement "Le boulon fait 5mm". On cherche donc 

$P(B_3|A) = \frac{P(A|B_3)P(B_3)}{P(A)}= \frac{0.15*0.55}{0.1925}=0.428$. 
````
On a calculé dans l'exemple une **probabilité a posteriori**, c'est à dire sachant une information supplémentaire (le boulon fait 5mm). La prise en compte de cette information modifie la valeur de la probabilité associée à $B_3$. La théorie des probabilités au travers de l'approche bayésienne est adaptée pour prendre en compte toute information nouvelle.


## Variable aléatoire

### Concept de variable aléatoire
Soit un espace probabilisé $(\Omega, T,P)$, avec $\Omega$ = (Pile,Face). On considère la loi de probabilité $P$ telle que : $(\forall \omega\in\Omega)\; P(\omega)=\frac12$

````{prf:definition} Variable aléatoire
Une variable aléatoire est une application $X:\Omega\rightarrow E$ (on prendra $E=\mathbb R$)
```` 

Pour obtenir la probabilité d'une valeur quelconque image par $X$, il suffit de dnombrer les $\omega$ qui réalisent cette valeur. Ici, $P(X=1)= P(\{Pile\}) = \frac12$. On dit que l'on transporte la loi de probabilité de $\Omega$ sur $E$ par l'application $X$.

Les éléments de $E$ sont les **réalisations** de la variable aléatoire.

````{prf:example}
Si l'expérience consiste à observer le résultat du tirage de deux dés à 6 faces, $\Omega = \{(1,1), (1,2), \cdots (6,5), (6,6)\}$, on considère la loi de probabilité telle que $(\forall \omega\in\Omega)\; P(\omega)=\frac{1}{36}$. 

Si l'application $X$ réalise la somme des deux éléments de $\omega\in\Omega$, alors on a par exemple $P(X=3)= P(\{(1,2),(2,1)\}) = \frac{2}{36}$, ou encore $P(X=5)= P(\{(1,4),(2,3),(3,2),(4,1)\}) = \frac{4}{36}$
````

### Variable aléatoire mesurable
On définit sur $E$ une tribu $T'$.  $(E,T')$ est alors un espace probabilisable, et tout élément $B$ de $T'$ est un évènement. On note alors $X^{-1}(B) = \{\omega\in\Omega,\; X(\omega)\in B\}$

````{prf:definition} Variable aléatoire mesurabe
Une variable aléatoire $X$ est dite mesurable  si et seulement si : $(\forall B\in T')\; X^{-1}(B)\in T$
```` 

Dans les deux exemples précédents, on a par exemple $X^{-1}(1)= \{Pile\}$ ou encore $X^{-1}(3) = \{(1,2),(2,1)\}$ et $P(X=3)=P(X^{-1}(3)) = \frac{2}{36}$.

On note souvent $P_X(B) = P(X^{-1}(B))=P(\{\omega / X(\omega)\in B\})$ et on l'appelle **probabilité image** de $P$ par $X$. En calculant la probabilité de chaque réalisation de la variable aléatoire $X$, on peut en déduire la **loi de probabilité** (ou **distribution**) de $X$.

- Pour une variable aléatoire discrète $X$, la loi de probabilité est donc $P_X(x_i)= P(X=x_i) = P(\{\omega / X(\omega)=x_i\})$. $P_X$ est appelée **masse ponctuelle**
- Pour une variable aléatoire continue $X$, la loi de probabilité est donc $f_X(x)dx = P(x\leq X\leq x+dx) = P(\{\omega /x\leq X(\omega)\leq x+dx\})$. $f_X$ est appelée **densité de probabilité**


```{code-cell} ipython3
from math import floor
from random import random
import numpy as np
import matplotlib.pyplot as plt

def tirage():
    d1=floor(6*random()+1)   
    d2=floor(6*random()+1)  
    return d1+d2 -1          

x = np.arange(0,12)+1
f = np.zeros(12)
n=10000                       
for i in range(n):        
    f[tirage() ] += 1
f=f/n                      

plt.plot( x, f, 'o' )   
plt.vlines( x, 0, f )   
plt.ylim( bottom=0 ) 
plt.show()
```



```{prf:definition} Fonction de répartition
La fonction de répartition d'une variable aléatoire $X$ est l'application $F_X$ de $\mathbb R$ dans [0,1] telle que $F_X(x) = P(X\leq x)$.
```

$F_X$ est donc monotone croissante, continue à droite et on a en particulier :  
- $P(a\leq X\leq b) = F_X(b)-F_X(a)$
- $P(X>x) = 1-P(X\leq x) = 1-F_X(x)$


```{code-cell} ipython3
from math import floor
from random import random
import numpy as np
import matplotlib.pyplot as plt

def tirage():
    d1=floor(6*random()+1)   
    d2=floor(6*random()+1)  
    return d1+d2 -1          

x = np.arange(0,12)+1
f = np.zeros(12)
n=10000                       
for i in range(n):        
    f[tirage() ] += 1
f=f/n     

data = np.arange(0, 14)
fn = np.insert(np.cumsum(f), 0, 0)

plt.figure(figsize=(10,5))          
plt.subplot(121)
plt.plot( x, f, 'o' )   
plt.vlines( x, 0, f )   
plt.ylim( bottom=0 ) 
plt.title("Distribution")
plt.subplot(122)

plt.hlines(y=fn, xmin=data[:-1], xmax=data[1:],
          color='red', zorder=1)
plt.vlines(x=data[1:-1], ymin=fn[:-1], ymax=fn[1:], color='red',
          linestyle='dashed', zorder=1)
plt.ylim( bottom=0 ) 
plt.title("Fonction de répartition")
plt.show()
```

La notion de variable aléatoire est ainsi une formalisation de la notion de grandeur variant selon le résultat d'une expérience aléatoire. On peut alors préciser et formaliser la définition précédente.

````{prf:definition} Variable aléatoire
Une variable aléatoire est une application mesurable $X:(\Omega,T,P) \rightarrow (E,T')$ 
```` 

```{prf:remark}
:class: dropdown
- Si $E=\mathbb N$, on parle de variable aléatoire (réelle) discrète
- Si $E=\mathbb R$, on parle de variable aléatoire (réelle) continue. $T'$ est alors la tribu **borélienne**
- Si $E=\mathbb N^n$ ou $E=\mathbb R^n$n on parle de **vecteur aléatoire** de dimension $n$.
```

### Caractéristiques des variables aléatoires
Une loi de probabilité est caractérisée par un certain nombre de grandeurs :
- sa valeur centrale
- sa dispersion
- sa forme

#### Espérance mathématique d'une variable aléatoire

````{prf:definition} Espérance
Soit $X$ une variable aléatoire. On définit l'espérance mathématique de $X$, et on note $\mathbb E(X)$ par :
- $\mathbb E(X) = \mu_X = \displaystyle\sum_{x_i} x_iP(X=x_i)= \displaystyle\sum_{x_i} x_i P_X(x_i)$ si $X$ est discrète et si la somme converge.
- $\mathbb E(X) = \mu_X =\int_x xdP(x) = \int_x x f_X(x) dx$ si $X$ est continue et si l'intégrale converge.
````

$\mathbb E(X)$ est la moyenne arithmétique (également notée $\mu_X$) des différentes valeurs prises par $X$ pondérées par leur probabilité.

On dira que $X$ est **centrée** si $\mathbb{E}(X)=0$.

````{prf:example}
Pour l'expérience d'un lancer de dé à 6 faces  : $\mathbb E(X) = \mu_X = \displaystyle\sum_{i=1}^6 i\frac16 = \frac72$
````

````{prf:property}
- $(\forall a\in\mathbb{R})\; \mathbb{E}(a)= a$
- $(\forall a\in\mathbb{R})\; \mathbb{E}(aX)= a\mathbb{E}(X)$
- $(\forall a\in\mathbb{R})\; \mathbb{E}(X+a) = \mathbb{E}(X) +a$
````

#### Moment d'une fonction d'une variable aléatoire

Soit $\phi$ l'application qui associe à toute variable aléatoire $X$ la variable aléatoire $Y=\phi(X)$.

````{prf:definition} Moment
Le moment  $\mathbb{E}[\phi(X)]$ de la fonction $\phi$ de la variable aléatoire $X$ est égal à :
- $\mathbb{E}[\phi(X)] = \displaystyle\sum_{x_i} \phi(x_i)P_X(x_i)$ si $X$ est discrète
- $\mathbb{E}[\phi(X)] = \int_x \phi(x) f_X(x)dx$ si $X$ est continue
```` 

````{prf:definition} Moment d'ordre $k$
Le moment d'ordre $k$ d'une variable aléatoire $X$ est égal à :
- $\mathbb{E}(X^k) = \displaystyle\sum_{x_i} x_i^k P_X(x_i)$ si $X$ est discrète
- $ \mathbb{E}(X^k) = \int_x x^k f_X(x)dx$ si $X$ est continue
```` 

Le moment d'ordre $k$ est donc un cas particulier avec $Y=X^k$.

```{prf:remark}
:class: dropdown
L'espérance $\mathbb{E}(X)$ est le moment d'ordre 1.
``` 

````{prf:definition} Moment centré d'ordre $k$
On appelle moment centré d'ordre $k$ la quantité $\mathbb{E}\left [(X-\mathbb{E}(X))^k \right]$
````
Ainsi : 
- pour une variable aléatoire discrète $X$, $\mathbb{E}\left [(X-\mathbb{E}(X))^k \right] = \displaystyle\sum_{x_i} (x_i-\mathbb{E}(X))^k P_X(x_i) = \displaystyle\sum_{x_i} (x_i-\mu_X)^k P_X(x_i)$
- pour une variable aléatoire continue $X$, $\mathbb{E}\left [(X-\mathbb{E}(X))^k \right] = \int_x (x-\mathbb{E}(X))^k f_X(x)dx = \int_x (x-\mu_X)^k f_X(x)dx$

#### Variance d'une variable aléatoire

Pour $k$=2, le moment centré d'ordre 2 est appelé la **variance** et est noté $\mathbb{V}(X)$. La racine carrée de la variance est **l'écart type** et est noté $\sigma_X$. On a donc $\sigma_X^2=\mathbb{V}(X)$.

````{prf:proposition} Formule de Koenig
$\mathbb{V}(X) = \mathbb{E}(X^2)-\mu_X^2$ 
````
En effet, $\mathbb{E}\left [(X-\mu_X)^2 \right] = \mathbb{E}\left [(X^2-2\mu_XX+\mu_X^2 \right] = \mathbb{E}(X^2)-2\mu_X\mathbb{E}(X)+\mu_X^2$.

````{prf:property}
- $(\forall a,b\in\mathbb{R})\; \mathbb{V}(aX+b)= a^2\mathbb{V}(X)$
- $(\forall a\in\mathbb{R})\; \mathbb{E}\left [(X-a)^2\right ] = \mathbb V(X) +(\mathbb{E}(X)-a)^2$ (théorème de Huygens)
- $\forall k>0\; P(|X-\mathbb{E}(X)|\geq k\sigma_X)\leq \frac{1}{k^2}$ (inégalité de Bienaymé-Tchebychev)
````

On dira que la variable aléatoire $X$ est **réduite** (ou **normée**) si $\mathbb{V}(X)=1$.

#### Moments d'ordre supérieur
On considère également souvent les moments d'ordre 3 (coefficient d'asymétrie ou skewness) et 4 (coefficient d'applatissement ou kurtosis).

