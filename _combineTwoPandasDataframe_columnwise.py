#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title - Combine pandas dataframes

Created on Sun Aug 25 02:06:31 2019
@author: k as root
"""

import pandas as pd

df1 = pd.read_csv('/root/ai/_worKCLASSICAL/SurajKNayak/_ResultBasicStatisticsB-NB.csv') # DATAFRAME 1
df2 = pd.read_csv('/root/ai/_worKCLASSICAL/SurajKNayak/_ResultsEntropy.csv')

#bigdata=pd.concat([df1,df2], axis=1, sort=False) # -columnwise combine
#bigdata = pd.concat([df1, df2.reindex(df1.index)], axis=1)
bigdata = pd.merge(df1, df2, how='inner', on=['Name'])

print(bigdata)

#writing to csv file
#bigdata.to_csv('/root/ai/_worKCLASSICAL/SurajKNayak/_combResultsEntropy.csv', sep='\t',encoding='utf-8')
with open('/root/ai/_worKCLASSICAL/SurajKNayak/_ResultsAll.csv', 'w', encoding='utf-8') as f:
    bigdata.to_csv(f, index=False)



# More info:------
# https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html