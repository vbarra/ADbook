#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy import stats
import scipy
import warnings
warnings.simplefilter('ignore', DeprecationWarning)


# # Distributions de probabilité discrètes

# ## Distribution Binomiale

# ### Variables aléatoires de Bernoulli

# - Expériences à deux issues,  0 ou 1
# - Variable aléatoire de Bernoulli de paramètre  $p$, $0 \leq p \leq 1$, $p$ probabilité que l'issue soit 1
# - The Bernoulli distribution $Ber(p)$ is:
# \begin{equation}
#     f(x;p) = p^x(1-p)^{1-x}, \text{   } x= 0,1
# \end{equation}
# - $\mathbb E(X) = p$
# - $\mathbb V(X) = p(1-p)$

# In[2]:


from scipy.stats import bernoulli
n = 10 #nombre de répétitions de l'expérience
p = 0.3 # probabilité de succès
print("Moyenne : ", bernoulli.mean(p))
print("Variance: ", bernoulli.var(p))


# ## Distribution binomiale

# - Expérience : $n$ expériences indépendantes de Bernoulli $X_1, \cdots, X_n$ de même paramètre $p$
# - Le nombre total de succès $X = \displaystyle\sum_{i=1}^m X_i$ est une variable aléatoire de distribution (binomiale)
# \begin{equation}
#     X \sim B(n,p)
# \end{equation}
# de paramètres $n$ et $p$

# - La densité de probabilité $B(n, p)$ est :
# $$
#     f(x;n,p) = \binom{n}{x}p^x(1-p)^{n-x}, \text{   } x= 0,1, \cdots, n
# $$
# 
# - $\mathbb E(X) = np$
# - $\mathbb V(X) = np(1-p)$

# In[3]:


from scipy.stats import binom

n = 10 
x = 7 
p = 0.2 

print("Moyenne : ", binom.mean(n, p))
print("Variance: ", binom.var(n, p))
print("Densité de probabilité : ", binom.pmf(x, n, p))
print("Fonction de répartition : ", binom.cdf(x,n,p))


# ### Proportion de succès

# - Si $X \sim B(n,p)$. alors, si $Y = \frac{X}{n}$
# - $\mathbb E(Y) = p$
# - $\mathbb V(Y) = \frac{p(1-p)}{n}$

# ## Distributions Géométrique et binomiale négative

# ### Distribution géométrique
# 
# - Le nombre d'essais  $X$ jusqu'au premier succès (inclus) dans une suite d'expériences indépendantes de Bernoulli de même paramètre $p$ suit une distribution géométrique de paramètre $p$
# - Densité de probabilité :
# \begin{equation}
#     P(X = x) = (1 - p)^{x-1}p, \text{   } x=1,2, \cdots.
# \end{equation}
# - Fonction de répartition :
# \begin{equation}
#     P(X \leq x) = 1 - (1-p)^x
# \end{equation}
# - $\mathbb E(X) = \frac{1}{p}$
# - $\mathbb V(X) = \frac{1-p}{p^2}$

# In[4]:


from scipy.stats import geom
x = 5 
p = 0.23 
print("Moyenne : ", geom.mean(p))
print("Variance: ", geom.var(p))
print("Densité de probabilité : ", geom.pmf(x, p))
print("Fonction de répartition : ", geom.cdf(x, p))


# ### Distribution binomiale négative

# - Le nombre d'essais  $X$ jusqu'au $r^e$ succès (inclus) dans une suite d'expériences indépendantes de Bernoulli de même paramètre $p$ suit une distribution binomiale négative de paramètre $p$
# - Densité de probabilité :
# \begin{equation}
#     P(X = x) =  \binom{x-1}{r-1} (1-p)^{x-r}p^r \text{,  } x=r,r+1, \cdots.
# \end{equation}
# - $\mathbb E(X) = \frac{r}{p}$
# - $\mathbb V(X) = \frac{r(1-p)}{p^2}$

# In[5]:


from scipy.stats import nbinom
x = 7 
r = 4 
p = 0.55 

print("Moyenne: ", nbinom.mean(r, p))
print("Variance: ", nbinom.var(r, p))
print("Densité de probabilité : ", nbinom.pmf(x-r, r, p)) # the distribution takes x-r, which is the number of failures
print("Fonction de répartition : ", nbinom.cdf(x-r, r, p))


# ##  Distribution hypergéométrique

# - Collection de $N$ objets dont $r$ sont d'un certain type
# - Probabilité qu'un objet soit d'un type donné: $p = \frac{r}{N}$
# - Si $n$ objets sont choisis au hasard sans remise, la distribution de $X \sim B(n,p)$

# - Densité de probabilité : 
# \begin{equation}
#     f(x; N, n, r) = \frac{ \binom{r}{x} \binom{N-r}{n-x} }{ \binom{N}{n} },
# \end{equation}
# \begin{equation}
#     max \{ 0, n-(N-r) \} \leq x \leq min \{ n, r \}
# \end{equation}
# - $\mathbb E(X) = n\frac{r}{N}$
# - $\mathbb V(X) = \frac{N-n}{N-1} n \frac{r}{N}(1- \frac{r}{N})$

# - Comparaison avec $B(n,p)$ lorsque $ p = \frac{r}{N}$
#     - $\mathbb E_B(X) = \mathbb E_H(X) = np$
#     - $\sigma_B ^2 (X) = npq \geq \sigma_H ^2(X) = \frac{N-n}{N-1} npq$

# In[6]:


from scipy.stats import hypergeom

x = 2 
N = 15 
r = 9 
n = 5 

print("Moyenne : ", hypergeom.mean(N, r, n))
print("Variance: ", hypergeom.var(N, r, n))
print("Densité de probabilité : ", hypergeom.pmf(x, N, r, n))
print("Fonction de répartition : ", hypergeom.cdf(x, N, r, n))


# ##  Distribution de Poisson

# - Nombre d'évènements se produisant dans un certain intervalle (temps, espace)
# - Une variable aléatoire $X$ suit une distribution de Poisson de paramère $\lambda$ s'écrit :
# \begin{equation}
#     X \sim P(\lambda)
# \end{equation}
# - Densité de probabilité : 
# \begin{equation}
#     P(X = x) = \frac{ e^{- \lambda} \lambda ^ {x}} {x!} \text{   } x=0,1,2, \cdots.
# \end{equation}
# - $\mathbb E (X) = \mathbb V (X) = \lambda$

# In[7]:


from scipy.stats import poisson

x = 1 
Lambda = 2/3 

print("Moyenne : ", poisson.mean(Lambda))
print("Variance: ", poisson.var(Lambda))
print("Densité de probabilité : ", poisson.pmf(x, Lambda))
print("Fonction de répartition : ", poisson.cdf(x, Lambda))


# ## Distribution multinomiale

# - Suite de $n$ essais indépendants où chaque essai a  $k$ issues possibles de probabilités constantes $p_1, p_2, \cdots , p_k$ avec $p_1 + p_2 + \cdots + p_k = 1$
# - Les variables aléatoires $X_1, X_2, \cdots , X_k$ avec $\displaystyle\sum_{i=1}^k X_i = n$ qui comptent le nombre d'occurrences des $k$ issues respectives ont une distribution multinomiale.

# - Densité de probabilité jointe de  $X_1, X_2, \cdots , X_k$ :
# \begin{equation}
#     f(x_1, x_2, \cdots, x_k; p_1, \cdots , p_k , n) = \binom{n}{x_1,x_2,\cdots, x_k} p_1^{x_1} p_2^{x_2} \cdots p_k^{x_k}
# \end{equation}
# avec $\displaystyle\sum_{i=1} ^ k x_i = n$ et $\displaystyle\sum_{i=1}^k p_i = 1$
# - ce qui s'écrit encore :
# \begin{equation}
#     (X_1, \cdots , X_k) \sim M_k(p_1, \cdots, p_k, n)
# \end{equation}

# - $\mathbb E(X_i) = np_i$
# - $\mathbb V(X_i) = np_i(1-p_i)$

# In[8]:


from scipy.stats import multinomial

x = [3, 3, 4, 5] 
n = 15 
p = [1/6, 1/6, 1/6 , 3/6] 

print("Densité de probabilité : ", multinomial.pmf(x, n=n, p=p))

