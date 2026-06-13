import math
# basic utilities for working with fractions as 2d vectors

def lcm(int1, int2):
    return int(int1 * int2 // math.gcd(int1, int2))

def sign(frac):
    if (frac[0] < 0 and frac[1] > 0 or frac[0] > 0 and frac[1] < 0):
        return -1
    return 1

def build_sequence(seed, coeff, iterations):
    for i in range(iterations):
        seed += [[coeff ** (i+1), seed[i][1] * (seed[i+1][1] + coeff)]]
    return seed


def add_fracs(fraction1, fraction2):
    denominator = lcm(fraction1[1], fraction2[1])
    numerator = denominator // fraction1[1] * fraction1[0] + denominator // fraction2[1] * fraction2[0]
    result = simplify_frac([numerator, denominator])
    return result


def substract_fracs(fraction1, fraction2):
    denominator = lcm(fraction1[1], fraction2[1])
    numerator = denominator // fraction1[1] * fraction1[0] - denominator // fraction2[1] * fraction2[0]
    result = simplify_frac([numerator, denominator])
    return result


def simplify_frac(fraction):
    gcd = math.gcd(fraction[0], fraction[1])
    fraction = [fraction[0] // gcd, fraction[1] // gcd]
    return fraction


def whole_frac_part(fraction):
    simplify_frac(fraction)
    whole = [fraction[0] // fraction[1], 1]
    fractional = [fraction[0] - whole[0] * fraction[1], fraction[1]]
    return [whole, fractional]


def divide_fracs(fraction1, fraction2):
    result = [fraction1[0] * fraction2[1], fraction1[1] * fraction2[0]]
    result = simplify_frac(result)
    return result


def continued_frac(num, iterations):
    contd_frac = []
    for i in range(iterations):
        if num[1] == 0:
            break
        whole_fractional = whole_frac_part(num)
        num = whole_fractional[1]
        contd_frac += [whole_fractional[0][0]]
        if num[1] == 0:
            break
        num = divide_fracs([1, 1], num)
    return contd_frac