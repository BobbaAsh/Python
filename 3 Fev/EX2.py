#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 14:36:18 2020

@author: bobba
"""

s = "Le prix est de 78"
x = s.split()
def inflation(x):
    for index , prix in enumerate(x) : 
        if prix.isnumeric() == True:
            return "Le prix est de", int(prix)*2


print(inflation(x))