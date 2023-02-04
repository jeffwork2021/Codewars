# Check to see if a string has the same amount of 'x's and 'o's. The method #
# must return a boolean and be case insensitive. The string can contain any 
# char.
# 
# Examples input/output:
# 
# xo("ooxx") => true
# xo("xooxx") => false
# xo("ooxXm") => true
# xo("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# xo("zzoo") => false
# 
def xo(s):
    return s.casefold().count('o') == s.casefold().count('x')

print(xo("ooxx"))
print(xo("xooxx"))
print(xo("ooxXm"))
print(xo("zpzpzpp"))
print(xo("zzoo"))
