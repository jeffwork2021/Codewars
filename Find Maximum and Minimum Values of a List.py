# Your task is to make two functions ( max and min, or maximum and minimum, etc., depending on the language ) that 
# receive a list of integers as input, and return the largest and lowest number in that list, respectively.
# Examples (Input -> Output)
#
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
#
# Notes
#     You may consider that there will not be any empty arrays/vectors.

def minimum(arr):
    return compareVal(lambda a, b: a < b, arr, float('inf'))

def maximum(arr):
    return compareVal(lambda a, b: a > b, arr, Integer.MIN_VALUE)

def compareVal(f, arr, initialVal):
    ret = initialVal
    for x in arr:
        if f(x, ret):
            ret = x 
    return ret

print(minimum([1, 2, 3, 4, 5, 10]), maximum([4,6,2,1,9,63,-134,566]))
