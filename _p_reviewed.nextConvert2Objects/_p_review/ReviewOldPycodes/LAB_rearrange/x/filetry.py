import os

for file in os.listdir('/home/kishore/tempora'):
	fileTemp = open(file)
	for line in fileTemp:
		fileLine = fileTemp.readline()
		if 'kishore' in fileLine:
			print('found')
			break
	fileTemp.close()
