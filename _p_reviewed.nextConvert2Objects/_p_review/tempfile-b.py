#block
#write o/p ina temporary file

def tempfile(x):
    tempFile = open('tempFile.txt','w')
    tempFile.write(x)###determine x
    tempFile.close()
    return tempFile
