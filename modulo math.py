# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 19:14:17 2021

@author: aherrera
"""

import math
pi=3.14
def sin(x):
    if 2*x==pi:
        return 0.9999999
    else:
        return None
    
print(sin(pi/2))
print(math.sin(math.pi/2))