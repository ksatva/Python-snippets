#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title - plot data
 (SKNayak PhD)

Created on Thu Aug 29 00:19:45 2019
@author: k as root
"""

import pandas as pd
%matplotlib inline
import random
import matplotlib.pyplot as plt
import seaborn as sns

df =  pd.read_csv('/root/ai/_worKCLASSICAL/SurajKNayak/_ResultsAll_forClassification.csv')
dfcolnames = list(df.columns.values)  #getting column names


#start plotting
#df.loc[:,[dfcolnames[1]]]  # OR df[dfcolnames[1]] #Selecting single column pandas dataframe
#df.loc[:,[dfcolnames[1],dfcolnames[3]]]           #Selecting multiple columns pandas dataframe
df[dfcolnames[1]]