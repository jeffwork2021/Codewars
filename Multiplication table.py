# Your task, is to create N×N multiplication table, of size provided in 
# parameter.
#
# For example, when given size is 3:
#
# 1 2 3
# 2 4 6
# 3 6 9
#
# For the given example, the return value should be:
#
# [[1,2,3],[2,4,6],[3,6,9]]
def multiplication_table(size):
    l = list(range(1,size+1))
    return [list(map(lambda x: x*i, l)) for i in l]

print(multiplication_table(3))