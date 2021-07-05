# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 20:33:41 2021

@author: aherrera
"""

def suma(*arg):
    print("\nTipo de datos del argumento")
    sum=0
    
    for n in arg:
        sum+=n
        
    print("Suma: ", sum)
    
suma(3)
suma(3,5)
suma(4,5,6,7)
suma(1,2,3,5,6)
suma(1,2,3,4,5,6,7,8,9)