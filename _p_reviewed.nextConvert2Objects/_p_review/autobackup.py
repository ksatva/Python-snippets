class device():

srcDevice = device()
dstDevice = device()

tizen = device()
uui = device()

tizen.startpath = '/run/user/1001/gvfs'
tizen.locationkey = '/Phone/Documents/docsync'
uui.startpath = '/media'
uui.locationkey = '/UUI/3460bookbackup'

#working with pendrive
#not working on mtp device

def locatefolder(startpath, locationkey):
    import os, shutil
    for folder, subfolder, files in os.walk(startpath):
        if locationkey in folder:
            print('located...')
            return folder

def walkreturnlist(folderpath):
    
    
def structuredata(locatedfolderpath):
    walkwork(locatedfolderpath):
    
def copy4backup(src,dst):
    srcData = []
    for folder,sub, files in os.walk(src):
        

    
    srcContent = os.listdir(src)
    dstContent = os.listdir(dst)
    for content in srcContent:
        tempsrcpath = os.path.join(src,content)
        if os.path.isfile(srcpathaddress):
            print('file: '+content)
            tempdstpath = os.path.join(dst,content)
            shutil.copy(src, topath)
            backup +=1

            
        if path
        if content in dstContent:
            continue
        e
    #locate folder
    frompath = '/home/kishore/Documents/'
    topath=''

    startpath = '/run/user/1001/gvfs'
    locationkey = '/Phone/Documents/docsync'
    #startpath = '/media'
    #locationkey = '/UUI/3460bookbackup'

    backup=0

    import os, shutil
    for folder, subfolder, files in os.walk(startpath):
        if locationkey in folder:
            print('located...')
            topath = folder
            break

frompathcontent = os.listdir(frompath)
topathcontent= os.listdir(topath)
for content in frompathcontent:
    if content in topathcontent:
        continue
    else:
        if os.path.isdir(os.path.join(frompath,content)):
            print('dir: '+content)
            src = os.path.join(frompath,content)
            dst = os.path.join(topath,content)
            #shutil.copytree(src, dst)
        elif os.path.isfile(os.path.join(frompath,content)):
            print('file: '+content)
            src = os.path.join(frompath,content)
            #dst = os.path.join(topath,content)
            #shutil.copy(src, topath)
            backup +=1
            #print(src)
print('%d file backup.'%backup)
#if file not exist
    #copy file from mother source to located folder
