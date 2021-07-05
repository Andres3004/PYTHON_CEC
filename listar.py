# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 20:30:17 2021

@author: aherrera
"""
listaR=[]
listaS=[]
listaA=[]
lista=["R1", "R3", "R4",
       "S1", "S2", "S3", "AP1", "AP2"]
for p in lista:
    if "R" in p:
        listaR.append(p)
    elif "S" in p:
        listaS.append(p)
    else:
        listaA.append(p)
print("Elementos de lista R:" ,listaR)
print("Elementos de lista S:" ,listaS)
print("Elementos de lista A:" ,listaA)