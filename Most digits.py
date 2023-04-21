# Find the number with the most digits.
#
# If two numbers in the argument array have the same number of digits, return 
# the first one in the array.
def find_longest(arr):
    max_len = max([len(str(a)) for a in arr])
    for a in arr:
        if len(str(a))==max_len:
            return a
    