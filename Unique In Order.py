# Implement the function unique_in_order which takes as argument a sequence and 
# returns a list of items without any elements with the same value next to each 
# other and preserving the original order of elements.
# 
# For example:
#
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
# unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]
#
# Algorithm
def unique_in_order(seq):
    return [c for i, c in enumerate(seq) if i+1 == len(seq) or c != seq[i+1]]

print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcAD'))
print(unique_in_order([1, 2, 2, 3, 3]))
print(unique_in_order((1, 2, 2, 3, 3)))
