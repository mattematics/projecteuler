import time

#find biggest palindrome made by multiplying two 3-digit numbers

def f1():
    # naive first solution
    # make a list to store every palindrome we find
    palindromes = []
    # loop over each pair of 3-digit numbers
    for x in range(100,1000):
        for y in range(100,1000):
            # get their product
            p = x*y
            # check if p is a palindrome by casting to string and reversing
            if str(p) == str(p)[::-1]:
                # store p if it is a palindrome
                palindromes.append(p)
    # get the biggest palindrome from our list
    biggest = max(palindromes)
    # print it
    print biggest

def f2():
    # we don't need all pairs (x,y)
    # here we only consider (x,y) with x <= y
    palindromes = []
    for x in range(100,1000):
        for y in range(x,1000):
            p = x*y
            if str(p) == str(p)[::-1]:
                palindromes.append(p)
    biggest = max(palindromes)
    print biggest

def f3():
    # we don't need to store the list
    # here we only keep the biggest found so far
    biggest = 0
    for x in range(100,1000):
        for y in range(x,1000):
            p = x*y
            if str(p) == str(p)[::-1]:
                if p > biggest:
                    biggest = p
    print biggest

def f4():
    # we don't need to cast p to a string if it is too large
    # here we compare to biggest first
    biggest = 0
    for x in range(100,1000):
        for y in range(x,1000):
            p = x*y
            if p > biggest:
                if str(p) == str(p)[::-1]:
                    biggest = p
    print biggest

def f5():
    # the biggest palindrome is probably near the larger values of x,y
    # here we loop from 999 down
    # and we skip smaller values of x,y using breaks
    # since multiplication is increasing in each coordinate
    biggest = 0
    for x in range(999,99,-1):
        if x*999 < biggest:
            break
        for y in range(999,x-1,-1):
            p = x*y
            if p <= biggest:
                break
            if str(p) == str(p)[::-1]:
                biggest = p
    print biggest

def f6():
    # using that 6 digit palindromes (likely where answer is)
    # are divisible by 11, so at least one of x or y must be.
    biggest = 0
    for x in xrange(999,99,-1):
        if x*999 <= biggest:
            break
        if x%11==0:
            for y in xrange(999,x-1,-1):
                p = x*y
                if p <= biggest:
                    break
                s = str(p)
                if s == s[::-1]:
                    biggest = p
                    break
        else:
            for y in xrange(990,x-1,-11):
                p = x*y
                if p <= biggest:
                    break
                s = str(p)
                if s == s[::-1]:
                    biggest = p
                    break
    #print biggest

N = 1000
t0 = time.time()
for k in xrange(N):
    f6()
t1 = time.time()
total = t1 - t0
print total
print total/N, 'seconds per call'