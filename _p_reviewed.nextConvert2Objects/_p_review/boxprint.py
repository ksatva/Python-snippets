def boxprint(symbol,width,height):
    if len(symbol) != 1:
        raise Exception('symbol must besingle character string')
    if width<=2:
        raise Exception('width must be greater than 2')
    if height<=2:
        raise Exception('Height must nbe greater than 2')
    print(symbol*width)
    for i in range(height-2):
        print(symbol+(' '*(width-2))+symbol)
    print(symbol*width)

for sym,w,h in (('*',4,4),('0',20,5),('x',3,3),('ZZ',3,3)):
    try:
        boxprint(sym,w,h)
    except Exception as err:
        print('an exception occured: '+str(err))
