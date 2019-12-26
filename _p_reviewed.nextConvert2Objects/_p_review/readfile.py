#! /usr/lib/python3

#read file

import os

for file in os.listdir('/home/kishore/x'):
	fileTemp = open(file)
	for line in fileTemp:
        	fileLine = fileTemp.readline()
        	if 'Helloworld' in fileLine:
                	print('found')
                	break
	fileTemp.close()
	

