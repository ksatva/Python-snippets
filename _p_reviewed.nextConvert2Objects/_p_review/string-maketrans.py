import string

leet = string.maketrans('abegiloprstz','463611092572')
s='the quick brown fox jumps over the lazy dog'
print(s)
print(s.translate(leet))
