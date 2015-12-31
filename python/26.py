# find d < 1000 with the longest recurring cycle
# in the decimal part of 1/d

def cycle_length(d):
    # finds the length of the longest recurring sequence
    # in the decimal part of 1/d
    # returns 0 if there is no such sequence
    # does this by long division

    remainder = 1
    
    when_seen = {}
    step_count = 0

    # while remainder is nonzero
    while remainder:
        # find remainder after division by d
        remainder = remainder % d
        # if we've already seen this remainder
        if when_seen.has_key(remainder):
            # the length associated to that remainder 
            # is (our current step number) - (when we saw that remainder)
        	return step_count - when_seen[remainder]
        # otherwise, record the step on which we first see this remainder
        when_seen[remainder] = step_count
        # increase the step by 1
        step_count += 1
        # next step in long division
        remainder *= 10

    # the while will terminate because d is an int
    # so 1/d is either finite or repeats
    return 0

max_len = 0
max_num = 0

for d in range(1,1000):
	length = cycle_length(d)
	if (length > max_len):
		max_len = length
		max_num = d

print 'd', max_num
print 'length', max_len