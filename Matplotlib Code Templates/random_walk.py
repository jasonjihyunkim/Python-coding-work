# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 16:41:52 2020

@author: Jason
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 15:57:46 2020

@author: Jason
"""

import random

class RandomWalk:
    """A class to generate random walks"""
    
    def __init__(self,num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points=num_points
        #all walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]
        """The latest value in these lists represent the current x-coord &
        y-coord of the object"""
        
    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step = self.get_step_x()
            y_step = self.get_step_y()
            if x_step == 0 and y_step == 0:
                continue
            else:
                x = self.x_values[-1] + x_step
                y = self.y_values[-1] + y_step
                self.x_values.append(x)
                self.y_values.append(y)
                

    def get_step_x(self):
            x_direction = random.choice([-1,1])
            x_distance = random.choice([0,1,2,3,4])
            x_step = x_direction*x_distance
            return x_step
    
    def get_step_y(self):
        while len(self.y_values) < self.num_points:
            y_direction = random.choice([-1,1])
            y_distance = random.choice([0,1,2,3,4])
            y_step = y_direction*y_distance
            return y_step
       
            
         
        
            