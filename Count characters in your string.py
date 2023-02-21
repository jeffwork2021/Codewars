# The main idea is to count all the occurring characters in a string. If you 
# have a string like aba, then the result should be {'a': 2, 'b': 1}.
# 
# What if the string is empty? Then the result should be empty object literal, 
# {}.
def count(string):
    # The function code should be here
    return dict(zip(set(string), [string.count(c) for c in set(string)]))

