# Given an array of integers.
# 
# Return an array, where the first element is the count of positives numbers 
# and the second element is sum of negative numbers. 0 is neither positive nor 
# negative.
# 
# If the input is an empty array or is null, return an empty array.
# Example
# 
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you 
# should return [10, -65].
def count_positives_sum_negatives(arr):
    n_positive = 0
    n_negative = 0
    if arr:
        for i in arr:
            if i > 0: n_positive += 1 
            if i < 0: n_negative += i
        return [n_positive, n_negative]
    else:
        return []

print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))