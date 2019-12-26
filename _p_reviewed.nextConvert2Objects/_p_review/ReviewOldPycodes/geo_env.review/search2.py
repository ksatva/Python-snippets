#! /usr/bin/env python3
#Foundations of python network programming
#https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter01/search2.py

import requests

def geocode(address):
	parameters = {'address':address,'sensor':'false'}
	base = 'http://maps.google.com/maps/api/geocode/json'
	response = requests.get(base, params=parameters)

	answer = response.json()
	print(answer['results'][0]['geometry']['location'])
	
if __name__=='__main__':
	address = input('address for coordinates: ')	
	geocode(address)
