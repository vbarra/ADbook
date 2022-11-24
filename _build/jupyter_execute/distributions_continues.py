#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy import stats
import scipy
import warnings
warnings.simplefilter('ignore', DeprecationWarning)


# # Distributions de probabilité continues

# ## Distribution uniforme

# - Distribution uniforme dans $[\![a,b]\!]$,  $U(a,b)$:
# 
# $
#     f_X(x) = \frac{1}{b-a} \text{ , } a \leq x \leq b
# $
# 
# - $\mathbb E(x) = \frac{a+b}{2}$
# - $\mathbb V(x) = \frac{(b-a)^2}{12}$

# In[2]:


from scipy.stats import uniform

a = 1 
b = 5 

print("Espérance: ", (a+b)/2 )
print("Variance: ", (b-a)**2/12 )


# ## Distribution exponentielle

# ### Définition

# - $Exp( \lambda )$, $\lambda$ pouvant être interprété comme un taux d'occurence
# - Décrit souvent le temps avant qu'un évènement se produise
# - Densité de probabilité :
# $
#     f_X(x) = \lambda e ^ {- \lambda x} \text{ , } x > 0
# $
# - Fonction de répartition:
# $
#     F_X(x) = 1 - e^{\lambda x}
# $
# - $\mathbb E(X) = \frac{1}{\lambda}$
# - $\mathbb V(X) = \frac{1}{\lambda^2}$

# In[3]:


from scipy.stats import expon

Lambda = 0.5 
x = 1 

print("Espérance : ", expon.mean(scale = Lambda))
print("Variance : ", expon.var(scale = Lambda))
print("Densité de probabilité : ", expon.pdf(x, scale = Lambda))
print("Fonction de répartition : ", expon.cdf(x, scale = Lambda))


# ### La distribution exponentielle n'a pas de mémoire ...

# - Pour tout $x,y>0, 
#     P(X \geq x + y \mid X \geq x) = P( X \geq y)$
# - ce qui est équivalent à
# $
#     P(X \geq x + y, X \geq x) = P( X \geq x) P( X \geq y)
# $
# 
# $\Rightarrow$ le futur ne dépend pas du passé

# **Proposition** : si $ X_1, \cdots, X_n $ sont des variables aléatoires indépendantes de paramètres respectifs $\lambda_1 , \cdots, \lambda_n$, alors $min \{ X_1, \cdots , X_n \} $ suit une loi exponentielle de paramètre  $\sum_{i = 1}^n \lambda_i$

# ### Processus de Poisson

# - Un processus stochastique est une suite d'évènements aléatoires
# - Processus de Poisson de paramètre $\lambda$ = processus stochastique où le temps (ou l'espace) entre deux occurrences d'évènements  suit une loi exponentielle de paramètre $\lambda$
# - Si $X$ est le nombre d'évènements se produisant dans un intervalle de temps (ou d'espace) de longueur $t$ alors 
# $
#     X \sim Poisson(\lambda t)
# $
# 

# ## Distribution Gamma

# - Utile en fiabilité
# - Fonction Gamma :
# 
# $
#     \Gamma(k) = \int_0^{\infty} x^{k-1}e^{-x}dx \text{ for } k>0
# $

# In[4]:


from scipy.special import gamma as gamma_function
k = 4
print("Fonction Gamma: ", gamma_function(k))


# - Distribution Gamma $Gam(k, \lambda)$ où $k>0$ et $\lambda >0$
# 
# $
#     f(x; k, \lambda) = \frac{\lambda ^k}{\Gamma (k)} x ^ {k-1} e ^ {- \lambda x} \text{ , } x > 0
# $
# 
# - $ \mathbb E(X) = \frac{k}{ \lambda }$
# - $ \mathbb V(X) = \frac{k}{ \lambda ^2}$

# In[5]:


from scipy.stats import gamma

x = 3 # nombre d'évènements
k = 3 # paramètre de la fonction gamma
Lambda = 1.8 

print("Moyenne : ", gamma.mean(k,  scale = 1/Lambda))
print("Variance : ", gamma.var(k, scale = 1/Lambda))
print("Densité de probabilité : ", gamma.pdf(x, k,  scale = 1/Lambda))
print("Fonction de répartition : ", gamma.cdf(x, k, scale = 1/Lambda))


# ### Propriétés de la fonction Gamma

# - $\Gamma (\alpha + 1) = \alpha \Gamma(\alpha)$
# - $\Gamma (1) = 1$
# - $\Gamma (1/2) = \sqrt{\pi}$
# - $\Gamma (n) = (n-1) !$

# ### Propriétés de la distribution Gamma

# - Si $X_1, \cdots, X_n$ sont des variables aléatoires indépendantes Gamma de paramètres respectifs $(k_i, \lambda)$, alors
# 
# $
#     \sum_{i=1}^n X_i \sim Gam(\sum_{i=1}^n k_i , \lambda)
# $

# ## Distribution Beta

# - Modélisation des proportions
# 
# $
#     f(x; \alpha, \beta) = \frac{\Gamma( \alpha + \beta)}{ \Gamma(\alpha) \Gamma(\beta)} x^{\alpha - 1} (1 - x) ^{\beta - 1} \text{ , } 0 < x < 1
# $
# 
# - $\mathbb E(X) = \frac{ \alpha}{ \alpha + \beta}$
# - $\mathbb V(X) = \frac{ \alpha \beta}{ (\alpha + \beta) ^2 ( \alpha + \beta + 1)}$
# 

# In[6]:


from scipy.stats import beta

x = 0.7 
a = 10 
b = 4 

print("Moyenne : ", beta.mean(a, b)) # not sure about this
print("Variance: ", beta.var(a, b)) # not sure about this
print("Densité de probabilité : ", beta.pdf(x, a, b))
print("Fonction de répartition : ", beta.cdf(x, a, b ))

