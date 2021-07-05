# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 18:50:46 2021

@author: aherrera
"""

def isPrime(x):

    if x<2:
        return False
    elif x==2:
        return True
    for i in range (2,x):
        if x % i==0:
            return False
    return True

for i in range(1,20):
    if isPrime(i+1):
        print(i+1, end=" ")
print()  