import string
values = {'var':'foo'}

t = string.Template("""
variable         :$var
Escape          :$$
variable in text  :${var}iable
""")
print('TEMPLATE:',t.substitute(values))


s = """
variable         :%(var)s
Escape          :%%
variable in text  :%(var)siable
"""
print('INTERPOLATION:',s%values)
