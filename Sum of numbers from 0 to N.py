# We want to generate a function that computes the series starting from 0 and ending until the given number.
# Example:
#
# Input:
#
# > 6
#
# Output:
#
#     0+1+2+3+4+5+6 = 21
#
# Input:
#
# > -15
#
# Output:
#
#     -15<0
#
# Input:
#
# > 0
#
# Output:
#
#     0=0
def show_sequence(n):
    if n > 0:
        return  f'{"+".join(map(str, range(n+1)))} = {sum(range(n+1))}'
    elif n == 0:
        return "0=0"
    else:
        return f'{n}<0'
    
print(show_sequence(6))