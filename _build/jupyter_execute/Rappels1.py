#!/usr/bin/env python
# coding: utf-8

# # Rappels
# 
# Dans l'expression "?tude statistique", il faut distinguer :
# 
# 1. les donn?es statistiques : suivant l'?tude, plusieurs probl?mes peuvent ?tre pos?s :
# 
# 		-  Recueil des donn?es (brutes) avec notamment le probl?me des sondages
# 		-  -Nature des donn?es avec ?ventuellement la transformation des donn?es brutes, notamment pour les s?ries chronologiques (s?rie corrig?e des variations saisonni?res)
# 		-  Organisation des donn?es : il s'agit le plus souvent de r?sumer l'information par les techniques de la statistique descriptive 
# 
# 2. le mod?le math?matique : une analyse du ph?nom?ne ?tudi? doit permettre de traduire les probl?mes pos?s par l'?tude dans un langage formel, celui des probabilit?s. Apr?s avoir fait des choix, des hypoth?ses sur la loi de probabilit? et sur les param?tres de cette loi, on s'efforce de se placer dans un mod?le statistique dans lequel des outils th?oriques permettent de r?soudre un certain nombre de probl?mes th?oriques. Dans ce mod?le th?orique, il s'agit de donner une interpr?tation aux donn?es exp?rimentales et, souvent, des hypoth?ses implificatrices de ``m?me loi'' et d'ind?pendance sont faites.
# 3. l'analyse statistique : l'utilisation d'outils statistiques adapt?s au mod?le retenu permet de faire l'interface entre les donn?es statistiques et le mod?le th?orique choisi pour d?crire le ph?nom?ne ?tudi?.
# 
# 
# L'?tude statistique peut alors se traduire sous diverses formes :
# -  pr?ciser le mod?le choisi, en estimant les param?tres intervenant dans celui-ci
# -  juger la validit? d'hypoth?ses faites sur ces param?tres qui se traduira non pas en ''confirmation d'hypoth?ses'', mais en ''d?tecteur d'hypoth?ses fausses''
# -  juger l'ad?quation du mod?le retenu en termes de lois de probabilit? avec la m?me r?serve que ci-dessus
# \end{itemize}
# 
# Les r?sultats th?oriques devront ?tre interpr?t?s dans le contexte de l'?tude en consid?rant que ces r?sultats ont ?t? obtenus dans le cadre d'un mod?le th?orique pr?cis, d'o? la n?cessit? d'une analyse correcte et d'une bonne formalisation. De plus, il faudra prendre en compte les techniques utilis?es, qui ne permettent de r?pondre qu'? des questions pr?cises. Enfin, dans le cas d'une application pratique, il faudra garder ? l'esprit que les conclusions auront des cons?quences ?conomiques (ou autres).
# 
# La section **preciser** rappelle les principaux mod?les probabilistes, dont certains sont utilis?s dans la suite de ce chapitre. Il pourra donc ?tre utile de s'y r?f?rer au besoin.
# 
# ## Echantillon d'une variable al?atoire
# ### D?finition
# ````{prf:definition} Echantillon
# Soit une variable al?atoire $X:(\Omega,\mathcal A,P)\mapsto \mathbb{R}$. On appelle $n$-?chantillon de la variable al?atoire parente $X$ la donn?e de $n$ variables al?atoires $X_1\cdots X_n$, d?finies sur le m?me espace, ind?pendantes, ayant m?me loi que $X$.
# ````
# On a donc 
# 
# $\forall (x_1\cdots x_n)^T\in\mathbb{R}^n\;P(X_1<x_1\cdots X_n<x_n)=P(X_1<x_1)\cdots P(X_n<x_n)=P(X<x_1)\cdots P(X<x_n)$
# 
# On consid?re alors une exp?rience al?atoire $\mathcal E$ d?crite par l'interm?diaire de la variable al?atoire $X$. Consid?rer un $n$ ?chantillon de $X$ consiste ? supposer la possibilit? de $n$ r?p?titions de l'exp?rience $\mathcal E$ dans des conditions identiques, sans interactions entre elles.
# 
# Chaque r?p?tition conduit ? l'observation d'une valeur prise par $X$, d'o? l'observation de $n$ valeurs $x_1\cdots x_n$ ? la suite des $n$ r?p?titions, consid?r?es comme une valeur effectivement prise par le $n$-?chantillon $(X_1\cdots X_n)$ de $X$. Les valeurs $(x_1\cdots x_n)$  rel?vent de l'observation : ce sont les donn?es statistiques recueillies ? la suite des $n$ exp?riences : elles sont appel?es r?alisation du $n$-?chantillon.
# 
# A noter que les hypoth?ses de m?me loi et d'ind?pendance sont simplificatrices.
# 
# ### Sch?ma de Bernoulli et mod?le binomial
# Si $\mathcal E$ n'a que deux ?ventualit?s possibles (r?alisation ou non d'un ?v?nement $A$), alors l'exp?rience peut ?tre d?crite par l'interm?diaire d'une variable al?atoire $X$ ($\mathbb{1}_A$, fonction indicatrice de $A$), de Bernoulli $X:(\Omega,\mathcal A,P)\mapsto \{0,1\}$ avec $P(X=1)=P(A)=p\in]0,1[$.
# 
# Si $\mathcal E$ est r?p?t?e $n$ fois dans des conditions identiques, sans interaction entre elles, on consid?er un $n$-?chantillon $(X_1\cdots X_n)$ de variable al?atoire parente $X$. Les valeurs proses par la variable al?atoire $S_n=X_1+\cdots X_n$ repr?sentent le nombre de r?alisations de $A$ ? la suite des $n$ r?p?titions. Une telle situation est dite relever du sch?ma de Bernoulli.
# 
# ````{prf:property}
# $S_n:(\Omega,\mathcal A,P)\mapsto \{0,1\cdots n\}$ a une loi binomiale $\mathcal{B}(n,p)$ : 
# 
# -  $\forall k\in[\![0,n]\!]\; P(S_n=k)=\begin{pmatrix}n\\k\end{pmatrix} p^k (1-p)^{n-k}$
# -  $\mathbb{E}(S_n)=np,\; \mathbb{V}(S_n)=np(1-p)$
# ````
# 
# En effet, d'apr?s l'ind?pendance pour toute suite ($\delta_1\cdots \delta_n$) avec pour tout $k\in[\![1,n]\!]$ $\delta_k\in\{0,1\}$, on a :
# 
# $P(X_1=\delta_1\cdots X_n=\delta_n) = \displaystyle\prod_{k=1}^n P(X_k=\delta_k) = \displaystyle\prod_{k=1}^n P(X=\delta_k)=p^{s_n}(1-p)^{(n-s_n)}$
# 
# avec $\delta_1+\cdots+ \delta_n=s_n$ , les variables al?atoires ayant m?me loi de Bernoulli que $X$.
# 
# Le nombre de solutions de $\delta_1+\cdots+ \delta_n=s_n$ avec $s_n\in[\![0,n]\!]$ et $\delta_k\in\{0,1\}$ est $\begin{pmatrix}s_n\\n\end{pmatrix}$, d'o? le r?sultat.
# 
# D'apr?s la lin?arit? de l'esp?rance et l'?galit? de Bienaym?, on a de plus
# $\mathbb{E}(S_n) = \displaystyle\sum_{k=1}^n \mathbb{E}(X_k)=n\mathbb{E}(X)=np\quad \mathbb{V}(S_n)=\displaystyle\sum_{k=1}^n \mathbb{V}(X_k)=n\mathbb{V}(X)=np(1-p)$
# 
# 
# 
# ### Moyenne et variances empiriques d'un $n$-?chantillon
# Etant donn? un $n$-?chantillon $(X_1\cdots X_n)$ d'une variable al?atoire parente $X$, on appelle :
# 
# - moyenne empirique du $n$-?chantillon\index{moyenne empirique} la variable al?atoire $$\bar{X_n}=\frac1n \displaystyle\sum_{k=1}^n X_k$$
# -  variance empirique biais?e du $n$-?chantillon\ la variable al?atoire (Ne pas confondre avec la variable $S_n$ du sch?ma de Bernoulli)
# -  
# -  $S_n^2=\frac1n \displaystyle\sum_{k=1}^n (X_k-\bar{X_n})^2=\frac1n \displaystyle\sum_{k=1}^n X_k^2 -\bar{X_n}^2$
# 
# -  variance empirique non biais?e du $n$-?chantillon\index{variance!non biaisee@non biais?e} la variable al?atoire 
# ${S'}_n^2=\frac{1}{n-1} \displaystyle\sum_{k=1}^n (X_k-\bar{X_n})^2$
# 
# 
# On a bien s?r $(n-1){S'}_n^2=nS_n^2$.
# 
# Les valeurs prises par $\bar{X_n}$ co?ncident avec la moyenne exp?rimentale $\bar{x_n}$ des donn?es exp?rimentales $(x_1\cdots x_n)$, r?alisation du $n$-?chantillon. De m?me pour $S_n^2$ pour la variance exp?rimentale.
# 
# ````{prf:property}
# 1.  $\mathbb{E}(\bar{X_n})= \mathbb{E}(X)=m\; ;\; \mathbb{V}(\bar{X_n}) = \frac{\mathbb{V}(X)}{n}=\frac{\sigma^2}{n}$
# 2.  $\mathbb{E}(S_n^2) = \frac{n-1}{n}\sigma^2\; ;\;  \mathbb{E}({S'}_n^2)=\sigma^2$
# 3. Sous l'hypoth?se de normalit?, $\mathbb{V}({S'}_n^2)=\frac{2\sigma^4}{n-1}$
# \end{enumerate}
# ````
# 
# En effet :
# 1.  Imm?diat d'apr?s la lin?arit? de l'esp?rance, l'?galit? de Bienaym? et la propri?t? $\mathbb{V}(\alpha X)=\alpha^2\mathbb{V}(X)$
# 2. $(n-1){S'}_n^2=\displaystyle\sum_{k=1}^n X_k^2-n\bar{X_n^2}$ d'o? 
# $$(n-1)\mathbb{E}({S'}_n^2)=\displaystyle\sum_{k=1}^n\mathbb{E}(X_k^2)-n\mathbb{E}(\bar{X_n^2})=n(\sigma^2+m^2)-n\left (\frac{\sigma^2}{n}+m^2 \right )$$
# et le r?sultat.
# 3. Admis
# 
# 
# ### Echantillons de variables al?atoires normales
# #### Etude d'un $n$-?chantillon
# Soit un $n$-?chantillon $X_1\cdots X_n$ de variable al?atoire parente $X$ de loi $\mathcal{N}(m,\sigma)$. On a les r?sultats suivants :
# 
# 1.  $\sqrt{n} \frac{\bar{X}_n-m}{\sigma}$ suit une loi $\mathcal{N}(0,1)$
# 2. $\frac{nS_n^2}{\sigma^2} = \frac{(n-1)S'^2_n}{\sigma^2}$ suit une loi $\chi^2_{n-1}$
# 3.  les variables al?atoires $\bar{X}_n$ et $S_n^2$ sont ind?pendantes
# 4.  $T=\sqrt{n}\frac{\bar{X}_n-m}{S'_n}=\sqrt{n-1}\frac{\bar{X}_n-m}{S_n}$ suit une loi de Student ? $n-1$ degr?s de libert?.
# 
# #### Etude de deux ?chantillons ind?pendants
# Soient un $n$-?chantillon $X_1\cdots X_n$ de $X$ de loi $\mathcal{N}(m_1,\sigma_1)$, un $m$-?chantillon $Y_1\cdots Y_m$ de $Y$ de loi $\mathcal{N}(m_2,\sigma_2)$, les ?chantillons ?tant ind?pendants. Avec des notations ?videntes, on a les r?sultats suivants :
# 
# 
# -  $F = \frac{\sigma_2^2 S'^2_n(X)}{\sigma_1^2 S'^2_m(Y)} = \frac{(m-1)n}{(n-1)m}\frac{\sigma_2^2S_n^2(X)}{\sigma_1^2S_m^2(Y)}$ admet une loi de Fisher-Sn?d?cor FS($n-1$,$m-1$)
# -  $T = \sqrt{\frac{(n+m-2)mn}{m+n}}\frac{(\bar{X}_n-\bar{Y}_m)-(m_1-m_2)}{\sqrt{nS_n^2(X)+mS_m^2(Y)}}$ admet, sous l'hypoth?se $\sigma_1=\sigma_2$, une loi de Student ? $(n+m-2)$ degr?s de libert?.
# 
# 
# 
# ```{prf:remark}
# Sous l'hypoth?se $\sigma_1=\sigma_2=\sigma$ :
# 
# -  $\bar{X}_n-\bar{Y}_m$ suit une loi $\mathcal{N}(m_1-m_2,\sigma\sqrt{\frac1n+\frac1m})$
# -  $\frac{nS_n^2(X)}{\sigma^2}+\frac{mS_m^2(Y)}{\sigma^2}$ a une loi $\chi^2_{n-1+m-1}$.
# \end{itemize}
# ```
# 
# 
# ## Loi des grands nombres
# ### In?galit? de Tchebychev
# ```{prf:theorem}
# Soit une variable al?atoire $X$ de moyenne $m$ et d'?cart-type $\sigma$. Alors :
# $$(\forall t>0)\; P(|X-m|\geq t)\leq \frac{\sigma^2}{t^2}\quad\textrm{et}\quad (\forall u>0)\; P(\frac{|X-m|}{\sigma}\geq u)\leq \frac{1}{u^2}$$
# ```
# En effet :
# Soit $A=\left \{|X-m|\geq t\right \}$ et $\mathbb{1}_A(\omega)$ = 1 si $\omega\in A$, 0 sinon. Alors :
# 
# $(\forall \omega\in\Omega)\; |X(\omega)-m|^2\geq |X(\omega)-m|^2\mathbb{1}_A(\omega) \geq t^2\mathbb{1}_A(\omega)$
# 
# L'esp?rance ?tant croissante et v?rifiant $\mathbb{E}(\mathbb{1}_A)=P(A)$, on a 
# $\sigma^2=\mathbb{E}(|X-m|^2)\geq t^2P(A) = t^2P(|X-m|\geq t)$ et le r?sultat.
# 
# ```{prf:remark}
# Ces in?galit?s, souvent tr?s grossi?res et d'int?ret essentiellement th?orique, n'ont d'utilit? que pour $t>\sigma$ ou $u>1$ (une probabilit? est toujours inf?rieure ? 1). La seconde donne un majorant de la probabilit? d'observer des valeurs prises par $X$ ? l'ext?rieur de l'intervalle $[m-u\sigma,m+u\sigma]$
# ```
# 
# ### Ph?nom?ne de r?gularit? statistique
# Consid?rons plusieurs s?quences de 100 lancers d'une pi?ce de monnaie et notons, pour chaque s?quence, la suite $(f_n)_{n\geq 1}$ des fr?quences des ``piles`` obtenues. Un exemple de simulation avec $p=0.4$ est propos? dans la figure suivante.
# 
# ![](./images/freqpile.png)
# 
# 
# La fluctuation de la fr?quence est importante pour des petites valeurs de $n$, puis elle s'att?nue, pour se stabiliser autour d'une valeur voisine de $p$.
# 
# Cette constatation exp?rimentale conduit aux remarques suivantes, qui sont pr?cis?es dans la suite dans le cadre th?orique :
# 
# - $f_n$ donne une id?e de la valeur de $p$ avec une plus ou moins grande pr?cision
# - la probabilit? appara?t comme une fr?quence limite.
# 
# 
# ### Loi faible des grands nombres
# ```{prf:theorem}
# Soit $(X_n)_{n\geq 1}$ une suite de variables al?atoires ind?pendantes, identiquement distribu?es (i.i.d) de m?me loi qu'une variable $X$, admettant une moyenne $m$ et un ?cart-type $\sigma$. Si $(\bar{X_n})_{n\geq 1}$ est la suite des moyennes empiriques associ?e ? $(X_n)_{n\geq 1}$ alors
# $(\forall t>0)\; \displaystyle\lim_{n\rightarrow\infty} P(|\bar{X_n}-m|\geq t) = 0$
# On dit que la suite converge en probatilit? vers $m$ et on note $\bar{X_n}\xrightarrow[n\rightarrow\infty]{P} m$
# ```
# 
# C'est une cons?quence imm?diate de l'in?galit? de Tchebychev : $P(|\bar{X_n}-m|\geq t)\leq\frac{\sigma^2}{nt^2}$ puisque $\mathbb{V}(\bar{X_n})=\frac{\sigma^2}{n}$
# 
# 
# L'observation des valeurs prises par la moyenne empirique donne une bonne information sur la moyenne th?orique $m$ de $X$. La pr?cision, au sens ci-dessus, est d'autant meilleure que $n$ est grand.
# 
# ### Loi forte des grands nombres
# avec les hypoth?ses pr?c?dentes, on peut montrer que 
# 
# $P(\{\omega\in\Omega, \displaystyle\lim_{n\rightarrow\infty} \bar{X_n}(\omega)=m\})=1$
# 
# Sauf cas tr?s improbable (avec probabilit? nulle), la suite des r?alisations $(\bar{x}_n)_{n\geq 1}$ des moyennes exp?rimentales des mesures converge vers la moyenne th?orique $m$. On dit que la suite $(\bar{X_n})_{n\geq 1}$ converge presque s?rement vers $m$ et on note $\bar{X_n}\xrightarrow[n\rightarrow\infty]{p.s.} m$.
# 
# ```{prf:remark}
# :class: dropdown
# Si $X=\mathbb{1}_A$ alors $m=p=P(A)$ et la probabilit? de l'?v?nement $A$ appara?t comme une fr?quence limite.
# ```
# 
# ## Approximation de $\mathcal{B}(n,p)$ par la loi de Poisson $\mathcal P(\lambda)$
# ### Th?or?me d'analyse
# ```{prf:theorem}
# Si $p$ est une fonction de $n$ telle que $\displaystyle\lim_{n\rightarrow\infty}np(n)=\lambda>0$, alors pour tout $k\geq 0$
# $$\displaystyle\lim_{n\rightarrow\infty}\begin{pmatrix}n\\p\end{pmatrix} p^k(1-p)^{n-k} = e^{-\lambda}\frac{\lambda^k}{k!}$$
# ```
# En effet 
# \begin{eqnarray*}
# \begin{pmatrix}n\\p\end{pmatrix} p^k(1-p)^{n-k}&=&\frac{n(n-1)\cdots (n-k+1)}{k!}p^k(1-p)^{n-k}\\ 
# &=&\frac{(np)^k}{k!}\displaystyle\prod_{j=0}^k\left (1-\frac{j}{n}\right )(1-p)^{n-k}
# \end{eqnarray*}
# et le r?sultat est d?montr? en remarquant que $\displaystyle\lim_{n\rightarrow\infty} p(n)=0$.
# 
# 
# ### Application
# Soit $S_n$ une variable al?atoire de loi $\mathcal{B}(n,p)$. Lorsque $n$ est grand (>50) et $p$ petite ($np$<10), on peut approcher la loi de $S_n$ par une loi de Poisson $\mathcal P(np)$. On lit alors la valeur correspondante dans la table de la loi de Poisson, pour tout $k\in[\![0,n]\!]$ $$P(S_n=k)\approx e^{-\lambda}\frac{\lambda^k}{k!}$$. 
# 
# De plus, en remarquant que $\Sigma_n=n-S_n$ suit $\mathcal{B}(n,1-p)$, on a 
# 
# $P(\Sigma_n=k)=P(S_n=n-k)=\begin{pmatrix}n\\p\end{pmatrix} p^{n-k}(1-p)^{k} $
# et quand $n$ est grand (>50) et $p$ voisin de 1 ($n(1-p)<10$) on peut approcher la loi de $\Sigma_n$ par une loi de Poisson $\mathcal P(n(1-p))$.
# 
# 
# ## Th?or?me central limite
# ### Le T.C.L.
# ```{prf:theorem}
# Soit une suite $(X_n)_{n\geq 1}$ de variables al?atoires, i.i.d. de m?me loi qu'une variable parente $X$, d?finies sur le m?me espace $(\Omega,\mathcal A,P)$. On consid?re la suite des moyennes empiriques $(X_n)_{n\geq 1}$ des $n$-?chantillons $(X_1\cdots X_n)$.
# 
# Si $X$ admet une moyenne $m$ et un ?cart-type $\sigma$, alors 
# 
# $(\forall x\in\mathbb{R})\; \displaystyle\lim_{n\rightarrow\infty}P\left (\sqrt{n}\frac{\bar X_n-m}{\sigma} <x\right) = \phi(x)$
# o? $ \phi(x)$ est la fonction de r?partition de la loi normale centr?e r?duite $\mathcal{N}(0,1)$.
# 
# On dit que $\left (\sqrt{n}\frac{\bar X_n-m}{\sigma}\right )_{n\geq 1}$ converge en loi vers $\mathcal{N}(0,1)$.
# ```
# La figure suivante illustre ce mod?le dans le cas o? la variable al?atoire parente $X$ suit un sch?ma de Bernoulli avec $P(X = 1)=0.2, P(X=0)=0.8$.
# 
# ![](./images/tcl.png)
# 
# 
# ### Commentaires
# Pour mesurer une grandeur de valeur inconnue $m$, il suffit d'une seule mesure lorsqu'il n'y a pas d'erreur exp?rimentale. Mais les mesures sont toujours ent?ch?es d'erreur et une exp?rience ou mesure peut ?tre mod?lis?e par une variable al?atoire $X$ dnot la moyenne th?orique $\mathbb{E}(X)$ est la valeur cherch?e $m$ si les mesures ne sont pas biais?es, c'est-?-dire affect?es d'une erreur syst?matique.
# 
# Ayant effectu? $n$ mesures, on a une r?alisation d'un $n$-?chantillon de $X$ et une valeur observ?e $\bar x_n$ de la moyenne empirique $/bar X_n$. On peut prendre cette valeur comme estimation de $m$, l'?cart $|\bar x_n-m|$ ?tant une r?alisation de $|\bar X_n-m|$. 
# 
# - La loi forte des grands nombres justifie cette estimation en supposant  $\mathbb{E}(X)=m$
# - L'in?galit? de Tchebychev donne une id?e grossi?re de l'?cart en terme de probabilit?
# - le th?or?me central limite donne une ?valuation asymptotique de cet ?cart al?atoire
# 
# 
# Dans la pratique, pour $n$ grand, dans le cadre de ce th?or?me, on a l'approximation suivante :
# 
# $(\forall a<b)\;\;\;\; P\left (a\sqrt{n}\frac{\bar X_n-m}{\sigma} <b\right)\approx \phi(b)-\phi(a)$
# 
# ### Cas particulier : th?or?me de Moivre-Laplace
# ```{prf:theorem}
# Soit $X=\mathbb{1}_A$  une variable al?atoire de Bernoulli avec $P(A)=p$. Dans les conditions du th?or?me central limite la variable $S_n=\displaystyle\sum_{k=1}^n X_k=n\bar X_n$ suit une loi binomiale $\mathcal{B}(n,p)$ et 
# 
# $ (\forall x\in\mathbb{R})\; \displaystyle\lim_{n\rightarrow\infty}P\left (\frac{S_n-np}{\sqrt{np(1-p)}} <x\right) = \phi(x)$
# ``` 
# On peut donc approcher une loi binomiale par une loi normale.
# 
# ## Mod?les probabilistes usuels
# 
# On donne ici un catalogue non exhaustif des principaux mod?les probabilistes, et leurs principales propri?t?s. Une illustration graphique des lois correspondantes est propos?e dans les figures suivantes.
# 
# ![](./images/discretes.png)
# 
# ![](./images/continues.png)
# 
# 
# 
# \subsection {Lois discr?tes}
# On consid?re une variable al?atoire $X:(\Omega,\mathcal A,P)\mapsto \mathcal D$
# 
# \renewcommand{\arraystretch}{2.2}
# | {\bf Mod?le}                                | $\boldsymbol{\mathcal D}$ | $\boldsymbol{P(X=k)}$   | $\boldsymbol{\mathbb{E}(X)}$ | $\boldsymbol{\mathbb{V}(X)}$ | {\bf Utilisation}                         |
# |---------------------------------------------|---------------------------|-------------------------|------------------------------|------------------------------|-------------------------------------------|
# | Bernoulli                                   | $\{0,1\}$                 | $P(X=1)=p,P(X=0)=1-p=q$ | $p$                          | $pq$                         | Exp?rience ayant 2 ?ventualit?s possibles |
# | Binomiale $\mathcal{B}(n,p) $               | $\{0,\cdots n\}$          | $\begin{pmatrix}n       |
# | \makecell[c]{Hyperg?om?trique               |
# | Uniforme                                    | $\{1,\cdots n\}$          | $\frac1n$               | $\frac{n+1}{2}$              | $\frac{n2-1}{12}$            | Equiprobabilit? des r?sultats             |
# | \makecell[c]{Poisson $\mathcal{P}(\lambda)$ |
# 
# 
# 
# \subsection {Lois absolument continues}
# | {\bf Mod?le}                           | $\boldsymbol{\mathcal D}$ | Densit?                                                          | $\boldsymbol{\mathbb{E}(X)}$ | $\boldsymbol{\mathbb{V}(X)}$ | {\bf Utilisation}                  |
# |----------------------------------------|---------------------------|------------------------------------------------------------------|------------------------------|------------------------------|------------------------------------|
# | Uniforme                               | $[a,b]$                   | $f(x)=\frac{1}{b-a}\mathbb{1}_{]a,b[}(x)$                        | $\frac{b+a}{2}$              | $\frac{(b-a)^2}{12}$         | Pas d'a priori sur la distribution |
# | \makecell[c]{Exponentiel               |
# | \makecell[c]{Pareto                    |
# | Normale $\mathcal{N}(m,\sigma)$        | $\mathbb{R}$              | $f(x)=\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{(x-m)^2}{2\sigma^2}}$ | $m$                          | $\sigma^2$                   | voir T.C.L.                        |
# | \makecell[c]{Gamma $\gamma(a,\lambda)$ |
# | \makecell[c]{Khi-deux $\chi_n^2$       |
# | \makecell[c]{Student                   |
# | \makecell[c]{Fisher-Sn?d?cor           |
# |                                        |                           |                                                                  |                              |
# 
# 
# 
# 
# 
# 
# ### Quelques propri?t?s de lois classiques
# #### Mod?le exponentiel
# On parle de loi de probabilit? sans m?moire car elle v?rifie : 
# $ (\forall s,t\in(\mathbb{R}^+)^*\; P(X>s+t |X>t) = P(X>s)$
# 
# 
# #### Loi normale
# Sous l'hypoth?se de normalit?, de nombreux outils statistiques sont disponibles. Souvent, l'hypoth?se de normalit? est justifi?e par l'interm?diaire du th?or?me centrale limite. Des consid?rations, parfois abusives, permettent de se placer dans le cadre d'utilisation de ce th?or?me et de choisir un mod?le normal alors qu'une ?tude des donn?es statistiques met en d?faut le choix de ce mod?le (probl?me dit d'ad?quation).
# 
# ````{prf:property}
# Si $X$ est une variable al?atoire de loi $\mathcal{N}(m,\sigma)$ alors la variable $Z=\frac{X-m}{\sigma}$ est la variable centr?e r?duite associ?e, et suit une loi $\mathcal{N}(0,1)$ dite aussi loi de Gauss-Laplace.
# ````
# La fonction de r?partition de $Z$ est $\phi(Z) = P(Z<z) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^z e^{-\frac{t^2}{2}}dt$, dont les valeurs peuvent ?tre lues dans une table. 
# 
# ```{prf:theorem}
# Soient $X_1$ et $X_2$ deus variables al?atoires ind?pendantes, de loi respective $\mathcal{N}(m_1,\sigma_1)$ et $\mathcal{N}(m_2,\sigma_2)$. Alors la variable al?atoire $X=\alpha_1X_1+\alpha_2X_2$ admet une loi $\mathcal{N}(m,\sigma)$ avec 
# $$m = \alpha_1 m_1+\alpha_2 m_2\quad \textrm{et}\quad \sigma_2^2 = \alpha_1^2 \sigma_1+\alpha_2^2 \sigma_2^2$$ 
# En particulier, ?tant donn?es $n$ variables al?atoires $X_1\cdots X_n$ i.i.d. de loi $\mathcal{N}(m,\sigma)$, alors la variable al?atoire $\bar X_n = \frac1n \displaystyle\sum_{k=1}^nX_k$ suit une loi normale $\mathcal{N}(m,\sigma/\sqrt{n})$.
# ``` 
# ```{prf:remark}
# Dans ce cas, $\sqrt{n}\frac{\bar X_n-m}{\sigma}$ suit une loi $\mathcal{N}(0,1)$.
# ```
# 
# 
# #### Mod?le Gamma
# Les propri?ts de cette loi reposent sur celles de la fonction $\Gamma(a) = \int_0^{+\infty} x-{a-1}e^{-x}dx$, int?grale convergente pour tout $a>0$.
# 
# ```{prf:theorem}
# Si $X$ et $Y$ sont des variables al?atoires ind?pendantes de loi respective $\gamma(a,\lambda)$ et $\gamma(b,\lambda)$, alors $X=X_1+X_2$ est de loi $\gamma(a+b,\lambda)$
# ```
# 
# ```{prf:theorem}
# Si $X$ est de loi $\mathcal{N}(0,1)$ alors la variable al?atoire $Y=X^2$ admet une loi $\gamma(\frac12,\frac12)$.\\ 
# Etant donn?es plus g?n?ralement $n$ variables al?atoires i.i.d. de loi $\mathcal{N}(m,\sigma)$, alors  la variable al?atoire $V=\displaystyle\sum_{k=1}^n \left (\frac{X_k-m}{\sigma}\right )^2$ admet une loi $\gamma(\frac{n}{2},\frac12)$. C'est la loi du khi-deux ? $n$ degr?s de libert?.
# ```
# 
# #### Loi de Student
# L'utilisation pratique de cette loi est ?nonc?e par le th?or?me suivant :
# 
# ```{prf:theorem}
# Soient deux variables al?atoires $X$ et $Y$ ind?pendantes, de loi respective $\mathcal{N}(0,1)$ et $\chi_n^2$. Alors la variable al?atoire $T=\frac{X}{\sqrt{Y/n}}$ admet une loi de Student ? $n$ degr?s de libert?. 
# ```
# 
# #### Loi de Fisher-Sn?d?cor
# ```{prf:theorem}
# Soient deux variables al?atoires $X$ et $Y$ ind?pendantes, de loi respective $\chi_n^2$ et $\chi_m^2$. Alors la variable al?atoire $T=\frac{X/n}{Y/m}$ admet une loi de Fisher-Sn?d?cor ? $n$ et $m$ degr?s de libert?. 
# 
# ```
