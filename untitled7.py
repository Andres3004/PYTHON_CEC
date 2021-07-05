# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 19:36:15 2021

@author: aherrera
"""

print("inicio")
try:
    x=int(input("enter a number: "))
    y= 1 / x
    print(y)
    
except ZeroDivisionError:
    print("error no se puede dividir para cero /0.")
except ValueError:
    print("error debe ingresar numero")
except:
    print ("error, algo no salio bien...")
    
print("fin.")