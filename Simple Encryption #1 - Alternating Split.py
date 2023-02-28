# Implement a pseudo-encryption algorithm which given a string S and an integer 
# N concatenates all the odd-indexed characters of S with all the even-indexed 
# characters of S, this process should be repeated N times.
#
# Examples:
#
# encrypt("012345", 1)  =>  "135024"
# encrypt("012345", 2)  =>  "135024"  ->  "304152"
# encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"
#
# encrypt("01234", 1)  =>  "13024"
# encrypt("01234", 2)  =>  "13024"  ->  "32104"
# encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
#
# Together with the encryption function, you should also implement a decryption 
# function which reverses the process.
#
# If the string S is an empty value or the integer N is not positive, return 
# the first argument without changes.
def decrypt(encrypted_text, n):
    if n < 1 or not encrypted_text:
        return encrypted_text
    else:
        text = decrypt(encrypted_text, n-1)
        l = len(text)
        even_part = list(text[l//2:])
        odd_part = list(text[0:l//2].ljust(len(even_part)))
        return ''.join(item for sublist in zip(even_part, odd_part) 
                                for item in sublist)[0:l]


def encrypt(text, n):
    if n < 1 or not text:
        return text
    else:
        text = encrypt(text, n-1)
        return ''.join(text[i] for i in range(1,len(text),2)) \
                + ''.join(text[i] for i in range(0,len(text),2))

#print(encrypt("01234", 3))
#print(decrypt("20314", 3))
print(decrypt("This is a test!", 4))