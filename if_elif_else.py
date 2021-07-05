# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 19:35:53 2021

@author: aherrera
"""

acl=int(input("Ingrese el numero de acl:"))
if acl >=1 and acl <=99:
    print(" ")
    print("La acl es estandar")
elif acl >=100 and acl <=199:
    print(" ")
    print("La acl es extendida")
else:
    print(" ")
    print("El # ingresado no es acl")