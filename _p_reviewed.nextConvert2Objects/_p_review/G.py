#The worlds simpliest web browser
#https://www.google.co.in/#q=hello+hi&*
import socket

'''
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.google.co.in',80))
#-----------

search_string = raw_input('Search: ')
searchurl = 'https://www.google.co.in/#q='+search_string+'&*'
print searchurl


mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True:
	data = mysock.recv(512)
	if (len(data)<1):
		break
	print data

mysock.close()
'''

request_text = """\
GET /maps/api/geocode/json?address={}&sensor=false HTTP/1.1\r\n\
Host: maps.google.com:80\r\n\
User-Agent: search4.py (Foundations of Python Network Programming)\r\n\
Connection: close\r\n\
\r\n\
"""
'''
if __name__ == '__main__':
	# Translating from the outside world of bytes to Unicode characters.
	input_bytes = b'\xff\xfe4\x001\x003\x00 \x00i\x00s\x00 \x00i\x00n\x00.\x00'
	input_characters = input_bytes.decode('utf-16')
	print(repr(input_characters))
	
	#
	#output_characters = output_characters.encode
'''


from urllib.parse import quote_plus

def eocode(address):
    sock = socket.socket()
    sock.connect(('maps.google.com',80))#
    
    request = request_text.format(quote_plus(address))
    
    sock.sendall(request.encode('ascii'))
    raw_reply = b''
    while True:
        more = sock.recv(4096)
        if not more:
            break
        raw_reply += more   
    print(raw_reply.decode('utf-8'))
    
    
if __name__=='__main__':
    eocode('207 N. Defiance St, Archbold, OH')
	#fetching data from socket
    #parsing
    #format1 = Template($$\n)
   # print(format1.substitute)
    
