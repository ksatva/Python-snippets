#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title - Select a row from pandas dataframe 

Created on Sun Aug 25 03:17:46 2019
@author: k as root
"""

import pandas as pd

df = pd.read_csv('/root/ai/_worKCLASSICAL/SurajKNayak/_ResultBasicStatisticsB-NB.csv') # DATAFRAME 1

df.iloc[[1]]


#https://stackoverflow.com/questions/16096627/selecting-a-row-of-pandas-series-dataframe-by-integer-index#16099579
#https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html