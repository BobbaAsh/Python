#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 09:48:10 2020

@author: ash
"""


class formulaire:
    
    def __init__(self, nom, prenom, naissance):
        self.nom = nom
        self.prenom = prenom
        self.naissance = naissance
        
    def _set_naissance(self, naissance):
          if isinstance(naissance, list):
            na = ''.join([str(x) for x in naissance])
            if na.isnumeric():
                self._naissance = int(na)
            else:
              self._naissance = 1900  
          else:
                na = str(naissance)
          if na.isnumeric():
            self._naissance = int(na)
          else:
            self._naissance = 1900          
  
    def _get_naissance(self):        
        print("Valeur de Naissance :" , self._naissance)
        return   self._naissance       
    naissance = property(_get_naissance, _set_naissance)

    def _set_nom(self, nom):
        self._nom = str(nom).upper()
        
    def _get_nom(self):
        return  self._nom   
    nom = property(_get_nom, _set_nom)
    
    def _set_prenom(self, prenom):
        self._prenom = str(prenom).upper()
        
    def _get_prenom(self):
        return  self._prenom   
    prenom = property(_get_prenom, _set_prenom)
   
    def age(self):
        return 2020 - self._naissance
             
    def majeur(self):
        return self.age >= 18
    
    def memeFamille(self, formulaire):
        return self.nom == formulaire.nom
    
   
class data(formulaire):
    
    def __init__ (self, nom, prenom, naissance):
        formulaire.__init__(self, nom, prenom, naissance)
    
    def buildID (self):
        id = self.nom[0:2] + self.prenom[0:2] + str(self.age())
        return id
    
class recensement:
    
    def __init__(self, l1, l2, l3):
        self.f2020 = l3
        self.f2019 = l2
        self.f2018 = l1
        
    def permanents(self):
        return [f for f in self.f2020 
                if f in self.f2019 and f in self.f2018]

class listeelectorale(recensement, formulaire):
    
    def __init__(self, l1, l2, l3, nom, prenom, naissance):
        recensement.__init__(self, l1, l2, l3)
        formulaire.__init__(self, nom, prenom, naissance)
        

    
jd = data("doe", "jhon" , 1999)
print(jd.buildID())