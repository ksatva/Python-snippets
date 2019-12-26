#! /usr/bin/python

from hashlib import  *
lorem = 'A quick brown fox jumps over the lazy dog'
#from hashlib_data import lorem
h=hashlib.md5()
h.update(lorem)
print h.hexdigest()

