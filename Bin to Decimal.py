# Complete the function which converts a binary number (given as a string) to a 
# decimal number.
def bin_to_decimal(inp):
    return sum(int(val)*2**ind for ind, val in enumerate(inp[::-1]))
