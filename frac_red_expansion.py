import math
import frac_ops

#take fraction a/b and find the Bezout coefficients such that ax-by=1. 
# If you multiply a/b by x/x and subtract 1 from the numerator, 
# you get y/x. Take the difference a/b-y/x and you get a unit fraction. 
# repeat for y/x and so on until one of the Bezout is 1. 
# Then you have an egyptian fraction expansion of a/b. 
# The coefficients start out the same for fractions that are nearly equal, 
# even if the numerators and denominators differ massively. 
# For fractions close to 1 you ge the famous telescoping series n(n+1). 
# And if you take approximations of sqrt2, y
# ou also get similar numbers, so you can express it as a series. 
# you get 1+1/3+1/15+1/85+1/493+1/2871+1/16731 and so on

def bezout(frac, neg):
    a=b=1
    minimum = min(frac[0], frac[1])
    gcd = math.gcd(frac[0], frac[1])
    diff = frac[0] * a - frac[1] * b
    while (diff != gcd and -neg*diff != gcd):
        if (diff == 0):
            return frac
        if (diff > minimum):
            b+=1
        else:
            a+=1
        diff = frac[0] * a - frac[1] * b
    return [b, a]

def expansion(frac, neg):
    expansion=[]
    init = bezout(frac, neg) 
    while (frac[0] != 1):
        result = frac_ops.substract_fracs(frac, init)
        result = frac_ops.simplify_frac(result)
        expansion.insert(0, frac_ops.sign(result) * result[1])
        frac = init
        init = bezout(init, neg)
    expansion.insert(0, frac[1])
    return expansion

def differences(arr):
    diffs = [[] for _ in range(len(arr))]
    diffs[0]=arr
    for i in range(1, len(arr)):
        for j in range(len(arr) - i):
            diffs[i].append(diffs[i-1][j]-diffs[i-1][j+1])
            print(diffs[i][j], end=" ")
        print('\n')

fraction = [191, 2178]
print(bezout(fraction, 1))
print(expansion(fraction, 1))

#differences([3,7,9,10])
