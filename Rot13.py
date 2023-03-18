# ROT13 is a simple letter substitution cipher that replaces a letter with the 
# letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar 
# cipher.
# 
# Create a function that takes a string and returns the string ciphered with 
# Rot13. If there are numbers or special characters included in the string, 
# they should be returned as they are. Only letters from the latin/english 
# alphabet should be shifted, like in the original Rot13 "implementation".
# 
# Please note that using encode is considered cheating.
def rot13(message):
    return ''.join(chr((ord(c)+13)-(c>'M')*26
                        if c.isupper() 
                            else (ord(c)+13)-(c>'m')*26)
                                if c.isalpha() else c
                                    for c in list(message))

