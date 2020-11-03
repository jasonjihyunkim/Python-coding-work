# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 13:40:15 2020

@author: Jason
"""

""""class to simulate a bank account""" 

class BankAccount:
    
    def __init__(self, first_name, last_name, balance = 0.0):
        self.log("Account has been created!")
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
    
    def deposit(self, amount):
        self.log(f"Deposit of {amount} has been made!")
        self.balance += amount
        
    def withdrawal(self, amount):
        self.log(f"Withdrawal of {amount} has been made!")
        self.balance -= amount
    
    def get_balance(self):
        self.log(f"Balance in your account is {self.balance}.")
        return self.balance
    
    
    def log(self, message):
        with open('Logging Info', 'a') as log:
            log.write(f"\n {message}")
        print(f"{message}")    
    
    