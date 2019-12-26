import re
heroRegex = re.compile(r'Natman|Tina Fey')
mo1 = heroRegex.search('Natman and Tina Fey')
print(mo1.group())
mo2 = heroRegex.search('nd Tina Fey Natman')    
print(mo2.group())


batregex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batregex.search('batmobile, Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))
