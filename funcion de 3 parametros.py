# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 19:38:04 2021

@author: aherrera
"""

def direct(barrio,codigopostal,ciudad):
    print("Su barrio es: \nBarrio", barrio)
    print("Su codigo postal es: \t", codigopostal)
    print("Su ciudad es: \nCiudad", ciudad)
    
print("Ingrese los siguientes datos")
ba=input("Ingrese su barrio: ")
cp=input("Ingrese su codigo postal: ")
ci=input("Ingrese su ciudad: ")

direct(ba,cp,ci)