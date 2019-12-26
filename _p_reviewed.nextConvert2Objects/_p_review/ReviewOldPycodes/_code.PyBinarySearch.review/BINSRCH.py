#recursion
A = 'array'
def binsrch( A,n,x,j ):
	lower = 1
	upper = n
	while ( lower<upper ):
		mid = (lower+upper)/2
		if x>A(mid):
			lower = mid+1
		else if x<A(mid):
			upper = mid-1
		else:
			j = mid
	j = 0
	
	return 
