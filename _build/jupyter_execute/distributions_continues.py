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
# \begin{equation}
#     f_X(x) = \frac{1}{b-a} \text{ , } a \leq x \leq b
# \end{equation}
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
# \begin{equation}
#     f_X(x) = \lambda e ^ {- \lambda x} \text{ , } x > 0
# \end{equation}
# - Fonction de répartition:
# \begin{equation}
#     F_X(x) = 1 - e^{\lambda x}
# \end{equation}
# - $\mathbb E(X) = \frac{1}{\lambda}$
# - $\mathbb V(X) = \frac{1}{\lambda^2}$

# In[3]:


from scipy.stats import expon

Lambda = 0.5 
x = 1 

print("Espérance: ", expon.mean(scale = Lambda))
print("Variance: ", expon.var(scale = Lambda))
print("Densité de probabilité: ", expon.pdf(x, scale = Lambda))
print("Fonction de répartition: ", expon.cdf(x, scale = Lambda))


# ### The memoryless property of the Exponential Distribution

# - For any non-negative $x$ and $y$
# \begin{equation}
#     P(X \geq x + y \mid X \geq x) = P( X \geq y)
# \end{equation}
# - This is equivalent to:
# \begin{equation}
#     P(X \geq x + y, X \geq x) = P( X \geq x) P( X \geq y)
# \end{equation}
# - Meaning: the future does not depend on the past

# - Proposition: if $ X_1, \cdots, X_n $ are independent exponential random variables having respective parameters $\lambda_1 , \cdots, \lambda_n$, then $min \{ X_1, \cdots , X_n \} $ is the exponential random variable with paramenter $\sum_{i = 1}^n \lambda_i$

# ### The Poisson process

# - A stochastic process is a sequence of random events
# - Poisson process with parameter $\lambda$: a stochastic process where the time (or space) intervals between events-occurrences follow the Exponential Distribution with parameter $\lambda$
# - If $X$ is the number of events occurring within a fixed time (or space) interval of length $t$, then
# \begin{equation}
#     X \sim Poi(\lambda t)
# \end{equation}
# 

# ## The Gamma Distribution

# ### Definition of the Gamma distribution

# - Useful for describing reliability
# - Gamma function:
# \begin{equation}
#     \Gamma(k) = \int_0^{\infty} x^{k-1}e^{-x}dx \text{ for } k>0
# \end{equation}

# In[4]:


from scipy.special import gamma as gamma_function
k = 4 # parameter of the gamma function
print("Gamma function result: ", gamma_function(k))


# - Gamma distribution $Gam(k, \lambda)$ with $k>0$ and $\lambda >0$
# \begin{equation}
#     f(x; k, \lambda) = \frac{\lambda ^k}{\Gamma (k)} x ^ {k-1} e ^ {- \lambda x} \text{ , } x > 0
# \end{equation}
# - $ E(X) = \frac{k}{ \lambda }$
# - $ Var(X) = \frac{k}{ \lambda ^2}$

# In[5]:


from scipy.stats import gamma

# Parameters
x = 3 # number of events
k = 3 # parameter of the gamma function
Lambda = 1.8 # lambda parameter

print("Mean: ", gamma.mean(k,  scale = 1/Lambda))
print("Variance: ", gamma.var(k, scale = 1/Lambda))
print("Probability mass function: ", gamma.pdf(x, k,  scale = 1/Lambda))
print("Cumulative distribution function: ", gamma.cdf(x, k, scale = 1/Lambda))
print("Survival function (1-cdf): ", gamma.sf(x, k, scale = 1/Lambda))


# ### Properties of the Gamma function

# - $\Gamma (\alpha + 1) = \alpha \Gamma(\alpha)$
# - $\Gamma (1) = 1$
# - $\Gamma (1/2) = \sqrt{\pi}$
# - $\Gamma (n) = (n-1) !$

# ### Properties of the Gamma distribution 

# - If $X_1, \cdots, X_n$ are independent Gamma random variables with respective parameters $(k_i, \lambda)$, then
# \begin{equation}
#     \sum_{i=1}^n X_i \sim Gam(\sum_{i=1}^n k_i , \lambda)
# \end{equation}

# ## Weibull Distribution
# 

# ### Definition of the Weibull Distribution

# - Useful for modeling failure and waiting times
# - If $X \sim Exp(1)$ and $Y = \frac{1}{\lambda} x ^ { \frac{1}{a}}$ for $ a>0$, $\lambda > 0$ ,then 
# \begin{equation}
#     Y \sim Weibull(\lambda, a)
# \end{equation}
# 

# - Probability distribution function of $Weibull(\lambda, a)$
# \begin{equation}
#     f(y) = a \lambda (\lambda y )^{a-1} e^{- (\lambda y) ^a} \text{ for } a>0 \text{ , } \lambda > 0
# \end{equation}
# - If $a = 1$, the Weibull distribution is the same as the Exponential distribution with parameter $\lambda$
# - Cumulative distribution function:
# \begin{equation}
#     F(y) = 1 - e^{- (\lambda y) ^a}
# \end{equation}
# - $E(Y) = \frac{1}{\lambda} \Gamma(1 + \frac{1}{a})$
# - $Var(Y) = \frac{1}{\lambda ^2} \Big\{  \Gamma(1 + \frac{2}{a}) - \big[ \Gamma(1 + \frac{1}{a}) \big]^2 \Big\} $

# In[6]:


from scipy.stats import weibull_min

# Parameters
x = 8 # number of events
a = 2.3 # a parameter
Lambda = 0.09 # lambda parameter

print("Mean: ", weibull_min.mean(a)) # not sure about this
print("Variance: ", weibull_min.var(a)) # not sure about this
print("Probability mass function: ", weibull_min.pdf(x*Lambda, a))
print("Cumulative distribution function: ", weibull_min.cdf(x*Lambda, a ))
print("Survival function (1-cdf): ", weibull_min.sf(x*Lambda, a))


# ## The Beta Distribution

# ### Definition of the Beta Distribution

# - Useful for modeling proportions and personal probability
# - Probability distribution function:
# \begin{equation}
#     f(x; \alpha, \beta) = \frac{\Gamma( \alpha + \beta)}{ \Gamma(\alpha) \Gamma(\beta)} x^{\alpha - 1} (1 - x) ^{\beta - 1} \text{ , } 0 < x < 1
# \end{equation}
# - $E(X) = \frac{ \alpha}{ \alpha + \beta}$
# - $Var(X) = \frac{ \alpha \beta}{ (\alpha + \beta) ^2 ( \alpha + \beta + 1)}$
# 

# In[7]:


from scipy.stats import beta

# Parameters
x = 0.7 # (number of events?)
a = 10 # alpha parameter
b = 4 # beta parameter

print("Mean: ", beta.mean(a, b)) # not sure about this
print("Variance: ", beta.var(a, b)) # not sure about this
print("Probability mass function: ", beta.pdf(x, a, b))
print("Cumulative distribution function: ", beta.cdf(x, a, b ))
print("Survival function (1-cdf): ", beta.sf(x, a, b))

