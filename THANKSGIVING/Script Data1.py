#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 14:43:31 2020

@author: bobba
"""
import pandas as pd 
import time

df = pd.read_csv('/home/bobba/code/Simplon/Exercices/THANKSGIVING/thanksgiving.csv',encoding='latin-1')
thanksgivig_yes = df[df['Do you celebrate Thanksgiving?'] == "Yes"]
df = thanksgiving_yes.dropna()
df = thanksgiving_yes.reset_index(drop=True)

apple_isnull = pd.isna(df['Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple'])
pumpkin_isnull = pd.isna(df['Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin'])
pecan_isnull = pd.isna(df['Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan'])

pie = apple_isnull & pumpkin_isnull & pecan_isnull
print(pie.value_counts())

def isnull(x):
    df = data()
    if pd.isnull(x):
        return None
    else : 
        l = x.split(' ')
        l = l[0]
        l = l.replace("+", "")
    return int(l) 
    df['int_age'] = df['Age'].apply(isnull)
    print(df['int_age'])
