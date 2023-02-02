# This time no story, no theory. The examples below show you how to write function accum:
# Examples:
# 
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# 
# The parameter of accum is a string which includes only letters from a..z and A..Z.
def accum(s):
    ret = ""
    for i in range(len(s.lower())):
        ret += "-" + str(s[i].lower()*(i+1)).title()
    return ret[1:]
        
# return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

print(accum("abcd"))
print(accum("RqaEzty"))
print(accum("cwAt"))
