# -*- coding: utf-8 -*-
"""
Created on Mon May 17 20:24:48 2021

@author: norbe
"""

import pandas as pd

for i in range(1000, 3700, 100):
    for j in range(1, 5):
        df = pd.read_csv('or'+str(i)+'q'+str(j)+'Completo.csv')
        df = df.rename(columns = {'Nombre': 'Nombre', 'Factor': 'Factor', 'Categoria': 'Categoria', 'Indice-H': 'IndiceH', 'Cantidad-articulos-ultimo': 'CantidadArticulosUltimo', 'Cantidad-articulos-ultimos-tres': 'CantidadArticulosUltimosTres', 'Enlace': 'Enlace'})
        df.to_csv('or'+str(i)+'q'+str(j)+'Completo.csv', header = True, index = False) 
        
for x in range(1, 5):
        df = pd.read_csv('orq'+str(x)+'Completo.csv')
        df = df.rename(columns = {'Nombre': 'Nombre', 'Factor': 'Factor', 'Categoria': 'Categoria', 'Indice-H': 'IndiceH', 'Cantidad-articulos-ultimo': 'CantidadArticulosUltimo', 'Cantidad-articulos-ultimos-tres': 'CantidadArticulosUltimosTres', 'Enlace': 'Enlace'})
        df.to_csv('orq'+str(x)+'Completo.csv', header = True, index = False) 
