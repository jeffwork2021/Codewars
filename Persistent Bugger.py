# Write a function, persistence, that takes in a positive parameter num and 
# returns its multiplicative persistence, which is the number of times you must 
# multiply the digits in num until you reach a single digit.
# 
# For example (Input --> Output):
# 
# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
# 4 --> 0 (because 4 is already a one-digit number)
# 
from functools import reduce

def persistence(n):
    i = 0
    now_n = str(n)
    while len(str(now_n)) > 1:
        now_n = str(reduce(lambda a, b: int(a)*int(b), now_n))
        i += 1
    return i

print(persistence(39))
print(persistence(999))
print(persistence(4))