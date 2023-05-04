# Given a mixed array of number and string representations of integers, add up 
# the non-string integers and subtract the total of the string integers.
#
# Return as a number.
def div_con(x):
    return sum(map(lambda a: -float(a) if isinstance(a, str) else a, x))