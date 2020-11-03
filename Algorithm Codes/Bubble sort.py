# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 15:25:06 2020

@author: Jason
"""

lis = [2,5,3,9,7]

def bubble_sort(lis):
    for i in range (len(lis)-1):
        for i in range (len(lis)-1):
            if lis[i] > lis[i+1]:
                lis[i],lis[i+1] = lis[i+1],lis[i]
            else:
                continue
    print(lis)
        