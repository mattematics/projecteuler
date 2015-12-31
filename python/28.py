# sum of diagonals in a 1001 x 1001 square formed by
# increasing spiral of numbers eg
"""
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
"""

#4*7^2 - 6*(7-1)

total = 1
dimensions = 1001 # must be odd

for k in xrange(3,dimensions+1,2):
	total += 4*(k*k) - 6*(k-1)

print total