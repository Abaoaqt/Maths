import prime_counter

# brute force approach
def get_relative_primes(n, largest):
	totients = [1]
	i = 2
	while i < n: 
		if gcd(i,n) == 1:
			totients.append(i)
		i += 1

	return totients

def gcd(a, b):
    if b ==0:
       return a 
    else:
       return gcd(b, a % b);

# proposition: 	for any bound n, the number with the greatest ratio of x to its number of coprimes
#				will be the product of the most, smallest, consecutive primes possible for x to be 
#				equal to or less than n
#				e.g: 
#					n = 10: 	x = 6 = 2*3
#					n = 100: 	x = 30 = 2*3*5 
#					n = 1000:	x = 210 = 2*3*5*7

def prime_product_method(n, primes):
	idx = 0
	products = set()
	n_cpy = n
	while idx < len(primes) and n_cpy != 1:
		if n_cpy % primes[idx] == 0:
			products.add(primes[idx])
			n_cpy /= primes[idx]
		else:
			idx += 1

	totients = 210

if __name__ == "__main__":
	p = [2,3,5,7,11]
	prime_product_method(210,p)
	combs = set()
	l = ['a','b','c','d']
	for no in range(1, len(l)+1):
		for i in range(0,len(l)):
			combs.add("".join(l[i:i+no]))

	print(combs)
