# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 14:44:01 2021

@author: steve
"""

# Les boucles 

for i in range(1,11):

    print("i a pour valeur", i)
    
villes = ["Eauze", "Paris", "Bordeaux","tours","Manciet"]

for ville in villes:
    print(f'les villes de la liste, {ville}')
    
for ville in range(1):
    print("Les villes de ma liste2", villes[0:5])
    
    
p = 'steve'

for i in range(len(p)):
    print(p[i])
    
print(  )

for i in p:
    print(i,end=" ")


import pandas as pd 

df = pd.read_csv('data.csv')

print(df)

des = df.describe().round(2)
print(des)
print("------------------------------------------")

# recherche des types de valeur
for col in df:
    print(col,type(col))
    print(df[col],type(df[col]))
print("--------------------------------------------")

print("je suis pret")

#afficher les 10 premieres ligne de la FCmax:

for index, rows in df.head(10).iterrows():
    print(rows['FCMAX'])
          

print("-----------------------------------")

with open('data.csv') as f:
    for line in f.readlines():
        print(line.split(',')[6])
  
#changer valeur dans un tableau

df['ANGINE'] = df['ANGINE'].map({'Oui': 1, 'Non': 0})
df['SEXE'] = df['SEXE'].map({'homme': 1, 'femme': 0})
df['TDT'] = df['TDT'].map({'AA': 1, 'AT': 2, 'DNA': 3, 'ASY':4})
df['PENTE'] = df['PENTE'].map({'Ascendant': 1, 'Plat': 2, 'Descendant': 3})
df['ECG'] = df['ECG'].map({'Normal': 0, 'ST': 1, 'LVH': 2})

print(df)

# deuxieme façon
'''
X=df.iloc[:, 1:10] #Paramètres qui estimeront CŒUR
Y=df.iloc[:,11] # CŒUR est la variable à prédire
'''





    

    
    

    
    
    

