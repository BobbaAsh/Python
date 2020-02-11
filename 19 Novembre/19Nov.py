#polynome de second degrés

import math as m

#exercice 1
a = 3
b=  -7
c= -23
delta= b**2 - 4 * a * c

x1 = (-b + m.sqrt(delta))/ (2 * a)
x2 = (-b - m.sqrt(delta))/ (2 * a)
print(x1)
print(x2)

#exercice 2
d = m.gcd(217,440)
e = m.gcd(101,256)
f = m.gcd(86,71)

print(d,e,f)


#exercice 3
print("Calcule l'air d'un Cone droit")
r= float(input("Rayon?"))
h= float(input("Hauteur?"))

print(m.pi * r**2 * h /3)