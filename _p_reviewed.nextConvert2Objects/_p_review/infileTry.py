count = 1
def infile(path, key):
    
    try:
        fileTemp = open(path)
        print('file open..')
        while True:
            for key in fileTemp:
                global count
                count= count+1
                print(fileTemp.readLine())
        return count
    except:
        return 'null'
