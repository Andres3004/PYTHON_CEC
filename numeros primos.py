# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 18:45:30 2021

@author: aherrera
"""

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

#print(isPrime(4))

for i in range(1,20):
    if isPrime(i+1):
        print(i+1, end=" ")
print()        