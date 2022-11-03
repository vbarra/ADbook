#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Import here useful libraries
Run this cell first for convenience
'''
import numpy as np
from scipy import stats
import scipy
import warnings
warnings.simplefilter('ignore', DeprecationWarning)


# # Chapter 3 - Discrete Probability Distributions

# ## The Binomial Distribution

# ### Bernoulli Random Variables

# - Modeling of a process with two possible outcomes, labeled 0 and 1
# - Random variable defined by the parameter $p$, $0 \leq p \leq 1$, which is the probability that the outcome is 1
# - The Bernoulli distribution $Ber(p)$ is:
# \begin{equation}
#     f(x;p) = p^x(1-p)^{1-x}, \text{   } x= 0,1
# \end{equation}
# - $E(X) = p$
# - $Var(X) = p(1-p)$

# In[2]:


from scipy.stats import bernoulli
n = number of trials
p = 0.3 # probability of success
print("Mean: ", bernoulli.mean(p))
print("Variance: ", bernoulli.var(p))


# ### Definition of the Binomial Distribution

# - Let's consider and experiment consisting of $n$ Bernoulli trials $X_1, \cdots, X_n$ independent and with a constant probability $p$ of success
# - Then the total number of successes $X = \sum_{i=1}^m X_i$ is a random variable whose Binomial distribution with parameters $n$ (number of trials) and $p$ is:
# \begin{equation}
#     X \sim B(n,p)
# \end{equation}

# - Probability mass function of a $B(n, p)$ random variable is:
# \begin{equation}
#     f(x;n,p) = \binom{n}{x}p^x(1-p)^{n-x}, \text{   } x= 0,1, \cdots, n
# \end{equation}
# - $E(X) = np$
# - $Var(X) = np(1-p)$

# In[15]:


from scipy.stats import binom

# Parameters
n = 10 # number of trials
x = 7 # number of successes
p = 0.2 # probability of success

print("Mean: ", binom.mean(n, p))
print("Variance: ", binom.var(n, p))
print("Probability mass function: ", binom.pmf(x, n, p))
print("Cumulative distribution function: ", binom.cdf(x,n,p))


# ### Proportion of successes in Bernoulli Trials

# - Let $X \sim B(n,p)$. Then, if $Y = \frac{X}{n}$
# - $E(Y) = p$
# - $Var(Y) = \frac{p(1-p)}{n}$

# ## The Geometric and Negative Binomial Distributions

# ### Definition of the Geometric Distribution

# - Number of $X$ of trials up to and including the first success in a sequence of independent Bernoulli trials with a constant success probability $p$ has a geometric distribution with parameter $p$
# - Probability mass function:
# \begin{equation}
#     P(X = x) = (1 - p)^{x-1}p, \text{   } x=1,2, \cdots.
# \end{equation}
# - Cumulative distribution function:
# \begin{equation}
#     P(X \leq x) = 1 - (1-p)^x
# \end{equation}
# - $E(X) = \frac{1}{p}$
# - $Var(X) = \frac{1-p}{p^2}$

# In[26]:


from scipy.stats import geom
x = 5 # number of trials up to and including the first success
p = 0.23 # probability of success
print("Mean: ", geom.mean(p))
print("Variance: ", geom.var(p))
print("Probability mass function: ", geom.pmf(x, p))
print("Cumulative distribution function: ", geom.cdf(x, p))


# ### Definition of the Negative Binomial Distribution

# - Number $X$ of trials up and including the $r$th success in a sequence of independent Bernoulli trials with a consant success probability $p$ has a negative binomial distribution with parameter $p$
# - Probability mass function:
# \begin{equation}
#     P(X = x) =  \binom{x-1}{r-1} (1-p)^{x-r}p^r \text{,  } x=r,r+1, \cdots.
# \end{equation}
# - $E(X) = \frac{r}{p}$
# - $Var(X) = \frac{r(1-p)}{p^2}$

# In[29]:


from scipy.stats import nbinom
x = 7 # number of trials up and including the r-th success
r = 4 # number of successes
p = 0.55 # probability of success
#########################################NOT WORKING!!!!!!!!!!!####################
print("Mean: ", nbinom.mean(r, p))
print("Variance: ", nbinom.var(r, p))
print("Probability mass function: ", nbinom.pmf(x-r, r, p)) # the distribution takes x-r, which is the number of failures
print("Cumulative distribution function: ", nbinom.cdf(x-r, r, p))


# ## Hypergeometric Distribution

# ### Definition of the Hypergeometric Distribution

# - Consider a collection of $N$ items of which $r$ are of a certain kind
# - Probability the item is of the special kind: $p = \frac{r}{N}$
# - If $n$ items are chosen at random without replacement, then the distribution of $X \sim B(n,p)$

# - Hypergeometric distribution: $n$ items chosen at random without replacement
# - Probability mass function:
# \begin{equation}
#     f(x; N, n, r) = \frac{ \binom{r}{x} \binom{N-r}{n-x} }{ \binom{N}{n} },
# \end{equation}
# \begin{equation}
#     max \{ 0, n-(N-r) \} \leq x \leq min \{ n, r \}
# \end{equation}
# - $E(X) = n\frac{r}{N}$
# - $Var(X) = \frac{N-n}{N-1} n \frac{r}{N}(1- \frac{r}{N})$

# - Comparison with $B(n,p)$ when $ p = \frac{r}{N}$
#     - $E_B(X) = E_H(X) = np$
#     - $\sigma_B ^2 (X) = npq \geq \sigma_H ^2(X) = \frac{N-n}{N-1} npq$

# In[46]:


from scipy.stats import hypergeom

x = 2 # number of rare elements picked
N = 15 # total number of elements
r = 9 # number of rare elements
n = 5 # picked up elements

print("Mean: ", hypergeom.mean(N, r, n))
print("Variance: ", hypergeom.var(N, r, n))
print("Probability mass function: ", hypergeom.pmf(x, N, r, n))
print("Cumulative distribution function: ", hypergeom.cdf(x, N, r, n))


# ## The Poisson Distribution

# ### Definition of the Poisson Distribution

# - Describes the number of "events" occurring within certain specified boundaries of space and time
# - A random variable $X$ distributed as a Poisson random variable with parameter $\lambda$ is written as:
# \begin{equation}
#     X \sim P(\lambda)
# \end{equation}
# - Probability mass function:
# \begin{equation}
#     P(X = x) = \frac{ e^{- \lambda} \lambda ^ {x}} {x!} \text{   } x=0,1,2, \cdots.
# \end{equation}
# - $Eprint("Mean: ", multinomial.mean(x, p))(X) = Var(X) = \lambda$

# In[51]:


from scipy.stats import poisson

# Parameters
x = 1 # number of events
Lambda = 2/3 # lambda parameter

print("Mean: ", poisson.mean(Lambda))
print("Variance: ", poisson.var(Lambda))
print("Probability mass function: ", poisson.pmf(x, Lambda))
print("Cumulative distribution function: ", poisson.cdf(x, Lambda))


# ## The Multinomial Distribution

# ### Definition of the Multinomial Distribution

# - Consider a sequence of $n$ independent trials in which each individual trial can have $k$ outcomes occurring with a constant probability value $p_1, p_2, \cdots , p_k$ with $p_1 + p_2 + \cdots + p_k = 1$
# - The random variables $X_1, X_2, \cdots , X_k$ with $\sum_{i=1}^k X_i = n$ that count the number of occurrences of the $k$ respective outcomes are said to have a multinomial distribution

# - Joint probability mass function of $X_1, X_2, \cdots , X_k$ :
# \begin{equation}
#     f(x_1, x_2, \cdots, x_k; p_1, \cdots , p_k , n) = \binom{n}{x_1,x_2,\cdots, x_k} p_1^{x_1} p_2^{x_2} \cdots p_k^{x_k}
# \end{equation}
# with $\sum_{i=1} ^ k x_i = n$ and $\sum_{i=1}^k p_i = 1$
# - Also written as:
# \begin{equation}
#     (X_1, \cdots , X_k) \sim M_k(p_1, \cdots, p_k, n)
# \end{equation}

# - $E(X_i) = np_i$
# - $Var(X_i) = np_i(1-p_i)$

# In[90]:


from scipy.stats import multinomial

# Parameters
x = [3, 3, 4, 5] # number of successes (! Need to insert the remaining variable)
n = 15 # number of trials
p = [1/6, 1/6, 1/6 , 3/6] # probabilities corresponding to the successes (! Need to insert the remaining probability)

print("Probability mass function: ", multinomial.pmf(x, n=n, p=p))


# In[ ]:




