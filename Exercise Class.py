# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 02:44:30 2020

@author: Jason
"""

class ExerciseSession:
    
    def __init__(self, exercise_name, exercise_intensity, length_min):
        self.exercise_name = exercise_name
        self.exercise_intensity = exercise_intensity
        self.length_min = length_min
    
    def get_exercise(self):
        return self.exercise_name
    
    def get_intensity(self):
        return self.exercise_intensity
    
    def get_duration(self):
        return self.length_min
    
    def set_exercise(self, new_name):
        self.exercise_name = new_name
    
    def set_intensity(self, new_intensity):
        self.exercise_intensity = new_intensity
    
    def set_duration(self, new_length):
        self.length_min = new_length
    
    def calories_burned (self):
        if self.exercise_intensity == "Low":
            calories = 4*self.length_min
        elif self.exercise_intensity == "Moderate":
            calories = 8*self.length_min
        elif self.exercise_intensity == "High":
            calories = 12*self.length_min
        return calories
        
    