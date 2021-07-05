# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 18:41:18 2021

@author: aherrera
"""

contar=input("Ingrese el # al que debo contar: ")
contador=1
contar=int(contar)
while contador<=contar:
    print(contador)
    contador+=1
    print("dentro del while")
print("fuera del while") 