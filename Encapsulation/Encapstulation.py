#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 09:46:46 2020

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
    
ad = formulaire('doe', 'Alice', "1991")

print(ad.naissance)
print(ad.prenom) 
print(ad.nom) 