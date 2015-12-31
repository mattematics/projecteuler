# which n under 10^6 produces the longest Collatz sequence

h = {1:0}

def L(k):
	if h.has_key(k):
		return h[k]
	else:
		if k&1:
			h[k] = 2 + L((3*k+1)/2)
		else:
			h[k] = 1 + L(k/2)
		return h[k]

mval = 0
mkey = 0

for k in xrange(2,10**6 + 1):
	v = L(k)
	if v > mval:
		mkey,mval = k,v

print mkey, mval