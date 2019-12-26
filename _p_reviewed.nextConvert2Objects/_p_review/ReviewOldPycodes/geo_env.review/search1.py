#! /usr/bin/env python3
#Foundations of python network programming
#https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter01/search1.py

from pygeocoder import Geocoder

if __name__ == '__main__':
	#address = '207 N. Defiance St, Archbold, OH'
	address = input('address for coordinates: ')	
	print(Geocoder.geocode(address)[0].coordinates)

