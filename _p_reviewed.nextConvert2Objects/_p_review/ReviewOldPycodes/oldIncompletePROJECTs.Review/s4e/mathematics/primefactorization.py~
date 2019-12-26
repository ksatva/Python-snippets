# Prime factorisation

A = int(input('Prime Factors of: '))
print('-----prime factorisation------ \nA = %d' %A)

primefactors = [1]
n=2

import functools
while functools.reduce(lambda p,q:p*q,primefactors) < A :
	if A % n == 0:
		A = A/n
		primefactors += [n]
		
	else:
		n += 1
				
print('Prime Factors:\n'+str(primefactors[1:]))

