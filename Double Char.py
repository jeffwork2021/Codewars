# Given a string, you have to return a string in which each character 
# (case-sensitive) is repeated once.
# Examples (Input -> Output):
# 
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "
# 
# Good Luck!
def double_char(s):
    return ''.join(x*2 for x in s)

print(double_char("String"))
print(double_char("Hello World"))
print(double_char("1234!_ "))