# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 16:45:28 2024

@author: adwit
"""
import numpy as np
import pandas as pd 
car = pd.read_csv ('C:/Users/adwit/OneDrive/Documents/Python Scripts/file.csv')

print (car.head())

# Data Cleaning
# Find all the null values in the dataset. If there is any null value in any coloumn,
# then fill it with the mean of the column

car.isnull() # পুরো ডাটাসেট output এ দেখিয়ে null value গুলো চিহ্নিত করবে
car.isnull().sum () # কোন কলামে কতগুলো null value আছে।
completed_values = car['Cylinders'].fillna(car['Cylinders'].mean()) 
print (completed_values)                                           

# Value count :  Check what are the different types of "Make" are there in dataset ?
# What is the count of each "Make" ( particular column name ) in the data ?

car['Make'].value_counts()

# Data filtering : Show all the records where Origin is Asia or Europe

specific_origin = car['Origin'].isin(['Asia', 'Europe'])
print (car [specific_origin] )

# Removing unwanted records : Remove all the records where column weight is above 4000

Removed_rows = car['Weight'] > 4000 
print (car[~(Removed_rows)])

# Increase all values of 'MPG_City" column by 3

Increased_value = car['MPG_City'].apply (lambda x:x+3)
print (Increased_value)






































































































