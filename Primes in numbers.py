# Given a positive number n > 1 find the prime factor decomposition of n. The 
# result will be a string with the following form :
#
#  "(p1**n1)(p2**n2)...(pk**nk)"
#
# with the p(i) in increasing order and n(i) empty if n(i) is 1.
#
# Example: n = 86240 should return "(2**5)(5)(7**2)(11)"

def prime_factors(n):
    remaining = n
    i = 2
    ret = ''
    while i < remaining: 
        count = 0
        while remaining % i == 0:
            count += 1
            remaining = remaining / i
        if count > 0:
            ret += f'({i}**{count})' if count > 1 else f'({i})'
        i += 1
    if remaining > 1:
        ret += f'({int(remaining)})'
    return ret

print(prime_factors(86240))