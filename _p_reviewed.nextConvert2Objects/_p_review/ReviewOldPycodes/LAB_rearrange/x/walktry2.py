
"""
os.walk(path)

1) GO TO NEXT ROOM:
2) CHECK FOR ARTICLES AND SUBROOMS:
3-N) IF NO ARTICLES AND SUBROOMS: COME OUT FOR STEP (1)
3-Y) IF ATRICLES FOUND: NOTE DOWN; IF SUBROOMS FOUND: NOTE DOWN
4) GO TO SUB ROOM
5) REPEAT STEP (2),(3-N),(3-Y)

THATS HOW IT WORKS.
"""
import os

def walk(path):
    folcount = 0
    filecount = 0
    for fol, sf, file in os.walk(path):
        folcount+=1
        #print('\n'+ 'CURRENT FOLDER: '+str(fol))
        for f in file:
            filecount+=1
            #print('\t\tFILE IN: '+str(fol)+':'+str(f))
        #for s in sf:
            #print('\tSUBFOLDER OF: '+str(fol)+':'+str(s))
        
    
    print('Files : %d nos.'%filecount)
    print('Folders : %d nos.'%folcount)

    
