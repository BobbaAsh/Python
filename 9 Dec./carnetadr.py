"""
Gestion de fiche de contact avec
prenom, nom, naissance, couriel
"""
import pickle

### Section class
class CarnetAdr(object):
    """ Conteneur de fiches """
    carnet_adresse = []   
    def __init__(self, prenom=None, nomfami=None,
                datenaiss=None, courriel=None):
        self.prenom = str(input("Quel est ton prenom ? "))
        self.nomfami = str(input("Quel est ton nom de famille ? "))
        self.datenaiss = str(input("Quel est ta date de naissance ? "))
        self.courriel = str(input("Quel est ton mail ? "))
        description =  self.prenom, self.nomfami,self.datenaiss,self.courriel
        with open('foo','wb') as d:
            pickle.dump(description,d)
 
        
class FichAdr(object):
    """ Fiche d'un contact """
    #Ajout méthode
    def __init__(self, prenom=None, nomfami=None,
                datenaiss=None, courriel=None):
        """ Initialise les 4 attributs.
        le format de datenaiss est JJ/MM/AAAA"""
        
        self.prenom = prenom
        self.nomfami = nomfami
        self.datenaiss = datenaiss
        self.courriel = courriel
        
    def __repr__(self):
        """ Produit une chaine selon l'objet FichAdr
        fourni en argument self."""
        
        patron = "FichAdr(prenom = '%s', "+\
            "nomfai = '%s', "+\
            "datenaiss = '%s' "+\
            "courriel = '%s')"
        return patron%(self.prenom, self.nomfami,
                       self.datenaiss, self.courriel)
    
### Section fonction
### Section principal main

if __name__ == "__main__":
    carnet_adr = CarnetAdr()
    with open('foo','rb') as d:
        e = pickle.load(d)
print(e)