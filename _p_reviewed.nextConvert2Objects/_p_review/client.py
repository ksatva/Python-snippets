#client.py

from socket import *

#create a socket object
s = socket(AF_INET,SOCK_STREAM)

#GET LOCAL MACHINE NAME
host = gethostname()

port=9999

#connection to hostname on the port
s.connect((host,port))

#Receive no more than 1024 bytes
tm = s.recv(1024)

s.close()
print(' the time got from the server is %s'%tm.decode('ascii'))
