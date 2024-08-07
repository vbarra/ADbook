# Introduction


## Eléments de vocabulaire
On définit ici de manière informelle les termes utilisés dans la suite :
```{index} Population
```
- **Population** : ensemble de cardinalité finie, notée $N$, ou infinie ;
```{index} Echantillon
```
- **Echantillon** : sous-ensemble de la population, de cardinalité $n$ ;
```{index} Individu
```
- **Individu** : sous-ensemble de la population ou de l'échantillon, de cardinalité 1 ;
```{index} Caractère
```
- **Caractère** : nature de la caractéristique à laquelle on s'intéresse statistiquement. Il peut être **qualitatif** (nominal ou ordinal) ou **quantitatif** (discret ou continu).


## Probabilités et statistiques
La question qui se pose est la suivante : comment définir ou estimer la valeur de probabilité associée à un  évènement ?
Plusieurs points de vue ont été proposés et adoptés que nous synthétisons très brièvement.

### Approche fréquentiste
Ce point de vue historique, souvent présenté comme le plus “naturel” ou “objectif”, consiste à définir une probabilité comme la limite de la fréquence d'observation de la caractéristique lorsque la taille de l'echantillon devient infinie. On suppose ici que les probabilités sont une loi de la nature qu’il faut mesurer par l’expérience. En pratique, la probabilité d’un  évènement est donc estimée/approximée en répétant un très grand nombre de fois l’expérience dans les mêmes conditions. C'est de ces expériences répétées que sont nés les outils de la statistique tels que la régression linéaire ou le test du $\chi^2$.
On rencontre néanmoins très rapidement des limitations avec ce type d'approche. D’une part, il est impossible d’un point de vue fréquentiste de traiter de petits échantillons de données. De plus, certains types de données ne sont 
pas exploitables en raison de leur caractère non expérimental (par exemple, quelle probabilité associer à un évènement du type “nombre de votants aux prochaines élections” qui n’est pas répétable). Enfin, il est parfois difficile de définir un modèle  permettant de modéliser une erreur de mesure ou la variation observée d’un caractère dans une population.

### Approche bayésienne
```{margin} T. Bayes
![](./images/bayes.jpeg)
```
Un point de vue bien différent consiste à définir les probabilités comme une mesure subjective de l'incertitude. Dans ce cadre, tout événement peut être probabilisé à partir d’un a priori de l’observateur. Ce point de vue est appelé Bayésien (fait appel à la règle de Bayes) pour calculer la loi de probabilité des évènements à partir des échantillons de données a posteriori. L’intérêt majeur de ce type de démarche est que tout est probabilisable (jusqu’aux paramètres du modèle utilisé) et qu'il s’appuie sur des résultats de la théorie des probabilités, comme le théorème central limite.
Ce point de vue “subjectif” a longtemps été dénoncé par les adeptes de l'approche fréquentiste qui rejettent l’idée que l’on puisse définir un tel a priori sur les évènements. En effet, l’objection majeure que l’on oppose souvent à la méthodologie bayésienne est que deux observateurs différents, ayant des a priori différents, donneront des résultats ou des interprétations différentes.

## Démarche générale
De manière assez générale, une étude statistique consiste à obtenir des informations sur un caractère concernant une population de grande taille en s'appuyant sur celles d'un sous-ensemble de taille réduite (l'échantillon), afin le plus souvent d'orienter une décision. Le choix de l'échantillon se fera par tirage avec ou sans remise, par tirage uniforme ("au hasard") ou non (tirage stratifié dans le cas d'un sondage par exemple, ou selon une loi de probabilité précise si une information a priori est disponible). 
On estime alors des propriétés d'un caractère de l'échantillon. A partir de ces estimations, on cherche à donner "au mieux" des valeurs aux paramètres correspondant de la population (la moyenne, la variance,...). L'estimation pourra être ponctuelle ou par intervalle de confiance. On pourra également s'intéresser à des tests d'ajustement (ou d'adéquation) à une loi de type donné. La décision, étape finale de l'analyse statistique, se fera par des tests statistiques.

````{prf:example}
Un cuisinier cherche à savoir si sa sauce est suffisamment salée. Après avoir remué sa casserole, il prélève une cuillérée de sauce (l'échantillon). Il la goûte (il estime le caractère salé de l'échantillon). En fonction du résultat, il décide que la casserole de sauce (la population) est suffisamment salée ou pas.
````

::::{important}
```{index} Statistique ; descriptive
```
```{index} Statistique ; inférentielle
```
La science des statistiques se décompose donc en :
- la **statistique descriptive**, dont l'objectif est de décrire le caractère d'un échantillon en résumant l'information qu'il contient ;
- la **statistique inférentielle**, dont l'objectif est d'inférer, à partir de l'information recueillie sur l'échantillon, des propriétés valables sur la population, de manière la plus fiable possible.
::::

```{index} Statistique ; exploratoire
```
A cette dichotomie s'ajoute la **statistique exploratoire**, branche de l'analyse de données, qui cherche à comprendre l'organisation des individus de l'échantillon (existe-t-il des groupes d'individus semblables ? les caractères mesurés sont-ils les plus pertinents ?...)



Nous n'abordons pas dans ce cours la statistique inférentielle.