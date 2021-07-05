# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 18:43:10 2021

@author: aherrera
"""
while True:
    x=input("ingrese un numero a contar: ")
    if x=="q" or x=="salir":
        break
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break