# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 19:33:17 2021

@author: aherrera
"""
lista1=["juan",5,5.7,True,5] #lista entre corchetes
print(type(lista1))
print(len(lista1))#len muestra el tamaño de cada estructura
tupla1=("juan",5,5.7,False,5,True)#tupla entre parentesis
print(type(tupla1))
print(len(tupla1))
print(lista1[0],"\n")
print(lista1[1],"\n")
print(lista1[2],"\n")
print(tupla1[0], "\n")
print(tupla1[-1], "\n")
lista1[1]="carlos"
print(lista1)
del lista1[2]
del tupla[0]
