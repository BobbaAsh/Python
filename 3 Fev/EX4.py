Proposer un programme qui renvoie la liste de tout les nombres (y compris décimaux et négatifs) d’une chaîne de caractères.
A tester sur la chaîne : « Les 2 maquereaux valent 6.50 euros ».

def numList(x):
    motif = '[0-9]*(?:[\.\,]?[0-9]+)'
    print(findall(motif, x))

m = 'Les 2 maquereaux valent 6.50 euros'
numList(m)

