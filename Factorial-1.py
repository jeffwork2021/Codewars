# Your task is to write function factorial.
from functools import reduce
def factorial(n):
    return reduce(lambda x, y: x*y, range(1, n+1), 1)

print(factorial(3))
