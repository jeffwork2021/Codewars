# Complete the solution so that the function will break up camel casing, using 
# a space between words.
# Example

# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""
def solution(s):
    return ''.join(c if ord(c)>96 else f' {c}' for c in list(s))

print(solution("camelCasing"))
print(solution("identifier"))
print(solution(""))
