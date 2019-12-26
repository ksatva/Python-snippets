#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 23:44:53 2019

@author: root
"""

import requests

url='https://docs.python.org/3/library/functions.html' # ----------< INPUT >

r = requests.get(url) # use try catch  # MY RESEARCH : "OBJECT" r


class _anatomy():
    def __init__(self,rdata):
        self.rdata = rdata
        self.alldirs =  dir(self.rdata)    #
        #self.allvars =  vars(r)   #dictionary
        self.countdirs = len(self.alldirs)
## -----ANALYSE request object 'r' 
#alldirs =  dir(r)    #list
#allvars =  vars(r)   #dictionary
#. type
#. id
#. 

"""
type()    :type of object
dir()     :set of attributes
id()
getattr()
hasattr()
globals()
locals()
callable()
"""


# -----< alldirs >---creating command strings (to read objects of [alldirs]
command = list()
for i in range(0,len(alldirs)):
    command.append('r.' + str(alldirs[i]))

#### -- HOW DO I RANDOMLY EXECUTE A COMMAND FROM THE ENTIRE LIST???
# >>>>>> ACCESSING OBJECT 'r' with r.<f
#-evaluate created commands--- e.g. eval(command[0]) 
for i in range(0,len(command)):
    print(command[i])
    
#   ----------< to view the contents of "each" object 1/1 >--
    #input('ACommandPress key for next..')
    print(eval(command[i]))
    input('->')
    
    # OR
# ---------------< RUN till here to test >----    
    
    
    











    
    
    
"""    
## Modify try ----< OOP >  --- Do I need it ????  
#--------< first look into the obhect >
class Obj1stLook():
    
    def __init__(self,obj):
        self.obj = obj
        print("Object type:\n", type(self.obj))
            
        # ------------< if a "requests object" >-

    def lookin(self):
        #return "Object type:\n{} \n\n Object content:\n{} \n\n Object id: \n{}".format(type(self.obj), dir(self.obj), id(self.obj))
        print(dir(self.obj))
            #print(id(self.obj)
            #self.getattr  =getattr(self.obj)
            #self.hasattr  =hasattr(self.obj)
            #self.globals  =globals(self.obj)
            #self.locals   =locals(self.obj)
            #self.callable =callable(self.obj)

    #def createCommand(self):#self.dir):
     #   print(self.dir)
    
x = Obj1stLook(r)
"""

##--------- other paradigm
def lookin(obj):
    return "Object type: {} |||| Object content: {} ||||  Object id: {}" \
            .format(type(obj), dir(obj), id(obj))
    #print(dir(self.obj))
    #print(id(self.obj)
            #self.getattr  =getattr(self.obj)
            #self.hasattr  =hasattr(self.obj)
            #self.globals  =globals(self.obj)
            #self.locals   =locals(self.obj)
            #self.callable =callable(self.obj)