#Tuple data type
#Immutable

eggs =('hello', 42, 0.5)

print(eggs[0])
print(eggs[1:3])
print(len(eggs))

#( , ) is important for type
type(('hello',))

#conversion list to tuple/tuple to list
listl = [1,2,3,4]
print(tuple(listl))
print(list(eggs))

