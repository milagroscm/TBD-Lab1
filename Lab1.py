# -*- coding: utf-8 -*-
"""
Created on Sun May 17 13:51:36 2020

@author: MILAGROS PC
"""

import pandas as pd
import numpy as np
from math import sqrt
import time

dato = pd.read_csv('data.csv', sep = ',', index_col = 0)

diccionario = dato.to_dict('dict')


inicio = time.time()

def filtrar_nan_dict(diccionario):
    newDict = dict()
    for (key, value) in diccionario.items():
        if not np.isnan(value):
            newDict[key] = value
    return newDict

usuario = dict()
for (key , value) in diccionario.items():
    usuario[key] = filtrar_nan_dict(value)

# print(usuario['Angelica'])

#Distancia de manhatan
def dist_Manhatan(user1, user2):
    manhatan = 0
    for key in user1:
        if key in user2:
            manhatan += abs(user1[key] - user2[key])
    return (manhatan)

print("\n")
# print("Distancia de Manhatan entre Hailey y Veronica :")
# print(dist_Manhatan(usuario['Hailey'], usuario['Veronica']))

def dist_Euclidiana(user1, user2):
    euclidiana = 0
    for key in user1:
        if key in user2:
            euclidiana += (user1[key] - user2[key])**2
    euclidiana = sqrt(euclidiana)
    return euclidiana

# print("Distancia Euclidiana entre Hailey y Jordyn :")
# print(dist_Euclidiana(usuario['Hailey'], usuario['Jordyn']))

def dist_Minkowski(user1, user2, r):
	minkowski = 0
	for key in user1:
		if key in user2:
			minkowski += (abs(user1[key] - user2[key]))**r
	minkowski = minkowski**(1.0/r)
	return minkowski

print("Distancia de Minkowski entre Angelica y Bill (r = 1):")
print(dist_Minkowski(usuario['Angelica'], usuario['Bill'], 1))

fin = time.time()
tiempo = fin - inicio
print("Tiempo de carga: ",tiempo)

    
    

