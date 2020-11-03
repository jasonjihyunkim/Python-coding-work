# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 14:40:03 2020

@author: Jason
"""

def make_factorial(position):
    if position == 0:
        return 1
    else:
        factorial = int(position) * make_factorial(position-1)
    return factorial
        