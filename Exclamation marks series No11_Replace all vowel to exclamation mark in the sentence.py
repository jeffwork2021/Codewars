# Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.
#
# Examples
#
# replace("Hi!") === "H!!"
# replace("!Hi! Hi!") === "!H!! H!!"
# replace("aeiou") === "!!!!!"
# replace("ABCDE") === "!BCD!"
def replace_exclamation(s):
    return s.translate(str.maketrans("aeiouAEIOU", "!!!!!!!!!!"))

print(replace_exclamation("Hi!"))
print(replace_exclamation("!Hi! Hi!"))
print(replace_exclamation("aeiou"))
print(replace_exclamation("ABCDE"))