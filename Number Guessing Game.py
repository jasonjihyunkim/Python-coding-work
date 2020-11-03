# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 00:05:04 2020

@author: Jason
"""

import random
import time 
def main_loop():
    num = random.randint(0,100)
    score = 10
    starting_hint(num)
    while True:
        guess = input("Enter your guess here. Type quit to exit: ")
        if guess.lower() == 'quit':
            break
        if score == 0:
            print("\nYou're out of luck. Try again next time!")
            break
            c
        elif int(guess) == num:
            print("\nYou got it! Your score is: ", score)
            break
        elif int(guess) > num:
            wrong_choice_high(guess,num)
            score = score - 1
            if score == 5:
                another_hint(num)
                sleep(3)
            continue
        else:
            wrong_choice_low(guess,num)
            score = score - 1
            if score == 5:
                another_hint(num)
                sleep(3)
            continue
        
    print(f"\nGame over. The correct answer was {num}")
    print("\n")
    play_again()
    
        
def play_again():
    play_again = input("\nWould you like to play again?(y/n) ")
    
    if play_again == 'y':
        main_loop()
    else:
        print("\nCome play again next time!")
    
    
def wrong_choice_high(guess,num):
    diff = int(guess) - num
    if diff > 0 and diff in range (50,100):
        print("You guessed way too high!")
    elif diff > 0 and diff in range (25,50):
        print("Getting close but still too high")
    elif diff > 0 and diff in range (1,25):
        print("A little high but in range!")
    
        
def wrong_choice_low(guess,num):
    diff = num - int(guess)
    if diff > 0 and diff in range (50,100):
        print("You guessed way too low!")
    elif diff > 0 and diff in range (25,50):
        print("Getting close but still too low")
    elif diff > 0 and diff in range (1,25):
        print("A little low but in range!")
        
def starting_hint(num):
    for i in range (2,num):
        if num % i == 0:
            if num % 10 ==0:
                print("/nHERE IS YOUR STARTING HINT: The number is a" 
                      "multiple of 10.")
                break
            elif num % 5 == 0:
                print("\nHERE IS YOUR STARTING HINT: The number is a" 
                      "multiple of 5, but not a multiple of 10.")
                break
            else:
                print("\nHERE IS YOUR STARTING HINT: The number is a composite,"
                      "and not a multiple of 5")
                break
        else:
            print("\nHERE IS YOUR STARTING HINT: The number is a prime number.")
            break
def another_hint(num):
    for i in range (2,num):
        if num % 2 == 0:
            print("HERE IS A HINT: The number is even")
            break
        else:
            print("HERE IS A HINT: The number is odd")
            break
    

if __name__ == '__main__':
    main_loop()
    