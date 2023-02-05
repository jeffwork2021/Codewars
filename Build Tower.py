# Build Tower
# 
# Build a pyramid-shaped tower, as an array/list of strings, given a positive 
# integer number of floors. A tower block is represented with "*" character.
# 
# For example, a tower with 3 floors looks like this:
# 
# [
#   "  *  ",
#   " *** ", 
#   "*****"
# ]
# 
# And a tower with 6 floors looks like this:
# 
# [
#   "     *     ", 
#   "    ***    ", 
#   "   *****   ", 
#   "  *******  ", 
#   " ********* ", 
#   "***********"
# ]
# 
def tower_builder(n_floors):
    return [ " "*(n_floors-i-1) + "*"*(i*2+1) + " "*(n_floors-i-1) \ 
                for i in range(0, n_floors)]