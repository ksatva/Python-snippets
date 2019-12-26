#server.py

from socket import *
from time import *

#create a socket object
serverSocket = socket(AF_INET, SOCK_STREAM)

#get local machine name
host = gethostname()

port = 9999

#bind to the port
serverSocket.bind((host,port))

#queue for five requests
serverSocket.listen(5)

while True:
    #establish a connection
    clientSocket,addr = serverSocket.accept()

    print("Got a connection from %s"%str(addr))
    currentTime = ctime(time())+"\r\n"
    clientSocket.send(currentTime.encode('ascii'))
    clientSocket.close()
