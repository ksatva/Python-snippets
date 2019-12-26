#create empty bytes
empbyte = bytes(4)
print(empbyte)
print(type(empbyte))

#casst bytes to byte array
mutablebytes = bytearray(b'\00\x0F')
#bytearray allows modification
mutablebytes[0]=255
mutablebytes.append(255)
print(mutablebytes)
#cast bytearray back to bytes
immutablebytes = bytes(mutablebytes)
print(immutablebytes)

#reaing bytes from a file
with open('/home/kishore/cookie.dat','rb') as binaryfile:
    #read the whole file
    data = binaryfile.read()
    print(data)

    print()
    #seekpositon and redN bytes
    binaryfile.seek(0) #go to the begingng
    couplebytes=binaryfile.read(2)
    print(couplebytes)

print()

#integer to bytes
i= 14

#create one byte from the integer
sbyte = i.to_bytes(1,byteorder='big',signed=True)
print(sbyte)


#create four byte from the integer
fourbyte = i.to_bytes(4,byteorder='big',signed=True)
print(fourbyte)

#
print()
for i in range(20):
    print(i.to_bytes(1,byteorder='big',signed=True))

    
#compare differences tolittle endian
print(i.to_bytes(4,byteorder='little',signed=True))

#
bytesfromlist=bytes([255,254,253,252])
print(bytesfromlist)

onebyte =int('11110000',2)
print(onebyte)

#print out the binary string
print(bin(22))


print('BYTES TO INTEGER')
#CREATE INT FROM BYTES defau;t isunsigned
somebytes = b'\x00\xF0'
i = int.from_bytes(somebytes,byteorder ='big')
print(i)

#create signed int
i = int.from_bytes(b'\x00\x0F',byteorder ='big', signed=True)
print(i)

#use a list of integers 0-255 as a source ofbyte values
i = int.from_bytes([255,0,0], byteorder='big')
print(i)

#text encoding'
binarydata = b'I am text.'
text = binarydata.decode('utf-8')
print('text encodint')
print(text)

binarydata = bytes([65,66,67])
text =binarydata.decode('utf-8')
print(type(binarydata))
                   



























