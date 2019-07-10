import prime_counter
import itertools
import numpy as np

# basic and inefficient approach
def get_num_coprimes(n, largest):
	totients = [1]
	i = 2
	while i < n: 
		if gcd(i,n) == 1:
			totients.append(i)
		i += 1

	return len(totients)

def gcd(a, b):
    if b ==0:
       return a 
    else:
       return gcd(b, a % b);

# more efficient brute-force approach
def prime_product_method(n, primes = [2,3,5,7,11,13,17,19]):
	prod = 1
	if n >= 2:
		idx = 0
		products = set()
		n_cpy = n
		diff = 0
		while idx < len(primes) and n_cpy != 1:
			if n_cpy % primes[idx] == 0:
				products.add(primes[idx])
				n_cpy /= primes[idx]
			else:
				idx += 1

		prod = n
		for p in products:
			prod *= (1-1/p)

	return int(prod)

# proposition: 	for any bound n, the number with the greatest ratio of x to its number of coprimes
#				will be the product of the most, smallest, consecutive primes possible for x to be 
#				equal to or less than n
#				e.g: 
#					n = 10: 	x = 6 = 2*3
#					n = 100: 	x = 30 = 2*3*5 
#					n = 1000:	x = 210 = 2*3*5*7

def maximum_primes_solution(upper):
	result = 1
	idx = 0
	root = np.floor((np.sqrt(upper))).astype('int32')
	primes = prime_counter.prime_counter(root)

	while result < upper and idx < len(primes):
		result *= primes[idx]
		idx += 1

	return result / primes[idx-1]


if __name__ == "__main__":

	print(maximum_primes_solution((1000000)))
	# 510510
	
