import os

folcount = 0
sfcount = 0
filecount = 0
for fol, sf, file in os.walk('/home/kishore/testfol'):
    folcount+=1
    print('\nCURRENT FOLDER: '+str(fol))
    for s in sf:
        #sfcount+=1
        print('\tSUBFOLDER OF: '+str(fol)+':'+str(s))
    for f in file:
        filecount+=1
        print('\t\tFILE IN: '+str(fol)+':'+str(f))

print(folcount)
print(sfcount)
print(filecount)
