# Statistique descriptive
## D�finitions
Dans la suite, nous nous int�ressons � des unit�s statistiques ou individus statistiques ou unit�s d'observation (individus,  entreprises,  m�nages, donn�es abstraites...). Bien que le cas infini soit envisageable, nous nous restreignons ici � l'�tude d'un nombre fini de ces unit�s. Un ou plusieurs caract�res (ou variables) est mesur� sur chaque unit�. Les variables sont d�sign�es par simplicit� par une lettre. Leurs valeurs possibles sont appel�es modalit�s et l'ensemble des valeurs possibles ou des modalit�s est appel� le domaine. L'ensemble des individus statistiques forment la population.
### Typologie des variables
La typologie des variables d�finit le type de probl�me statistique que l'on doit aborder :
````{prf:definition} Variable qualitative
La variable est dite qualitative lorsque les modalit�s sont des cat�gories. Suivant qu'il existe une relation d'ordre sur les cat�gories, on distingue :
- la variable qualitative nominale, si les modalit�s  ne peuvent pas �tre ordonn�es
- la variable qualitative ordinale, si les modalit�s peuvent �tre ordonn�es
````

````{prf:definition} Variable quantitative
La variable est dite quantitative lorsque les modalit�s sont des valeurs num�riques (scalaires ou vectorielles) :
- la variable est quantitative discr�te si les modalit�s forment un ensemble d�nombrable
- la variable quantitative est continue si les modalit�s vivent dans un espace continu.
````

Dans certains cas (l'�ge par exemple), une variable d'un type (quantitative continue ici) peut �tre exprim�e d'une autre mani�re pour des raisons pratiques de collecte ou de mesure. De m�me, les variables qualitatives ordinales peuvent �tre cod�es, par exemple selon une �chelle de satisfaction.

````{prf:definition} S�rie statistique
On appelle s�rie statistique une suite de $n$ valeurs prises par une variable $X$ sur les unit�s d'observation, not�es $x_1\cdots x_n$.
````


### Variable qualitative nominale
Une variable qualitative nominale a des valeurs distinctes qui ne peuvent pas �tre ordonn�es. On note $J$ le nombre de valeurs distinctes ou de modalit�s, not�es $x_1\cdots x_J$. On appelle effectif d'une modalit� ou d'une valeur distincte le nombre de fois que cette modalit� (ou valeur distincte) appara�t dans la s�rie statistique. On note $n_j$ l'effectif de la modalit� $x_j$. La fr�quence d'une modalit� $j$ est  alors �gale � $f_j=\frac{n_j}{n}$.

Le tableau statistique d'une variable qualitative nominale peut �tre repr�sent� par deux types de graphiques. Les effectifs sont repr�sent�s par un diagramme en tuyau d'orgue et les fr�quences par un diagramme en secteurs. Pour ce dernier, si le nombre de modalit�s devient trop important, la repr�sentation perd de son int�r�t.

![](./images/baton.png)


### Variable qualitative ordinale
Le domaine peut �tre muni d'une relation d'ordre.  Les valeurs distinctes d'une variable ordinale peuvent donc �tre ordonn�es $x_1\leq x_2\cdots\leq  x_J$, � permutation pr�s dans l'ordre croissant des indices. L'effectif cumul� $N_j$ et la fr�quence cumul�e $F_j$ des variables sont alors d�finis par 
$$(\forall j\in[\![1,J]\!])\quad N_j=\displaystyle\sum_{i=1}^j n_i\quad \textrm {et}\quad F_j=\displaystyle\sum_{i=1}^j f_i$$

Les fr�quences et les effectifs (cumul�s ou non) peuvent �tre repr�sent�s sous la forme d'un diagramme en tuyaux d'orgue.

### Variable quantitative discr�te
Le domaine d'une telle variable est d�nombrable. Comme pour les variables qualitatives ordinales, on peut calculer les effectifs (cumul�s ou non) et les fr�quences (cumul�es ou non). 

La r�partition des valeurs de la variable peut �tre repr�sent�e par un diagramme en b�tonnets. Les fr�quences cumul�es  sont visualis�es par la fonction de r�partition de la variable , d�finie par 

$F(x) = \left \{
\begin{tabular}{ll}
0&si $x<x_1$\\
$F_j$ &si  $x\in[x_j,x_{j+1}[$\\
1& si  $x_J\leq x$
\end{tabular}\right .$

![](./images/baton2.png)

### Variable quantitative continue
Le domaine d'une  variable quantitative continue est infini et est assimil� � $\mathbb{R}$ ou � un intervalle de $\mathbb{R}$. Cependant, la mesure �tant limit�e en pr�cision, on peut traiter ces variables comme des variables discr�tes.

La repr�sentation graphique de ces variables (et la construction du tableau statistique) passe par le regroupement des modalit�s ou valeurs en classes. Le tableau ainsi construit est souvent appel� distribution group�e. La classe $j$ est l'ensemble des valeurs incluses dans $[c^-_j,c^+_j[$, o� $c^-_j$ et $c^+_j$ sont les bornes inf�rieure et sup�rieure de la classe. Sur cet intervalle, on peut calculer la fr�quence $f_j$ de la classe, la fr�quence cumul�e, l'effectif $n_j$... La r�partition en classes n�cessite de d�finir a priori le nombre de classes $J$ et l'amplitude $a_j$ des intervalles. Si elles peuvent �tre d�finies de mani�re empirique, quelques r�gles permettent d'�tablir $J$ et l'amplitude pour une s�rie statistique de $n$ observations. Par exemple :
- $J=1+3.3log_{10}(n)$ (r�gle de Sturge)
- $J=2.5\sqrt[4\,]{n}$ (r�gle de Yule)



```{prf:remark}
:class: dropdown
Toutes les classes n'ont pas n�cessairement la m�me amplitude
```

Les effectifs (ou les fr�quences) sont repr�sent�(e)s par un histogramme. Si l'on s'int�resse � la repr�sentation des effectifs (resp. des fr�quences), la densit� d'effectif $h_j$ (resp. de fr�quence $d_j$),  d�finie par $h_j=\frac{n_j}{a_j}$ (resp. $d_j=\frac{f_j}{a_j}$), d�termine la hauteur du rectangle repr�sentant la classe $j$. L'aire de l'histogramme est �gale � l'effectif total $n$ pour l'histogramme des effectifs, et � 1 pour l'histogramme des fr�quences.

Comme dans le cas discret, la fonction de r�partition peut �tre calcul�e de la mani�re suivante :

$F(x) = \left \{
\begin{tabular}{ll}
0&si $x<c^-_1$\\
$F_{j-1}+\frac{f_j}{c^+_j-c^-_j}(x-c^-_j)$ &si  $x\in[c^-_j,c^+_j[$\\
1& si  $c^+_J\leq x$
\end{tabular}\right .$


\section {Statistique descriptive univari�e}
La statistique descriptive univari�e consiste � �tudier un ensemble d'unit�s d'observations, lorsque celles-ci sont d�crites par une seule variable. 

Soit donc $X$ une variable et $x_j,j\in [\![1,n]\!]$ l'ensemble des valeurs prises par cette variable, $n_i$ �tant le nombre de fois o� la valeur $x_i$ est prise. $X$ peut �tre qualitative ou quantitative, les param�tres de description d�crits dans la suite s'appliqueront � l'une de ces natures ou au deux.
\begin{defin}{Moment}{}
Le moment � l'origine d'ordre $r$  est d�fini par :
$$m'_r=\displaystyle\sum_{i=1}^n x_i^r$$
\end{defin}

\subsection{Param�tres de position}
Plusieurs param�tres permettent de d�crire la position "la plus repr�sentative" d'une variable :
\begin{defin}{Mode} {}
Le mode est la valeur distincte correspondant � l'effectif le plus �lev�. Il est not� $x_M$.
\end{defin}
Le mode peut �tre calcul� pour tout type de variable, n'est pas n�cessairement unique. Lorsqu'une variable continue est d�coup�e en classes, il est possible de d�finir une classe modale (classe correspondant � l'effectif le plus �lev�)
\begin{defin}{Moyennes} {} Les moyennes ne peuvent �tre d�finies que sur des variables quantitatives. Plusieurs moyennes peuvent �tre calcul�es, parmi lesquelles :
\begin{itemize}
\item la moyenne arithm�tique  $$\bar{x} = \frac{1}{n}{\displaystyle\sum_{i=1}^nx_i}=  \frac{1}{n}{\displaystyle\sum_{i=1}^J n_ix_i}$$ C'est le moment � l'origine d'ordre 1.
\item la moyenne g�om�trique : si les $x_i$ sont positifs, la moyenne g�om�trique est la quantit� $$G=\left (\displaystyle\prod_{i=1}^n x_i\right )^\frac{1}{n}$$C'est donc l'exponentielle de la moyenne arithm�tique des logarithmes des valeurs observ�es. 
\item la moyenne harmonique : si les $x_i$ sont positifs, la moyenne harmonique est d�finie par $$H=\frac{n}{\displaystyle\sum_{i=1}^J 1/x_i}$$
\item la moyenne pond�r�e : dans certains cas, on n'accorde pas la m�me importance � toutes les observations (fiabilit�, confiance...). La moyenne pond�r�e est alors d�finie par 
$$\bar{x}_w= \frac{\displaystyle\sum_{i=1}^n w_ix_i}{\displaystyle\sum_{i=1}^n w_i}$$

\end{itemize}
\end{defin}
Dans le cas o� $\forall i,w_i=1/n$, la moyenne pond�r�e est la moyenne arithm�tique. De plus, dans tous les cas, on peut montrer que $H\leq G\leq \bar{x}$.


\begin{rem}
en centrant les moments par rapport � une valeur repr�sentative, on d�finit les moments centr�s :
\end{rem}
\begin{defin}{Moment centr�}{}
Le moment centr� d'ordre $r$ est d�fini par :
$$m_r=\displaystyle\sum_{i=1}^n \left (x_i-\bar{x}\right )^r$$
\end{defin}

\begin{defin}{M�diane} {}
La m�diane, not�e $x_\frac{1}{2}$ est la valeur centrale de la s�rie statistique tri�e par ordre croissant. 
\end{defin}
En d'autres termes, c'est la valeur de la s�rie tri�e telle qu'au moins 50\% des effectifs soient inf�rieurs � $x_\frac{1}{2}$. Elle peut �tre calcul�e sur des variables quantitatives ou qualitatives ordinales (dans le cas o� des �chelles de valeur ont �t� d�finies).
\begin{defin}{Quantiles} {}
Le quantile d'ordre $p$ est d�fini par $x_p=F^{-1}(p)$, o� $F$ est la fonction de r�partition. 
\end{defin}
La notion de quantile g�n�ralise la notion de m�diane. Si la fonction de r�partition �tait continue et strictement croissante, la d�finition de $x_p$ serait unique. Or $F$ est discontinue et d�finie par paliers et les valeurs de quantiles varient suivant par exemple l'utilisation ou non d'une m�thode d'interpolation de $F$. Pour calculer $x_p$, on peut par exemple consid�rer que si $np$ est pair, 
$$x_p=\frac{x_{np}+x_{np+1}}{2}$$
on remarque alors que la m�diane est le quantile d'ordre $\frac{1}{2}$
et sinon
$$x_p=x_{\lceil{np}\rceil}$$
En particulier, un quartile est chacune des 3 valeurs qui divisent les donn�es tri�es en 4 parts �gales, de sorte que chaque partie repr�sente 1/4 de l'�chantillon de population.


\subsection{Param�tres de dispersion}
Il est tr�s souvent utile d'appr�cier la dispersion des mesures autour du param�tre de position. Pour cela, sur des variables quantitatives uniquement, plusieurs outils sont disponibles :
\begin{defin}{Etendue}{}
L'�tendue est la simple diff�rence entre la plus grande et la plus petite valeur observ�e.
\end{defin}
\begin{defin}{Distance interquartile}{}
La distance interquartile est la diff�rence entre le troisi�me et le premier quartile.
\end{defin}

\begin{defin}{Variance}{}
La variance est la somme des carr�s des �carts � la moyenne, normalis�e par le nombre d'observations
$$\sigma^2 = \frac{1}{n}\displaystyle\sum_{i=1}^n\left (x_i-\bar{x}\right )^2$$
\end{defin}
Cette variance est dite biais�e. La variance non biais�e est obtenue en divisant non pas par $n$, mais par $n-1$.\\
\begin{defin}{Ecart type}{}
L'�cart type est la racine carr�e de la variance. 
\end{defin}

\begin{defin}{Ecart moyen absolu}{}
L'�cart moyen absolu est la somme des valeurs absolues des �carts � la moyenne divis�e par le nombre d'observations. 
\end{defin}
Notons qu'il s'agit de la distance $L_1$ du vecteur des observations au vecteur compos� de la valeur moyenne, divis� par le nombre d'observations. La variance est la distance $L_2$ entre ces deux vecteurs. Lorsque la distance est calcul�e par rapport au vecteur compos� de la valeur m�diane, on parle d'�cart m�dian absolu.


La figure \ref{F:deciles} r�sume l'ensemble de ces param�tres.
\begin{center}
\begin{figure}[ht!]
\includegraphics[width=\textwidth]{figures/deciles.png}
\caption{\label{F:deciles} Illustration des param�tres de position et de dispersion.}
\end{figure}
\end{center}
\subsection{Param�tres de forme}
Les param�tres de forme sont souvent calcul�s en r�f�rence � la forme de la loi normale, pour �valuer la sym�trie, l'aplatissement ou la d�rive par rapport � cette loi.
\begin{defin}{Skewness}{}
$$g_1 = \frac{m_3}{\sigma^3}$$
\end{defin}
Le skewness est �galement appel� coefficient d'asym�trie de Fisher.
\begin{defin}{Kurtosis}{}
$$K=\frac{m_4}{m_2^2}$$
\end{defin}
$K$ permet de mesurer l'aplatissement.
\begin{defin}{Coefficient d'asym�trie de Yule}{}
$$A_Y = \frac{x_{3/4}+x_{1/4}-2x_{1/2}}{x_{3/4}-x_{1/4}}$$
\end{defin}
Ce coefficient est fond� sur les positions de trois quartiles (le premier, la m�diane et le troisi�me) et est normalis� par la distance interquartile.
\begin{defin}{Coefficient d'asym�trie de Pearson}{}
$$A_P = \frac{\bar{x}-x_M}{\sigma}$$
\end{defin}
Ce coefficient est fond� sur la comparaison de la moyenne et du mode, et est normalis� par l'�cart type.
\vskip 5pt
Tous les coefficients d'asym�trie ont des propri�t�s similaires : ils sont nuls si la distribution est sym�trique, n�gatifs si la distribution est allong�e � gauche (left asymmetry), et positifs si la distribution est allong�e � droite (right asymmetry).\\
On peut aussi chercher � mesurer l'aplatissement (ou kurtosis) d'une distribution de mesure. Dans ce cas, on utilise le coefficient d'aplatissement de Pearson ou de Fisher, respectivement donn�s par 
$$\beta_2=\frac{m_4}{\sigma^4}\quad\textrm{et}\quad g_2=\beta_2-3$$
Une distribution est alors dite m�sokurtique si $g_2$ est proche de 0, leptokurtique si $g_2>0$ (queues plus longues et distribution plus pointue); et platykyrtique si $g_2<0$ (queues plus courtes et distribution arrondie).


\section {Statistique descriptive bivari�e}
On s'int�resse � deux variables $x$ et $y$, mesur�es sur les $n$ unit�s d'observation. La s�rie statistique est alors une suite de $n$ couples $(x_i,y_i)$ des valeurs prises par les deux variables sur chaque individu.
\subsection{Cas de deux variables quantitatives}
Le couple est un couple de valeurs num�riques. C'est donc un point dans le plan $\mathbb{R}^2$. Les variables $x$ et $y$ peuvent �tre analys�es s�par�ment, en op�rant une statistique univari�e sur chacune de ces variables. Les param�tres calcul�s (de position, de dispersion...) sont dits marginaux. Cependant, il est int�ressant d'�tudier le lien entre ces deux variables, par l'interm�diaire des valeurs des couples. On d�finit pour cela un certain nombre d'outils :
\begin{defin}{Covariance}{}
La covariance de $x$ et $y$ est d�finie par :
$$\sigma_{xy}=\frac{1}{n}\displaystyle\sum_{i=1}^n\left (x_i-\bar{x}\right )\left (y_i-\bar{y}\right )$$
\end{defin}

\begin{defin}{Coefficient de corr�lation}{}
Le coefficient de corr�lation  de deux variables $x$ et $y$ est d�fini par 
$$r_{xy}=\frac{\sigma_{xy}}{\sigma_{x}\sigma_{y}}$$
Le coefficient de d�termination est le carr� du coefficient de corr�lation.
\end{defin}
Le coefficient de corr�lation est donc la covariance normalis�e par les �carts types marginaux des variables. Il mesure la d�pendance lin�aire entre $x$ et $y$. Il est compris dans l'intervalle [-1,1] est est positif (resp. n�gatif) si les points sont align�s le long d'une droite croissante (resp. d�croissante), d'autant plus grand en valeur absolue que la d�pendance lin�aire est v�rifi�e. Dans le cas o� le coefficient est nul, il n'existe pas de d�pendance lin�aire.

Pour conna�tre plus pr�cis�ment la relation lin�aire qui lie $x$ et $y$, on effectue une r�gression lin�aire en calculant par exemple la droite de r�gression (chapitre~\ref{ch:regression}).
Si $y=a+bx$, il est facile de montrer que 
$$b=\frac{\sigma_{xy}}{\sigma_x^2}\quad\textrm{et}\quad a=\bar{y}-b\bar{x}$$

et la droite de r�gression s'�crit $y-\bar{y}=\frac{\sigma_{xy}}{\sigma_x^2}\left ( x-\bar{x}\right )$.

A partir de cette droite, on peut calculer les valeurs ajust�es, obtenues � partir de la droite de r�gression : $y^*_i=a+bx_i$. Ce sont les valeurs th�oriques des $y_i$ et les r�sidus $e_i=y_i-y_i^*$ repr�sentent la partie inexpliqu�e des $y_i$ par la droite de r�gression (ceux l� m�me que l'on essaye de minimiser par la m�thode des moindres carr�s).

\subsection{Cas de deux variables qualitatives}
\label{P:contingence}
Le couple est un couple de valeurs $(x_i,y_i)$ o� $x_i$ et $y_i$ prennent comme valeurs des modalit�s qualitatives. Notons $x_1\cdots x_J$ et $y_1\cdots y_K$ les valeurs distinctes prises. \\

Les donn�es peuvent �tre regroup�es sous la forme d'un tableau de contingence prenant la forme suivante :

\begin{center}
\begin{tabular}{c|ccccc|c}
&$y_1$&$\cdots$&$y_k$&$\cdots$&$y_K$&total\\
\hline
$x_1$&$n_{11}$&$\cdots$&$n_{1k}$&$\cdots$&$n_{1K}$&$n_{1.}$\\
$\vdots$&$\vdots$&$\vdots$&$\vdots$&$\vdots$&$\vdots$&$\vdots$\\
$x_j$&$n_{j1}$&$\cdots$&$n_{jk}$&$\cdots$&$n_{jK}$&$n_{j.}$\\
$\vdots$&$\vdots$&$\vdots$&$\vdots$&$\vdots$&$\vdots$&$\vdots$\\
$x_J$&$n_{J1}$&$\cdots$&$n_{Jk}$&$\cdots$&$n_{JK}$&$n_{J.}$\\
\hline
total&$n_{.1}$&$\cdots$&$n_{.k}$&$\cdots$&$n_{.K}$&$n$\\
\end{tabular}
\end{center}

o� $n_{j.}$ (resp $n_{.k}$ )sont les effectifs marginaux repr�sentant le nombre de fois o� $x_j$ (resp. $y_k$) appara�t, et $n_{jk}$ le nombre d'apparition du couple $(x_j,y_k)$.

Le tableau des fr�quences $f_{jk}$ s'obtient en divisant tous les effectifs par la taille $n$ dans ce tableau.

Un tel tableau s'interpr�te toujours en comparant les fr�quences en lignes ou les fr�quences en colonnes (profils lignes ou colonnes), d�finies  respectivement par 
$$f_k^{(j)}= \frac{n_{jk}}{n_{j.}}=\frac{f_{jk}}{f_{j.}}\quad\textrm{ et }\quad f_j^{(k)}= \frac{n_{jk}}{n_{.k}}=\frac{f_{jk}}{f_{.k}}$$

Si l'on cherche un lien entre les variables, on construit un tableau d'effectifs th�oriques qui repr�sente la situation o� les variables ne sont pas li�es (ind�pendance). Ce tableau est constitu� des effectifs 
$$n_{jk}^*=\frac{n_{j.}n_{.k}}{n}$$
Les effectifs observ�s $n_{jk}$ ont les m�mes marges que les $n_{jk}^*$, et les �carts � l'ind�pendance sont calcul�s par la diff�rence $e_{jk}=n_{jk}-n_{jk}^*$



La d�pendance du tableau se mesure au moyen du khi-deux d�fini par 
$$\chi^2_{obs}= \displaystyle\sum_{k=1}^K\displaystyle\sum_{j=1}^J\frac{e_{jk}^2}{n_{jk}^*}$$
qui peut �tre normalis� pour ne plus d�pendre du nombre d'observations :
$$\phi^2=\frac{\chi^2_{obs}}{n}$$

La construction du tableau des effectifs th�oriques et sa comparaison au tableau des observations permet dans un premier temps de mettre en �vidence les associations significatives entre modalit�s des deux variables. Pour cela, on calcule la contribution au $\chi^2$ des modalit�s $j$ et $k$ :
$$\frac{1}{\chi^2_{obs}}\frac{\left (n_{jk}-n_{j.}n_{.k}\right )^2}{n_{jk}^*}$$
Le signe de la diff�rence $n_{jk}-n_{jk}^*$ indique alors s'il y a une association positive ou n�gative entre les modalit�s $j$ et $k$.

Plus g�n�ralement, le $\chi^2_{obs}$ est un indicateur de liaison entre les variables.  Dans le cas o� $\chi^2_{obs}=0$, il y a ind�pendance. Pour rechercher la borne sup�rieure du khi-deux et voir dans quel cas elle est atteinte, on d�veloppe le carr� et on obtient 
$$\chi^2_{obs} = n\left [\displaystyle\sum_{k=1}^K\displaystyle\sum_{j=1}^J \frac{n_{jk}^2}{n_{j.}n_{.k}} -1\right ]$$
Comme $\frac{n_{jk}}{n_{.k}}\leq 1$ on a $ \frac{n_{jk}^2}{n_{j.}n_{.k}} \leq \frac{n_{jk}}{n_{.k}}$ d'o�
$$\displaystyle\sum_{k=1}^K\displaystyle\sum_{j=1}^J\frac{n_{jk}^2}{n_{j.}n_{.k}}\leq \displaystyle\sum_{k=1}^K\displaystyle\sum_{j=1}^J \frac{n_{jk}}{n_{.k}} = \displaystyle\sum_{k=1}^K \frac{\displaystyle\sum_{j=1}^J n_{jk}}{n_{.k}}=\displaystyle\sum_{k=1}^K \frac{n_{.k}}{n_{.k}}=1$$

d'o� $\chi^2_{obs}\leq n(K-1)$. On pourrait de m�me montrer que $\chi^2_{obs}\leq n(J-1)$ et donc 
$$\phi^2\leq min(J-1,K-1)$$
la borne �tant atteinte dans le cas de la d�pendance fonctionnelle (si $\forall j \frac{n_{jk}}{n_{j.}}=1$, i.e. il n'existe qu'une case non nulle dans chaque ligne.)\\
A partir de ce khi-deux normalis�, on calcule finalement plusieurs coefficients permettant de mesurer l'ind�pendance, et parmi ceux-ci citons :
\begin{itemize}
\item le coefficient de Cramer:
$$V=\sqrt{\frac{\phi^2}{min(J-1,K-1)}}$$
\item le coefficient de contingence de Pearson :
$$C = \sqrt{\frac{\phi^2}{\phi^2 + 1}}$$
\item le coefficient de Tschuprow :
$$T = \sqrt{\frac{\phi^2}{\sqrt{(K-1)(J-1)}}}$$
\end{itemize}

Ces coefficients sont tous compris entre 0 (ind�pendance) et 1 (d�pendance fonctionnelle). Pour estimer � partir de quelle valeur la d�pendance fonctionnelle est significative, on proc�de de la mani�re suivante : si les $n$ observations �taient pr�lev�es dans une population o� les variables sont ind�pendantes, on recherche les valeurs probables de $\chi^2_{obs}$. \\
En s'appuyant sur la loi multinomiale et le test du $\chi^2$, on montre que $\chi^2_{obs}$ est une r�alisation d'une variable al�atoire $Z$ suivant approximativement une loi $\chi^2_{(K-1)(J-1)}$\footnote{Soient $U_1\ldots U_p$ $p$ variables i.i.d de loi normale centr�e r�duite. On appelle loi du $\chi^2$ � $p$ degr�s de libert� la loi de la variable $\displaystyle\sum_{i=1}^pU_i^2$.}. En effet, les $e_{jk}$ sont li�es par $(K-1)(J-1)$ relations lin�aires puisqu'on estime les probabilit�s de r�alisation de $x_j$ et $y_k$ respectivement par $n_{j,.}/n$ et $n_{.k}/n$ Il suffit alors de fixer un risque d'erreur $\alpha$ (une valeur qui, s'il y avait ind�pendance, n'aurait qu'une probabilit� faible d'�tre d�pass�e), et on rejette l'hypoth�se d'ind�pendance si $\chi^2_{obs}$  est sup�rieur � la valeur critique qu'une variable $\chi^2_{(K-1)(J-1)}$ a une probabilit� $\alpha$ de d�passer.
L'esp�rance d'un $\chi^2_{(K-1)(J-1)}$ �tant �gale � son degr� de libert�, $\chi^2_{obs}$ est d'autant plus grand que le nombre de modalit�s $J$ et/ou $K$ est grand. 
\vskip 10pt
D'autres indices existent, qui ne d�pendent pas de $\chi^2_{obs}$, comme par exemple l'indice $G^2$
$$G^2 = 2\displaystyle\sum_{k=1}^K\displaystyle\sum_{j=1}^J n_{jk} ln \left (\frac{ n_{jk}}{ n^*_{jk}} \right ) $$

qui sous l'hypoth�se d'ind�pendance suit une loi $\chi^2_{(K-1)(J-1)}$.

\subsection{Cas d'une variable quantitative et d'une variable qualitative}
On s'int�resse ici au cas o� les modalit�s $x_i$ sont qualitatives, et o� $y$ est une variable quantitative, dont les modalit�s sont des r�alisations d'une variable al�atoire $Y$.
Le rapport de corr�lation th�orique entre $x$ et $Y$ est d�fini par 
$$\eta^2_{Y\mid x} = \frac{\sigma^2_{\mathbb{E}_{Y\mid x}}}{\sigma^2_Y}$$
Si $n_j$ est le nombre d'observations de la modalit� $x_j,j\in[\![1\,J]\!]$, $y_{ij}$ la valeur de $Y$ du $i^e$ individu de la modalit� $j$, $\bar{y}_1\ldots \bar{y}_J$ sont les moyennes de $Y$ pour ces modalit�s et $\bar{y}$ la moyenne totale sur les $n$ individus, le rapport de corr�lation empirique est d�fini par 
$$e^2 = \frac{\frac{1}{n}\displaystyle\sum_{j=1}^J n_j\left (\bar{y}_j-\bar{y}\right )^2}{\sigma^2_y}$$


La quantit� 
$$\sigma^2_\cap = \frac{1}{n}\displaystyle\sum_{j=1}^J n_j\sigma_j^2$$
 avec $\sigma_j^2 =  \frac{1}{n_j}\displaystyle\sum_{i=1}^{n_j}\left (y_{ij}-\bar{y}_j \right )^2$,  est appel�e variance intra groupe (ou intra classe), et donne une id�e de la variabilit� � l'int�rieur de chaque modalit�. \\
 La quantit� 
 $$\sigma_\cup = \frac{1}{n}\displaystyle\sum_{j=1}^J n_j\left (\bar{y}_j-\bar{y}\right )^2$$
 est la variance inter groupes (ou inter classes), et mesure la variabilit� entre les diff�rentes modalit�s.\\
 Le th�or�me de d�composition de la variance (ou th�or�me de Huygens) affirme que la variance totale $\sigma^2_y$, calcul�e sans distinction de modalit� s'�crit :
 $$\sigma^2_y = \sigma^2_\cap + \sigma^2_\cup$$
 
 De ces d�finitions, on a alors :
\begin{itemize}
\item $e^2=0$ si toutes les moyennes de $Y$ sont �gales, d'o� l'absence de d�pendance en moyenne
\item $e^2=1$ si tous les individus d'une modalit� de $x$ ont m�me valeur de $Y$ et ceci pour chaque modalit� 
\item $e^2$ permet de comprendre, via le th�or�me de Huygens,  quelle variation est pr�dominante dans la variance totale. Ainsi par exemple, si la variable quantitative est la note d'un �l�ve � un examen, et la variable qualitative son assiduit� au cours correspondant, la variabilit� entre les notes obtenues dans toute la promotion d�pend de deux
facteurs : le fait que les �tudiants assistent ou pas aux cours, et le fait qu'� assiduit�
�gale (i.e. � l'int�rieur d'une m�me modalit� d'assiduit�) les �tudiants n'ont pas le m�me niveau. $e^2$  permet alors de savoir lequel de ces deux facteurs est pr�dominant
pour expliquer la variabilit� des notes dans toute la promotion.
\end{itemize}

Pour d�terminer � partir de quelle valeur $e^2$ est significatif, on compare donc $\sigma^2_\cap$ � $\sigma^2_\cup$. On peut montrer que si le rapport de corr�lation th�orique est nul, alors la variable 
$$\frac{\left (\frac{e^2}{J-1}\right )}{\left (\frac{1-e^2}{n-J}\right )}$$
suit une loi de Fisher Snedecor \footnote{Soient $U$ et $V$ deux variables al�atoires ind�pendantes suivant respectivement des lois $\chi^2_n$ et $\chi^2_p$. On d�finit $F(n,p)=\frac{U/n}{V/P}$} $F(J-1,n-J)$, en supposant que les distributions conditionnelles de $Y$ pour chaque modalit� de $x$ sont gaussiennes, de m�me esp�rance et de m�me variance. 

\section{Vers une analyse multivari�e}
Bien �videmment, dans la majorit� des cas, un individu sera d�crit par $p\geq 2$ variables. Si certains algorithmes de statistique descriptive multidimensionnelle sont abord�s dans les chapitres suivants, il est n�anmoins possible d'avoir une premi�re approche exploratoire de ce cas.
\subsection{Matrices de covariance et de corr�lation}
La premi�re id�e, lorsque l'on a observ� $p$ variables sur $n$ individus, est de calculer les $p$ variances de ces variables, et les $\frac{p(p-1)}{2}$ covariances. Ces mesures sont regroup�es dans une matrice $p\times p$, sym�trique, semi d�finie positive, appel�e matrice de variance-covariance (ou matrice des covariances), et classiquement not�e $\boldsymbol\Sigma$.\\
De m�me, on peut former la matrice des corr�lations entre les variables, � diagonale unit� et sym�trique. La matrice r�sultante, not�e $\mathbf R$, est �galement semi d�finie positive et sa repr�sentation graphique en fausses couleurs permet d'appr�cier les d�pendances lin�aires entre variables (figure \ref{F:R}).


\begin{figure}[hbtp!]
 \centering
 \includegraphics[width=.7\columnwidth]{figures/R.png}
 \caption{Exemple de matrice de corr�lation sur des donn�es �nerg�tiques de b�timents.}\label{F:R}
\end{figure}

Dans le cas de variables qualitatives, les coefficients de corr�lation peuvent �tre remplac�s par les coefficients de Cramer, de Tschuprow...

\subsection{Tableaux de nuages}
On peut proposer � partir de l� des repr�sentations entre sous-ensembles de variables. La figure \ref{F:grid} propose un exemple de tels tableaux, parfois appel�s splom (Scatter PLOt Matrix) :
\begin{itemize}
\item la partie triangulaire sup�rieure repr�sente les nuages de points de couples de variables
\item la diagonale repr�sente les histogrammes des variables
\item la partie trianglaire inf�rieure donne le coefficient de corr�lation entre les deux variables, et une estimation de la densit� de la distribution 2D des donn�es
\end{itemize}

\begin{figure}[ht!]
 \centering
 \includegraphics[width=\columnwidth]{figures/grid.png}
 \caption{Visualisation de relations entre sous-ensembles de variables.}\label{F:grid}
\end{figure}

\subsection{Tableaux de Burt}
Le tableau de Burt est une g�n�ralisation particuli�re de la table de contingence dans le cas o� l'on �tudie simultan�ment $p$ variables qualitatives $X_1\ldots X_p$. Notons $c_j$ le nombre de modalit�s de $X_j$ et posons $c=\displaystyle\sum_{j=1}^p c_j$. \\
Le tableau de Burt est une matrice carr�e sym�trique de taille $c$, constitu�e de $p^2$ sous-matrices. Chacune des $p$ sous-matrices diagonales est relative � l'une des $p$ variables, la $j^e$ �tant carr�e de taille $c_j$, diagonale, et de coefficients diagonaux les effectifs marginaux de $X_j$. La sous-matrice dans le bloc $(k,l)$ du tableau, $k\neq l$, est la table de contingence des variables $X_k$ et $X_l$.
\newpage
\section{Exercices}
\begin{exo}
 Quel est le type de chacune des variables suivantes:
 \begin{multicols}{2}
  \begin{enumerate}
   \item lieu de r�sidence,
   \item citoyennet�,
   \item nombre d'enfants,
   \item sexe,
   \item �tat matrimoniale,
   \item �ge,
   \item revenu annuel,
   \item pointure de chaussure,
   \item niveau d'�tude,
   \item langue maternelle,
   \item nombre de langue parl�es,
   \item tour de taille,
   \item taille de pantalon,
   \item satisfaction.
  \end{enumerate}
 \end{multicols}
\end{exo}

% \begin{Answer}[ref=stat_type]
%    \begin{enumerate}
%    \item lieu de r�sidence : qualitatif nominal,
%    \item citoyennet� : qualitatif nominal (fran�ais, anglais, russe),
%    \item nombre d'enfants : quantitatif discret,
%    \item sexe : qualitatif nominal,
%    \item �tat matrimoniale : qualitatif nominal,
%    \item �ge : quantitatif discret (21 ans,\dots) ou quantitatif continu (21.767899 ans, \dots),
%    \item revenu annuel : quantitatif continu (avec des virgules),
%    \item pointure de chaussure : quantitatif discret (38,39,\dots,45),
%    \item niveau d'�tude : qualitatif ordinal (DUT<L3) ou quantitatif discret (BAC+2<BAC+3),
%    \item langue maternelle : qualitatif nominal,
%    \item nombre de langue parl�es : quantitatif discret,
%    \item tour de taille : quantitatif continu,
%    \item taille de pantalon : qualitatif ordinal ($S<M<XL$) ou quantitatif discret (38, 42,\dots), ou quantitatif continu (taille en mm)
%    \item satisfaction.
%   \end{enumerate}
% \end{Answer}


\begin{exo} On consid�re le tableau suivant : \\
 \begin{center}
  \begin{tabular}{c|cc}
   Salaire moyen en euros & Entreprise A & Entreprise B\\
   \hline
   Hommes & 1700 & 1800\\
   Femmes & 1300 & 1400
  \end{tabular}
  \qquad
  \begin{tabular}{c|cc}
   R�partition & Entreprise A & Entreprise B\\
   \hline
   Hommes & 50\% & 20\%\\
   Femmes & 50\% & 80\%\\
  \end{tabular}
 \end{center}
 \begin{enumerate}
 \item Calculer pour chaque entreprise la moyenne des salaires.
 \item Commenter les r�sultats.
 \end{enumerate}
\end{exo}

% \begin{Answer}[ref=stat_moy]
%  \item{Entreprise A : $0.5\times 1700+0.5 \times 1300=1500$\\
%            Entreprise B : $0.2\times 1800+0.8 \times 1400=1480$}
%  \item{La pond�ration a une grande influence sur le salaire moyen !}
% \end{Answer}


\begin{exo}
 La distribution des demandeurs d'emploi selon le sexe et la classe d'�ge dans une localit� est la suivante :
 \begin{center}
  \begin{tabular}{|c|c|c|p{1.5cm}|p{1.5cm}|}
   \hline
   Age & Hommes & Femmes & & \\
   \hline
   $[16;26[$ &  280 &  160 & &\\
   \hline
   $[26;40[$ &  310 &  360 & &\\
   \hline
   $[40;50[$ &  240 &  120 & &\\
   \hline
   $[50;60[$ &  420 &  530 & &\\
   \hline
   $[60;65[$ &   70 &   50 & &\\
   \hline
   Total     & 1320 & 1220 & &\\
   \hline
  \end{tabular}
 \end{center}
 \begin{enumerate}
 \item{Quelles sont les variables �tudi�es ? Quels types de variables ?}
 \item{Calculer la moyenne arithm�tique d'�ge des demandeurs d'emploi hommes, puis celle des femmes, puis la moyenne pour l'ensemble de ces demandeurs d'emploi.}
 \item{Quelle est la classe modale pour les hommes et pour les femmes.}
 \item{Calculer l'�ge m�dian pour l'ensemble des demandeurs d'emploi. Pour simplifier les calculs on utilisera les centres de classe.}
 \item{D�terminer l'�tendue et l'�cart inter-quartiles pour l'ensemble des demandeurs d'emploi.}
 \item{D�terminer l'�cart-type des �ges pour les hommes et pour les femmes.}
 \item{Calculer l'�cart moyen absolu et l'�cart m�dian absolu pour les hommes et pour les femmes.}
 \item{Commenter l'ensemble des r�sultats.}
 \end{enumerate}
\end{exo}

\begin{exo}
 Le tableau suivant donne, pour un �ge en ann�es donn�, la pression art�rielle moyenne lors de la contraction du c\oe ur.
 \begin{center}
  \begin{tabular}{c|ccccc}
   Age $x_i$ & 36 & 42 & 48 & 54 & 60\\
   \hline
   Tension art�rielle $y_i$ & 12 & 13.5 & 12.6 & 14.3 & 15.4
  \end{tabular}
 \end{center}
  \begin{enumerate}
 \item{D�terminer les coordonn�es du point moyen.}
 \item{Indiquer si un ajustement affine semble pertinent.}
 \end{enumerate}
\end{exo}

\begin{exo} On se donne deux crit�res qualitatifs pour lesquels on cherche une �ventuelle d�pendance :
  \begin{center}
  \begin{tabular}{|c|c|c|c|c|p{1.5cm}|}
   \hline
   Yeux $\setminus$ Cheveux & bruns & ch�tains & roux & blonds & \\
   \hline
   marrons  & 68 & 119 & 26 & 7 & \\
   \hline
   noisette & 15 & 54 & 14 & 10 & \\
   \hline
   verts    & 5 & 29 & 14 & 16 &\\
   \hline
   bleus    & 20 & 84 & 17 & 94 & \\
   \hline
   & & & & &\\
   \hline
  \end{tabular}
 \end{center}
  \begin{enumerate}
 \item{Compl�ter le tableau des effectifs th�oriques :}
  \begin{center}
  \begin{tabular}{|c|p{1.5cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|}
   \hline
   Yeux $\setminus$ Cheveux & bruns & ch�tains & roux & blonds & \\
   \hline
   marrons  & & & & & \\
   \hline
   noisette & & & & & \\
   \hline
   verts    & & & & &\\
   \hline
   bleus    & & & & & \\
   \hline
   & & & & &\\
   \hline
  \end{tabular}
 \end{center}
 \item{Calculer le coefficient de Cramer.}
 \item{Les variables semblent-elles d�pendantes ?}
 \end{enumerate}
\end{exo}



