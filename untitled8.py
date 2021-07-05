# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 19:19:21 2021

@author: aherrera
"""

file=open("devices.txt")
for item in file:
    item=item.strip()#elimina el criterio
    print(item)
file.close()
    
