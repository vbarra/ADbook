# Expérience aléatoire

## Définitions
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

## Notation et opérations sur les évènements
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


