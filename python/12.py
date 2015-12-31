import time

# first triangular number to have over 500 divisors

def count_divisors(n):
	# returns the number of divisors of n
	# we compute it by finding the exponents of prime factors
	# and multiplying them
	# i.e. find each prime power (p_i)^(e_i) dividing n
	# and compute the product of all e_i
	divisors = 1

	# first find the exponent for 2
	# i.e. how many times 2 goes into n
	count = 1
	while n%2 == 0:
		count += 1
		n /= 2
	# multiply by the exponent
	divisors *= count

	# next, 3 and higher, this way we can go up 2 at a time
	# skipping evens since we've factored out all the 2s
	p=3
	# while n still has factors
	while n != 1:
		# find next p that divides n
		while n%p != 0:
			p += 2
		# find the exponent for p
		count = 1
		while n%p == 0:
			count += 1
			n /= p
		# multiply by the exponent
		divisors *= count

	return divisors

def find_T_n(limit):
	# returns first triangular number with at least
	# 'limit' many divisors
	# we use that the n-th triangular number is n(n+1)/2
	# and that n, n+1 never share factors
	# so we can obtain the number of divisors of T_n
	# by multiplying those of n times those of (n+1)/2
	# or those of n/2 times those of n+1
	# we'll do the /2 on whichever of n, n+1 is even
	n = 1
	needs_halving = True
	a,b = count_divisors(n), count_divisors((n+1)/2)
	# while the number of factors of T_n is less than the limit
	while a*b < limit:
		n += 1
		needs_halving = not needs_halving
		if needs_halving:
			a,b = b,count_divisors((n+1)/2)
		else:
			a,b = b,count_divisors(n+1)
	return (n*(n+1))/2

N = 1
t0 = time.time()
for k in xrange(N):
    find_T_n(500)
t1 = time.time()
total = t1 - t0
print total
print total/N, 'seconds per call'