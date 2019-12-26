import os

def searchinfiles(path,key):
	count=exception=0
	for f,s,files in os.walk(path):
		for file in files:
			pathTemp = (f+'/'+file)
			#print(x)	
		#count+=1
		#path = f+'/'+str(file[count])
		#print(path)
			try:
				fileTemp = open(pathTemp)
			#print(fileTemp)

				for line in fileTemp:
					fileLine = fileTemp.readline()
				#print(fileLine) 					
					if key in fileLine:
						count+=1
						print('<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
						print('found in %s'%file)
						print(fileLine)
						print(pathTemp)
						print('<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')	
						break
				fileTemp.close()
			except:
				#print('=+++++++++++++++++'+file)
				exception+=1
	if count == 0:
		print('no match')
	print('MATCH = %s'%count)
	print('EXCEPTION = %s'%exception)

searchinfiles('/','Helloworld')
