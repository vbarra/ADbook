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

# Exercices

## Exercice 1

Soient $n\leq 365$ personnes. On suppose qu’une année dure 365 jours. On suppose aussi que toutes les dates de naissance sont équiprobables.
1. Exprimer en fonction de $n$ la probabilité $P$ qu’un groupe de $n$ personnes choisies au hasard dans la rue soit tel que toutes les dates de naissance soient différentes (jour et mois seulement).
2. Ecrire un code Python représentant $P$ pour $n$ variant de 1 à 40.
3. Combien faut-il de personnes au minimum pour que $P\leq 0.5$?
4. Combien faut-il de personnes au minimum pour que $P\leq 0.2$ ?
5. Si $n$=50, quelle est la probabilité que deux au moins de ces personnes aient la même date anniversaire ?


````{admonition} Solution
:class: dropdown
1. $P\approx 0.9973$
3. $n=23$
4. $n=35$
5. la probabilité est approximativement égale à 0.97
````

Le code Python de la question 2 peut s'écrire
```{code-cell} ipython3
import matplotlib.pyplot as plt 
import math
N=41 
n=[]
P=[]
t=1

for j in range(1,N):
    n.append(j)
    t=t*(1-(j-1)/365) 
    P.append(t) 
plt.figure()
plt.subplot(211)
plt.plot(n,P,color='red',label='proba dates differentes')
plt.plot(n,P,'k+')
plt.xlabel('n')
plt.ylabel('P')
plt.title('probleme des anniversaires')
plt.grid(True)
plt.legend()
plt.subplot(212)
plt.plot(n,P,color='red',label='proba dates differentes')
plt.plot(n,P,'k+')
plt.xlim(15,25)
plt.ylim(0.4,0.7)
plt.ylabel('P') 
plt.grid(True) 
plt.legend()
plt.show()
```





