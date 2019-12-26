import time
def calcProd():
    #calculate the productof the first 100000numbers
    product =1
    for i in range(1,100000):
        product*=i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is  %s digits long'%(len(str(prod))))
print('Took %s secondsto calculate'%(endTime-startTime))
