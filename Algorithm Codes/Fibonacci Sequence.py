# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 14:21:23 2020

@author: Jason
"""

def get_fib(position):
#first define the values of 0 and 1
#next, get_fib(position) will have a value of the sum of the previous two.
#afterwards, increment the position value 
    if position == 0 or position == 1:
        return position 
    return get_fib(position-1) + get_fib(position-2)

    