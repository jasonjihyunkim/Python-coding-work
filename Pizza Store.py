# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 21:42:25 2020

@author: Jason
"""

def pizza_store():
    available_toppings = ['pepperoni', 'mushrooms', 'onion', 'pepper', 'bacon']
    requested_toppings = []
    while True: 
        topping = input ("What would you like on your pizza? ")
        requested_toppings.append(topping)
        if topping == str.lower("That's all"):
            requested_toppings.remove("that's all")
            break
    for topping in requested_toppings:
        topping = topping.lower()
    if requested_toppings:
        print("\nYou requested", *requested_toppings)
        print()
        for toppings in requested_toppings:
            if toppings in available_toppings:
                print(f"Adding {toppings}")
            else:
                print(f"{toppings.title()} is currently not available!")
    else: 
        print("Are you sure you want no toppings on your pizza?")
    print("\nYour pizza is ready!")