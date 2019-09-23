#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 13:05:22 2019

@author: frederik
"""
#1 a
#At first sight the file contains
#SURVIVED - a column containing information on wether the passengers survived, 
#Survived:1, Dead:0 (int)
#PCLASS - The respective passengerclasses, 1,2 and 3 (int)
#NAME - Full names and titles (str)
#SEX - male or female (string)
#AGE - (float)
#SIBLINGS/SPOUSES ABOARD - (int)
#PARENTS/CHILDREN ABOARD - (int)
#FARE - The respective passengers' ticketfare (float)

#1 b
#I haven't found any missing data in the presented dataset 
#2) 
import pandas as pd
#I'm creating a variable for the titanic.csv-file
titanic=pd.read_csv('titanic.csv')
print(titanic)
#Let us first make sure, that no values will result in null:
titanic.isnull().sum() #OK let's go
#Let us identify the categories in each column
print(titanic.dtypes)
#ALso we should make sure, all 887 passengers are represented
print(len(titanic)) #Good
#And if all 8 columns are there. And making sure, the names match the csv
print(titanic.columns) #All there!
#And here goes the total number of cells
print(titanic.size) #which is 7096
#3) 
#Let us first take a look at, how many of the 887 recorded passengers survived
print(titanic['Survived'])
print(titanic['Survived'].sum())
#Assuming 1 is survived and zero is death, the sum shows that 342 persons survived the accident
#In order to find statistics on the passenger ages, we will run the .describe() command on the Passenger-Column
titanic['Age'].describe()
#Here we'll see that the ages span from 0.42 up to 80
#We can find the median age by calling it directly from the column:
titanic['Age'].median() #Which turns out to be 28
#Let us also take a look at the average ticket price
titanic['Fare'].describe() #Which turns out to be 32.3 pound sterling
#And a surprising minimum at 0 for one lucky passenger
#Now let us investigate, if the survivors are mainly male of female (women and children)
titanic_pivot=titanic.pivot_table(index='Sex', columns ='Survived', values='Age', aggfunc='count')
print(titanic_pivot.head())
#Ved at lave en pivot-tabel, kan vi se at overlevelsesraten var højst for kvinder
#4) Findes der personer med samme efternavn
#First off we extract the Name-column as a list, and create an empty list for the last names
Name=(titanic['Name'])
last_names=[]
#Then we creat a for loop, that goes through the column 'Name', and appends
#-the last word.
for i in range(0, len(Name)):
    last_names.append(Name[i].split()[-1])
#Which should leave us with a list of the 887 last names
len(last_names) #great success
#The we create a for loop that calculates the recurrences of each name
recurrences=([last_names.count(x) for x in last_names])
print(recurrences)
#Which gives a rather chaotic visual, but although shows that several names (last names) are recurring
print(len(last_names)==len(recurrences))
#shows us, that all passengers are represented
#Then to make a smoother visual, we will make a dataframe showing the recurrency of each name
recurring_names=pd.DataFrame({'Last Name': last_names, 'Amount':recurrences})
print(recurring_names)
#Opg 5
passenger_per_class=titanic.pivot_table(columns='Pclass', values='Age', aggfunc='count')
print(passenger_per_class)
#first class=216, second class=184, third classe=487
#5) del 2 - Which passenger class had the highest mortality rate
pivot_passenger_class=titanic.pivot_table(index='Pclass', columns='Survived',values='Age', aggfunc='count')
print(pivot_passenger_class)
#3. within this dataset, third class had the highest mortality rate - 368 people died