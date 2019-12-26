#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title - 

Created on Mon Aug 26 20:10:46 2019
@author: k as root
"""

import pandas as pd

# lets create a list of songs.
songs = ['In the name of love','Scream','Till the sky falls down','In and out of Love']

# lets also create a list of corresponding artists. FYI: 'MG' stands # for Martin Garrix, 'TI' for Tiesto, 'DB' for Dash Berlin, 'AV'for # Armin Van Buuren.
artists = ['MG','TI','DB','AV']

# likewise lets create a dictionary that contains artists and songs.
song_arts = {'MG':'In the name of love','TI':'Scream','DB':'Till the sky falls down','AV':'In and out of Love'}


# create a Series object whose data is coming from songs list.
ser_num = pd.Series(data=songs)
"""OUTPUT:
0	In the name of love
1	Scream
2	Till the sky falls down
3	In and out of Love
------
Q. So, what is a “Series” object in Pandas?
A. It is a data structure defined by Pandas. Basically it looks like a table having rows and columns.
   (numbers on the first column were added automatically by pandas. They serve as index.)
"""
# Accessing data in ser_num data structure
ser_num[1]

# make artists the index this time.-----< indexing > "Changing numbers to another value in list 
ser_art = pd.Series(data=songs,index=artists)
ser_art
"""OUTPUT:
MG        In the name of love
TI                     Scream
DB    Till the sky falls down
AV         In and out of Love 
"""
ser_art['MG']

# get the indices only
ser_art.index


# same rule as above for ---Dictionary
ser_dict= pd.Series(song_arts)
ser_dict



"""
https://hackernoon.com/intro-to-pandas-1-an-absolute-beginners-guide-to-machine-learning-and-data-science-a1fed3a6f0f3
http://gregreda.com/2013/10/26/intro-to-pandas-data-structures/
http://tomaugspurger.github.io/modern-1-intro
"""