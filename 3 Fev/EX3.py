s = "Onze ans déjà que cela passe vite Vous"
s += "vous étiez servis simplement de vos armes la"
s += "mort n‘éblouit pas les yeux des partisans Vous"
s += "aviez vos portraits sur les murs de nos ville"
l = s.split()
ligne = [""]
for mot in l:
    mot += " "
    if len(ligne[-1]) + len(mot) < 24:
         ligne[-1] += mot
    else:
        ligne.append(mot)

print(ligne)
        