#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 11:04:59 2018

@author: Mac
"""

import pandas as pd
from plotnine import *

#Question 1: Plot two relatd variables, load them into a text file, and produce a
#scatter plot of the two of them, including a trendline

iceTemp=pd.read_csv('tempIceCream.txt',sep=',',header=0)

a=ggplot(iceTemp,aes(x="temp",y="iceCream"))+geom_point()+coord_cartesian()+xlab("Temperature")+ylab("Ice Cream Sales")+stat_smooth(method="lm")
print(a)

#Question 2: Write a script that generates two figures to summarize the data in "data.txt"
#First, a barplot of population means
data = pd.read_csv("data.txt",sep=',',header=0)
mean_north = 0
count_north = 0
mean_south = 0
count_south= 0
mean_east = 0
count_east = 0
mean_west = 0
count_west = 0
#Calculating the mean
for i in range(0,len(data)):
    if(data.region[i] == "north"):
        mean_north = mean_north + data.observations[i]
        count_north = count_north + 1
    if(data.region[i] == "south"):
        mean_south = mean_south + data.observations[i]
        count_south = count_south + 1
    if(data.region[i] == "east"):
        mean_east = mean_east + data.observations[i]
        count_east = count_east + 1
    if(data.region[i] == "west"):
        mean_west = mean_west + data.observations[i]
        count_west = count_west + 1
#Calculating the means
mean_north = mean_north / count_north
mean_south = mean_south / count_south
mean_east = mean_east / count_east
mean_west = mean_west / count_west
#Creating a dataframe from the means
df = pd.DataFrame({"mean":[mean_north,mean_south,mean_east,mean_west],"region":['\'north\'','\'south\'','\'east\'','\'west\'']})
a=ggplot(df,aes(x='region',y='mean'))+geom_bar(stat='identity')
print(a)

#Second, a scatterplot of all observations

b = ggplot(data,aes(x='region',y='observations'))+geom_point()+geom_jitter()
print(b)



#Leaving this here as evidence for thinking, but wasn't a great process, and didn't actually solve the problem

#list_north=[]
#list_south=[]
#list_east=[]
#list_west=[]

#for i in range(len(data)):
#    if(data.region[i] == 'north'):
#        list_north.append(data.observations[i])
#    if(data.region[i] == 'south'):
#        list_south.append(data.observations[i])
#    if(data.region[i] == 'east'):
#        list_east.append(data.observations[i])
#    if(data.region[i] == 'west'):
#        list_west.append(data.observations[i])

#col_north = ['north']*len(list_north)
#col_south = ['south']*len(list_south)
#col_east = ['east']*len(list_east)
#col_west = ['west']*len(list_west)

        
#df_north = pd.DataFrame({'region':col_north,'observations':list_north})
#df_south = pd.DataFrame({'region':col_south,'observations':list_south})
#df_east = pd.DataFrame({'region':col_east,'observations':list_east})
#df_west = pd.DataFrame({'region':col_west,'observations':list_west})


