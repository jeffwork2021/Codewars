# The maximum sum subarray problem consists in finding the maximum sum of a 
# contiguous subsequence in an array or list of integers:
# 
# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]
# 
# Easy case is when the list is made up of only positive numbers and the 
# maximum sum is the sum of the whole array. If the list is made up of only 
# negative numbers, return 0 instead.
# 
# Empty list is considered to have zero greatest sum. Note that the empty list 
# or array is also a valid sublist/subarray.
# 
# Answer:
# Kadane's Algorithm is an iterative dynamic programming algorithm. It 
# calculates the maximum sum subarray ending at a particular position by using 
# the maximum sum subarray ending at the previous position.

def max_sequence(arr):
    max_sum = 0
    current_sum = 0

    for i in range(0, len(arr)):
        current_sum += arr[i]
        if current_sum < 0:
            current_sum = 0

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_sequence([]))
#print(max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]))


    