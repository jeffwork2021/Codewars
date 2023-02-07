# Complete the function that accepts a string parameter, and reverses each word 
# in the string. All spaces in the string should be retained.
# 
# Examples
# 
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"
# 
def reverse_words(text):
    return ' '.join(s[::-1] for s in text.split(" "))

print(reverse_words("This is an example!"))
print(reverse_words("double   spaces"))