# Your task is to sum the differences between consecutive pairs in the array in 
# descending order.
# Example
#
# [2, 1, 10]  -->  9
#
# In descending order: [10, 2, 1]
#
# Sum: (10 - 2) + (2 - 1) = 8 + 1 = 9
#
# If the array is empty or the array has only one element the result should be 
# 0 (Nothing in Haskell, None in Rust).
def sum_of_differences(arr):
    arr.sort(reverse=True)
    return sum([arr[i] - arr[i+1] for i in range(len(arr)-1)]) if len(arr) > 1 else 0 
        
print(sum_of_differences([2, 1, 10]))