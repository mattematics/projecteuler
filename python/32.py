"""
The product 7254 is unusual, as the identity,
39 * 186 = 7254,
is written with each digit 1 through 9 exactly once.

Find the sum of all products ab such that a * b = ab have this property
"""

import itertools

#sum all the <= nine digit numbers c which can be written as a*b=c with a,b,c containing each 1-9 exactly once
#9! is 362880

products = set()
def intify(n):
    return int(''.join(map(str,n)))

digits = range(1,10)

for ab in itertools.permutations(digits, 5):
	for star in xrange(1,3):
	    product = intify(ab[:star])*intify(ab[star:])
	    if sorted(list(ab)+map(int,str(product))) == digits:
	        products.add(product)

ans = sum(list(products))
print ans