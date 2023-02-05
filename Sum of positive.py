# You get an array of numbers, return the sum of all of the positives ones.
# 
# Example [1,-4,7,12] => 1 + 7 + 12 = 20
# 
# Note: if there is nothing to sum, the sum is default to 0.
def positive_sum(arr):
    return sum(x if x > 0 else 0 for x in arr)

print(positive_sum([1, -4, 7, 12]))
