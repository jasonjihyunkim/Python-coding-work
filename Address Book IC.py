# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 02:20:28 2020

@author: Jason
"""


address_book = {}

def main_menu():
    """This is the main menu from where users can select a specific submenu."""

    print("\nwelcome to the address book. Please select on the following options:")
    user_choice = input("\tTo enter a new contact, enter 1. \n\tTo update a"
                        " contact, enter 2. \n\tTo find a contact, enter 3."
                        "\n\tTo remove a contact, enter 4."
                        "\n\tTo quit, enter 'quit': ")
    if user_choice == '1':
        enter_new()
    elif user_choice == '2':
        update_number()
    elif user_choice == '3':
        find()
    elif user_choice == '4':
        remove()
    elif user_choice == 'quit':
        return  
    else:
        print("\nSorry, your command was not recognized.")
        main_menu()


def enter_new():
    """This function allows entering new contact, which will be inserted to our 
    address book"""
    
    print("\nEnter 'quit' at any time to exit from this submenu.")
    while True:
        user_prompt = input("\nWould you like to enter a new contact? ")
        if user_prompt.lower() == 'quit' or user_prompt.lower() == 'no':
            break
        
        else:
            first_name = input("\n\tEnter your first name: ")
            if first_name == 'quit':
                break
        
            last_name = input("\tEnter your last name: ")
            if last_name == 'quit':
                break
        
            phone_number = input("\tEnter your phone number: ")
            if phone_number == 'quit':
                break
        
            full_name = first_name + " " + last_name
            address_book[full_name] = phone_number
    
    return_menu()
            
def update_number():
    """This function allows for updating the number of an existing contact."""
    
    print("\nEnter 'quit' at any time to exit from this submenu.")
    while True:
        user_prompt = input("\nWould you like to update a contact? ")
        if user_prompt.lower() == 'quit' or user_prompt.lower() == 'no':
            break
        else:
            name_update = input("\n\tEnter the full name of the contact that you"
                                " wish to update: ")
            number_update = input("\tEnter the new number for this person: ")
            if name_update == 'quit' or number_update == 'quit':
                break
            else:
                address_book[name_update.title()] = number_update
    return_menu()     


def find():
    """This function allows for searching the number of an existing contact."""
    
    print("\nEnter 'quit' at any time to exit from this submenu.")
    while True:
        user_prompt = input("\nWould you like to look for a contact? ")
        if user_prompt == 'quit' or user_prompt == 'no':
            break
        else:
            name_search = input("\n\tEnter the full name of the contact to search: ")
            if name_search == 'quit':
                break
            else:
                print(f"\n\tHere is the contact number for {name_search.title()}:" 
                      f" {address_book[name_search.title()]}")
    return_menu()
    
def remove():
    """This function allows deleting existing contact from the address book."""
    
    print("\nEnter 'quit' at any time to exit from this submenu.")
    while True:
        user_prompt = input("\nWould you like to delete a contact? ")
        if user_prompt.lower() == 'quit' or user_prompt.lower() == 'no':
            break
        
        else:
            name_delete = input("\n\tEnter the full name of the contact that"
                                " you wish to delete: ")
            if name_delete == 'quit':
                break
            else:
                address_book.pop(name_delete, "That contact doesn't exist.")
                print(f"\n\t{name_delete} has been removed from the address book.")
    
    return_menu()
    
    
        
def return_menu():
    
    user_prompt2 = input("\nWould you like to see the updated address book? ")
    if user_prompt2.lower() == 'yes' and address_book:
        print(address_book)
    else:
        print("The address book is empty.")
    
    user_prompt3 = input("\nEnter '1' to go back to the main menu, "
                         "and '2' to quit: ")
    if user_prompt2 == '1':
        main_menu()
    elif user_prompt2 == '2':
        return None
    else:
        print("\nCommand not recognized. Returning to main menu.")
        main_menu()
            
#you can use the pop function for them to delete entry by fullname, and give option
#in case they misspelled the name.
#Give a prompt before actually deleting


if __name__ == '__main__':
    main_menu()
#This ensures that if our program is ran as the main program (not called in as 
#part of another program, that we will always start with the function main_menu)
#This is particularly useful when we're using the cmd