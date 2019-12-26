#Augmented assignment operators
#5 nos.

print('input var: ')
var = input()
def augAssign(var):
    var+=1
    print(var)
    var-=1
    print(var)
    var*=3
    print(var)
    var/=1
    print(var)
    var%=1
    print(var)

    return var

augAssign(var)
