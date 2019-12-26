#! /usr/lib/python3

#read file

import os

for file in os.listdir('/home/kishore/LearnPY'):
	fileTemp = open(file)
	for line in fileTemp:
        	fileLine = fileTemp.readline()
        	if 'helloworld' in fileLine:
                	print('found')
                	break
	fileTemp.close()
	

