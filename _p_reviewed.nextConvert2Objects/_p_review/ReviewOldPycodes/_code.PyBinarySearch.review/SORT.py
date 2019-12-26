A = 'array'
def sort(A,n):
	for i in range(1,n):
		j = i
		for k in range(j+1,n):
			if( A(k)<A(j) ):
				j = k
		t = A(i)
		A(i) = A(j)
		A(j) = t
	
	return A

