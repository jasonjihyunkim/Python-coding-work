# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 23:43:24 2020

@author: Jason
"""

#%%
"""Have a list of words that is chosen at random as the answer. 
The user inputs letters one at a time.
Keep a list (initially empty) of guessed letters. 
If the user guesses the same letter twice, give them a warning but don't deduct score.
If wrong letter is guessed, deduct score. Every time score is deducted, print 
out a progressive drawing of hangman. 
Once score reaches 0, game is over. 
If a letter is guessed correctly, print out the word with _ and the correct letter.'
If the user gets all the letters before their score is up, they win.
"""




#import the random library for choosing random word from a given category
import random


def main():
    guessed_letters = []
    mistake_count = 0
    
    word_dic = {
        'animals':['dog','cat','tiger','elephant','shark'],
        'cities':['toronto','boston','london','paris'],
        'fruits':['apple','bananas','watermelon','cherries']}
    
    print("\nWelcome to Hangman!\n")
    user_choice = input("Choose the category of words you'd " 
                        "like to play with (categories available: " 
                        "'animals', 'cities', 'fruits'): ")
    if user_choice.lower() == 'animals':
        chosen_word = random.choice(word_dic['animals'])
    elif user_choice.lower() == 'cities':
        chosen_word = random.choice(word_dic['cities'])
    elif user_choice.lower() == 'fruits':
        chosen_word = random.choice(word_dic['fruits'])
        
    word_so_far = ['__' for letter in range(len(chosen_word))]
    print(' '.join(map(str, word_so_far)))
    
    while True:
        guessed_letter = input("\nGuess a letter: ")
        guessed_letter = guessed_letter.lower()
        if guessed_letter not in guessed_letters:
            
            if guessed_letter in chosen_word:
                print(f"Yes, {guessed_letter} is one of the letters.\n")
                for i in range (len(chosen_word)):
                    if guessed_letter == chosen_word[i]:
                        word_so_far[i] = guessed_letter
          
            else:
                print(f"\nSorry, {guessed_letter} is not one of the letters.")
                guessed_letters.append(guessed_letter)
                print(f"Here is a list of incorrectly guessed letters so far: {guessed_letters}")
                mistake_count = mistake_count + 1
                print("\n")
                draw_hangman(mistake_count)
                
                
        else:
            print(f"You already guessed {guessed_letter}! Here is a list"
                  "of the guessed letters so far: {guessed_letters}")
        
        print(' '.join(map(str, word_so_far)))
        
        if ''.join(map(str,word_so_far)) == chosen_word:
            print("You got it! Congratulations!")
            break
        
        elif mistake_count == 4:
            print("Game over. You're out of guesses!\n")
            break
                
    play_again = input("Would you like to play again?(y/n) ")
    if play_again.lower() == 'y':
        main()
    else:
        print("Thanks for playing!")
        
        
def draw_hangman(mistake_count):
    if mistake_count == 1:
        print("---------")
        print("\t\tO")
    elif mistake_count == 2:
        print("---------")
        print("\t\t O\n\t\t\ /")
    elif mistake_count == 3:
        print("---------")
        print("\t\t O\n\t\t\ /\n\t\t I")
    elif mistake_count == 4:
        print("---------")
        print("\t\t O\n\t\t\ /\n\t\t I\n\t\t| |")
        print("Sorry, game over!")
    print("\n\n")



if __name__ == '__main__':
    main()  
            
    