#! /usr/bin/env python3
#Foundations of python network programming
#https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter01/getname.py

import socket

if __name__ =='__main__':
	hostname = 'www.python.org'
	addr = socket.gethostbyname(hostname)
	print('{} \tIP address:: {}'.format(hostname,addr))
