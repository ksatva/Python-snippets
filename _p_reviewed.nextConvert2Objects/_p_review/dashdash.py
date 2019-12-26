string='/ / /'
while True:
    print(string,end='')
    for i in range(len(string)):
        print('\b'*i,end='',flush =True)

def dotprint(dots):
    print(dots,end='')

def dotdel(dots):
    for i in range(len(dots)):
        print('\b'*i,end='',flush =True)
