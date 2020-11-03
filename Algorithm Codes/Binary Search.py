# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 23:54:31 2020

@author: Jason
"""

"""
The computer generates a list of random numbers between 0 to 100. 
The user inputs a random number. 
The goal of the program is to check whether this random number is in the list
by using binary search. 
It will do this by:
    1) splitting the list into halves
    2) if number is in first half, eliminate the other half (and vice versa)
    3) continue this method until the number is found, or the size of the 
    list (or half of the list) becomes 0, at which point the program can
    conclude that the number is not in the list.
"""
def binary_search(input_array, value):
    low = input_array[0]
    high = input_array[len(input_array)-1]
    try:
        while low <= high:
            mid = (low + high)//2
            if value == mid:
                return input_array.index(mid)
                break
            elif value < mid:
                high = mid - 1
            elif value > mid:
                low = mid + 1

    except ValueError:
        return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
    
            
        
