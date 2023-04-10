# In mathematics, the factorial of a non-negative integer n, denoted by n!, is 
# the product of all positive integers less than or equal to n. For example: 5! 
# = 5 * 4 * 3 * 2 * 1 = 120. By convention the value of 0! is 1.
#
# Write a function to calculate factorial for a given input. If input is below 
# 0 or above 12 throw an exception of type ArgumentOutOfRangeException (C#) or 
# IllegalArgumentException (Java) or RangeException (PHP) or throw a RangeError 
# (JavaScript) or ValueError (Python) or return -1 (C).
#
# More details about factorial can be found here.
from functools import reduce

def factorial(n):
    if n < 0 or n > 12:
        raise ValueError("Input is below 0 or above 12")
    elif n == 0:
        return 1
    else:
        return reduce(lambda x, y: x*y, range(1,n+1))


print(factorial(5))