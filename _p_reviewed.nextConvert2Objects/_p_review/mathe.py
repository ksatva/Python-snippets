#!

#mathe.py


def splitcomplex(z = complexnumber):
	real = z.real
	imag = z.imag
	conjugate = z.conjugate()
	
	magnitude = (z.real**2 + z.imag**2) ** 0.5	
	#or
	magnitude = abs(z)	
	

	print('REAL: '+z.real)
	print('IMAG: '+z.imag)
	print('CONJUGATE: '+z.conjugate())
	

def is_factor(b, a)
	if b%a == 0:
		return True
	else:
		return False

#factorize------------
def factorize(b):

	if b<0 and b.is_integer() == False:
	 	print('not a +ve integer :: taking absolute %s'%str(abs(b)))
	
	number = abs(b)
	factors = []
	for i in range(1,number+1):
		if number%i == 0:
			factors += [i]
	
	print(factors)
	return factors


