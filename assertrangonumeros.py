# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 19:42:15 2021

@author: aherrera
"""

def readint(prompt, min, max):
    while (True):
        try:
            x=int(input(prompt))
            assert x>= min and x<=max
            return x
        except ValueError:
            print("error debe ingresar un numero")
        except:
            print ("error, el valor debe estar en el rango")

v = readint("Ingrese un numero entre -10 to 10: ", -10, 10)

print("The number is:", v)
