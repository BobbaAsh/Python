#exercices 1
prix = 1
while prix != 0:
    i= float(input("Ecrit un prix HT:"))
    prix= i*1.2
    print("Le prix TTC est de", prix, "€")

#exercices2
myList = [1, 2, 3, 4, 3, 2, 1]
list_reversed = []
for item in myList:
    list_reversed.insert(0, item)
if myList == list_reversed:
    print('palindrome')
else:
    print('pas palindrome')