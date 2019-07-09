import numpy as np

def prime_counter(upper):
	primes = []
	for i in range(2, upper):
	    sqval = np.floor((np.sqrt(i)))
	    pbool = True
	    
	    j = 0
	    while j != len(primes) and primes[j] <= sqval and pbool:
	        if i % primes[j] == 0 and primes[j] != 1:
	            pbool = False
	        j += 1
	    
	    if pbool:
	        primes.append(i)

	return primes

print(len(prime_counter(1000000)))