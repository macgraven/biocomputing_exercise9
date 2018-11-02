#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 11:04:59 2018

@author: Mac
"""

import pandas as pd
from plotnine import *

data=pd.read_csv('tempIceCream.txt',sep=',',header=0)

a=ggplot(data,aes(x="temp",y="iceCream"))+geom_point()+coord_cartesian()+xlab("Temperature")+ylab("Ice Cream Sales")+stat_smooth(method="lm")
print(a)