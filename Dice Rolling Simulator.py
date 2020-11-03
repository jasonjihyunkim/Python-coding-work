# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 23:42:59 2020

@author: Jason
"""

import random
import time
def main_loop():
    while True:
        dice_value = random.randint(1,7)
        sleep(2)
        see_dice = input("Would you like to see the value of the dice?(y/n)"
                         " Type 'quit' to stop playing: ")
        if see_dice == 'y':
            print(dice_value)
        elif see_dice.lower() == 'quit':
            break
        else:
            print("Okay, moving onto the next one then!")
    print("Come play again sometime!")