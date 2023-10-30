import string

capital_letters = string.ascii_uppercase
lowercase = string.ascii_lowercase

capital_reversed = capital_letters[::-1]
lowercase_reversed = lowercase[::-1]

# bad

# 1,0,4

# yzw

# capital_letters = ABCDEFGHIJKLMNOPQRSTUVWXYZ
# lowercase = abcdefghijklmnopqrstuvwxyz

# lower_rever = zyxw....dcba
# capital_reversed = ZYX.....BA

# a = input()
# # print(lowercase.find(a))
# dec = ""

# # STAN IS NOT.-88

# for i in a:
#     if i in lowercase:
#         position = lowercase.find(i)
#         new_pos = position - 3
#         new_char = lowercase[new_pos]

#     elif i in capital_letters:
#         position = capital_letters.find(i)
#         new_pos = position - 3
#         new_char = capital_letters[new_pos]
    
#     else:
#         new_char = i
        
#     dec = dec + str(new_char)

# print(dec)




# x = 'A'
# y = ord(x)
# y += 1
# z = chr(y)
# print(z)


# stringa = "hi whats up"

# for i in stringa:
#     print(i)

# text = "rht"
# oeq

def decrypt_caesar(text: str, shift: int) -> str:

    decrypted_text = ""

    for i in text:
        ascii_code = ord(i)
        conversion = ascii_code - shift
        back_to_char = chr(conversion)
        decrypted_text = decrypted_text + str(back_to_char)

    return (decrypted_text)

def decrypt_atbash(text: str) -> str:

    dec = ""

    for i in text:
        if i in lowercase:
            position = lowercase.find(i)
            new_char = lowercase_reversed[position]

        elif i in capital_letters:
            position = capital_letters.find(i)
            new_char = capital_reversed[position]
        
        else:
            new_char = i
            
        dec = dec + str(new_char)

    print(dec)

def decrypt_a1z26(text: str) -> str:
    # dec = ""
    # for i in text:
    #     if i in lowercase:
    #         position = lowercase.find(i)
    #         new_char = position+1

    #     elif i in capital_letters:
    #         position = capital_letters.find(i)
    #         new_char = position+1
        
    #     else:
    #         new_char = i
            
    #     dec = dec + str(new_char) + "-"

    decrypted = ""

    for i in text:
        number = ""
        char = ""
        while i != '-':
            char_position = number + str(i)
        new_char = char_position.replace()
        decrypted = decrypted + str(capital_letters[char_position])
    

    print(decrypted)

    
def main() -> None:
    text = input("Enter a text to decipher: ")
    shift = 3

    # decrypt_caesar(text,shift)
    # decrypt_atbash(text)
    decrypt_a1z26(text)


main()





