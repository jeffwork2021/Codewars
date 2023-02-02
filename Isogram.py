# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that 
# determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. 
# Ignore letter case.
#
# Example: (Input --> Output)
#
# "Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)
#
# isIsogram "Dermatoglyphics" = true
# isIsogram "moose" = false
# isIsogram "aba" = false
#
def is_isogram(string):
    dict = [];
    for c in string:
        uc = c.upper()
        if uc in dict:
            return False  
        else: 
            dict.append(uc)
    return True
    
print(is_isogram("Dermatoglyphics"))
print(is_isogram("moose"))
print(is_isogram("aba"))
