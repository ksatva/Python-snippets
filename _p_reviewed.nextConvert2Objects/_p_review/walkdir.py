import os

counta = bcount = ccount = parcc = parc = parb = 0

for a, b, c in os.walk('/home/kishore/Music'):
    counta+=1
    print(a)
    for b in a:
        bcount+=1
        #print(b)
        for c in b:
            ccount+=1
            #print(c)
        parc+=ccount
    parcc+=parc
    parb+=bcount

print(counta)
print(parb)
print(parc)
#..............

bcount=ccount=0

for a, b, c in os.walk('/home/kishore'):
    for b in a:
        #print(a)
        bcount+=1
        for c in b:
            ccount+=1
    #print(a[+':'+str(bcount)+'::'+str(ccount))
    
for x,y,z in os.walk('/home/kishore/Music'):
    print(z)
