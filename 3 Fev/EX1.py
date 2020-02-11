#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 10:14:09 2020

@author: bobba
"""
#Exercices 1 
s = "L'eau Minérale est Nécéssaire pour le bon fonctionnement du Corps"
def hascap():
    for mot in s.split():
        list_empty = []
        if 65 <= ord(mot[0]) <= 90 :
             list_empty += [mot]             
    return ' '.join(list_empty)

print(hascap())

