#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 19:46:04 2017

@author: k
"""
#Write the contents of a folder on a spreadsheet
import os
path = input('Enter path:')
contents = os.listdir(path)
print(contents)

import openpyxl
wb = openpyxl.Workbook()
sheet = wb.get_active_sheet()

def writesheet(sheetname,what2write):
    startcellrow=1
    for item in what2write:
        count=startcellrow
        cellnumber = 'A'+str(count)
        print(cellnumber)
        sheet[cellnumber] = item
        startcellrow+=1
             
writesheet(sheet,contents)
savingfilename = input('file name for saving current sheet:')
savingfilepath=os.path.join(path,savingfilename)
wb.save(savingfilename)
print('Updated on spreadsheet')

#Next: arrange the contents of spreadsheet