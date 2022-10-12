# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 15:16:30 2022

@author: Kunj
"""

import csv     # imports the csv module
import sys      # imports the sys module
import pandas as pd #import pandas
import numpy as np  #import numpy
import matplotlib.pyplot as plt  #import matplotlib
import os        #import os module
import math      #import math

#Task 1
#1
f = open('TB_burden_countries_2014-09-29.csv') # opens the csv file
rows = f.readlines()
f.close()
print('numbers of rows in the csv file:',len(rows)) # number of rows,

#2
df = pd.read_csv('TB_burden_countries_2014-09-29.csv')
column = df['e_prev_num_lo']
sum = 0 
num_rows = 0 
for i in column :
     try : 
          if np.isnan(i) :
             continue 
          else:
             sum += 1
             num_rows += 1 
     except:
        continue 
average  = sum / num_rows 
print('average is :', average ) #average value of the column


#Task 2 

#1
array_a = np.linspace(5, 16)   #array of int ranging from 5 to 15
print('array_a is :',array_a)

#2
array_b = np.linspace(0, 23, 7)  #array containing 7 equally spaced numbers between 0 to 23
print('array_b is :' ,array_b)

#3
array_c = np.random.uniform(-1, 1, 5)
print('array_c is :', array_c) #array that follows uniform data distribution
#4
plt.hist(array_c, bins= [-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1])
plt.title('histogram')
plt.show()

#5
array_d = np.random.rand(10)   #generating two random arrays
array_e = np.random.rand(10)
temp = array_d - array_e 
distance = np.sqrt(np.sum(np.square(temp)))
print("Euclidean distance :", distance)   #finding euclidean distance between the two random arrays
    
