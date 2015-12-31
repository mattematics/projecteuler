"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def d(n):
	# returns sum of proper divisors of n
	# uses that divisors generally come in pairs n = k * (n/k)
	# except if n is a square
	s = 1
	sqrt_n = int(n**(0.5))
	for k in xrange(2,sqrt_n):
		if n%k==0:
			s += k + (n/k)
	if n == sqrt_n**2:
		s += sqrt_n
	return s

s = 0
h = {1:-1}
for a in xrange(3,10000):
	b = d(a)
	h[a] = b
	if not h.has_key(b):
		h[b] = d(b)
	if a != b and h[b] == a:
		s += a

print s