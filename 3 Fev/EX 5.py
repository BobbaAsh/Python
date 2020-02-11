Exercice 5.
Proposer une fonction arrondi(s) qui dans la chaîne s troncature tout les nombre décimaux. On autorise les nombres négatifs.q
Pour ce faire, vous avez la possibilité d’utiliser :
des () pour désigner des blocs de données dans l’expression rationnelle. pour remplacer chacun des blocs l’expression est r’\1_\2_’.

def arrondi(x):
    s1 = sub('\.[0-9]*', '', x)
    print(s1)

arrondi(m)
