# Probabilités
## Objectif
L'objectif des probabilités est de donner une **mesure** à la chance qu'a un évènement de se réaliser lors d'une expérience aléatoire. Pour ce faire, on définit une fonction $P:\Omega\rightarrow [0,1]$ vérifiant certains axiomes et propriétés.

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

## Probabilité
```{margin} A. Kolmogorov
![](./images/kolmogorov.jpeg)
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
## Conditionnement
Les probabilités **conditionnelles** intègrent une information supplémentaire sous la forme de l'observation de la réalisation d'un évènement donné.
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

## Indépendance
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

## Théorème des probabilités totales

```{prf:theorem}
Soit $B_i$ un système complet d'évènements (qui forment donc une partition de $\Omega$). Pour tout évènement $A$, on peut écrire 

$P(A) = \displaystyle\sum_i P(A\bigcap B_i) = \displaystyle\sum_i P(A| B_i) P(B_i)$
```

\`A partir de l'égalité $P(A\bigcap B) = P(A|B)P(B)=P(B|A)P(A), on définit la règle de Bayes

$(\forall A,B)\quad P(B|A)=\frac{P(B)P(A|B)}{P(A)}$

et en utilisant le théorème des probabilités totales on a

````{prf:property}

$(\forall A,B_i,i\in[\![1,n]\!])\quad \frac{}{}
````




