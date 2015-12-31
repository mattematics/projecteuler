"""
In England the currency is made up of pound, $, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, $1 (100p) and $2 (200p).

How many different ways can $2 be made using any number of coins?
"""

# we'll build an array a = []
# a[n] will be the number of ways to make n cents in change

# start with ways to get to any value using 1c coins
# there's 1 way to make any value with only pennies
a = [1]*201

coins = [2,5,10,20,50,100,200]
# for each other coin, from lowest to highest
for c in coins:
	# for each value k up to $2
	for k in xrange(201):
		# if adding this coin gets you to another value k+c up to $2
		if k + c <= 200:
			# we've found a way to get to k+c from every path to k, so
			# add the number of ways to get to k to the number of ways to get to k+c
			a[k+c] += a[k]

# a[200] has the number of ways to get to exactly $2
print a[200]