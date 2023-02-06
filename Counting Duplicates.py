# Count the number of Duplicates
# 
# Write a function that will return the count of distinct case-insensitive 
# alphabetic characters and numeric digits that occur more than once in the 
# input string. The input string can be assumed to contain only alphabets (both 
# uppercase and lowercase) and numeric digits.
# Example
# 
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice
def duplicate_count(text):
    return sum([1 if text.casefold().count(x) > 1 else 0 
                        for x in list(set(text.casefold()))])

print(duplicate_count("abcde"))
print(duplicate_count("aabbcde"))
print(duplicate_count("aabBcde"))
print(duplicate_count("indivisibility"))
print(duplicate_count("Indivisibilities"))
print(duplicate_count("aA11"))
print(duplicate_count("ABBA"))