# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 16:06:32 2020

@author: Jason
"""

import matplotlib.pyplot as plt

from random_walk import RandomWalk
"""Importing the class RandomWalk. We would create an instance of this class
which will already contain a default number of points, and instructions on how
to advance its position"""

#make an instance of random walk. Use the desired number of points.
rw = RandomWalk(50_000)
#this will create the list of x-coord and y-coord
rw.fill_walk()

plt.style.use('seaborn')
fig, ax = plt.subplots()
#when using colormap, gradient works based on the order of the points.
##point_numbers below numbers the points in the exact order they were plotted.
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues, 
           edgecolors = 'none', s = 1)
#emphasize the first and last point by replotting them and make them different
ax.scatter(0,0,c='green',edgecolors='none',s=50)
ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=50)

plt.annotate("Start",(0,0))
plt.annotate("End",(rw.x_values[-1],rw.y_values[-1]))

ax.set_title("Random Walk of 50 000 points", fontsize = 24)
ax.set_xlabel("x-coordinate", fontsize = 14)
ax.set_ylabel("y-coordinate", fontsize = 14)
ax.tick_params(axis = 'both', labelsize = 14)
#if you don't want to show the axes, you can do the following.
"""ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)"""

#To make the data more organized, you should put in a title and label the axes.

#This will simply show the plot. You can also save by plt.savefigt("Title")
plt.show()


    
"""If you want, you can use a while loop to keep this process running multiple
times"""

