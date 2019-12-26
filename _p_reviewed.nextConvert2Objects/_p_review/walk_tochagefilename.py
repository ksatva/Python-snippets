
#FUNCTION
#FOR MODIFICATION IN NEED

#-------work defined in files'----------
#def walkwork(path,work):
def walkwork(path):

    import os
    
    folcount = filecount = 0
    for folder, subfolder, files in os.walk(path):
        folcount+=1
        #write work
                
        for file in files:
            filecount+=1
            #write work
           
           
folder = 'E:/.../1936342-G/test'
for filename in os.listdir(folder):
       infilename = os.path.join(folder,filename)
       if not os.path.isfile(infilename): continue
       oldbase = os.path.splitext(filename)
       newname = infilename.replace('.grf', '.las')
       output = os.rename(infilename, newname)
           
           
            print(file)
            #work


    print('count data returns...')        
    return {'PATH' : path, 'FOLDERS' : folcount, 'FILES' : filecount}
    
if __name__=='__main__':
	walkwork("/home/k/workbench/MTech_Research_work_NIT/SIGNALPROCESSING/Kaushik/copy of 5 sec")
	
	

