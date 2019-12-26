#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 21:53:00 2019

@author: root
"""

class googling():
    def __init__(self,query):
    	self.query = query
    	for j in search(self.query, tld="co.in", num=10, stop=10, pause=2): 
		    print(j) 


if __name__ == '__main__':
	try:
		from googlesearch import search 
	except ImportError:
		print("No module named 'google' found") 

    #taking user input query for google search
	query = input('google search: ')
	googling(query)

