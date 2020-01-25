# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 17:11:36 2019

@author: 300997447
"""

import numpy as np
np.random.randint(1,100)
#Generate a random number between 0 and 1
import numpy as np
np.random.random()
#Define a function to generate several random numbers in a range
def randint_range_mayy(n,a,b):
    x=[]
    for i in range(n):
        x.append(np.random.randint(a,b))
    return x
list_x= randint_range_mayy(5,30,70)
#d.	Generate three random numbers between 0 and 100, which are all multiples of 5
import random
for i in range(3):
    print( random.randrange(0,100,5)) 
#  Select three numbers randomly from a list of numbers 
    list = [20, 30, 40, 50 ,60, 70, 80, 90]
sampling = random.choices(list, k=3)
print("sampling with choices method ", sampling)
#Generate a set of random numbers that retain their value, i.e. use the seed option
np.random.seed(1)
for i in range(3):
    print (np.random.random())
#Shuffle a list of 5 numbers
a = [1,2,3,4,5]
print(a)
np.random.shuffle(a)    
print(a)


import pandas as pd
filepath='C:/Users/300997447/Desktop/Data Wirehouse/New folder/Chapter 3/lotofdata'
data_final=pd.read_csv(filepath+'/'+'001.csv')
data_final_size=len(data_final)
for i in range(1,333):
    if i<10:
        filename='0'+'0'+str(i)+'.csv'
    if 10<=i<100:
        filename='0'+str(i)+'.csv'
    if i>=100:
        filename=str(i)+'.csv'
        
    file=filepath+'/'+filename
    data=pd.read_csv(file)
    data_final_size+=len(data)
    data_final=pd.concat([data_final,data],axis=0)
print (data_final_size)
data_final.shape


