# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 02:06:40 2020

@author: Jason
"""

import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates, high, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high.append(int(row[5]))
        dates.append(current_date)
        lows.append(int(row[6]))
    

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, high, c='red', alpha = 0.5)
ax.plot(dates, lows, c = 'blue', alpha = 0.5)
ax.fill_between(dates, high, lows, facecolor = 'blue', alpha = 0.1)

ax.set_title("Daily high and low temperatures - 2018", fontsize = 24)
ax.set_xlabel("", fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize = 16)
ax.tick_params(axis = 'both', which = 'major', labelsize = 16)

plt.show()
    
    