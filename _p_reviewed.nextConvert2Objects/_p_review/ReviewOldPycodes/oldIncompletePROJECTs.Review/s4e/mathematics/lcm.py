#LCM

class lcm:
	def __init__( self, numbers ):
		while True:
			numbers 

	divisorPrime = [2,3,5,7,11,13,17]

	def __nextnumbers__(self, inputNumbers, divisorPrime ):
		
		self._okflag = 0
		self._nokflag = 0
		self._newNumbers = []
		
		for number in inputNumbers:
			if number % divisorPrime == 0:
				self._newNumbers += [number / divisorPrime]
				self._okflag += 1
			else:
				self._newNumbers += [number]
				self._nokflag += 1
	
		if self._okflag >= self._nokflag:
			return self._newNumbers
		else:
			return inputNumbers
	
	def __nextPrime__( self, previousPrime ):
		for 
