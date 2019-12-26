from socket import *
s= socket(AF_INET, SOCK_STREAM)
s.bind((" ",7000))
s.listen(5)
while True:
    c, a = s.accept()
    print('received connection from ',a)
    c.send('hello %s\n' %a[0])
    c.close()
           
           
