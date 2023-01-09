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


# ## Distribution normale

# ### Définition générale

# -  $N( \mu, \sigma)$:$
#     f(x; \mu, \sigma) = \frac{1}{\sqrt{2 \pi} \sigma } e ^{- \frac{(x - \mu) ^2}{2 \sigma ^2}}$
# - $\mu$ et la moyenne $\sigma$ l'écart type, $\sigma^2$ la variance

# In[3]:


from scipy.stats import norm

x = 1.3 
mu = 0 
sigma = 1 

print("Moyenne : ", norm.mean(loc = mu, scale = sigma))
print("Variance : ", norm.var(loc = mu, scale = sigma)) 
print("Densité de probabilité : ", norm.pdf(x, loc = mu, scale = sigma))
print("Fonction de répartition : ", norm.cdf(x, loc = mu, scale = sigma))


# ### Loi normale centrée réduite

# $\mu = 0$ et  $\sigma = 1$
# - Densité de probabilité :
# $
#     f(x) = \frac{1}{\sqrt{2 \pi}} e ^{- \frac{x ^2}{2}}
# $
# - Fonction de répartition: $\Phi(x)$ 

# ### Calcul de probabilités

# - $X \sim N(\mu, \sigma^2) \Longrightarrow Z = \frac{X - \mu}{\sigma} \sim N(0,1)$
# - Donc, $P(a \leq X \leq b) = P \left( \frac{ a - \mu}{ \sigma} \leq \frac{ X - \mu}{ \sigma} \leq \frac{ b - \mu}{ \sigma} \right) = P \left( \frac{ a - \mu}{ \sigma} \leq Z \leq \frac{ b - \mu}{ \sigma} \right) = \Phi \left(\frac{ b - \mu}{ \sigma} \right) - \Phi \left( \frac{a - \mu}{ \sigma} \right)$
# - Propriétés :
#     - $P( \mu -c \sigma \leq X \leq \mu + c \sigma) = P(-c \leq Z \leq c)$
#     - $P(X \leq \mu + \sigma z_{\alpha}) = P(Z \leq z_ {\alpha}) = 1 - \alpha$

# In[4]:


from scipy.stats import norm

x = 1300 
mu = 1320 
sigma = 15 

Z = (x - mu)/sigma


print("Moyenne : ", mu) 
print("Variance: ", sigma**2) 
print("Densité de probabilité : ", norm.pdf(Z))
print("Fonction de répartition : ", norm.cdf(Z))


# ### Distributions reliées à la loi normale

# **Loi log normale** 
# - $Y = ln(X) \sim N(\mu, \sigma^2)$
# - Densité de probabilité :
# $
#     f(x) = \frac{1}{\sqrt{2\pi} \sigma x} e^{ - \frac{ (ln(x) - \mu)^2}{2 \sigma ^2}} \text{ pour } x > 0
# $
# 
# - Fonction de répartition : 
# $    F(x) = \Phi( \frac{ln (x) - \mu}{\sigma})
# $
# - $E(X) = e^{ \mu + \frac{ \sigma ^2}{2}} $
# - $ Var(X) = e^{ 2\mu + \sigma^2} ( e^{\sigma^2} -1)$
# 
# **Distribution du $\chi^2$**
# - $X_i \sim N(0,1)$ et $X = \sum_{i =1}^ v X_i ^2$, et $X_i$ sont indépendants. Alors $X \sim \chi_\nu^2$ où $\nu$ est le nombre de degrés de libertés de la distribution
# - Densité de probabilité :
# $
#     f(x) = \frac{ \frac{1}{2} e ^ {-x/2} (\frac{x}{2} ) ^ { \frac{\nu}{2} -1} } { \Gamma( \frac {\nu}{2} )}
# $
# 
# $
#     \chi_{\nu}^2 = \Gamma( \frac{ \nu}{2} , \frac{1}{2} )
# $ (Voir plus bas)
# 
# - $E(X) = \nu$
# - $Var(X) = 2 \nu$
# 
# **Distribution t**
# - Etant donné $ Z \sim N(0,1)$ et $W \sim \chi_{\nu} ^2$ où $Z$ et $W$ are indépendants, alors
# $
#     T_{\nu} = \frac{Z} {\sqrt{ W/ \nu }} \sim t_{\nu}
# $ 
# est une distribution t à $\nu$ degrés de liberté
# 
# 
# **Distribution F**
# - $W_i \sim \chi_{\nu_i}^2$ pour $ i = 1,2$ indépendants. Alors
# $
#     \frac{W_1/  \nu_1}{W_2 / \nu_2} \sim F_{\nu_1 , \nu_2}
# $
# est une distribution F de degrés de liberté $\nu_1, \nu_2$
# - $F_{1 - \alpha, \nu_1, \nu_2} = \frac{1}{ F_{\alpha, \nu_1, \nu_2}}$
# 
# **Loi normale multivariée**
# - Loi bivariée $(X,Y)$ de paramètres $\mu_1 , \mu_2 , \sigma_1^2 , \sigma_2^2 , \rho$, où $\mu_1 = E(X)$
# - Variables : $\mu_1 = E(X), \mu_2 = E(Y) , \sigma_1^2 = Var(X)  , \sigma_2^2 = Var(Y) , \rho = Corr(X,Y)$
# - Densité de probabilité jointe de $(X,Y)$:
# $
#     f(x,y) = \frac{1}{2 \pi \sigma_1 \sigma_2 \sqrt{ 1- \rho ^2} } e^ { \left( - \frac{1}{2 (1 - \rho^2)} \left[ x^2 + y^2 -2 \rho xy \right] \right) } \text{ pour } x< \infty, y < \infty
# $
# 
# - En particulier, lorsque $\mu_1 = \mu_2 = 0 $ et $\sigma_1 = \sigma_2 = 1$
# $
#     f(x,y) = \frac{1}{2 \pi \sqrt{1 - \rho^2}} e^ { \left( - \frac{1}{2 (1 - \rho^2)} \left[ x^2 + y^2 -2 \rho x y \right] \right) }
# $
# - Lorsque $\mu_1 = \mu_2 = 0 $ et $\sigma_1 = \sigma_2 = 1$ et indépendance entre  $X$ et $Y$, alors $\rho = 0$
# $
#     f(x,y) = \frac{1}{2 \pi} e^ { \left( - \frac{1}{2} \left[ x^2 + y^2 \right] \right) }
# $

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

# In[5]:


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

# In[6]:


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

# In[7]:


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

# In[8]:


from scipy.stats import beta

x = 0.7 
a = 10 
b = 4 

print("Moyenne : ", beta.mean(a, b)) # not sure about this
print("Variance: ", beta.var(a, b)) # not sure about this
print("Densité de probabilité : ", beta.pdf(x, a, b))
print("Fonction de répartition : ", beta.cdf(x, a, b ))

