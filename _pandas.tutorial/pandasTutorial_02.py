#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title - Preparing data set for ML classification 
 (Removing and renaming of columns in feature table)
 (for SKNayak -PhD)
 
Created on Wed Aug 28 13:35:46 2019
@author: k as root
"""
import pandas as pd
#import seaborn as sns

df =  pd.read_csv('/root/ai/_worKCLASSICAL/SurajKNayak/_step1_PreprocessingAndFeatureExtraction_complete_OptimizationNeeded/_ResultsAll_raw.csv')

#df.shape
#df.head
#df.columns


# Slicing a column pandas
df.loc[1:5,['Name.1', 'Name.2', 'Name.3', 'Name.4', 'Name.5', 'Name.6']] #indexing
df.loc[1:5,['N','N.1', 'N.2', 'N.3', 'N.4', 'N.5', 'N.6']] #indexing and slicing
  

#get "column names" and rename them
dfcolnames = list(df.columns.values)  #getting column names


##--- write a rule for renaming (based on the data in 'dfcolnames')
# creating list of new names
newcols=list()
for el in dfcolnames:#range(1,164):
   
    if el == 'Name':
        #print(el)
        newcols.append(el)
        
    elif '.' in el:
        elx = el.split('.')
        nx = int(elx[1])+1
        newcols.append(elx[0] + '_IMF' + str(nx)) #new
        #print(newcols)
    
    else:
        newcols.append(el + '_IMF' + str(1)) #new
        #print(newcols)

#renaming
#df.rename(columns={'oldName1': 'newName1', 'oldName2': 'newName2'}, inplace=True)
for i in range(0,175):
    df.rename(columns={dfcolnames[i]: newcols[i]}, inplace=True)
#---renaming column names < end >



#--- Deleting column pandas
# del df['N']
for ix in range(1,8):
    #string = 'Name.'+str(ix)
    string1 = 'N_IMF'+str(ix)    #creating the 'name of the column'
    del df[string1]            #delete that column
    if ix > 1:
        string2 = 'Name_IMF'+str(ix)    #creating the 'name of the column'
        del df[string2]            #delete that column
#----deleting cols < end >




#--- saving to csv
with open('/root/ai/_worKCLASSICAL/SurajKNayak/_ResultsAll_rawNew.csv', 'w', encoding='utf-8') as f:
    df.to_csv(f, index=False)
#---write to csv < end > 


"""Done manually
#renaming 'elements' in column 'Name'
for i in range(0,200):
    sx = df.ix[i,'Name']   # pick the element
    sxl = sx.split('_')    # slicing with '_' present in element
    newsx = sxl[0]         # selecting the needed slice
    df = df.replace(sx,newsx)    
"""

"""## ---troubleshoot
#compare 2 pandas dataframe
from pandas.util.testing import assert_frame_equal
df1 =  pd.read_csv('/root/ai/_worKCLASSICAL/SurajKNayak/_ResultsAll_raw.csv')
df2 =  pd.read_csv('/root/ai/_worKCLASSICAL/SurajKNayak/_ResultsAll_rawNew.csv')

assert_frame_equal(df1, df2)
"""
