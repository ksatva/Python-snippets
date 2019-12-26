#! /usr/bin/env python3
#Foundations of python network programming
#https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter02/udp_local.py
#UDP client and server on localhost

import argparse, socket
from datetime import datetime

MAX_BYTES = 65535

def server(port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind(('127.0.0.1',port))
	print('Server ear at: {}'.format(sock.getsockname()))
	while True:
		data, address = sock.recvfrom(MAX_BYTES)
		text = data.decode('ascii')
		print('::Incoming:: Client at {} says {!r}'.format(address,text))
		text = '::Incoming:: data size: {} bytes '.format(len(data))
		data = text.encode('ascii')
		sock.sendto(data, address)

def client(port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	text = 'Client time: {}'.format(datetime.now())
	data = text.encode('ascii')
	sock.sendto(data,('127.0.0.1',port))
	print('Client Address assigned by OS: {}'.format(sock.getsockname()))
	data, address = sock.recvfrom(MAX_BYTES) #Danger!
	text = data.decode('ascii')
	print('The Server {} replied {!r}'.format(address,text))

if __name__ == '__main__':
	choices = {'client':client,'server':server}
	parser = argparse.ArgumentParser(description='Send and receive UDP locally')
	parser.add_argument('role',choices=choices,help='which role to play')
	parser.add_argument('-p',metavar='PORT',type=int,default=1060, help='UDP port (default 1060)')
	args = parser.parse_args()
	function = choices[args.role]
	function(args.p)

