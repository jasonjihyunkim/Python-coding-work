# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 23:57:37 2020

@author: Jason
"""

"""
The user and computer plays rock-paper-scissors. 
Have a list of possible options for the computer and the user. Make sure that 
if a value not in the list is chosen, produce an error message. 
Computer randomly selects a value from the list
User inputs a value from the list
Print out both values, and determine who has won
Have an option to play again or quit the game.
"""

import random
def rps():
    possible_moves = {'rock':'scissors','paper':'rock','scissors':'paper'}
    computer_move = random.choice(list(possible_moves))
    
    while True:
        user_move = input("Enter your move: ")
        user_move = user_move.lower()
        if user_move not in list(possible_moves):
            print("User didn't select a valid choice")
        else:
            break
    
    print(f"\nComputer played: {computer_move}. \nUser played {user_move}.")
    if user_move == computer_move:
        print("\nIt's a draw!")
    else:
        for move1,move2 in possible_moves.items():
            if user_move == move1:
                if computer_move == move2:
                    print("\nUser wins!")
                else:
                    print("\nComputer wins!")
                    
    replay = input("\nWould you like to play again? (y/n): ")
    if replay.lower() == 'y':
        rps()
    elif replay.lower() == 'n':
        print("\nThanks for playing! See you next time.")
    
        
        