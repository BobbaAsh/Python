#exer
n = float(input("Entre un nombre:cice 1"))
if (n%2 == 0):
    print("pair")
else:
    print("impair");

#exercice 2
ac = float(input("Entre AC:"))
bc = float(input("Entre BC:"))
ab = float(input("Entre AB:"))

v = [ac,bc,ab]
h = max(v)
if h == ac :
     *(ab**2 + bc**2 == h**2)
    print("Le triangle est rectangle")
elif h == ab :
    (ac**2 + bc**2 == h**2)
    print("Le triangle est rectangle")
elif h == bc:
    (ac**2 + ab**2 == h**2)
    print("Le triangle est rectangle")
else:
    print("Le Triangle n'est pas rectangle")
