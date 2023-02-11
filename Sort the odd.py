# Task
# 
# You will be given an array of numbers. You have to sort the odd numbers in 
# ascending order while leaving the even numbers at their original positions.
# Examples
# 
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
# 
def sort_array(source_array):
    temp = []
    for ind, val in enumerate(source_array):
        if val % 2 == 1:
            source_array[ind] = '-'
            temp.append(val)
    temp.sort()
    for val in temp:
        source_array[source_array.index("-")] = val
    return source_array

print(sort_array([7, 1]))
print(sort_array([5, 8, 6, 3, 4]))
print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))