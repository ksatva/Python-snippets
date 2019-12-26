import openpyxl
wb = openpyxl.load_workbook('/home/kishore/NOVEMBERBILL.xlsx')
print(type(wb))

print(wb.get_sheet_names())

sheet=wb.get_sheet_by_name('Sheet3')
print(sheet)

print(type(sheet))
print(sheet.title)

anothersheet = wb.get_active_sheet()
print(anothersheet)


