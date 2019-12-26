import os

#for foldername, subfolders, filenames in os.walk('/home/kishore'):
    #print('foldername: '+foldername)
    #for subfolder in subfolders:
        #print('subfolder: '+foldername+':'+subfolder)
    #print('*')    
    #for filename in filenames:
       # print('file inside: '+foldername+':'+filename)

    #print(' >')
        
###just dispaly counted .next...
#fold=[]
foldercount =0
subcount = 0
sub=0

for foldername, subfolders, filenames in os.walk('/home/kishore'):
    #print('foldername: '+foldername)
    foldercount +=1
    for subfolder in subfolders:
        #print('subfolder: '+foldername+':'+subfolder)
        #for i in subfolder:
         #   fold[i] = 0
        #fold[i]
        subcount+=1
    #print('*')    
    #for filename in filenames:
     #   print('file inside: '+foldername+':'+filename)
    sub+=subcount
    #print(' >')

print(foldercount)
print(sub)
#for count in subcount:
 #   print(count)
    #+'::'+subdount
