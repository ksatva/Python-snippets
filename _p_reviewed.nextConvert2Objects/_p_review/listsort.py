#list sorting  ::sort(), sort(reverse=True)

#works for integer and string as well
#integer : ascending order
#string : alphabetical order

#input for list
#..

spam = [2,5,7.98,5,3,3.4,-5]
spam.sort()
print(spam)

spam = ['rats','bats','cats','ants','elephants']
spam.sort()
print(spam)

spam.sort(reverse=True)
print(spam)

#above doesnot work when list contains both int & str

#spam.sort(key=str.lower)
#considers all letters as lower case

spam = list('a quick BROWN fox JUMPS over a lazy DOG')
print(spam)
spam.sort(key=str.lower)
print(spam)

