# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 01:32:44 2020

@author: Jason
"""
"""A random four digit number is generated, and the user tries to guess the 
number. For every time the guess matches the answer (with correct digit), 
this is called 'cow'. For every time a number in the guess is in the answer,
this is called 'bull'."""

import random
def cows_and_bulls():
    print ("Wlecome to the Cows and Bulls Game!")
    correct_num = random.randint(1000,10000)
    while True:
        guess_num = input("Enter a number:")
        cows_ct = 0
        bulls_ct = 0
        if guess_num.lower() == 'quit':
            break
        for i in [0,1,2,3]:
            if str(guess_num)[i] == str(correct_num)[i]:
                cows_ct = cows_ct + 1
            if str(guess_num)[i] in str(correct_num):
                bulls_ct = bulls_ct + 1
        print(f"{cows_ct} cows, {bulls_ct} bulls")
                
    print(f"The answer was {correct_num}")
        
        

    