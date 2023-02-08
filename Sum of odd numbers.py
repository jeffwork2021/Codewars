# Given the triangle of consecutive odd numbers:
# 
#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...
# 
# Calculate the sum of the numbers in the nth row of this triangle 
# (starting at index 1) e.g.: (Input --> Output)
# 
# 1 -->  1
# 2 --> 3 + 5 = 8
# 3 --> 7 + 9 + 11 = 27
# 4 --> 13 + 15 + 17 + 19 = 64
# 5 --> 21 + 23 + 25 + 27 + 29 = 125
def row_sum_odd_numbers(n):
    return n*n*(n-1) + sum(list(range(1,n*2+1,2)))

print(row_sum_odd_numbers(1))
print(row_sum_odd_numbers(2))
print(row_sum_odd_numbers(3))
print(row_sum_odd_numbers(4))
print(row_sum_odd_numbers(5))
