#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 21:53:00 2019

@author: root
"""


try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
# to search 
query = "Shubham Mallik + Rourkela"
  
for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
    print(j) 

"""
#dev vcs
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    yield b'Hello, World\n'

if __name__ == '__main__':
    application()
    """