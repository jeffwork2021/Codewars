# Create a function that takes 2 integers in form of a string as an input, and # outputs the sum (also as a string):
#
# Example: (Input1, Input2 -->Output)
#
# "4",  "5" --> "9"
# "34", "5" --> "39"
# "", "" --> "0"
# "2", "" --> "2"
# "-5", "3" --> "-2"
#
# Notes:
#
#     If either input is an empty string, consider it as zero.
#
#     Inputs and the expected output will never exceed the signed 32-bit 
# integer limit (2^31 - 1)
def sum_str(a, b):
    # happy coding !
    return str((0 if a == '' else int(a)) + (0 if b == '' else int(b)))

print(sum_str("4", "5"))
print(sum_str("34", "5"))
print(sum_str("", ""))
print(sum_str("2", ""))
print(sum_str("-5", "3"))