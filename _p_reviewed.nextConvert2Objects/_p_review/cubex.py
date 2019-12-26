#!
#find the cube root of a perfect cube
def cubex():
    x=int(input('ENTER AN INTEGER: '))
    ans = 0
    while ans**3 < abs(x):
        ans += 1
    if ans**3 != abs(x):
        print(str(x)+ ' : Not a perfect cube')
    else:
        if x < 0:
            ans = -ans
        print('Cube root of ' + str(x) +' = '+str(ans))

'''while input('start? ')!='n':
    cubex()
'''
