import socket

from urllib.parse import quote_plus

def geocode(address):
	sock = socket.socket()
	sock.connect(('maps.google.com',80))
	request = request_text.format(quote_plus(address))
	sock.sendall(requests.encode('ascii'))
	raw_reply = b''
	while True:
		more = sock.recv(4096)
		print(more)#
		if not more:
			break:
		raw_reply += more
	print(raw_reply.decode('utf-8'))
	
