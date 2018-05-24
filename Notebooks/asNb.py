import pandas as pd
import math

sp_authors = pd.read_csv("sp_authors.tsv", sep="\t")
print(sp_authors.head())

sp_authors["life-span"][0:10]*10
#wie Vektor-Mult

#sp_authors["new-life-span"] = sp_authors["death"] - sp_authors["death"] - sp_authors["birth"]
#add column with life-span ezpz

#Arithmetisches Mittel
#sp_authors["life-span"].sum() / len(sp_authors)
print(sp_authors["life-span"].mean())
n = len(sp_authors["life-span"])

#Markup
### Arithmetisches Mittel -> Lageparameter
## Mittlwert der Stichprobe
# $\overline{x} = \frac{1}{n} \sum \limits_{i = 1}^n {x_i} $
mean = sp_authors["life-span"].mean()

## Mittlerwert der Grundgesamtheit
# my
## Varianz der Stichprobe (Standardabweichung) -> Streuparameter
# $ s = \sqrt{\frac{1}{n-1} \sum \limits_{i = 1}^n (x_i - \overline{x})^2 } $
var = math.sqrt(
    sum(
        (sp_authors["life-span"] - mean)**2) /
        (n-1
    )
)
print(var)
## Varianz der Grundgesamtheit
# sigma
# sp_authors["life-span"].std()
# Standardabweichung ezpz