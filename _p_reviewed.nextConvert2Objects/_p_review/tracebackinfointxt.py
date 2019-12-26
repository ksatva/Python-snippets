import traceback
try:
	raise Exception('This is the error message')
except:
	errorfile=open('errorinfo.txt','w')
	errorfile.write(traceback.format_exc())
	errorfile.close()
	print('the traceack info was written to errorinfo.txt')
