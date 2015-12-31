"""
qudratics of the form
n^2 + an + b, where |a| < 1000 and |b| < 1000

find the product of the coefficients a and b in the
quadratic expression which produces the maximum number
of primes for consecutive values of n, starting with n=0
"""
def prime_test(n):
	if n < 2:
		return False
	if n % 2 == 0:
		return False
	k=3
	sqrt_n = int(n**(0.5))
	while (k <= sqrt_n):
		if(n%k == 0):
			return False
		k += 2
	return True

def poly(a,b,n):
	return n*n + a*n + b

primes = {}
#we will have to check all of these, so precompute them now
for b in xrange(0,1000):
	primes[b] = prime_test(b)

beststreak = 0
besta = 0
bestb = 0
for a in xrange(-999,1000):
	# don't need to check b < 2
	# since then poly(a,b,0) not prime
	# if a < 0, we don't need to check b < |a| + 2
	# since then poly(a,b,1) < 2 and not prime
	lower = 2
	if a < 0:
		lower += abs(a)
	for b in xrange(lower,1000):
		streak = 0  #also using this as n, since they're the same the whole time
		if primes[b]: #take advantage of pre-checked primes to avoid loop
			v = b #poly is just b when n = 0, this cuts down computations
			while True:
				if not primes.has_key(v):
					primes[v] = prime_test(v)
				if primes[v]:
					streak += 1
				else:
					if streak > beststreak:
						beststreak = streak
						besta = a
						bestb = b
					break
				#v = poly(a,b,streak)
				v += a + (streak << 1) - 1  #inductively compute next value of polynomial

print beststreak
#print besta, bestb
print 'answer', besta*bestb