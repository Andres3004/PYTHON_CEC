# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 19:31:25 2021

@author: aherrera
"""
lista=[]
file=open("devices.txt")
for item in file:
    item=item.strip()#elimina el criterio
    lista.append(item)
    print(item)
file.close()
print(lista)