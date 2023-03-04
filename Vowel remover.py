# Create a function called shortcut to remove the lowercase vowels (a, e, i, o, # u ) in a given string.
# Examples
#
# "hello"     -->  "hll"
# "codewars"  -->  "cdwrs"
# "goodbye"   -->  "gdby"
# "HELLO"     -->  "HELLO"
#
#     don't worry about uppercase vowels
#     y is not considered a vowel for this kata
def shortcut( s ):
    return s.replace('a', '').replace('e', '').replace('i', '') \
            .replace('o', '').replace('u', '')

print(shortcut('hello'))
print(shortcut('codewars'))
print(shortcut('goodbye'))
print(shortcut('HELLO'))