#
#pathvaliditycheckblock.py
#mother path.py
def pathvalidcheck(path):
    import os
    if not os.path.exists(path):
        return False    #return -1 if path invalid
    else:
        return True
