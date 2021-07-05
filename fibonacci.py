# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 18:31:35 2021

@author: aherrera
"""
def fibonacci(n):
    a,b = 0,1 #a igual a 0 y b igual a 1
    while a<n:
        print(a,end=" ")
        """ c=a+b
        a=b
        b=c"""
        a,b =b, a+b
    print()

fibonacci(8)
    