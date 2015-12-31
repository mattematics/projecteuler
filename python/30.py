# the sum of all numbers that can be written
# as the sum of 5th powers of their digits

# array of 5th powers of digits 0 through 9
fifth_pows = []
for k in xrange(10):
	fifth_pows.append(k**5)

def f(x):
	return fifth_pows[int(x)]

def summify(n):
	return sum(map(f,str(n)))

# find an upper bound on the number of digits in such numbers
max_digits = 1
while max_digits*(9**5) >= int("9"*max_digits):
	max_digits += 1

total = 0
for k in xrange(2,10**max_digits):
	if summify(k) == k:
		total += k

print total