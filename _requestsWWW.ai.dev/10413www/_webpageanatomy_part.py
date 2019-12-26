#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 05:28:28 2019

@author: root
"""

#% reset
import requests
from bs4 import BeautifulSoup
# import json

#name = 'https://anaconda.org/anaconda/requests'
#name = 'https://2.python-requests.org/en/master/'
name = 'https://www.amazon.in/'
data = requests.get(name)
headers = data.headers['content-type']
encoding = data.encoding

pg_rcontent = data.content

#print(name)
#print(data)
print("Headers: ", headers)
print("Encoding: ", encoding)
#print(pg_rcontent)

soup = BeautifulSoup(pg_rcontent)#, 'html.parser')

tags=[]
for link in soup.find_all(True):
    #print(link.name)
    tags.append(link.name)

#length of tags[] and tags---
print("ListLength: ",len(tags),"\n",tags, "\n")

#removing duplicates---
distinct_tags=set(tags)
print("ListLength: ",len(distinct_tags),"\n",distinct_tags,"\n")

#words histogram---
hist = {i:tags.count(i) for i in tags}
print("Histogram of tags: \n", hist)

#soup.title
#soup.title.name
soup.title.string
#soup.title.parent.name
soup.p
#soup.p['class']

#soup.a
soup.find_all('a') # tag name goes inside "quotes
soup.find(id="link3")

#x=soup.get_text()
#len(x)

# NEXT:
# Apply AI ML: Identify important features (tags)..
# .. read for known knowledges
# .. compute to know more
# (understand the html structure)
# methods for all tags types
# NLP for text mining and summary (ref siraj raval youtube)
# cv for media mining
# download media
# fill forms