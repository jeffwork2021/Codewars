# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. 
# Return the resulting string.
#
# Note: input will never be an empty string
#
def fake_bin(x):
    ret = ""
    for c in x:
        ret += "0" if c < '5' else "1"
    return ret 

print(fake_bin("45385593107843568"))


