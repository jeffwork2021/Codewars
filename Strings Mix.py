# Given two strings s1 and s2, we want to visualize how different the two 
# strings are. We will only take into account the lowercase letters (a to z). 
# First let us count the frequency of each lowercase letters in s1 and s2.
#
# s1 = "A aaaa bb c"
#
# s2 = "& aaa bbb c d"
#
# s1 has 4 'a', 2 'b', 1 'c'
#
# s2 has 3 'a', 3 'b', 1 'c', 1 'd'
#
# So the maximum for 'a' in s1 and s2 is 4 from s1; the maximum for 'b' is 3 
# from s2. In the following we will not consider letters when the maximum of 
# their occurrences is less than or equal to 1.
#
# We can resume the differences between s1 and s2 in the following string: 
# "1:aaaa/2:bbb" where 1 in 1:aaaa stands for string s1 and aaaa because the 
# maximum for a is 4. In the same manner 2:bbb stands for string s2 and bbb 
# because the maximum for b is 3.
#
# The task is to produce a string in which each lowercase letters of s1 or s2 
# appears as many times as its maximum if this maximum is strictly greater than 
# 1; these letters will be prefixed by the number of the string where they 
# appear with their maximum value and :. If the maximum is in s1 as well as in 
# s2 the prefix is =:.
#
# In the result, substrings (a substring is for example 2:nnnnn or 1:hhh; it 
# contains the prefix) will be in decreasing order of their length and when 
# they have the same length sorted in ascending lexicographic order (letters 
# and digits - more precisely sorted by codepoint); the different groups will 
# be separated by '/'. See examples and "Example Tests".
#
# Hopefully other examples can make this clearer.
#
# s1 = "my&friend&Paul has heavy hats! &"
# s2 = "my friend John has many many friends &"
# mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/
# =:ss"
#
# s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
# s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
# mix(s1, s2) --> "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/
# =:ee/=:ss"
#
# s1="Are the kids at home? aaaaa fffff"
# s2="Yes they are here! aaaaa fffff"
# mix(s1, s2) --> "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"
#
# Note for Swift, R, PowerShell
#
# The prefix =: is replaced by E:
#
# s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
# s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
# mix(s1, s2) --> "1:mmmmmm/E:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/
# E:ee/E:ss"
from operator import itemgetter

def mix(s1, s2):
    tokens = list(set(s1+s2))
    l = []
    for t in tokens:
        if t.isalpha() and t.islower():
            c1 = s1.count(t)
            c2 = s2.count(t)

            if c1 > 1 or c2 > 1:
                if c1 == c2:
                    l.append(tuple(['=', t, -c1]))
                elif c1 > c2:
                    l.append(tuple(['1', t, -c1]))
                elif c2 > c1:
                    l.append(tuple(['2', t, -c2]))
    
    return '/'.join(f'{k[0]}:{k[1]*-k[2]}' 
                        for k in sorted(l, key=itemgetter(2,1), reverse=True)

print(mix("my&friend&Paul has heavy hats! &", 
          "my friend John has many many friends &"))
        