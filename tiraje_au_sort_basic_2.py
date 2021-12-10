#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 16:37:53 2021

@author: cesar
"""

import pandas as pd

# Préparation de la dataframe

# importation du fichier .csv dans un data frame
df = pd.read_csv("/home/cesar/Dos_IA/tiraje_au_sort/info_apprenants_IA.csv")

# sélection des étudiants uniquement
df = df[1:17]

# nous faisons un mélange aléatoire des noms
df = df.sample(frac=1).reset_index(drop=True)

#print(df)

#print(df['Prénom'][0])

#print(len(df))

print()
print("Les groupes pour les veilles sont:")
print()
for i in range(0, len(df), 2):
    print( f"{df['Prénom'][i]} et {df['Prénom'][i+1]}")
    

'''
for col in df:
	print(col)
