# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 18:38:33 2021

@author: aherrera
"""

contar=input("Ingrese el # al que debo contar: ")
contar=int(contar)
contador=1
while True:
    print(contador)
    contador+=1
    if contador>contar:
        break