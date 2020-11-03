# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 17:20:27 2020

@author: Jason
"""

import tkinter as tk
#use Tkinter to make GUI applications

from PIL import Image, ImageTk
#PIL is Python Imaging Library. Allows performing operations involving images
#in our UI

import random

root = tk.Tk()
#this initalizes the window manager, and assign to a variable. This creates
#a blank window with close, maximize and minimize buttons on the top
root.geometry('500x500')
root.title('Dice Rolling Simulator')

#calls the mainloop of Tk

BlankLine = tk.Label(root, text="")
BlankLine.pack()
#adding label into the frame

HeadingLabel = tk.Label(root, text="Hello! Roll the die!", fg = "white", 
                             bg = "black", 
                             font = "Calibri 18 bold")
HeadingLabel.pack()

AuthorLabel = tk.Label(root, text = "-Jason K.", fg = "dark green", font = "Calibri 14 bold")
AuthorLabel.pack()
#adding label with different font and formatting

dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']

DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
#simulating the dice with random numbers between 1 to 6 and generating the 
#corresponding image
#PhotoImage is a class that takes image or file location containing images as
#argument. 

ImageLabel = tk.Label(root, image = DiceImage)
#construct a label widget for image

ImageLabel.pack(expand = True)
#packing a widget in the parent widget

def rolling_dice():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    ImageLabel.configure(image = DiceImage)
    #update image
    ImageLabel.image = DiceImage
    #keep a reference

button = tk.Button(root, text = 'Roll the Dice', fg = 'blue', command = rolling_dice)
#adding button, and command will use rolling_dice function
button.pack(expand = True)
#pack a widget in the parent widget


if __name__ == '__main__':
    root.mainloop()