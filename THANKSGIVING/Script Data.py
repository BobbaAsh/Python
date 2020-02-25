#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 14:43:31 2020

@author: bobba
"""
import pandas as pd 


df = pd.read_csv('/home/bobba/code/Simplon/Exercices/THANKSGIVING/thanksgiving.csv',encoding='latin-1')
thanksgiving_yes = df[df['Do you celebrate Thanksgiving?'] == "Yes"]
df = thanksgiving_yes.dropna()
df = thanksgiving_yes.reset_index(drop=True)



apple_isnull = pd.isna(df['Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple'])
pumpkin_isnull = pd.isna(df['Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin'])
pecan_isnull = pd.isna(df['Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan'])
pie = apple_isnull & pumpkin_isnull & pecan_isnull
print(pie.value_counts())


def isnull(x):
    if pd.isnull(x):
        return None
    else : 
        l = x.split(' ')
        l = l[0]
        l = l.replace("+", "")
    return int(l) 
 
df['int_age'] = df['Age'].apply(isnull)

print(df['int_age'])

def convert(x):
    if pd.isnull(x):
        return None
    else : 
        l = x.split(' ')
        l = l[0]
        if l == "Prefer":
            return None
        l = l.replace("$", "").replace(",", "")
    return int(l) 


df['int_income'] = df['How much total combined money did all members of your HOUSEHOLD earn last year?'].apply(convert)

print(df['int_income'])