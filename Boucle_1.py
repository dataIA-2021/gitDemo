# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 14:44:01 2021

@author: steve
"""



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





    

    
    

    
    
    

