# Write a function that checks if a given string (case insensitive) is a 
# palindrome.
def is_palindrome(s):
    rs = [*s]
    rs.reverse()
    return s.casefold() == ''.join(rs).casefold()

