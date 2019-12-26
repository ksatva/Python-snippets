#! python3
#backuptozip.py
#azip file whose file name increments

import zipfile, os
print(os.getcwd())

def backuptozip(folder):
    #Backup the entire contents of a "folder" into a zip file

    folder = os.path.abspath(folder) #make sure folder is absolute

    #figure out the file name code for
    #what files already exist
    number = 1
    while True:
        zipfilename = os.path.basename(folder)+'_'+str(number)+'.zip'
        #if not os.path.exists(zipfilename):
         #   break
        number += 1

        #create the zipfile
        print('Creating%s...' %(zipfilename))
        backupzip = zipfile.ZipFile(zipfilename,'w')

        #walk the entire folder tree and compress files in each folder
        for foldername, subfolders, filenames in os.walk(folder):
            print('Adding files in %s....'%(foldername))
            #add the current folder to the zip file
            backupzip.write(foldername)
            #add all files in this folder to the zipfile
            for filename in filenames:
                newbase=os.path.basename(folder)+'_'
                if filename.startswith(newbase) and filename.endswith('.zip'):
                    continue #dont backup the backup zip files
                backupzip.write(os.path.join(foldername,filename))
        backupzip.close()
        print('Done.')
        break


backuptozip('/home/kishore/LearnPY')
