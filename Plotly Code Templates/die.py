# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 22:08:40 2020

@author: Jason
"""
import random

class Die:
    
    def __init__(self,num_sides=6):
        self.num_sides = num_sides
    
    def roll (self):
        return random.randint(1, self.num_sides)